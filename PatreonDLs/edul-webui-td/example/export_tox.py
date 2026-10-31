# Save /project1/HtmlUIDemo as HtmlUIDemo.tox for people who just want to drop it into TD (no Claude, no files).
# The text DATs are file-synced while you develop; the .tox gets their text embedded instead, so it works anywhere.
# Run inside TD after build.py.
import os
R = op.HtmlUI
folder = os.path.dirname(os.path.dirname(R.op('logic').par.file.eval()))
synced = {d: d.par.file.eval() for d in R.findChildren(type=textDAT) if d.par.syncfile.eval()}
for d in synced:
    d.par.syncfile = False                 # the DAT keeps its current text
    d.par.file = ''
path = os.path.join(folder, 'HtmlUIDemo.tox').replace('\\', '/')
saved = {k: R.storage.pop(k) for k in ('html', 'test') if k in R.storage}   # runtime / test state stays out
R.save(path)
R.storage.update(saved)
for d, f in synced.items():                # back to editing from disk
    d.par.file = f
    d.par.syncfile = True
result = path
