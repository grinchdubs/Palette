# ParentHierarchy

Package `FNS_ParentHierarchy`.

Hover a parent in the pane-bar path with Alt to see its parent shortcut, global shortcut and internal operators, and Ctrl to see its custom parameters and values. Click any item to copy a reference to it. It works on the path you already have and adds no button of its own.

- Category: Network
- Version: 3.2.9
- Access: Free
- Docs: https://functionstore.tools/docs/fns-parenthierarchy/

## What it does

- **Shortcuts on Alt-hover**: Hold `Alt` over a COMP in the pane-bar path to see its parent shortcut, global shortcut and internal operators.
- **Parameter values on Ctrl-hover**: Hold `Ctrl` to see where each iop points and every custom parameter with its value; press `Ctrl` again to poll the values.
- **Copy a reference with a click**: Clicking any listed item copies a reference to it, ready to paste into an expression or script.
- **Open parameter customisation**: Right-clicking a listed parameter opens the parameter customisation window for it.
- **Hover the existing path bar**: Works on the path the pane bar already shows, so the bar keeps its buttons and its length.
- **iopBrowser integration**: With iopBrowser installed, the same hover also lists the internal operators in its browser.
- **Extension API on hover**: Each COMP lists its extensions by Extension Name or class; hovering one expands its promoted methods with signatures, properties and typed attributes.
- **Copy extension calls**: Clicking an extension or member copies an ext. reference, such as `ext.TimelineToolsExt.AcceptsDrop(items)`, with the signature intact.

## Reach it

`op.FNS_PARENTHIERARCHY` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `CloseNuggetIfAway()`: Close the hover popup, unless the pointer has landed on it.
- `ExtensionsOf(comp)`: [(label, object)] for a COMP's extensions.
- `GetInfo(comp=None)`: Get parent shortcuts recursively in a list
- `NavbarContent` (property): The text of the pane bar's path field, or None where there is no pane bar beside the widget.
- `NuggetList` (attribute)
- `OnNuggetRollover(info)`: Expand an extension row's public members while the pointer is on it.
- `PanePath` (property): Path of the network this widget navigates -- ALWAYS a string.
- `ParentBarcontainer` (attribute)
- `ParentCompList` (attribute)
- `ParentHierarchyContent()`: Build the parent-shortcut bar text (one entry per ancestor of the pane's network) and return it.
- `ParentNuggetContainer` (attribute)
- `ParentShortcutList` (attribute)
- `ParentShortcuts` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PointerOnNugget()`: Is the pointer on the popup itself (or on its list)?
- `PublicMembersOf(extobj, comp=None)`: Capitalized members of an extension -- what TD promotes to the COMP.
- `SelectParentContent(idx=None, extraInfo=False, extraTrigger=False, showPars=False, showVals=False)`: Act on the clicked entry of the parent bar: fill the nugget with that ancestor's shortcuts, internal ops, extensions and, with ctrl held, its parameters and values.
- `SelectedParentStr` (attribute)
- `ShowHideBar(show)`: Open or close the parent bar.
- `ShowHideNugget(show)`: Open or close the nugget list; a pinned nugget stays open.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_NavbarRegistry`

## Parameters

None.
