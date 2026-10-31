# OpToClipboard

Package `FNS_OpToClipboard`.

Copy the selected operator's reference to the system clipboard, ready to paste into an expression.

- Category: Parameters
- Version: 3.2.9
- Access: Free
- Docs: https://functionstore.tools/docs/fns-optoclipboard/

## What it does

- **Copy an operator reference**: `Ctrl+Shift+C` copies a reference to the selected operator, ready to paste into an expression.
- **Resolve the right path wherever you paste**: The pasted reference resolves to the right relative or shortcut path for the operator you paste it into.
- **Copy a parameter reference**: Over a parameter the same shortcut copies that parameter, or the whole group when over the name of a row with several fields.
- **Toggle the tool from quick-launch**: Toggle OpToClipboard switches the tool on and off, and Copy op to clipboard does the same as the key.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('FNS_OpToClipboard')`; its promoted methods are called on that COMP.

## Promoted API

- `CopyOpToClipboard()`: Copy the current operator to the OS clipboard.
- `OnCopy()`: Copy a reference to the hovered parameter, or to the current operator, to the clipboard; called by the hotkey.
- `OnRolloverPar(_op_str, _par_str, _expr)`: Called when a parameter is hovered: a pasted reference to the copied operator in its expression is rewritten as a relative path.
- `ToggleActive()`: Enable or disable OpToClipboard.

## Commands

- **Copy op to clipboard** (id `copyoptoclipboard`): Copy the current operator to the OS clipboard. Method `CopyOpToClipboard`.
- **Toggle OpToClipboard** (id `toggleactive`): Enable or disable OpToClipboard. Method `ToggleActive`.

## Hotkeys

- `shift.ctrl.c` (`shortcuts` on `keyboardin1`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn OpToClipboard on or off. When on, the copy shortcut puts the selected operator's reference on the clipboard ready to paste into an expression. Off leaves the component installed but idle.
- **Shortcut** (`par.Shortcut`, Str): Hotkey that copies the selected operator's reference to the clipboard.
