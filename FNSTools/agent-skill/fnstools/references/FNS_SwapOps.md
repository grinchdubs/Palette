# SwapOps

Package `FNS_SwapOps`.

Swap one operator for another while keeping connections intact.

- Category: Network
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-swapops/

## What it does

- **Swap two operators**: Two selected operators trade places and connections, from the hotkey, the toolbar button or quick-launch.
- **Wires stay on their inputs**: Connections keep their input and output numbers, so a Merge or Composite keeps its input order, and COMPs keep their top and bottom connections.
- **Mirror a row**: With more than two operators selected, the row is mirrored end to end.
- **Keep extra inputs in place**: When one operator takes fewer inputs than the other, the inputs it cannot hold stay where they were.
- **Undo the whole swap in one step**: A single undo puts everything back.

## Reach it

`op.SWAP_OPS` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `OnSwap()`: Swap the positions and the wiring of the selected operators, pairwise from the outside in; called by the hotkey.
- `SwapSelected()`: Swap the connections of the selected operators.

## Commands

- **Swap selected ops** (id `swapselected`): Swap the connections of the selected operators. Method `SwapSelected`.

## Hotkeys

- `alt.shift.s` (`Shortcuts` on `FNS_SwapOps`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn SwapOps on or off. When on, the shortcut and the toolbar button swap the selected operators in place. Off leaves the component installed but idle.
- **Swap** (`par.Swap`, Pulse): Swap the operators selected right now, the same action as the shortcut and the toolbar button.
- **Shortcuts** (`par.Shortcuts`, Str), default `alt.shift.s`: Key that swaps the selected operators. Two swap with each other; a longer selection is mirrored end to end.
