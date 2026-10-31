# Misc

Package `FNS_Misc`.

Two small toolbar utilities: a Background Viewer toggle for the network's backdrop TOPs and CHOPs, and a global Mouse In CHOP you can drag channels from onto parameters.

- Category: Project
- Version: 3.2.12
- Access: Free
- Docs: https://functionstore.tools/docs/fns-misc/

## What it does

- **Global Mouse In CHOP**: A popup with a global Mouse In CHOP whose channels you drag straight onto parameters, with no operator to place first.
- **Background viewer toggle**: Turns the current pane's backdrop TOP and CHOP viewers on or off in one click.
- **Clear TOP display flags**: Right-click the Background Viewer button to turn off the display flag on every TOP in the current network.

## Reach it

`op.FNS_MISC` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `GlobalMouseActive()`: Whether the global mouse watcher is active (the input_mouse value).
- `OpenToolbarConfigurator()`: Open FNS_Hub on the Toolbar tab (the configurator lives in the hub).
- `ToggleGlobalMouse()`: Toggle the Global Mouse CHOP used for mappings.

## Commands

- **Open toolbar configurator** (id `opentoolbarconfigurator`): Open FNS_Hub on the Toolbar tab (the configurator lives in the hub). Method `OpenToolbarConfigurator`.
- **Toggle global mouse input** (id `toggleglobalmouse`): Toggle the Global Mouse CHOP used for mappings. Method `ToggleGlobalMouse`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

None.
