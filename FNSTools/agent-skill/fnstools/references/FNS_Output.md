# Output

Package `FNS_Output`.

A toolbar button for the perform window: drop an operator to route it, click to open or close, and switch NDI and Spout/Syphon streaming of the same window.

- Category: Show & output
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-output/

## What it does

- **Drop to set the Window Operator**: Dropping a TOP or a COMP on the toolbar button makes it the Window Operator of the /perform window, without opening the Window COMP's parameters.
- **Open the perform window**: Left-clicking the button opens the perform window.
- **NDI streaming**: The right-click popup streams the perform window over NDI to machines on the same network, under NDI Source Name; on by default.
- **Spout and Syphon streaming**: The same popup sends the perform window to other applications on the machine over Spout, or Syphon on macOS, under Sender Name; on by default.
- **Toggle streams from quick-launch**: Switch the NDI and Spout/Syphon streams on and off from quick-launch.
- **Choose the Window COMP**: The button's Perform parameter sets which Window COMP the drop and the click go to, taking effect on the next drop with nothing to re-install.

## Reach it

`op.FNS_OUTPUT` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `NdiActive()`: Whether the NDI output is active.
- `PerformWindowOpen()`: Whether the perform window is open.
- `SpoutActive()`: Whether the Spout output is active.
- `ToggleNdi()`: Enable or disable the NDI output stream.
- `TogglePerformWindow()`: Open or close the FNS perform output window.
- `ToggleSpout()`: Enable or disable the Spout/Syphon output (sender TD_FNS_OUT).

## Commands

- **Toggle NDI output** (id `togglendi`): Enable or disable the NDI output stream. Method `ToggleNdi`.
- **Toggle perform window** (id `toggleperformwindow`): Open or close the FNS perform output window. Method `TogglePerformWindow`.
- **Toggle Spout/Syphon output** (id `togglespout`): Enable or disable the Spout/Syphon output (sender TD_FNS_OUT). Method `ToggleSpout`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Perform Window** (`par.Performwindow`, COMP), default `/perform`: The Window COMP these tools drive. Dropping an operator on the toolbar button sets that window's Window Operator, and the streaming switches below follow the same window.
- **Spout Active** (`par.Spoutactive`, Toggle), default `on`: Stream the perform window to other applications on this machine over Spout (Windows) or Syphon (macOS).
- **Sender Name** (`par.Sendername`, Str), default `TDSyphonSpoutOut`: The name other applications see this Spout/Syphon stream under. Change it when two TouchDesigner instances would otherwise publish the same name.
- **NDI Active** (`par.Ndiactive`, Toggle), default `on`: Stream the perform window over NDI, so machines on the same network can receive it.
- **NDI Source Name** (`par.Name`, Str), default `TouchDesigner`: The NDI source name this machine publishes. It is what receivers pick from their source list, so make it identifiable when several machines are streaming.
