# OpenExt

Package `FNS_OpenExt`.

Open an operator's extension source quickly.

- Category: Developer
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-openext/

## What it does

- **Open extension by hotkey**: `Ctrl+E` on a COMP opens its first promoted extension in the external editor TouchDesigner is set to use; on a COMP without one nothing happens.
- **Command palette entry**: Also published as the quick-launch command Open extension of current, so it runs from the command palette without the hotkey.
- **Sync edits back with VSCodeTools**: With the extension synced to a file by VSCodeTools, every save in your editor lands back in the running component.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('FNS_OpenExt')`; its promoted methods are called on that COMP.

## Promoted API

- `OnOpen()`: Open the current COMP's promoted extension source in the editor; called by the hotkey.
- `OpenCurrentExt()`: Open the extension code of the current COMP.

## Commands

- **Open extension of current** (id `opencurrentext`): Open the extension code of the current COMP. Method `OpenCurrentExt`.

## Hotkeys

- `ctrl.e` (`Shortcuts` on `FNS_OpenExt`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### About

- **Shortcuts** (`par.Shortcuts`, Str): Key that opens the selected COMP's promoted extension in your external editor. The default is an expression that picks the right keys per platform. Typing a plain value over it pins the tool to one OS.
