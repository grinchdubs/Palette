# PasteFromClipboard

Paste the image on the clipboard into the current network as a Movie File In, a Script TOP or an annotation. Windows only.

- Category: Network
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/pastefromclipboard/

## What it does

- **Paste a clipboard image**: `Alt+V` pastes the image on the clipboard into the current network, at the mouse, with three ways to paste on the keys `1`, `2` and `3`.
- **Paste as Movie File In**: Saves the image in the tool's Save Folder, clipboard_images by default, and reads it with a Movie File In.
- **Paste as locked Script TOP**: Stores the image in a locked Script TOP, which grows the .toe file but avoids external dependencies.
- **Paste as annotation**: Pins the image in the network as an annotation the size of the image, kept inside the .toe like the Script TOP.
- **Paste image files**: Image files copied in Explorer paste from the original files, several at once, laid out in a row.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('PasteFromClipboard')`; its promoted methods are called on that COMP.

## Promoted API

- `BITMAPINFOHEADER` (attribute)
- `Bypass()`: Handle bypass state change.
- `CF_BITMAP` (attribute)
- `CF_DIB` (attribute)
- `CF_DIBV5` (attribute)
- `CloseClipboard` (attribute)
- `DragQueryFile` (attribute)
- `EnumClipboardFormats` (attribute)
- `GetClipboardData` (attribute)
- `GlobalLock` (attribute)
- `GlobalSize` (attribute)
- `GlobalUnlock` (attribute)
- `OnPopMenuCallback(infoDict)`: Called when a menu item is chosen (File In, ScriptTOP or Annotate); pastes in that form and closes the menu.
- `OnPopMenuShortcut(keyInfo)`: Called by the menu's key watcher; a pressed shortcut picks its menu item.
- `OnShortcut(shortcutName=None)`: Called by the hotkey: when the clipboard holds an image, open the menu that picks the paste form.
- `OpenClipboard` (attribute)
- `PasteAnnotate()`: Paste the clipboard image into an annotate.
- `PasteImage()`: Paste the clipboard image into the network.
- `PasteScriptTop()`: Paste the clipboard image as a Script TOP.
- `Pasteannotate()`: Paste the clipboard image as an annotate COMP.
- `Pasteimage()`: Paste the clipboard image into the current network as a Movie File In TOP.
- `Pastescriptop()`: Paste the clipboard image as a Script TOP.
- `PopMenuItemsShortcuts` (attribute)
- `RGBQUAD` (attribute)
- `Showbuiltin()`: Handle show built-in parameters toggle.
- `UpdateMouseData()`: Update mouse and camera data tables and return mouse data

## Commands

- **Paste as annotate** (id `pasteannotate`): Paste the clipboard image into an annotate. Method `PasteAnnotate`.
- **Paste image** (id `pasteimage`): Paste the clipboard image into the network. Method `PasteImage`.
- **Paste as Script TOP** (id `pastescripttop`): Paste the clipboard image as a Script TOP. Method `PasteScriptTop`.

## Hotkeys

- `alt.v` (`Shortcut` on `PasteFromClipboard`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Settings

- **Paste Image** (`par.Pasteimage`, Pulse): Paste image from clipboard as TOP
- **Paste As ScriptOP** (`par.Pastescriptop`, Pulse): Paste image from clipboard as a scriptTOP
- **Paste As Note** (`par.Pasteannotate`, Pulse): Paste image from clipboard as an annotate component
- **Shortcut** (`par.Shortcut`, Str), default `alt.v`: Key that pastes the image on your clipboard into the current network. Once pressed, 1 / 2 / 3 choose Movie File In, locked Script TOP or Annotate.
- **Save Folder** (`par.Folderpath`, Str), default `clipboard_images`: Folder to save images
- **Position at Mouse** (`par.Positionatmouse`, Toggle), default `on`: Position image at current mouse location
- **Copy Pasted Files** (`par.Copyfiles`, Toggle), default `on`: When the clipboard holds image files copied in Explorer, copy each one into the Save Folder so the pasted File In keeps working if the original moves. Off: the File In reads the original file where it is.
- **Status** (`par.Status`, Str): What the tool is doing, or why it cannot: read-only. It reports the Windows-only limitation here rather than failing silently on macOS.
- **Image Width** (`par.Imagewidth`, Int), default `0`: Width of last pasted image
- **Image Height** (`par.Imageheight`, Int), default `0`: Height of last pasted image

### About

- **Bypass** (`par.Bypass`, Toggle), default `off`: Switch the whole component off. It is set automatically on anything but Windows, where the clipboard route this tool uses does not exist.
- **Show Built-in Parameters** (`par.Showbuiltin`, Toggle), default `off`: Show TouchDesigner's built-in parameter pages on this component alongside its custom ones. Off keeps the parameter dialog to just this tool's own controls.
- **ChatTD Operator** (`par.Chattd`, OP): Optional: a ChatTD operator for this component to talk to. Leave it empty unless you use DotSimulate's ChatTD.
