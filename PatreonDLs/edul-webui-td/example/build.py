# Build /project1/HtmlUIDemo: an HTML/CSS/JS UI in a TD window with TD's own 3D render in a transparent hole.
#
# Run inside TouchDesigner, either
#   Textport:  BASE = 'C:/path/to/example'; exec(open(BASE + '/build.py', encoding='utf-8').read())
#   MCP:       execute_code with this file's text (set BASE below first)
# Re-running is safe: it refuses while the window is open (never destroy an open window COMP - it can hang TD).
# Then: HtmlUIDemo parameter page 'Demo' > Open Window.
#
# The build is a list of steps, one operator each. SLOW = True runs them STEP_FRAMES apart and makes the network
# editor follow each new operator (for screen recordings).
BASE = globals().get('BASE')
if not BASE:
    raise RuntimeError("Set BASE = '<path to this example folder>' before running build.py.")
SLOW = globals().get('SLOW', False)
STEP_FRAMES = globals().get('STEP_FRAMES', 24)
ON_DONE = globals().get('ON_DONE')          # optional callable, run after the last step
FOLLOW = globals().get('FOLLOW')            # optional network editor pane to follow (a recording's own)
STEP_HOOK = globals().get('STEP_HOOK')      # optional callable(i, n, docstring) before each step (captions)
PORT = 9981
W, H = globals().get('SIZE') or (1280, 720)   # e.g. SIZE = (1080, 1920) for a vertical video. Non-Commercial: max 1280
DPI = globals().get('DPI') or 1               # Web Render dpiscale: 2 = the page lays out at half size, drawn sharp
import secrets

proj = op('/project1')
old = proj.op('HtmlUIDemo')
if old is not None and old.op('WebWindow') is not None and old.op('WebWindow').isOpen:
    raise RuntimeError('Close the HtmlUIDemo window first, then run build.py again.')

N = {}                      # operators made so far, by name
STEPS = []


def step(fn):
    STEPS.append(fn)
    return fn


def at(o, x, y):
    o.nodeX, o.nodeY = x, y
    o.viewer = True                         # node viewers on: the network shows what each operator makes
    N[o.name] = o
    return o


def link(dst, *srcs):
    """Wire srcs into dst's inputs. SLOW mode: half a step after the operator appears, so the wire is seen."""
    def do():
        for i, s in enumerate(srcs):
            dst.inputConnectors[i].connect(s)
    if SLOW:
        run(do, delayFrames=max(1, STEP_FRAMES // 2))
    else:
        do()


def follow(o):
    """SLOW mode: show the new operator in the network editor."""
    if not SLOW:
        return
    panes = [FOLLOW] if FOLLOW else [p for p in ui.panes if p.type == PaneType.NETWORKEDITOR]
    for p in panes:
        if p.owner != o.parent():
            p.owner = o.parent()
        o.current = True
        p.showParameters = False                     # no parameter box over the network
        p.home()
        break


# ================================================================ root + custom parameters
@step
def s_root():
    """HtmlUIDemo  baseCOMP|One COMP holds it all. Its custom parameters are what the page may change."""
    o = proj.op('HtmlUIDemo')
    if o is not None:
        o.destroy()
    root = at(proj.create(baseCOMP, 'HtmlUIDemo'), 200, 0)
    root.par.opshortcut = 'HtmlUI'          # code uses op.HtmlUI, so the COMP can live anywhere
    pg = root.appendCustomPage('Demo')
    pg.appendPulse('Open', label='Open Window')
    pg.appendPulse('Reset', label='Reset View')
    p = pg.appendInt('Port')[0]; p.default = p.val = PORT; p.normMin, p.normMax = 1024, 65535
    p = pg.appendStr('Embedkey', label='Embed Key')[0]; p.val = secrets.token_hex(4); p.readOnly = True
    p.help = 'Only the TD window knows this key, so only it may send the viewport layout.'
    p = pg.appendFloat('Speed', label='Rotation Speed')[0]; p.normMin, p.normMax = 0, 360; p.default = p.val = 90
    p = pg.appendToggle('Spin')[0]; p.default = p.val = True
    p = pg.appendFloat('Scale')[0]; p.normMin, p.normMax = 0.2, 2; p.default = p.val = 1
    p = pg.appendMenu('Shape')[0]
    p.menuNames, p.menuLabels = ['torus', 'box', 'sphere'], ['Torus', 'Box', 'Sphere']
    p.default = p.val = 'box'
    p = pg.appendToggle('Wire', label='Wireframe')[0]; p.default = p.val = False
    p = pg.appendFloat('Hue')[0]; p.normMin, p.normMax = 0, 1; p.default = p.val = 0.6
    p = pg.appendFloat('Sat', label='Saturation')[0]; p.normMin, p.normMax = 0, 1; p.default = p.val = 0.65
    p = pg.appendFloat('Light')[0]; p.normMin, p.normMax = 0, 2; p.default = p.val = 1
    p = pg.appendFloat('Bg', label='Background')[0]; p.normMin, p.normMax = 0, 0.5; p.default = p.val = 0.08
    p = pg.appendFloat('Fov', label='Field of View')[0]; p.normMin, p.normMax = 20, 100; p.default = p.val = 45
    p = pg.appendFloat('Yaw')[0]; p.normMin, p.normMax = 0, 360; p.default = p.val = 30
    p = pg.appendFloat('Pitch')[0]; p.normMin, p.normMax = -85, 85; p.default = p.val = 20
    p = pg.appendFloat('Dist', label='Distance')[0]; p.normMin, p.normMax = 2, 20; p.default = p.val = 6
    follow(root)


# ================================================================ 3D scene (replace with your own)
@step
def s_geo():
    """geo1  Geometry COMP|A stand-in scene: torus, box and sphere behind a Switch SOP."""
    root = N['HtmlUIDemo']
    geo = at(root.create(geometryCOMP, 'geo1'), 0, 200)
    for c in list(geo.children):
        c.destroy()
    tor = geo.create(torusSOP, 'torus1'); tor.par.radx, tor.par.rady = 1.0, 0.4; tor.nodeX = -200
    box = geo.create(boxSOP, 'box1'); box.par.sizex = box.par.sizey = box.par.sizez = 1.4; box.nodeX = 0
    sph = geo.create(sphereSOP, 'sphere1'); sph.par.radx = sph.par.rady = sph.par.radz = 0.9; sph.nodeX = 200
    sw = geo.create(switchSOP, 'shape'); sw.nodeY = -150
    for i, s in enumerate((tor, box, sph)):
        sw.inputConnectors[i].connect(s)
    sw.par.input.expr = 'op.HtmlUI.par.Shape.menuIndex'
    sw.render = sw.display = True
    geo.par.scale.expr = 'op.HtmlUI.par.Scale'
    follow(geo)


@step
def s_mat():
    """mat1  Phong MAT|Colour from Hue / Saturation, wireframe from the Wire switch."""
    mat = at(N['HtmlUIDemo'].create(phongMAT, 'mat1'), 0, 50)
    mat.par.wireframe.expr = "'topology' if op.HtmlUI.par.Wire else 'off'"
    mat.par.wirewidth = 1.5
    N['geo1'].par.material = mat.path
    follow(mat)


@step
def s_cam():
    """cam1  Camera COMP|Orbits the shape. Yaw, Pitch and Distance come from mouse drags in the hole."""
    cam = at(N['HtmlUIDemo'].create(cameraCOMP, 'cam1'), 200, 200)
    cam.par.lookat = N['geo1'].path
    cam.par.fov.expr = 'op.HtmlUI.par.Fov'
    follow(cam)


@step
def s_light():
    """light1  Light COMP|Brightness follows the Light slider."""
    light = at(N['HtmlUIDemo'].create(lightCOMP, 'light1'), 400, 200)
    light.par.tx, light.par.ty, light.par.tz = 4, 6, 6
    light.par.dimmer.expr = 'op.HtmlUI.par.Light'
    follow(light)


@step
def s_render():
    """render1  Render TOP|The 3D picture. It is rendered at exactly the size of the hole in the page."""
    rnd = at(N['HtmlUIDemo'].create(renderTOP, 'render1'), 600, 200)
    rnd.par.camera, rnd.par.geometry, rnd.par.lights = N['cam1'].path, N['geo1'].path, N['light1'].path
    rnd.par.outputresolution = 'custom'
    rnd.par.resolutionw, rnd.par.resolutionh = 980, 630    # logic.updateSizes sets it to the hole size
    rnd.par.bgcolorr.expr = 'op.HtmlUI.par.Bg * 0.95'
    rnd.par.bgcolorg.expr = 'op.HtmlUI.par.Bg * 0.92'
    rnd.par.bgcolorb.expr = 'op.HtmlUI.par.Bg * 0.86'          # warm graphite like the page
    rnd.par.bgcolora = 1
    follow(rnd)


# ================================================================ code + page files (file-synced text DATs)
def synced(name, rel, x, y, doc):
    def fn():
        d = at(N['HtmlUIDemo'].create(textDAT, name), x, y)
        d.par.file = BASE + '/' + rel
        d.par.syncfile = True
        follow(d)
    fn.__doc__ = '%s  Text DAT|%s' % (name, doc)
    STEPS.append(fn)


synced('logic', 'td/logic.py', 0, -200, 'td/logic.py, synced from disk: protocol, value push, mouse routing.')
synced('server_cb', 'td/server_cb.py', 200, -200, 'Web Server callbacks: serve the page files, pass JSON to logic.')
synced('web_index', 'web/index.html', 400, -200, 'The page itself. Edit it on disk, reload, done.')
synced('web_app', 'web/app.js', 600, -200, 'Binds controls by markup, reports where the hole is.')
synced('web_css', 'web/style.css', 800, -200, 'The look. In TD the 3D area is transparent.')


@step
def s_server():
    """server  Web Server DAT|One port: HTTP serves the page, a WebSocket carries small JSON control messages."""
    srv = at(N['HtmlUIDemo'].create(webserverDAT, 'server'), 200, -400)
    for d in list(srv.docked):                              # TD docks a default callbacks DAT - ours is server_cb
        d.destroy()
    srv.par.callbacks = N['server_cb'].path
    srv.par.port.expr = 'parent().par.Port'
    srv.par.active = True
    follow(srv)


@step
def s_parexec():
    """par_exec  Parameter Execute DAT|Open Window and Reset View pulses."""
    pe = at(N['HtmlUIDemo'].create(parameterexecuteDAT, 'par_exec'), 400, -400)
    pe.par.op = N['HtmlUIDemo'].path
    pe.par.pars = 'Open Reset'
    pe.par.onpulse = True
    pe.par.valuechange = False
    pe.text = ("def onPulse(par):\n"
               "    if par.name == 'Open':\n"
               "        w = parent().op('WebWindow')\n"
               "        if not w.isOpen:\n"
               "            w.par.winopen.pulse()\n"
               "    elif par.name == 'Reset':\n"
               "        parent().op('logic').module.Reset()\n"
               "    return\n")
    follow(pe)


# ================================================================ webui = what the window shows
@step
def s_webui():
    """webui  Container COMP|What the window shows. Everything below lives inside it."""
    c = at(N['HtmlUIDemo'].create(containerCOMP, 'webui'), 800, 200)
    c.par.w, c.par.h = W, H
    follow(c)


@step
def s_web():
    """web  Web Render TOP|Draws the whole HTML page. Transparent, so the 3D area is a hole."""
    web = at(N['webui'].create(webrenderTOP, 'web'), 0, 200)
    web.par.url.expr = "'http://127.0.0.1:%d/?embed=1&key=%s' % (op.HtmlUI.par.Port, op.HtmlUI.par.Embedkey)"
    web.par.transparent = True
    web.par.dpiscale = DPI                                 # 1 = CSS px are texture px; the page reports its size
    web.par.alwayscook = True                              # otherwise it may never load
    web.par.outputresolution = 'custom'
    web.par.resolutionw, web.par.resolutionh = W, H
    web.par.active.expr = "op.HtmlUI.op('WebWindow') is not None and op.HtmlUI.op('WebWindow').isOpen"
    follow(web)


@step
def s_src():
    """viewport_render  Select TOP|Brings render1 into the container."""
    src = at(N['webui'].create(selectTOP, 'viewport_render'), 0, 0)
    src.par.top = N['render1'].path
    follow(src)


@step
def s_fit():
    """fit  Fit TOP|Scales the render to the hole the page reported."""
    fit = at(N['webui'].create(fitTOP, 'fit'), 200, 0)
    link(fit, N['viewport_render'])
    fit.par.outputresolution = 'custom'
    fit.par.fit = 'fitbest'
    fit.par.resolutionw, fit.par.resolutionh = 980, 630
    follow(fit)


@step
def s_bg():
    """bg  Constant TOP|The fixed background layer at window size."""
    bg = at(N['webui'].create(constantTOP, 'bg'), 200, -150)
    bg.par.colorr, bg.par.colorg, bg.par.colorb, bg.par.alpha = 0.075, 0.071, 0.063, 1
    bg.par.outputresolution = 'custom'
    bg.par.resolutionw, bg.par.resolutionh = W, H
    follow(bg)


@step
def s_place():
    """place  Over TOP|Puts the render at the hole: tx = x, ty = H - y - h."""
    place = at(N['webui'].create(overTOP, 'place'), 400, 0)    # the render at the hole: tx = x, ty = H - y - h
    link(place, N['fit'], N['bg'])
    place.par.size = 'input2'
    place.par.prefit = 'nativeres'
    place.par.justifyh = 'left'
    place.par.justifyv = 'bottom'
    place.par.tunit = 'pixels'
    follow(place)


@step
def s_comp():
    """comp  Over TOP|The page over the placed render."""
    comp = at(N['webui'].create(overTOP, 'comp'), 600, 100)    # the page over it
    link(comp, N['web'], N['place'])
    comp.par.size = 'input2'
    follow(comp)


@step
def s_out():
    """out  Null TOP|The container shows this. top = me.op('out')."""
    out = at(N['webui'].create(nullTOP, 'out'), 800, 100)
    link(out, N['comp'])
    N['webui'].par.top.expr = "me.op('out')"                   # a COMP's own path pars resolve from its PARENT
    follow(out)


@step
def s_panel():
    """panel  Panel CHOP|Mouse position and buttons inside the window."""
    pc = at(N['webui'].create(panelCHOP, 'panel'), 0, -300)
    pc.par.component = '..'
    pc.par.select = 'lselect mselect rselect u v rollu rollv inside wheel shift ctrl alt'
    follow(pc)


@step
def s_tick():
    """exec_tick  Execute DAT|Every frame: hole inside, not under a panel -> TD camera, else -> the page."""
    tick = at(N['webui'].create(executeDAT, 'exec_tick'), 200, -300)
    tick.text = ("def onFrameStart(frame):\n"
                 "    op.HtmlUI.op('logic').module.Tick(parent())\n"
                 "    return\n")
    tick.par.framestart = True
    tick.par.active = True
    follow(tick)


@step
def s_keys():
    """keys  Keyboard In DAT|Keys go to the page, or to the 3D view while the mouse is over it."""
    kb = at(N['webui'].create(keyboardinDAT, 'keys'), 400, -300)
    kb.par.panels = N['webui'].path
    kcb = kb.docked[0] if kb.docked else N['webui'].create(textDAT, 'keys_callbacks')
    kcb.text = ("def onKey(dat, keyInfo):\n"                # TD 2025 signature: one keyInfo namedtuple
                "    op.HtmlUI.op('logic').module.Key(keyInfo, parent())\n"
                "    return\n\n"
                "def onShortcut(dat, shortcutName, time):\n"
                "    return\n")
    kb.par.callbacks = kcb.path
    kb.par.executeloc = 'callbacks'                       # parent() in the callbacks = webui
    follow(kb)


@step
def s_window():
    """WebWindow  Window COMP|Opens the container as an app window."""
    win = at(N['HtmlUIDemo'].create(windowCOMP, 'WebWindow'), 1000, 200)
    win.par.winop = N['webui'].path
    win.par.title = 'HtmlUI Demo'
    win.par.size = 'custom'
    win.par.winw, win.par.winh = W, H
    follow(win)


# ================================================================ run
if SLOW:
    def _do(i, fn):
        if STEP_HOOK:
            STEP_HOOK(i + 1, len(STEPS), fn.__doc__ or fn.__name__)
        fn()
    for i, fn in enumerate(STEPS):
        run(_do, i, fn, delayFrames=1 + i * STEP_FRAMES)
    if ON_DONE:
        run(ON_DONE, delayFrames=1 + len(STEPS) * STEP_FRAMES)
    result = '%d steps, %d frames apart' % (len(STEPS), STEP_FRAMES)
else:
    for fn in STEPS:
        fn()
    if ON_DONE:
        ON_DONE()
    result = 'built /project1/HtmlUIDemo (port %d) - press Demo > Open Window' % PORT
