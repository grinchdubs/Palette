# The same UI as the web page, built from TouchDesigner's own panel COMPs (for the comparison video).
# Builds /project1/TDPanelDemo: same layout, colours and controls, driving the same HtmlUIDemo parameters, so moving
# a slider in either UI moves it in the other. Run after example/build.py (it needs op.HtmlUI and render1).
#   Textport / MCP execute_code:  exec(open('<example>/tdui/build_tdui.py', encoding='utf-8').read())
# What a panel UI needs that the page gets for free is the point: every position is a number, rounded corners,
# blur, hover states and text layout do not exist, and dragging needs its own Panel Execute code.
W, H = globals().get('SIZE') or (1080, 1920)
PORTRAIT = H > W                               # same rule as the page's CSS: taller than wide = stacked layout
CW = 540 if PORTRAIT else 720                  # layout written in the page's CSS px, scaled to the window
CH = CW * H / W
S = W / CW
VX, VY, VW, VH = (0, 62, 540, 470) if PORTRAIT else (300, 62, CW - 300, CH - 90)    # the 3D view

C = dict(accent=(1, .478, .302), bar=(.137, .133, .125), panel=(.114, .110, .102), group=(.165, .161, .153),
         field=(.078, .075, .067), text=(.953, .937, .910), text2=(.788, .769, .733), text3=(.604, .584, .549),
         green=(.239, .839, .549), chrome=(.086, .082, .075), grid=(.075, .071, .063), glass=(.118, .114, .106))

# slider name -> (parameter, min, max, format)
SLIDERS = {'Speed': ('Speed', 0, 360, '%d'), 'Scale': ('Scale', .2, 2, '%.2f'), 'Hue': ('Hue', 0, 1, '%.2f'),
           'Sat': ('Sat', 0, 1, '%.2f'), 'Light': ('Light', 0, 2, '%.2f'), 'Bg': ('Bg', 0, .5, '%.2f'),
           'Fov': ('Fov', 20, 100, '%d'), 'Dist': ('Dist', 2, 20, '%.1f')}

proj = op('/project1')
old = proj.op('TDPanelDemo')
if old is not None:
    w = old.op('TDWindow')
    if w is not None and w.isOpen:
        raise RuntimeError('Close the TDPanelDemo window first.')
    old.destroy()
root = proj.create(baseCOMP, 'TDPanelDemo')
root.nodeX, root.nodeY = 200, -300
root.par.opshortcut = 'TDUI'

ui = root.create(containerCOMP, 'ui')
ui.par.w, ui.par.h = W, H
ui.par.bgcolorr, ui.par.bgcolorg, ui.par.bgcolorb = C['panel']
ui.nodeX, ui.nodeY = 0, 0
N = {'n': 0}


def px(v):
    return int(round(v * S))


def box(parent, t, name, x, y, w, h, color=None, alpha=1.0):
    """x, y = top-left in CSS px of the parent (panel COMPs count y from the bottom, so convert)."""
    o = parent.create(t, name)
    o.par.x, o.par.w, o.par.h = px(x), px(w), px(h)
    o.par.y = parent.par.h.eval() - px(y) - px(h)
    if color:
        o.par.bgcolorr, o.par.bgcolorg, o.par.bgcolorb = color
        o.par.bgalpha = alpha
    o.nodeX, o.nodeY = (N['n'] % 12) * 160, -(N['n'] // 12) * 160
    N['n'] += 1
    return o


def text(parent, name, x, y, w, h, s, size=13, color='text', bg=None, alignx='left', bold=False, expr=None):
    o = box(parent, textCOMP, name, x, y, w, h, C[bg] if bg else None)
    if not bg:
        o.par.bgalpha = 0
    if expr:
        o.par.text.expr = expr
    else:
        o.par.text = s
    o.par.fontsize = size * S
    o.par.fontcolorr, o.par.fontcolorg, o.par.fontcolorb = C[color]
    o.par.alignx, o.par.aligny = alignx, 'center'
    o.par.textpaddingl = o.par.textpaddingr = 6 * S if alignx != 'center' else 0
    if bold:
        o.par.typeface = 'Bold'
    return o


buttons, sliders = [], []

# ---------------------------------------------------------------- toolbar
tb = box(ui, containerCOMP, 'toolbar', 0, 0, CW, 62, C['bar'])
import os
logo_img = root.create(moviefileinTOP, 'logo_img')                  # studio.edul mark (logo.png next to this file)
logo_img.nodeX, logo_img.nodeY = -300, 150
logo_img.par.file = os.path.join(os.path.dirname(op.HtmlUI.op('logic').par.file.eval()), '..', 'tdui', 'logo.png')
logo = box(tb, containerCOMP, 'logo', 12, 21, 13, 20)
logo.par.bgalpha = 0
logo.par.top, logo.par.topfill = logo_img.path, 'best'
x = 40
for group, par, items in (('SHAPE', 'Shape', [('Torus', 'torus'), ('Box', 'box'), ('Sphere', 'sphere')]),
                          ('SHADING', 'Wire', [('Solid', 0), ('Wire', 1)])):
    gx = x
    for label, val in items:
        b = text(tb, 'b_%s_%s' % (par, val), x, 9, 64, 28, label, 13, 'text', 'field', 'center')
        on = ("op.HtmlUI.par.%s.eval() == %r" % (par, val)) if isinstance(val, str) else ("int(op.HtmlUI.par.%s) == %d" % (par, val))
        for ch, a, b_ in zip('rgb', C['group'], C['field']):
            b.par['bgcolor' + ch].expr = '%r if %s else %r' % (a, on, b_)
        b.store('act', (par, val))
        buttons.append(b)
        x += 66
    text(tb, 'cap_' + par, gx, 40, x - gx, 14, group, 11, 'text3', None, 'center', True)
    x += 14
sp = text(tb, 'b_Spin', x, 11, 40, 24, '', 11, 'text', None, 'center', True,
          expr="'ON' if op.HtmlUI.par.Spin else 'OFF'")
for ch, a, b_ in zip('rgb', C['green'], C['field']):
    sp.par['bgcolor' + ch].expr = '%r if op.HtmlUI.par.Spin else %r' % (a, b_)
sp.par.bgalpha = 1
sp.store('act', ('Spin', 'toggle'))
buttons.append(sp)
text(tb, 'cap_Spin', x - 6, 40, 52, 14, 'SPIN', 11, 'text3', None, 'center', True)
text(tb, 'conn', CW - 100, 16, 88, 30, '', 12, 'text2', 'field', 'center',
     expr="'clients %d' % len(op.HtmlUI.storage.get('html', {}).get('subs', {}))")

# ---------------------------------------------------------------- viewport: the same render1, plus "glass" panels
view = box(ui, containerCOMP, 'view', VX, VY, VW, VH, C['grid'])
view.par.top = op.HtmlUI.op('render1').path
view.par.topfill = 'best'
nav = box(view, containerCOMP, 'nav', 12, 12, 228, 50, C['glass'], .84)
text(nav, 'navcap', 6, 6, 200, 16, 'NAVIGATE', 11, 'text2', None, 'left', True)
text(nav, 'navkeys', 6, 24, 216, 20, 'Drag orbit  ·  Home reset', 12, 'text')
cam = box(view, containerCOMP, 'cam', VW - 144, 12, 132, 76, C['glass'], .84)
for i, (lab, par, f) in enumerate((('Yaw', 'Yaw', '%d°'), ('Pitch', 'Pitch', '%d°'), ('Dist', 'Dist', '%.1f m'))):
    text(cam, 'l' + par, 6, 6 + i * 22, 60, 20, lab, 12, 'text2')
    text(cam, 'v' + par, 60, 6 + i * 22, 66, 20, '', 12, 'text', None, 'right', True,
         expr="'%s' %% op.HtmlUI.par.%s" % (f, par))
wm = box(view, containerCOMP, 'wmark', VW - 38, VH - 46, 22, 34)
wm.par.bgalpha, wm.par.opacity = 0, .14
wm.par.top, wm.par.topfill = logo_img.path, 'best'
text(view, 'tag', 12, VH - 30, 300, 20, '', 12, 'accent', None, 'left', True, expr="'TD PANEL UI · panel COMPs'")

# ---------------------------------------------------------------- side: two columns of grouped rows
side = box(ui, containerCOMP, 'side', 0, 532, 540, 400, C['panel']) if PORTRAIT else     box(ui, containerCOMP, 'side', 0, 62, 300, CH - 90, C['panel'])
COLS = (10, 280) if PORTRAIT else (10, 10)


def section(col, y, title, rows):
    x = COLS[col]
    text(side, 't_' + title, x, y, 250, 28, title.upper(), 11, 'text3', None, 'left', True)
    g = box(side, containerCOMP, 'g_' + title, x, y + 28, 250, 36 * len(rows), C['group'])
    for i, r in enumerate(rows):
        ry = i * 36
        kind, name = r[0], r[1]
        if kind == 'slider':
            par, lo, hi, fmt = SLIDERS[name]
            text(g, 'l_' + name, 4, ry, 84, 36, r[2], 12, 'text2')
            area = box(g, containerCOMP, 's_' + name, 88, ry, 88, 36)
            area.par.bgalpha = 0
            track = box(area, containerCOMP, 'track', 0, 16, 88, 4, C['field'])
            fill = box(area, containerCOMP, 'fill', 0, 16, 88, 4, C['accent'])
            track.par.layer, fill.par.layer = 0, 1               # panel children draw by name otherwise
            fill.par.w.expr = "max(1, int(parent().width * (op.HtmlUI.par.%s - %r) / %r))" % (par, lo, hi - lo)
            knob = box(area, containerCOMP, 'knob', 0, 11, 14, 14, C['accent'])
            knob.par.layer = 2
            knob.par.x.expr = "int((parent().width - me.width) * (op.HtmlUI.par.%s - %r) / %r)" % (par, lo, hi - lo)
            area.store('act', (par, lo, hi))
            sliders.append(area)
            text(g, 'v_' + name, 182, ry + 6, 44, 24, '', 13, 'text', 'field', 'right',
                 expr="%r %% op.HtmlUI.par.%s" % (fmt, par))
            text(g, 'u_' + name, 226, ry, 24, 36, r[3], 12, 'text3')
        elif kind == 'button':
            text(g, 'l_' + name, 4, ry, 150, 36, r[2], 13, 'text2')
            b = text(g, 'b_' + name, 180, ry + 6, 62, 24, r[3], 13, 'text', 'field', 'center')
            b.store('act', (name, 'pulse'))
            buttons.append(b)
        else:                                           # read-out
            text(g, 'l_' + name, 4, ry, 120, 36, r[2], 13, 'text2')
            text(g, 'v_' + name, 120, ry, 124, 36, '', 13, 'text', None, 'right', expr=r[3])
    return y + 28 + 36 * len(rows) + 8


ROWS = {
    'Motion': [('slider', 'Speed', 'Speed', '°/s'), ('slider', 'Scale', 'Scale', '×')],
    'Look': [('slider', 'Hue', 'Hue', ''), ('slider', 'Sat', 'Saturation', ''),
             ('slider', 'Light', 'Light', ''), ('slider', 'Bg', 'Background', '')],
    'Camera': [('slider', 'Fov', 'Field of View', '°'), ('slider', 'Dist', 'Distance', 'm'),
               ('button', 'Reset', 'Reset view', 'Reset')],
    'Render': [('read', 'Res', 'Resolution', "'%d × %d' % (op.HtmlUI.op('render1').width, op.HtmlUI.op('render1').height)"),
               ('read', 'Rms', 'Render', "'%.2f ms' % (op.HtmlUI.op('render1').cookTime + op.HtmlUI.op('render1').gpuCookTime)"),
               ('read', 'Pms', 'This panel UI', "'%.2f ms' % op.TDUI.op('ui').cookTime")],
}
if PORTRAIT:                                   # two columns, like the page
    y = section(0, 0, 'Motion', ROWS['Motion']); section(0, y, 'Camera', ROWS['Camera'])
    y = section(1, 0, 'Look', ROWS['Look']); section(1, y, 'Render', ROWS['Render'])
else:                                          # one sidebar column
    y = 0
    for name in ('Motion', 'Look', 'Camera', 'Render'):
        y = section(0, y, name, ROWS[name])

# ---------------------------------------------------------------- status bar
st = box(ui, containerCOMP, 'status', 0, CH - 28, CW, 28, C['chrome'])
perf = root.create(performCHOP, 'perf')
perf.nodeX, perf.nodeY = -300, 0
text(st, 'live', 6, 0, 60, 28, 'Live', 12, 'text', None, 'left', True)
text(st, 'fps', 70, 0, 80, 28, '', 12, 'text2', expr="'FPS %d' % op.TDUI.op('perf')['fps']")
text(st, 'brand', CW - 120, 0, 114, 28, 'studio.edul', 12, 'text', None, 'right', True)

# ---------------------------------------------------------------- interaction (what the page did with HTML/JS)
code = root.create(textDAT, 'interact')
code.nodeX, code.nodeY = -300, -150
code.text = '''# Panel Execute callbacks: sliders (drag = u while the button is held), buttons (click), viewport orbit.
def _slider(panelValue):
    area = panelValue.owner
    par, lo, hi = area.fetch('act')
    if area.panel.lselect:
        op.HtmlUI.par[par] = lo + max(0.0, min(1.0, area.panel.u.val)) * (hi - lo)

def _button(comp):
    par, val = comp.fetch('act')
    p = op.HtmlUI.par
    if val == 'pulse':
        p[par].pulse()
    elif val == 'toggle':
        p[par] = 0 if p[par].eval() else 1
    else:
        p[par] = val

def onOffToOn(panelValue):
    if panelValue.name == 'lselect':
        if panelValue.owner.fetch('act', None) and len(panelValue.owner.fetch('act')) == 3:
            _slider(panelValue)
        elif panelValue.owner.fetch('act', None):
            _button(panelValue.owner)
        elif panelValue.owner.name == 'view':
            me.storage['orbit'] = (panelValue.owner.panel.u.val, panelValue.owner.panel.v.val)
    return

def onValueChange(panelValue, prev):
    o = panelValue.owner
    if panelValue.name == 'u' and o.fetch('act', None) and len(o.fetch('act')) == 3:
        _slider(panelValue)
    elif panelValue.name in ('u', 'v') and o.name == 'view' and o.panel.lselect and 'orbit' in me.storage:
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
pe = root.create(panelexecuteDAT, 'panel_exec')
pe.nodeX, pe.nodeY = -300, -300
pe.par.panels = ' '.join(o.path for o in buttons + sliders + [view])
pe.par.panelvalue = 'lselect u v'
pe.par.offtoon = pe.par.valuechange = pe.par.ontooff = True
pe.text = code.text
code.destroy()

win = root.create(windowCOMP, 'TDWindow')
win.nodeX, win.nodeY = 300, 0
win.par.winop = ui.path
win.par.title = 'TD Panel Demo'
win.par.size = 'custom'
win.par.winw, win.par.winh = W, H
result = 'built %s (%d buttons, %d sliders)' % (root.path, len(buttons), len(sliders))
