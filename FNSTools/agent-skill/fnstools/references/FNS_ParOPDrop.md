# ParOPDrop

Package `FNS_ParOPDrop`.

Create Parameter CHOP/DAT and Parameter Execute DAT nodes inside a COMP from its custom parameters, by drag and drop or hotkey.

- Category: Parameters
- Version: 3.2.12
- Access: Free
- Docs: https://functionstore.tools/docs/fns-paropdrop/

## What it does

- **Parameter CHOP, DAT or Execute DAT by drop**: Inside a COMP, drop one of its custom parameters on the toolbar button with modifiers held for a Parameter CHOP, Parameter DAT or Parameter Execute DAT already pointed at it.
- **Hotkeys over parameters**: Hover a parameter and press `P` with the same modifiers, no dragging needed.
- **Collect several parameters in one operator**: While the operator it made is current, the next parameter you add with the same modifiers joins it.
- **Execute DATs from operator drops**: Drop a CHOP, one channel or a DAT on the button for a CHOP Execute or DAT Execute DAT already watching it.

## Reach it

`op.FNS_POP` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `OnChopPre(value: bool)`: Called when the CHOP pre-place toggle changes; clears the pending parameter CHOP when off.
- `OnDatExecPre(value: bool)`: Called when the DAT Execute pre-place toggle changes; clears the pending parameter execute DAT when off.
- `OnDatPre(value: bool)`: Called when the DAT pre-place toggle changes; clears the pending parameter DAT when off.
- `OnDropOperator(item)`: A CHOP / Channel / DAT dropped on the icon -> its Execute DAT.
- `OnPlaceParOp(_par=None)`: Place the parameter operator the mode names (CHOP, DAT or DAT Execute) for the hovered or given parameter beside the current operator; called by the hotkey.
- `ToggleActive()`: Enable or disable ParOPDrop.

## Commands

- **Toggle ParOPDrop** (id `toggleactive`): Enable or disable ParOPDrop. Method `ToggleActive`.

## Hotkeys

- `p` (`Keys` on `FNS_ParOPDrop`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn ParOPDrop on or off. When on, dragging a custom parameter onto the toolbar button (or pressing its hotkey over one) creates the matching Par CHOP, Par DAT or ParExec DAT inside the COMP. Off leaves the component installed but idle.
- **Key** (`par.Keys`, Str), default `p`: Key held to drop an operator reference onto a parameter. Modifiers are ignored.
