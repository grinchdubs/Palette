---
name: edul-webui-td
description: Web UI for TD. Build a TouchDesigner app UI as a web page (HTML/CSS/JS) shown inside a TD window (Web Render TOP) with TD's own 3D render composited into a transparent hole in the page, mouse/keys routed between the page and TD, control data over a local WebSocket served by a Web Server DAT, or (easier, optional) as plain channels through Studio Edul's WebSocket In / Out CHOP plugin. Use when a TD project wants a web-designed UI (app-like, Figma style) instead of panel COMPs, optionally also reachable from browsers on the LAN.
---

# Web UI for TD (a web page inside TouchDesigner)

A complete, tested example ships with this skill in `example/` (TD 2025.33070): `build.py` builds the whole network,
`td/logic.py` + `td/server_cb.py` are the TD side, `web/` is the page, `tests/` drives it with fake input.
**Start from it**: copy the folder, run `build.py`, then replace the torus scene and the page controls with the
user's own. Only write from scratch if the user asks.

## Idea in one picture

```
 <root> baseCOMP (opshortcut, custom pars = the values the page may touch)
   server      Web Server DAT  HTTP: page files from text DATs | WebSocket: JSON control
   logic       text DAT (file-synced .py) protocol, value push, sizes, mouse routing
   webui       containerCOMP   top = me.op('out')   <- what the window shows
     web            Web Render TOP  http://127.0.0.1:<port>/?embed=1&key=<key>  transparent, the whole UI
     viewport_render  select TOP -> your Render TOP (rendered at the hole size)
     fit            Fit TOP (res = hole)      bg  Constant TOP (window size, the fixed layer)
     place          Over TOP: fit over bg at the hole  (tx = x, ty = H - y - h)
     comp           Over TOP: web over place -> out (null)
     panel          Panel CHOP of webui     keys  Keyboard In DAT (panels = webui)
     exec_tick      Execute DAT onFrameStart -> logic.Tick(webui)
   WebWindow   windowCOMP  winop = webui
```

- The picture never goes over the network: TD renders and TD composites. The WebSocket only carries small JSON.
- The same page works in a normal browser without `?embed=1` (tablet / laptop on the LAN): controls only.

## Prerequisites

- TouchDesigner 2025.x. Non-Commercial licences cap TOP resolution at 1280 x 1280 -> keep the window <= 1280 wide.
- An MCP server inside TD that can run Python (e.g. TDMCP: `execute_code`, `get_help`, `view_operator`).
  Check parameter names with `get_help` before setting them; TD abbreviates unpredictably.
- Never destroy or re-create a window COMP while it is open (it has hung TD with a GPU driver error).
  Close it, rebuild, open it again in a later call.

## Protocol (example/td/logic.py)

```
page -> TD  {"op":"sub"}                                   push me every value now, then diffs
            {"op":"set", "name":"Speed", "value":90}        write a whitelisted custom parameter
            {"op":"embed", "key":K, "vp":[x,y,w,h], "hit":[[x,y,w,h]...], "modal":false}
TD -> page  {"op":"vals", "vals":{"Speed":90, ...}}         changed values only, ~10 Hz (every 6th frame)
```
- Whitelist what the page may write (`EXPOSED`). Never expose file paths or operator references.
- `embed` (where the hole and the floating panels are) must come only from TD's own Web Render TOP. A browser on the
  same PC also connects from 127.0.0.1, so check a key that only the Web Render TOP's URL carries (`Embedkey` par).

## Two ways to sync values: built-in only, or with WebSocket In / Out CHOP

Ask which one the user wants if it isn't clear. Check whether the plugin is installed first (the `websocket-chop`
skill's `scripts/ws_inspect.py` lists WebSocket In / Out nodes and the ports already in use).

**A. Built-in only (default, what `example/` does).** No plugin. The Web Server DAT's WebSocket carries the
protocol above; `logic.py` parses each message, checks `EXPOSED` and pushes the diff every 6th frame. Works on any TD
2025 install, so a shared `.tox` needs nothing else.

**B. With WebSocket In / Out CHOP (easier, needs the plugin).** Studio Edul's C++ CHOPs
([releases](https://github.com/studio-edul/WebSocketCHOP/releases), macOS + Windows) turn JSON into channels and
channels into JSON with no Python. Numeric values move to the CHOPs; the Web Server DAT stays for the rest.
```
 page --{"Speed":90}--> ws_in   WebSocket In CHOP, Mode Server, Port 9982 -> select_ui (only the allowed names) -> null_ui_in
                                custom pars:  Speed = op('null_ui_in')['Speed']   (or export the channels)
 page <--{"Speed":90}-- ws_out  WebSocket Out CHOP, Mode Server, Port 9983 <- parameter_ui (the root's custom pars)
 server (Web Server DAT, 9981)  HTTP page files + the embed / probe messages + strings and menus, as in A
```
- The page opens two more sockets: `new WebSocket('ws://' + location.hostname + ':9982')` to send,
  `:9983` to receive. Send flat objects keyed by the parameter name: `{"Speed": 90}`. Several values in one message
  are fine; keys missing from a message keep their value.
- Receiving: a new page gets the full state first, so `{"op":"sub"}` is not needed. With Out `Send Mode = On Change` +
  `Changed Keys Only` the page merges (`state = {...state, ...msg}`). Keep `dragging` in app.js: do not overwrite a
  control the user is holding.
- Whitelist = the Select CHOP's channel names. Unselected keys arrive as channels in `ws_in` but drive nothing. Never
  select file paths or operator references (they cannot be channels anyway: strings go to the In node's Info DAT).
- Pulses (`Reset`): the page sends `{"Reset":1}` then `{"Reset":0}`; TD shows 1 for exactly one frame. Drive the pulse
  with a CHOP Execute DAT `onOffToOn`, or keep pulses on the Web Server DAT protocol.
- Strings and menus (`Shape`) stay on the Web Server DAT (`{"op":"set"}`): channels carry numbers only. The `embed`
  message (key string + rectangle lists) also stays there, with its key check.
- Before the first message a channel does not exist yet, so an expression that reads it errors. Fall back to the
  parameter's default (`op('null_ui_in')['Speed'] or 90`), or have the page send its full state on open.
- Ports: three now (HTTP 9981, In 9982, Out 9983), all `ws://` on the LAN. Open them in the firewall for tablets.
- What it saves: the value parsing and diff push in `logic.py` (`Receive` set / sub, the 6-frame push loop) and the
  per-message Python; values update every frame instead of ~10 Hz. Worth it with many values or fast controls.
- Not yet built into `example/` - verify on build: read `null_ui_in` / the Out node's Info DAT (`last_message`) and
  drag a page slider once. Look up the built-in operators' parameter names with `get_help`; the plugin's own
  parameters are in the `websocket-chop` skill.

## Web Server DAT details (TD 2025)

- Callbacks: `onHTTPRequest(dat, request, response)` returns `response`; `onWebSocketOpen(dat, client, uri)`,
  `onWebSocketClose(dat, client)`, `onWebSocketReceiveText(dat, client, data)`. `client` is `"ip:port"`.
- The query string is NOT in `request['uri']` (`/?embed=1` arrives as uri `/`); it comes in `request['pars']`.
- Headers are plain response keys: `response['content-type'] = 'text/javascript; charset=utf-8'` (ES modules need a
  JS MIME type), `response['cache-control'] = 'no-cache'`. Status: `statusCode`, `statusReason`, body `data`.
- Serve page files from file-synced text DATs (`par.file` absolute path + `par.syncfile = True`): edits on disk show on
  the next reload. Send with `dat.webSocketSendText(client, json.dumps(...))`.
- Creating a Web Server DAT or Keyboard In DAT from Python docks a default callbacks DAT. Destroy it or reuse it.

## The page in embed mode (example/web/app.js, style.css)

- `html.embed, body, .app, .main, .viewport {background: transparent}`; bars with their own colour keep it.
- `html.embed {user-select: none}` - otherwise drags select text.
- Hide the page's own preview; report layout `{op:'embed', key, vp, hit, modal}` from `getBoundingClientRect()`
  (viewport + every floating panel over it) on change, on resize and every 1 s.
- While the user holds a control, do not overwrite it from TD's value push (`dragging` in app.js).
- Key from the URL (`?key=`), sent with every `embed` message.

## TD side - exact parameters (all verified)

- Web Render TOP: `transparent=True`, `alwayscook=True` (otherwise it may never load),
  `outputresolution='custom'` + `resolutionw/h` = container size, `url` by expression,
  `active` = window open (Chromium only runs while it is shown). **Created from Python it starts with
  `active=False`** - set it (or its expression) or `executeJavaScript` fails with "Cannot execute Javascript".
  A plain file path works as `url` for local pages (overlays); `file:///` did not load.
- When the window opens, pulse `reload` ~10 frames later: a page requested before Chromium started can stay blank.
- `dpiscale`: 1 = CSS px are texture px. For a phone-sized / vertical video use e.g. 1080 x 1920 with `dpiscale=2`
  (the page lays out at 540 x 960 and is drawn sharp). Then the page must send its own size
  (`size:[innerWidth, innerHeight]`) with the layout and TD scales the rectangles by `texture width / size[0]`,
  and `interactMouse` should use normalized coordinates (`pixels=False`, 0..1 from the bottom-left).
  A CSS `@media (orientation: portrait)` block turns the same page into the vertical layout.
- Container `top` param: **`me.op('out')`** - a COMP's own path params resolve from its PARENT (`'out'` = blank window).
- Fit TOP `outputresolution='custom'`, `fit='fitbest'`. Over TOP `place`: input 1 = fit, input 2 = bg,
  `size='input2'`, `prefit='nativeres'`, `justifyh='left'`, `justifyv='bottom'`, `tunit='pixels'`, `tx = x`,
  `ty = H - y - h`. Over TOP `comp`: input 1 = web, input 2 = place, `size='input2'`.
- Set sizes from Python only when they change; no extension calls in parameter expressions.
- Panel CHOP: `component='..'`, `select='lselect mselect rselect u v rollu rollv inside wheel shift ctrl alt'`.
- Keyboard In DAT: `panels` = the container, `executeloc='callbacks'`, callback **`onKey(dat, keyInfo)`** (one
  namedtuple: `key`, `character`, `shift`, `alt`, `ctrl`, `state` ...). Not the old long positional signature.
- Window COMP: `winop` = container path, `size='custom'`, `winw/winh`, open with `par.winopen.pulse()`.

## Input routing (every frame, logic.Route)

- Position: **`rollu/rollv` while hovering, `u/v` while a button is held**. Page coords `x = u*W`, `ytop = (1-v)*H`.
- target = `'vp'` if inside the hole, not inside any hit rect, no modal; else `'web'`. **Capture** the target on
  button-down until all buttons are up (a slider drag that leaves the panel keeps going to the page).
- web: `web.interactMouse(x / W, (H - ytop) / H, left=l, middle=m, right=r, wheel=w, pixels=False)` (bottom-left
  origin; `left=True` first = down, again = drag, `False` = up). Send only when position/buttons change.
- hole: drive the user's viewer. With no viewer, orbit the camera from the drag delta (example: Yaw/Pitch/Dist pars ->
  camera translate + `lookat`). Render at the hole size (`Render TOP resolution = w, h`).
- keys: to the viewer while the mouse was last over the hole, else `web.sendKey(key, char=, shift=, alt=, ctrl=)`.
- Window closed: forget held buttons / capture, Web Render inactive.

## Testing without a real mouse

The agent cannot move the mouse. Pause the real `exec_tick` (its panel values are zeros while the mouse is outside the
window and would land between fake frames as a button-up), then feed fake panel dicts one frame apart with
`run(code, values, delayFrames=...)` into `logic.Tick(webui, values)`, read results a few seconds later, re-enable
`exec_tick`. Do not hard-code control positions: TD sends `{op:'probe'}` and the page answers with the rectangles of
every `[data-par]` / `[data-pulse]` element, so the same test runs at any size. See `example/tests/test_routing.py`
(run twice: probe, then input) / `test_read.py` (pass / fail per check). Call the Keyboard In callback module directly
with a fake keyInfo namedtuple. Verify visually by capturing the **container the window shows**
(`view_operator` on `webui`), not an inner TOP. Ask the user to drag once with the real mouse at the end.

## Gotchas measured

- Web Render TOP: 0.2 - 0.7 ms for a 1280-1700 px page.
- There is no JS -> TD call in the Web Render TOP (TD -> JS only: `executeJavaScript`). Use the local WebSocket.
- Sending TD renders to browsers as JPEG (`TOP.saveByteArray('.jpg')`) costs ~18 ms main thread per frame. For remote
  video use WebRTC (`webrtcDAT` + Video Stream Out TOP `mode=webrtc`), signalling over the same WebSocket.
- Recording: render-only material (the app, overlays) goes straight from a TOP into a Movie File Out TOP - nothing on
  screen can leak in. A Screen Grab TOP copies a screen *area*: whatever covers the window is recorded. Make the
  window topmost while recording (`user32.SetWindowPos` with `argtypes` set, `HWND(-1)`; without argtypes it silently
  does nothing) and check a frame before you start. A floating network editor
  (`ui.panes.createFloating(type=PaneType.NETWORKEDITOR, maxWidth=1080)`) gives a vertical network view.
- To share without files: turn `syncfile` off on the text DATs (they keep their text) and `COMP.save('x.tox')`
  (`example/export_tox.py`).
