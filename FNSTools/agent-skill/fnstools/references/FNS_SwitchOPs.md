# SwitchOPs

Package `FNS_SwitchOPs`.

One hotkey jumps focus back and forth between the last two operators you selected, across networks.

- Category: Network
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-switchops/

## What it does

- **Toggle between the last two operators**: Jumps focus back to the operator you were on before this one, and back again on the next press.
- **Jump back across networks**: Remembers the last two selected operators wherever they are, so after diving into a component you return without retracing the path.
- **Rebind the key**: Rebind it on the tool or in HotkeyManager, like every shortcut in the toolkit.

## Reach it

`op.FNS_SWITCHOP` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `OnSelectOP(_op)`: Remember a newly selected operator in the recent list; called when the selection changes.
- `OnSwitch()`: Make the most recently selected other operator current; called by the hotkey.
- `ToggleActive()`: Enable or disable SwitchOPs.

## Commands

- **Toggle SwitchOPs** (id `toggleactive`): Enable or disable SwitchOPs. Method `ToggleActive`.

## Hotkeys

- `ctrl.tab` (`shortcuts` on `keyboardin1`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn SwitchOPs on or off. When on, the switch shortcut jumps focus back and forth between the two most recently selected operators. Off leaves the component installed but idle.
- **Shortcut** (`par.Shortcut`, Str): Hotkey that switches between recently visited operators.
