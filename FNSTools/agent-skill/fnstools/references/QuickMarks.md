# QuickMarks

Bookmark network locations and jump back to them with Ctrl+number. Your marks show on the network editor: a list in a corner you can click, and a pin at each marked spot. Bookmarks stay project-local by design. Based on Alex Guevara's QuickMarks.

- Category: Network
- Version: 3.2.12
- Access: Free
- Docs: https://functionstore.tools/docs/quickmarks/

## What it does

- **Save a mark**: Stores the network you are in, with its pan and zoom, in one of ten numbered slots.
- **Jump to a mark**: Takes you back to a saved mark from anywhere in the project.
- **Remove a mark**: Clears a numbered slot.
- **Save marks in the project file**: Marks live in the project file, so they are waiting the next time you open it.
- **Name and clear marks from quick-launch**: Store, jump to, name, list and clear marks from quick-launch, including slots past the first ten.
- **List marks in a corner**: A corner list shows each mark by number and name and highlights the one you are in; click to jump, right-click to rename.
- **Outline what each mark saved**: Outlines the area each mark saved, with its number and name, in the network you are viewing.
- **Toggle the overlay**: Hides or shows the list and the outlines together, while your marks and their keys keep working.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('QuickMarks')`; its promoted methods are called on that COMP.

## Promoted API

- `ClearMark(slot: int)`: Clear the quickmark stored in the given slot.
- `GetName(key)`: The user's label for a slot, empty when unset.
- `GetQuickmark(key)`: The stored dict for a slot, or None.
- `GoToMark(slot: int)`: Jump to the quickmark stored in the given slot.
- `HandleShortcut(shortcutName)`: Called by the hotkey watcher with the pressed combo: recall, store or clear the slot the digit names, toggle the overlay, or toggle Active.
- `ListMarks()`: List every populated quickmark slot with its name and network.
- `Marks()`: Every populated slot as {index, name, network}.
- `NameMark(slot: int, name: str = '')`: Set the label shown for a quickmark slot.
- `OverlayShown()`: True while the mark list or the outlines are switched on.
- `Quickmark0` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark1` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark2` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark3` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark4` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark5` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark6` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark7` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark8` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Quickmark9` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `RetrieveQuickmark(key)`: Jump the current pane to a stored mark (network, current operator, position, zoom); returns the mark.
- `SetName(key, name)`: Rename a slot.
- `StoreMark(slot: int)`: Store the current network location in the given slot.
- `StoreQuickmark(key)`: Store the current pane's network, current operator, position and zoom under a slot key.
- `ToggleActive()`: Enable or disable QuickMarks.
- `ToggleOverlay()`: Show or hide the mark list and the outlines; marks and Ctrl+number keep working.
- `UnstoreQuickmark(key)`: Clear a slot's mark and name.

## Commands

- **Clear quickmark** (id `clearmark`): Clear the quickmark stored in the given slot. Method `ClearMark`. Params: `slot: int (required)`.
- **Go to quickmark** (id `gotomark`): Jump to the quickmark stored in the given slot. Method `GoToMark`. Params: `slot: int (required)`.
- **List quickmarks** (id `listmarks`): List every populated quickmark slot with its name and network. Method `ListMarks`.
- **Name quickmark** (id `namemark`): Set the label shown for a quickmark slot. Method `NameMark`. Params: `slot: int (required)`, `name: str = ''`.
- **Store quickmark** (id `storemark`): Store the current network location in the given slot. Method `StoreMark`. Params: `slot: int (required)`.
- **Toggle QuickMarks** (id `toggleactive`): Enable or disable QuickMarks. Method `ToggleActive`.
- **Toggle QuickMarks overlay** (id `toggleoverlay`): Show or hide the mark list and the outlines; marks and Ctrl+number keep working. Method `ToggleOverlay`.

## Hotkeys

- `alt.shift.m` (`Overlayshortcut` on `QuickMarks`)
- `ctrl.[0-9] ctrl.alt.[0-9] ctrl.alt.shift.[0-9]` (`Shortcuts` on `QuickMarks`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_OverlayRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `off`: Turn QuickMarks on or off. When on, the number-key shortcuts save, recall and remove marks; the marks themselves are kept in the project file either way. Off leaves the component installed but idle.
- **Shortcuts** (`par.Shortcuts`, Str), default `ctrl.[0-9] ctrl.alt.[0-9] ctrl.alt.shift.[0-9]`: Hotkeys for storing and recalling marks. Character classes such as [0-9] expand.
- **Mark List** (`par.Showlist`, Toggle), default `off`: Show your marks in a corner of the network editor while QuickMarks is active: the one for the network you are in is highlighted, and a click jumps to a mark like Ctrl+number.
- **Overlay Hotkey** (`par.Overlayshortcut`, Str), default `alt.shift.m`: Hotkey that shows or hides the mark list and the outlines together. Your marks and Ctrl+number keep working while they are hidden.
- **List Corner** (`par.Listcorner`, Menu), default `topleft`, menu `topleft`, `topright`, `bottomleft`, `bottomright`: Which corner of the network editor the mark list sits in.
- **List Margin** (`par.Listmargin`, Int), default `12`: How far the mark list sits from the edges of the network editor, and from any other tool's widget before it in the same corner, in screen points.
- **List Order** (`par.Listorder`, Int), default `150`: The mark list's place among the widgets in the same corner: lower sits nearer the corner. The Overlay tab in FNS_Hub sets it when you drag.
- **Pins** (`par.Showpins`, Toggle), default `off`: While QuickMarks is active, outline the area each mark saved, with its number and name, in the network you are viewing.
- **Mark List Collapsed** (`par.Listcollapsed`, Toggle), default `off`: Fold the mark list to its title row. The arrow at the right of the title row does the same.

### Marks

- **Quickmarks** (`par.Mark`, Sequence), default `0`: One block per quickmark slot. Block N is the slot reached by ctrl+N, so the first ten line up with the hotkeys; extra blocks are reachable by command only.
- **Name** (`par.Mark0name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark0data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark1name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark1data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark2name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark2data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark3name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark3data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark4name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark4data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark5name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark5data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark6name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark6data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark7name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark7data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark8name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark8data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Name** (`par.Mark9name`, Str): Your label for this quickmark. Free text, shown in the command palette. Editing it never affects where the mark points.
- **Data** (`par.Mark9data`, Str): The stored location as JSON (network, current child, pan x/y, zoom). Written by Store; edit only if you know the shape.
- **Migrated From Storage** (`par.Migrated`, Toggle), default `off`: Set once the slots have been copied out of the legacy StorageManager into this sequence. The old storage is left in place untouched as a one-time backup; nothing reads it after migration.

### About

- **Help** (`par.Help`, Pulse): Open this tool's documentation page in your browser.
