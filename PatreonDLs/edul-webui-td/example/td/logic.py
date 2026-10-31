"""
HtmlUIDemo logic (text DAT 'logic'). Called from server_cb (WebSocket) and webui/exec_tick (every frame).

  page -> TD   {"op":"sub"}                              send me every value now, then diffs
               {"op":"set", "name":"Speed", "value":90}   write an exposed parameter
               {"op":"pulse", "name":"Reset"}             press an exposed pulse
               {"op":"embed", "key":..., "vp":[x,y,w,h], "hit":[[x,y,w,h]...], "modal":false}
                                                          TD window only: the viewport hole + floating panels
                                                          (page px, top-left origin)
  TD -> page   {"op":"vals", "vals":{"Speed":90, ...}}    changed values, ~10 Hz
               {"op":"stats", "stats":{"fps":60, ...}}    indicators, ~4 Hz
"""
import json, math, colorsys

# the page may write these (name -> type); menus take the menu name as a string
EXPOSED = {'Speed': float, 'Spin': int, 'Scale': float, 'Shape': str, 'Wire': int, 'Hue': float, 'Sat': float,
           'Light': float, 'Bg': float, 'Fov': float, 'Dist': float}
PULSES = {'Reset'}
PUSHED = list(EXPOSED) + ['Yaw', 'Pitch']                   # the page is told about these


def R():
    return op.HtmlUI


def st():
    S = R().storage
    if 'html' not in S:
        S['html'] = dict(subs={}, layout=None, frame=0, cap=None, prev=False, lastweb=None,
                         drag=None, overvp=False, sizes=None, open=None)
    return S['html']


# ================================================================ WebSocket protocol
def ClientOpen(client):
    st()['subs'][client] = {}                    # last values sent to this client


def ClientClose(client):
    st()['subs'].pop(client, None)


def Receive(client, msg):
    s = st()
    kind = msg.get('op')
    if kind == 'sub':
        s['subs'][client] = {}                   # full push on the next tick
    elif kind == 'set':
        name = msg.get('name')
        if name in EXPOSED:
            try:
                R().par[name] = EXPOSED[name](msg.get('value'))
            except Exception as e:
                debug('set failed', name, e)
    elif kind == 'pulse':
        if msg.get('name') in PULSES:
            R().par[msg['name']].pulse()                     # handled by par_exec, same as pressing it in TD
    elif kind == 'embed':
        # Only TD's own Web Render TOP knows the key (it is in its URL). A plain browser on this PC also connects
        # from 127.0.0.1, so the IP alone is not enough.
        if msg.get('key') != R().par.Embedkey.eval():
            return
        # The page measures in CSS px. With the Web Render TOP's dpiscale > 1 (big UI for a phone-sized video) CSS px
        # != texture px, so scale by texture width / the page's own width.
        size = msg.get('size')
        k = R().op('webui').width / float(size[0]) if isinstance(size, list) and size and size[0] else 1.0
        sc = lambda r: [v * k for v in r] if isinstance(r, list) and len(r) == 4 else None
        s['embed_client'] = client
        if 'rects' in msg:                                      # reply to Probe() (tests): control rectangles
            s['probe'] = {n: sc(r) for n, r in (msg.get('rects') or {}).items()}
            return
        s['layout'] = dict(vp=sc(msg.get('vp')), hit=[h for h in map(sc, (msg.get('hit') or [])[:64]) if h],
                           modal=bool(msg.get('modal')))


def Probe():
    """Tests: ask the TD window's page where its controls are (answer lands in st()['probe'], texture px)."""
    s = st()
    s.pop('probe', None)
    if s.get('embed_client'):
        R().op('server').webSocketSendText(s['embed_client'], json.dumps({'op': 'probe'}))


def _val(name):
    v = R().par[name].eval()
    return v if isinstance(v, str) else round(float(v), 3)


def pushValues():
    s = st()
    srv = R().op('server')
    cur = {n: _val(n) for n in PUSHED}
    for client, last in list(s['subs'].items()):
        diff = {k: v for k, v in cur.items() if last.get(k) != v}
        if diff:
            try:
                srv.webSocketSendText(client, json.dumps({'op': 'vals', 'vals': diff}))
                last.update(diff)
            except Exception:
                s['subs'].pop(client, None)


def pushStats():
    """Indicators for the status bar / render group: measured, not configured."""
    s = st()
    now, frame = absTime.seconds, absTime.frame
    t0, f0 = s.get('fpsmark', (now, frame))
    if now - t0 >= 0.5:
        s['fps'] = round((frame - f0) / (now - t0), 1)
        s['fpsmark'] = (now, frame)
    elif 'fpsmark' not in s:
        s['fpsmark'] = (now, frame)
    rnd, web = R().op('render1'), R().op('webui/web')
    stats = dict(fps=s.get('fps', 0), frame=frame, clients=len(s['subs']),
                 res='%d × %d' % (rnd.width, rnd.height),
                 render_ms=round(rnd.cookTime + rnd.gpuCookTime, 2),
                 web_ms=round(web.cookTime, 2) if web.par.active.eval() else 0,
                 target=s.get('target') or '-')
    msg = json.dumps({'op': 'stats', 'stats': stats})
    srv = R().op('server')
    for client in list(s['subs']):
        try:
            srv.webSocketSendText(client, msg)
        except Exception:
            s['subs'].pop(client, None)


def Reset():
    p = R().par
    p.Yaw, p.Pitch, p.Dist, p.Fov = 30, 20, 6, 45


# ================================================================ the scene (stand-in for your own project)
def updateScene():
    p = R().par
    geo = R().op('geo1')
    if p.Spin.eval():                                       # tumble on two axes: a turning box is obvious motion
        step = p.Speed.eval() / max(1.0, project.cookRate)
        geo.par.ry = (geo.par.ry.eval() + step) % 360
        geo.par.rx = (geo.par.rx.eval() + step * 0.6) % 360
    r, g, b = colorsys.hsv_to_rgb(p.Hue.eval(), p.Sat.eval(), 1.0)
    mat = R().op('mat1')
    if abs(mat.par.diffr.eval() - r) + abs(mat.par.diffg.eval() - g) + abs(mat.par.diffb.eval() - b) > 1e-4:
        mat.par.diffr, mat.par.diffg, mat.par.diffb = r, g, b
    yaw, pitch, dist = math.radians(p.Yaw.eval()), math.radians(p.Pitch.eval()), p.Dist.eval()
    x, y, z = dist * math.cos(pitch) * math.sin(yaw), dist * math.sin(pitch), dist * math.cos(pitch) * math.cos(yaw)
    cam = R().op('cam1')
    if abs(cam.par.tx.eval() - x) + abs(cam.par.ty.eval() - y) + abs(cam.par.tz.eval() - z) > 1e-5:
        cam.par.tx, cam.par.ty, cam.par.tz = x, y, z


# ================================================================ compositing (only when sizes change)
def updateSizes(ui):
    s = st()
    W, H = int(ui.width), int(ui.height)
    lay = s['layout']
    x, y, w, h = [int(v) for v in lay['vp']] if lay and lay.get('vp') else (0, 0, W, H)
    w, h = max(1, w), max(1, h)
    key = (W, H, x, y, w, h)
    if key == s['sizes']:
        return
    s['sizes'] = key
    rnd = R().op('render1')
    rnd.par.resolutionw, rnd.par.resolutionh = w, h          # render at the hole's size (sharp, no wasted pixels)
    ui.op('fit').par.resolutionw, ui.op('fit').par.resolutionh = w, h
    ui.op('bg').par.resolutionw, ui.op('bg').par.resolutionh = W, H
    ui.op('web').par.resolutionw, ui.op('web').par.resolutionh = W, H
    place = ui.op('place')
    place.par.tx, place.par.ty = x, H - y - h                 # TOP origin is bottom-left


# ================================================================ mouse / keys
def hitTarget(x, ytop):
    lay = st()['layout']
    if not lay or not lay.get('vp') or lay.get('modal'):
        return 'web'
    vx, vy, vw, vh = lay['vp']
    if not (vx <= x < vx + vw and vy <= ytop < vy + vh):
        return 'web'
    for hx, hy, hw, hh in lay.get('hit', []):
        if hx <= x < hx + hw and hy <= ytop < hy + hh:
            return 'web'                                      # a floating panel over the hole keeps the mouse
    return 'vp'


def Route(v, ui):
    """v = panel values: lselect mselect rselect u v rollu rollv inside wheel shift ctrl alt."""
    s = st()
    W, H = int(ui.width), int(ui.height)
    l, m, r = bool(v.get('lselect', 0)), bool(v.get('mselect', 0)), bool(v.get('rselect', 0))
    held = l or m or r
    u, vv = (v.get('u', 0), v.get('v', 0)) if held else (v.get('rollu', 0), v.get('rollv', 0))   # roll* = hover
    x, ytop = u * W, (1 - vv) * H
    wheel = v.get('wheel', 0)
    prevheld = s['prev']
    if held and not prevheld:
        s['cap'] = hitTarget(x, ytop)                          # a held button stays where it went down
    target = s['cap'] if (held or prevheld) else hitTarget(x, ytop)
    if not v.get('inside', 1) and not held and not prevheld:
        target = None
    if v.get('inside', 1):
        s['overvp'] = target == 'vp'
    s['target'] = target

    if target == 'web':
        sig = (round(x), round(ytop), l, m, r, wheel)
        if sig != s['lastweb']:                                # send only on change
            s['lastweb'] = sig
            # normalized coordinates (0..1, bottom-left origin) work for any resolution / dpiscale
            ui.op('web').interactMouse(x / W, (H - ytop) / H, left=l, middle=m, right=r, wheel=wheel, pixels=False)
    elif target == 'vp':                                       # your viewer goes here; this demo just orbits
        p = R().par
        if held and l:
            if s['drag'] is not None:
                dx, dy = x - s['drag'][0], ytop - s['drag'][1]
                p.Yaw = (p.Yaw.eval() - dx * 0.4) % 360
                p.Pitch = max(-85, min(85, p.Pitch.eval() + dy * 0.4))
            s['drag'] = (x, ytop)
        if wheel:
            p.Dist = max(2.0, min(20.0, p.Dist.eval() * (1 - 0.1 * wheel)))
    if not held:
        s['drag'] = s['cap'] = None
    s['prev'] = held


def Key(keyInfo, ui):
    """Keyboard In DAT -> the page, unless the mouse was last over the 3D hole (then: your viewer's shortcuts)."""
    if not keyInfo.state:
        return
    if st()['overvp']:
        if keyInfo.key == 'home':                              # demo shortcut: reset the camera
            Reset()
        return
    ui.op('web').sendKey(keyInfo.key, char=keyInfo.character or None,
                         shift=keyInfo.shift, alt=keyInfo.alt, ctrl=keyInfo.ctrl)


# ================================================================ per frame (webui/exec_tick)
def Tick(ui, panelvals=None):
    s = st()
    s['frame'] += 1
    updateScene()
    if s['frame'] % 6 == 0:
        pushValues()
    if s['frame'] % 15 == 3:
        pushStats()
    is_open = R().op('WebWindow').isOpen
    if is_open != s['open']:                                   # opened / closed: forget any held state
        s['open'] = is_open
        s['cap'] = s['drag'] = s['lastweb'] = None
        s['prev'] = False
        s['sizes'] = None
        s['reload_at'] = s['frame'] + 10 if is_open else None
    if s.get('reload_at') and s['frame'] >= s['reload_at']:
        # Chromium starts when the window opens; a page requested before that can stay blank. Load it once more.
        s['reload_at'] = None
        ui.op('web').par.reload.pulse()
    if not is_open and panelvals is None:
        if ui.op('web').par.active.eval():                  # page rendering without its window (recordings)
            updateSizes(ui)
        return
    updateSizes(ui)
    if panelvals is None:
        panelvals = {c.name: c.eval() for c in ui.op('panel').chans()}
    Route(panelvals, ui)
