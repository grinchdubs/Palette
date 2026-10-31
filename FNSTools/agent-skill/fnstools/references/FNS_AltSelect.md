# AltSelect

Package `FNS_AltSelect`.

Alternative selection helpers for operators in the network editor.

- Category: Network
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-altselect/

## What it does

- **Drag out a Select with Alt**: Alt-drag a selected operator and it stays where it was, while a Select pointed at it appears where you let go.
- **Match the operator family**: Works for TOPs, CHOPs, SOPs, DATs, POPs and panel COMPs, each getting the matching Select.
- **Ready to use**: The new Select arrives selected and current, with its viewer on and a tint that marks it as a reference.
- **Undo in one step**: A single undo takes the Select away again.
- **Find them later by tag**: Every Select it makes is tagged `FNS_AltSelect`, so a Find or a `findChildren(tags=...)` sweep can list them.

## Reach it

`op.ALT_SELECT` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `OnSelectOP(_op)`: Remember the newly selected operator's position, and its docked operators' positions, for the move check; called when the selection changes.
- `OnUpdate(_op: td.OP)`: Called when a watched operator changes: while the hotkey is held, a move since the selection is handed to onPosChange, which places the matching Select operator.
- `ToggleActive()`: Enable or disable AltSelect.

## Commands

- **Toggle AltSelect** (id `toggleactive`): Enable or disable AltSelect. Method `ToggleActive`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn AltSelect on or off. When on, dragging a selected operator away while the modifier is held leaves a Select OP wired to the original in its place instead of moving it. Off leaves the component installed but idle.
