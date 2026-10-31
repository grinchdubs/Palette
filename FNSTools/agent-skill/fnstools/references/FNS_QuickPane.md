# QuickPane

Package `FNS_QuickPane`.

Pane layout shortcuts.

- Category: Interface
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-quickpane/

## What it does

- **Split by drag gesture**: With a COMP selected, hold the modifiers and drag toward a side: a pane opens there, already inside the COMP and homed. The same drag closes it.
- **Split by arrow keys**: With a COMP selected, `Ctrl+Shift` and an arrow key splits on that side and drops you into the component; the same key closes the pane it opened.
- **Open a pane on each side at once**: Keeps a pane on each side at once, and marks the panes it opened with a green border so you can tell them from your own.
- **Split pane command**: A Split pane quick-launch command asks for the direction, right by default, so you can split without either gesture.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('FNS_QuickPane')`; its promoted methods are called on that COMP.

## Promoted API

- `OnOpenDir(dir='left')`: Split the current pane on the given side (left, right, top or bottom) with a new pane showing the current COMP, sized by the ratio parameters.
- `SplitPane(dir='right')`: Split the current pane in the given direction.
- `ToggleActive()`: Enable or disable QuickPane.

## Commands

- **Split pane** (id `splitpane`): Split the current pane in the given direction. Method `SplitPane`. Params: `dir: menu = 'right'`.
- **Toggle QuickPane** (id `toggleactive`): Enable or disable QuickPane. Method `ToggleActive`.

## Hotkeys

- `ctrl.shift.left ctrl.shift.right ctrl.shift.up ctrl.shift.down` (`Shortcuts` on `FNS_QuickPane`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn QuickPane on or off. When on, holding the modifier and dragging from a selected COMP splits the pane in that direction and navigates into it. Off leaves the component installed but idle.
- **Ratio Horz/Vert** (`par.Ratio`, WH x2), default `0.0`: How much of the pane the new split takes, 0-1: the first value for a horizontal split, the second for a vertical one.
- **Keys** (`par.Keys`, Str): The modifier keys held to trigger this gesture, space-separated (TouchDesigner key names). The default is an expression that picks the right keys per platform. Typing a plain value over it pins the tool to one OS.
- **Pane Shortcuts** (`par.Shortcuts`, Str), default `ctrl.shift.left ctrl.shift.right ctrl.shift.up ctrl.shift.down`: Hotkeys that split and navigate panes. Separate from Keys, which is the held-modifier set.
