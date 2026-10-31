# QuickCollapse

Package `FNS_QuickCollapse`.

Collapse a selection into a component, with an optional customize dialog.

- Category: Network
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-quickcollapse/

## What it does

- **Collapse the selection into a Base COMP**: Moves the selected nodes into a new Base COMP, wired as they were, and takes you inside it.
- **Name it as you collapse**: A second key asks for the new COMP's name and parent shortcut first, in a small dialog.
- **Undo the whole collapse in one step**: Undo reverses the whole collapse in one step and returns you to the network you collapsed from.
- **Collapse from quick-launch**: Collapse selected runs the same collapse from quick-launch.

## Reach it

`op.FNS_QUICKCOLLAPSE` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `CollapseSelected()`: Collapse the selected operators into a container.
- `OnCollapse(customize=False)`: Collapse the selected operators into a base COMP, after a name dialog when customize is on; called by the hotkey.
- `OnCustomizeCallback(info)`: Called when the name dialog closes; collapses with the entered name and shortcut when OK was pressed.
- `ToggleActive()`: Enable or disable QuickCollapse.

## Commands

- **Collapse selected** (id `collapseselected`): Collapse the selected operators into a container. Method `CollapseSelected`.
- **Toggle QuickCollapse** (id `toggleactive`): Enable or disable QuickCollapse. Method `ToggleActive`.

## Hotkeys

- `ctrl.shift.w` (`Shortcutcustomize` on `FNS_QuickCollapse`)
- `ctrl.w` (`Shortcut` on `FNS_QuickCollapse`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn QuickCollapse on or off. When on, the shortcuts below collapse the selected nodes into a Base COMP. Off leaves the component installed but idle.
- **Shortcut** (`par.Shortcut`, Str), default `ctrl.w`: Key that collapses the selected nodes into a new Base COMP straight away, with no dialog.
- **Shortcut Customize** (`par.Shortcutcustomize`, Str), default `ctrl.shift.w`: Key that collapses the selection but asks first, with a dialog for the new COMP's name and its parent shortcut.
