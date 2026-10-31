# OpenOp

A one-button shortcut to a deeply nested operator: drop it on the field once, then a pulse opens its parameter window, its viewer window, or both.

- Category: Network
- Version: 1.0.4
- Access: Base
- Docs: https://functionstore.tools/docs/openop/

## What it does

- **Shortcut to a nested operator**: Drag an operator onto OpenOp once and it keeps a reference to it wherever you place it, such as beside a control panel.
- **Open the parameter window, viewer or both**: The Open pulse brings up the operator's parameter window, a floating viewer, or both, from wherever you are in the network.
- **Open several operators at once**: One OpenOp can hold several operators and opens all of them on the same pulse.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `openOp` (Open Op) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/OpenOp.tox`. Its promoted methods are called on the placed copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Custom

- **OP** (`par.Op`, OP): The operator(s) to open: drag one or more operators onto this field, or type several paths separated by spaces. A bare name is a sibling of OpenOp; a child of OpenOp needs './name'.
- **Par Window** (`par.Parwindow`, Toggle), default `off`: Open the parameter window of the operator when Open is pulsed.
- **Viewer Window** (`par.Viewerwindow`, Toggle), default `off`: Open a floating viewer of the operator when Open is pulsed.
- **Open** (`par.Open`, Pulse): Open the windows enabled above for the operator(s) in Op.

### Info

- **ReadMe** (`par.Open2`, Pulse): Open this tool's readme.
