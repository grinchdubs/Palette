# Read the result of test_routing.py (run it a few seconds after). Also writes tests/last_result.json.
import json, os
R = op.HtmlUI
t = R.storage.get('test', {})
log, m = t.get('log', []), t.get('marks', {})
# log rows: (frame, Speed, Spin, Shape, Yaw, Pitch, Dist)
row = lambda k: log[m[k]] if k in m and m[k] < len(log) else None
r = {k: row(k) for k in m}
checks = {}
if len(log) > max(m.values() or [0]):
    checks = {
        'embed without key ignored': t.get('embed_without_key_ignored') is True,
        'slider dragged (Speed 45 -> ~288)': 250 < r['slider'][1] < 320,
        'switch clicked (Spin 0 -> 1)': r['switch'][2] == 1,
        'segment clicked (Shape -> box)': r['segment'][3] == 'box',
        'orbit in the hole (Yaw changed)': r['orbit'][4] != 30.0,
        'drag from a glass panel does not orbit': r['glass_drag'][4:6] == r['orbit'][4:6],
        'wheel zooms (Dist < 6)': r['wheel'][6] < 6,
        'Reset button (Yaw 30, Dist 6)': r['reset_button'][4] == 30 and r['reset_button'][6] == 6,
        'tick restored': R.op('webui/exec_tick').par.active.eval(),
    }
folder = os.path.join(os.path.dirname(os.path.dirname(R.op('logic').par.file.eval())), 'tests')
with open(os.path.join(folder, 'last_result.json'), 'w') as f:
    json.dump(dict(checks=checks, rows=r, size=[R.op('webui').width, R.op('webui').height],
                   dpi=R.op('webui/web').par.dpiscale.eval()), f, indent=1)
result = '%d / %d passed' % (sum(checks.values()), len(checks)) if checks else 'not finished yet - read again'
