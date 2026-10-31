# ParRandomizer

Package `FNS_ParRandomizer`.

Randomize parameter values within range, for quick exploration.

- Category: Parameters
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-parrandomizer/

## What it does

- **Randomize an operator**: A click on the toolbar button, or `Alt+Shift+R`, gives every parameter on the selected operator's open page a random value within its range.
- **Randomize one parameter**: Hover a parameter and press `Alt+R`, or drop it on the button, to randomize just that one.
- **Randomize by drag and drop**: Drop an operator on the button to randomize it without selecting it first.
- **Expressions left alone**: Parameters driven by an expression or an export keep their value; only constant and bound ones change.
- **Reset parameters**: `Ctrl+Shift+R` puts the hovered parameter back to its default; Ctrl+right-click or `Ctrl+Shift+Alt+R` resets the whole page.
- **Store current values as defaults**: Ctrl+Shift+right-click makes the current values of the operator's custom parameters their defaults.

## Reach it

`op.FNS_PARRANDOM` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `OnRandomizeOp(_op=None)`: Randomize every enabled parameter on the current page of an operator, the current one by default.
- `OnRandomizeRolloverPar()`: Randomize the parameter under the mouse.
- `OnRayTKChange(info)`: Called when RayTK's shortcut parameters change; checks for a conflict again.
- `OnResetAllCustom(all=False)`: Reset the current operator's custom parameters to their defaults: the current page, or every page with all.
- `OnShortcut(shortcutName)`: Called by the hotkey watcher with the pressed combo; dispatches to randomize, randomize the hovered parameter, reset, or reset all.
- `RandomizeOp()`: Randomize all parameters of the current operator.
- `RandomizePar(_par)`: Give one parameter, or every member of a group, a random value within its range, menu or toggle.
- `RandomizeRollover()`: Randomize the parameter under the mouse.
- `ResetCustomDefaults()`: Reset the current op's custom parameters to their defaults.
- `SaveAllCustomDefaults(_op=None)`: Make every custom parameter's current value, mode and expression its default on an operator, the current one by default.
- `SaveCustomDefaults()`: Store the current custom parameter values as defaults.
- `Shortcutop(_par, _val, _prev)`: Called when the Shortcutop parameter changes; checks for a RayTK shortcut conflict.
- `Shortcutpar(_par, _val, _prev)`: Called when the Shortcutpar parameter changes; checks for a RayTK shortcut conflict.
- `ToggleActive()`: Enable or disable ParRandomizer.

## Commands

- **Randomize pars of op** (id `randomizeop`): Randomize all parameters of the current operator. Method `RandomizeOp`.
- **Randomize rollover par** (id `randomizerollover`): Randomize the parameter under the mouse. Method `RandomizeRollover`.
- **Reset custom pars to defaults** (id `resetcustomdefaults`): Reset the current op's custom parameters to their defaults. Method `ResetCustomDefaults`.
- **Save custom defaults** (id `savecustomdefaults`): Store the current custom parameter values as defaults. Method `SaveCustomDefaults`.
- **Toggle ParRandomizer** (id `toggleactive`): Enable or disable ParRandomizer. Method `ToggleActive`.

## Hotkeys

- `alt.r` (`Shortcutpar` on `FNS_ParRandomizer`)
- `alt.shift.r` (`Shortcutop` on `FNS_ParRandomizer`)
- `ctrl.alt.shift.r` (`Shortcutresetallcustom` on `FNS_ParRandomizer`)
- `ctrl.shift.r` (`Shortcutreset` on `FNS_ParRandomizer`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn ParRandomizer on or off. When on, the toolbar button, drag-and-drop and the shortcuts below randomize parameters. Off leaves the component installed but idle.
- **Shortcut Randomize OP** (`par.Shortcutop`, Str), default `alt.shift.r`: Key that randomizes every value slider on the selected operator.
- **Shortcut Randomize Rollover Par** (`par.Shortcutpar`, Str), default `alt.r`: Key that randomizes just the parameter the mouse is over.
- **Shortcut Reset Parameter** (`par.Shortcutreset`, Str), default `ctrl.shift.r`: Key that puts the parameter under the mouse back to its default.
- **Shortcut Reset All Custom** (`par.Shortcutresetallcustom`, Str), default `ctrl.alt.shift.r`: Key that puts every parameter on the hovered parameter's page back to its default.
