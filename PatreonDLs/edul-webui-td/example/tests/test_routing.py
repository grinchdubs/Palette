# Fake-input test (run inside TD with the window open; works for any size / dpiscale).
# Run it twice: the first run asks the page where its controls are (Probe), the second queues the input.
# The real exec_tick is paused meanwhile - otherwise its real panel values (mouse outside the window = zeros) land
# between the fake frames as a button-up. Read the result with test_read.py a few seconds later.
from collections import namedtuple
R = op.HtmlUI
L = R.op('logic').module
ui = R.op('webui')
W, H = ui.width, ui.height
S = L.st()

if not S.get('probe'):
    L.Probe()
    result = 'asked the page for its control positions - run test_routing.py again'
else:
    P, lay = S['probe'], S['layout']
    R.par.Spin, R.par.Shape = 0, 'torus'
    R.par.Speed, R.par.Yaw, R.par.Pitch, R.par.Dist = 45, 30, 20, 6
    ui.op('exec_tick').par.active = False
    R.storage['test'] = dict(log=[], marks={})

    # security: a browser on this PC (also 127.0.0.1) without the key must not move the hole
    before = dict(lay)
    L.Receive('127.0.0.1:1', {'op': 'embed', 'vp': [0, 0, 10, 10], 'hit': []})
    R.storage['test']['embed_without_key_ignored'] = S['layout'] == before

    def pv(x, ytop, l=0, wheel=0):
        u, v = x / W, 1 - ytop / H                     # texture px -> panel u / v (v counts from the bottom)
        return dict(lselect=l, mselect=0, rselect=0, u=u if l else 0, v=v if l else 0,
                    rollu=u, rollv=v, inside=1, wheel=wheel, shift=0, ctrl=0, alt=0)

    def mid(r, fx=0.5, fy=0.5):
        return r[0] + r[2] * fx, r[1] + r[3] * fy

    def click(r):
        x, y = mid(r)
        return [pv(x, y)] * 2 + [pv(x, y, 1)] * 2 + [pv(x, y)] * 3

    K = namedtuple('K', 'key character shift alt ctrl state')
    steps, marks = [], {}

    def mark(name):
        marks[name] = len(steps) - 1

    sp = P['Speed']                                   # speed slider: press at 10 %, drag to 80 % of the track
    x0, y0 = mid(sp, 0.1)
    x1, _ = mid(sp, 0.8)
    steps += [pv(x0, y0)] * 2 + [pv(x0, y0, 1)] * 2 + [pv(x0 + (x1 - x0) * i / 10, y0, 1) for i in range(1, 11)] + [pv(x1, y0)] * 2
    mark('slider')
    steps += click(P['Spin']); mark('switch')
    steps += click(P['Shape=box']); mark('segment')
    vx, vy, vw, vh = lay['vp']                         # orbit: drag in the middle of the hole
    cx, cy = vx + vw * 0.5, vy + vh * 0.6
    steps += [pv(cx, cy)] * 2 + [pv(cx, cy, 1)] * 2 + [pv(cx + 10 * i, cy - 5 * i, 1) for i in range(1, 11)] + [pv(cx + 100, cy - 50)] * 2
    mark('orbit')
    hx, hy = mid(lay['hit'][0])                       # a drag that starts on a glass panel must not orbit
    steps += [pv(hx, hy)] * 2 + [pv(hx, hy, 1)] + [pv(hx + 10 * i, hy + 10 * i, 1) for i in range(1, 8)] + [pv(hx + 70, hy + 70)] * 2
    mark('glass_drag')
    steps += [pv(cx, cy, 0, 1)] * 3; mark('wheel')
    steps += click(P['Reset']); mark('reset_button')
    steps += [('key', K('home', '', False, False, False, True))]; mark('home_key')
    R.storage['test']['marks'] = marks

    code = ("R = op.HtmlUI; L = R.op('logic').module; ui = R.op('webui')\n"
            "if isinstance(args[0], tuple): ui.op('keys_callbacks').module.onKey(ui.op('keys'), args[0][1])\n"
            "else: L.Tick(ui, args[0])\n"
            "p = R.par; R.storage['test']['log'].append((args[1], p.Speed.eval(), int(p.Spin.eval()), p.Shape.eval(), "
            "round(p.Yaw.eval(), 1), round(p.Pitch.eval(), 1), round(p.Dist.eval(), 2)))")
    for i, v in enumerate(steps):
        run(code, v, i, delayFrames=2 + i * 2)
    run("op.HtmlUI.op('webui/exec_tick').par.active = True; op.HtmlUI.par.Spin = 1", delayFrames=2 + len(steps) * 2 + 20)
    S.pop('probe', None)
    result = 'queued %d frames' % len(steps)
