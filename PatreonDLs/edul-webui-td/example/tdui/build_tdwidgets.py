# The same UI a third time, from TouchDesigner's stock widgets (Palette > UI > Basic Widgets), default look.
# Builds /project1/TDWidgetDemo with the same layout as the page and tdui/build_tdui.py (toolbar, sidebar sections,
# 3D view, status bar). Each widget's Value0 is *bound* to the HtmlUIDemo parameter, so all three UIs move together.
# Colours and fonts stay TD's defaults on purpose: this is what a TD UI looks like out of the box.
#   Textport / MCP execute_code:  SIZE = (1080, 1080); exec(open('<example>/tdui/build_tdwidgets.py').read())
W, H = globals().get('SIZE') or (1080, 1920)
PORTRAIT = H > W
CW = 540 if PORTRAIT else 720                  # layout in the page's CSS px, scaled to the window
CH = CW * H / W
S = W / CW
VX, VY, VW, VH = (0, 62, 540, 470) if PORTRAIT else (300, 62, CW - 300, CH - 90)
LIB = app.samplesFolder + '/Palette/UI/Basic Widgets/'

proj = op('/project1')
old = proj.op('TDWidgetDemo')
if old is not None:
    w = old.op('TDWWindow')
    if w is not None and w.isOpen:
        raise RuntimeError('Close the TDWidgetDemo window first.')
    old.destroy()
root = proj.create(baseCOMP, 'TDWidgetDemo')
root.nodeX, root.nodeY = 400, -300
root.par.opshortcut = 'TDW'

# one copy of each stock widget, cloned from the Palette
lib = root.create(baseCOMP, 'lib')
lib.nodeX, lib.nodeY = -300, 300
for n in ('sliderHorz', 'buttonToggle', 'buttonRadio', 'buttonMomentary', 'label', 'header', 'footer'):
    wrap = lib.loadTox(LIB + n + '.tox')
    c = lib.copy(wrap.children[0])
    wrap.destroy()
    c.name = n                                   # the wrapper had the same name until now

ui = root.create(containerCOMP, 'ui')
ui.par.w, ui.par.h = W, H
N = {'n': 0}


def px(v):
    return int(round(v * S))


def place(o, parent, x, y, w, h):
    o.par.x, o.par.w, o.par.h = px(x), px(w), px(h)
    o.par.y = parent.par.h.eval() - px(y) - px(h)
    o.nodeX, o.nodeY = (N['n'] % 12) * 160, -(N['n'] // 12) * 160
    N['n'] += 1
    return o


def widget(kind, parent, name, x, y, w, h, label=None):
    o = place(parent.copy(lib.op(kind), name=name), parent, x, y, w, h)
    if label is not None and o.par['Widgetlabel'] is not None:
        o.par.Widgetlabel = label
    for p in ('Labelfontsize', 'Numericfieldfontsize', 'Buttonfontsize', 'Radiofontsize', 'Headerlabelfontsize',
              'Footerlabelfontsize', 'Sliderfontsize'):
        if o.par[p] is not None:
            o.par[p] = int(round(o.par[p].default * S))
    for p in ('Labelwidth', 'Numericfieldwidth'):
        if o.par[p] is not None:
            o.par[p] = int(round(o.par[p].eval() * S * 0.7))
    if kind == 'label':
        o.par.Labelwidth = px(w)                 # a plain label: the text gets the whole width
    if o.par['Sliderlabeldisplay'] is not None:
        o.par.Sliderlabeldisplay = False         # the stock slider prints 'Slider' on itself
    o.par.layer = 1                              # above full-width strips like the toolbar header
    return o


def bind(o, par, lo=None, hi=None):
    v = o.par.Value0
    if lo is not None:
        v.normMin, v.normMax = lo, hi
        v.min, v.max = lo, hi
    v.bindExpr = 'op.HtmlUI.par.%s' % par
    v.mode = ParMode.BIND


def container(parent, name, x, y, w, h):
    return place(parent.create(containerCOMP, name), parent, x, y, w, h)


# ---------------------------------------------------------------- toolbar: header strip + radios + toggles
tb = container(ui, 'toolbar', 0, 0, CW, 62)
title = widget('header', tb, 'title', 0, 0, CW, 62)
title.par.Headerlabel = 'HtmlUI Demo'
title.par.layer = 0
TBX = ((96, 186, 38), (288, 130, 52), (424, 108, 32)) if PORTRAIT else ((120, 220, 46), (350, 150, 60), (508, 110, 36))
shape = widget('buttonRadio', tb, 'shape', TBX[0][0], 12, TBX[0][1], 38, 'Shape')
shape.par.Radiolabels = 'Torus Box Sphere'
shape.par.Labelwidth = px(TBX[0][2])
bind(shape, 'Shape')
wire = widget('buttonToggle', tb, 'wire', TBX[1][0], 12, TBX[1][1], 38, 'Shading')
wire.par.Buttonofflabel, wire.par.Buttononlabel, wire.par.Labelwidth = 'Solid', 'Wire', px(TBX[1][2])
bind(wire, 'Wire')
spin = widget('buttonToggle', tb, 'spin', TBX[2][0], 12, TBX[2][1], 38, 'Spin')
spin.par.Labelwidth = px(TBX[2][2])
bind(spin, 'Spin')

# ---------------------------------------------------------------- 3D view: the same render1, label widgets on top
view = container(ui, 'view', VX, VY, VW, VH)
view.par.top = op.HtmlUI.op('render1').path
view.par.topfill = 'best'
widget('label', view, 'nav', 12, 12, 230, 26, 'Drag orbit  ·  Home reset')
for i, (lab, par, f) in enumerate((('Yaw', 'Yaw', '%d°'), ('Pitch', 'Pitch', '%d°'), ('Dist', 'Dist', '%.1f m'))):
    l = widget('label', view, 'cam_' + par, VW - 144, 12 + i * 26, 132, 26)
    l.par.Widgetlabel.expr = "'%s  ' + %r %% op.HtmlUI.par.%s" % (lab, f, par)
widget('label', view, 'tag', 12, VH - 34, 260, 26, 'TD STOCK WIDGETS · Palette')

# ---------------------------------------------------------------- sidebar sections
side = container(ui, 'side', 0, 532, 540, 400) if PORTRAIT else container(ui, 'side', 0, 62, 300, CH - 90)
COLS = (6, 274) if PORTRAIT else (6, 6)
SL = {'Speed': (0, 360), 'Scale': (.2, 2), 'Hue': (0, 1), 'Sat': (0, 1), 'Light': (0, 2), 'Bg': (0, .5),
      'Fov': (20, 100), 'Dist': (2, 20)}
ROWS = {
    'Motion': [('slider', 'Speed', 'Speed'), ('slider', 'Scale', 'Scale')],
    'Look': [('slider', 'Hue', 'Hue'), ('slider', 'Sat', 'Saturation'), ('slider', 'Light', 'Light'),
             ('slider', 'Bg', 'Background')],
    'Camera': [('slider', 'Fov', 'Field of View'), ('slider', 'Dist', 'Distance'), ('button', 'Reset', 'Reset view')],
    'Render': [('read', 'Res', "'Resolution  %d × %d' % (op.HtmlUI.op('render1').width, op.HtmlUI.op('render1').height)"),
               ('read', 'Rms', "'Render  %.2f ms' % (op.HtmlUI.op('render1').cookTime + op.HtmlUI.op('render1').gpuCookTime)"),
               ('read', 'Pms', "'This UI  %.2f ms' % op.TDW.op('ui').cookTime")],
}


def section(col, y, title, rows):
    x, w = COLS[col], 288 if not PORTRAIT else 260
    widget('header', side, 'h_' + title, x, y, w, 28).par.Headerlabel = title
    for i, r in enumerate(rows):
        ry = y + 30 + i * 32
        kind, name = r[0], r[1]
        if kind == 'slider':
            s = widget('sliderHorz', side, 's_' + name, x, ry, w, 30, r[2])
            bind(s, name, *SL[name])
            s.par.Numericfielddecimalplaces = 0 if name in ('Speed', 'Fov') else 2
        elif kind == 'button':
            b = widget('buttonMomentary', side, 'b_' + name, x, ry, w, 30, r[2])
            b.par.Buttonofflabel = b.par.Buttononlabel = 'Reset'
            b.par.Buttonfont = 'Arial'
            b.par.Offtoonscript0 = 'op.HtmlUI.par.Reset.pulse()'
        else:
            l = widget('label', side, 'r_' + name, x, ry, w, 30)
            l.par.Widgetlabel.expr = r[2]
    return y + 30 + 32 * len(rows) + 10


if PORTRAIT:
    y = section(0, 0, 'Motion', ROWS['Motion']); section(0, y, 'Camera', ROWS['Camera'])
    y = section(1, 0, 'Look', ROWS['Look']); section(1, y, 'Render', ROWS['Render'])
else:
    y = 0
    for name in ('Motion', 'Look', 'Camera', 'Render'):
        y = section(0, y, name, ROWS[name])

# ---------------------------------------------------------------- status bar
perf = root.create(performCHOP, 'perf')
perf.nodeX, perf.nodeY = -300, 0
ft = widget('footer', ui, 'status', 0, CH - 28, CW, 28)
ft.par.Footerlabel.expr = "'Live    FPS %d    studio.edul' % op.TDW.op('perf')['fps']"

# ---------------------------------------------------------------- orbit in the view (no stock widget for that)
pe = root.create(panelexecuteDAT, 'orbit')
pe.nodeX, pe.nodeY = -300, -150
pe.par.panels = view.path
pe.par.panelvalue = 'lselect u v'
pe.par.offtoon = pe.par.valuechange = pe.par.ontooff = True
pe.text = '''def onOffToOn(panelValue):
    if panelValue.name == 'lselect':
        o = panelValue.owner
        me.storage['orbit'] = (o.panel.u.val, o.panel.v.val)
    return

def onValueChange(panelValue, prev):
    o = panelValue.owner
    if panelValue.name in ('u', 'v') and o.panel.lselect and 'orbit' in me.storage:
        u0, v0 = me.storage['orbit']
        u, v = o.panel.u.val, o.panel.v.val
        p = op.HtmlUI.par
        p.Yaw = (p.Yaw.eval() - (u - u0) * o.width * 0.4) % 360
        p.Pitch = max(-85, min(85, p.Pitch.eval() - (v - v0) * o.height * 0.4))
        me.storage['orbit'] = (u, v)
    return

def onOnToOff(panelValue):
    me.storage.pop('orbit', None)
    return

def onWhileOn(panelValue):
    return

def onWhileOff(panelValue):
    return
'''

win = root.create(windowCOMP, 'TDWWindow')
win.nodeX, win.nodeY = 300, 0
win.par.winop = ui.path
win.par.title = 'TD Stock Widgets Demo'
win.par.size = 'custom'
win.par.winw, win.par.winh = W, H
result = 'built %s' % root.path
