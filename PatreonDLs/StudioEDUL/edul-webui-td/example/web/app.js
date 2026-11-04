// HtmlUI demo page.
// ?embed=1&key=..  -> inside TD's Web Render TOP: the viewport is a transparent hole, TD composites its render under
//                     it, and the page reports where the hole and the floating glass panels are.
// no query          -> a normal browser (laptop / tablet on the LAN): same controls, no 3D.
//
// Controls bind by markup, so adding one is HTML only (plus the parameter in TD's EXPOSED list):
//   <input type=range data-par="Speed">  + <input class="field num" data-num="Speed">   number
//   <button class="sw" data-par="Spin">                                                  toggle
//   <div class="seg" data-par="Shape"><button data-v="box">                              menu
//   <button data-pulse="Reset">                                                          pulse
//   <b data-val="Yaw" data-fix="0">   <b data-stat="fps">   <i data-meter="render_ms">    read-outs
const q = new URLSearchParams(location.search);
const EMBED = q.get('embed') === '1';
const KEY = q.get('key') || '';
if (EMBED) document.documentElement.classList.add('embed');

const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];
let ws = null;
let held = null;                    // the parameter the user is dragging / typing: TD's pushes must not overwrite it
const V = {};                       // last values from TD

function send(obj) { if (ws && ws.readyState === 1) ws.send(JSON.stringify(obj)); }
const set = (name, value) => { V[name] = value; send({ op: 'set', name, value }); show(name); };

// ---------------------------------------------------------------- connection
function connect() {
  ws = new WebSocket(`ws://${location.host}/ctl`);
  ws.onopen = () => { online(true); send({ op: 'sub' }); reportLayout(true); };
  ws.onclose = () => { online(false); setTimeout(connect, 1000); };
  ws.onmessage = (ev) => {
    const m = JSON.parse(ev.data);
    if (m.op === 'vals') { Object.assign(V, m.vals); Object.keys(m.vals).forEach(show); }
    else if (m.op === 'stats') stats(m.stats);
    else if (m.op === 'probe' && EMBED) probe();
  };
}
function online(on) {
  $('#addr').textContent = `ws://${location.host}`;
  $$('.pled').forEach((e) => e.classList.toggle('on', on));
  $('#sconn').textContent = on ? 'Live' : 'Offline';
}

// ---------------------------------------------------------------- TD -> page
function show(name) {
  const v = V[name];
  if (v === undefined) return;
  if (held !== name) {
    $$(`input[type=range][data-par="${name}"]`).forEach((e) => { e.value = v; });
    $$(`input[data-num="${name}"]`).forEach((e) => { if (document.activeElement !== e) e.value = fmt(v, e.step); });
  }
  $$(`.sw[data-par="${name}"]`).forEach((e) => e.classList.toggle('on', !!Number(v)));
  $$(`.seg[data-par="${name}"] button`).forEach((b) => b.classList.toggle('on', String(b.dataset.v) === String(v)));
  $$(`[data-val="${name}"]`).forEach((e) => { e.textContent = Number(v).toFixed(+e.dataset.fix || 0); });
  if (name === 'Hue' || name === 'Sat') $('#swatch').style.background = `hsl(${(V.Hue || 0) * 360} ${(V.Sat ?? 0.65) * 100}% 60%)`;
}
const fmt = (v, step) => { const d = (String(step).split('.')[1] || '').length; return Number(v).toFixed(d); };

function stats(s) {
  s.target = { vp: 'TD view', web: 'Page' }[s.target] || '—';
  for (const [k, v] of Object.entries(s)) {
    $$(`[data-stat="${k}"]`).forEach((e) => { e.textContent = typeof v === 'number' && !Number.isInteger(v) ? v.toFixed(2) : v; });
    $$(`[data-meter="${k}"]`).forEach((e) => {                      // budget bar: 16.7 ms = one 60 fps frame
      const pct = Math.min(100, (Number(v) / 16.7) * 100);
      e.style.width = pct + '%';
      e.className = pct > 60 ? 'bad' : pct > 30 ? 'warn' : '';
    });
  }
  $('#target').textContent = s.target === 'Page' ? 'PAGE' : 'TD VIEW';
}

// ---------------------------------------------------------------- page -> TD
for (const el of $$('input[type=range][data-par]')) {
  const name = el.dataset.par;
  el.addEventListener('pointerdown', () => { held = name; });
  el.addEventListener('input', () => {
    const v = Number(el.value);
    $$(`input[data-num="${name}"]`).forEach((n) => { n.value = fmt(v, n.step); });
    set(name, v);
  });
}
for (const el of $$('input[data-num]')) {
  const name = el.dataset.num;
  el.addEventListener('focus', () => { held = name; el.select(); });
  el.addEventListener('blur', () => { held = null; show(name); });
  el.addEventListener('keydown', (e) => { if (e.key === 'Enter') el.blur(); });
  el.addEventListener('change', () => { const v = Number(el.value); if (!Number.isNaN(v)) set(name, v); });
}
window.addEventListener('pointerup', () => { if (!(document.activeElement && document.activeElement.dataset.num)) held = null; });
for (const el of $$('.sw[data-par]')) el.addEventListener('click', () => set(el.dataset.par, el.classList.contains('on') ? 0 : 1));
for (const seg of $$('.seg[data-par]')) {
  for (const b of $$('button', seg)) {
    b.addEventListener('click', () => set(seg.dataset.par, /^\d+$/.test(b.dataset.v) ? Number(b.dataset.v) : b.dataset.v));
  }
}
for (const el of $$('[data-pulse]')) el.addEventListener('click', () => send({ op: 'pulse', name: el.dataset.pulse }));

// ---------------------------------------------------------------- layout report (embed only)
// The hole + every floating glass panel over it, in CSS px (= texture px with dpiscale=1).
// Sent on change, on resize, and every second (a cheap safety net).
function rect(el) { const r = el.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)]; }
let lastLayout = '';
function reportLayout(force) {
  if (!EMBED) return;
  const vp = $('#viewport');
  const msg = { op: 'embed', key: KEY, size: [innerWidth, innerHeight], vp: rect(vp), hit: $$('.glass', vp).map(rect), modal: false };
  const s = JSON.stringify(msg);
  if (force || s !== lastLayout) { lastLayout = s; send(msg); }
}
// Tests in TD ask where the controls are, so fake mouse input works for any layout / resolution.
function probe() {
  const rects = {};
  for (const el of $$('[data-par], [data-pulse]')) {
    if (el.classList.contains('seg')) $$('button', el).forEach((b) => { rects[`${el.dataset.par}=${b.dataset.v}`] = rect(b); });
    else rects[el.dataset.par || el.dataset.pulse] = rect(el);
  }
  send({ op: 'embed', key: KEY, size: [innerWidth, innerHeight], rects });
}
window.addEventListener('resize', () => reportLayout());
setInterval(() => reportLayout(true), 1000);
connect();
