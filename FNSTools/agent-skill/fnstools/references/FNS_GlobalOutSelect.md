# GlobalOutSelect

Package `FNS_GlobalOutSelect`.

Browse Global OP Shortcuts and the out operators inside them in a tree, and drag any of them into a network as a Select.

- Category: Network
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-globaloutselect/

## What it does

- **Tree of every shortcut and its outs**: Lists the Global OP Shortcuts in your project in a tree, with the Out operators found inside each one.
- **Drag a row out as a Select**: Dropping a row into a network editor places a Select pointing at that operator.
- **Open a viewer, the parameters or a network editor**: A row opens a viewer, the parameters, or a floating network editor at the operator's location.
- **Refresh only on demand**: The tree is rebuilt only when you press Refresh, so it never takes a frame while you work.

## Reach it

`op.GLOBAL_OUT_SEL` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_HubRegistry`

## Parameters

### Custom

- **Refresh** (`par.Refresh`, Pulse): Rescan the project for global OP shortcuts and their out operators. The list is refreshed only on demand, so that walking the project never costs a frame while you work.
