# SearchPalette

Package `FNS_SearchPalette`.

Search field for TouchDesigner's palette browser, installed into the palette on startup. Based on Yea Chen's TD-SearchPalette.

- Category: Interface
- Version: 3.2.11
- Access: Free
- Docs: https://functionstore.tools/docs/fns-searchpalette/

## What it does

- **Find components in the palette browser**: A search field in TouchDesigner's palette browser lists the matching components from every folder; it is put in every time a project opens, or added and removed on demand.
- **Focus the field by hotkey**: `Ctrl+Shift+F` brings TouchDesigner's own palette tab to the front and puts the cursor in an empty search field; the key is rebindable in HotkeyManager.
- **Ranked substring search**: Finds a word anywhere in a name, combines several words, and lists exact, prefix and word-start matches first.
- **Wildcard patterns**: Words with `*` or `?` match as patterns from the front of a name, so a wildcard can only widen the search.
- **Exclude matches with a minus**: A word starting with `-` takes its matches out of the results.
- **Fuzzy fallback for typos and spellings**: When nothing matches as typed, it tries the other side's spelling, initials, a typo, and finally letters in order.
- **Folder search**: A word containing / matches the palette folder, so tools/ on its own lists a whole folder.
- **Latest version only**: Numbered or duplicate copies of one component collapse to the most recently modified file.
- **Jump by word in the field**: The field edits like TouchDesigner's own text fields, including `Ctrl+Left` and `Ctrl+Right` to jump by word.

## Reach it

`op.TDX_SEARCH_PALETTE` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

- `ctrl.shift.f` (`Shortcuts` on `FNS_SearchPalette`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### TD-SearchPalette

- **Auto Install at startup** (`par.Autoinstall`, Toggle), default `on`: Put the search field into TouchDesigner's palette browser every time the project opens. This choice roams with your config, so it holds across projects.
- **Install** (`par.Install`, Pulse): Add the search field to the palette browser now, without waiting for the next project start.
- **Uninstall** (`par.Uninstall`, Pulse): Take the search field back out of the palette browser and leave TD's own UI as it was.
- **Live Search** (`par.Livesearch`, Toggle), default `on`: Rebuild the result list on every keystroke. Off waits until you stop typing, and is worth turning off only if a very large palette makes typing feel heavy.
- **Folder Search (token/)** (`par.Foldersearch`, Toggle), default `on`: Let a token containing '/' match the FOLDER instead of the component name, so 'gen/ noise' means folder ~gen and name ~noise, and 'tools/' on its own lists a folder.
- **Latest Version Only** (`par.Latestonly`, Toggle), default `on`: Collapse numbered versions of one component (tool, tool1, tool2, or the same name in two folders) to the most recently modified file.
- **Search Hotkey** (`par.Shortcuts`, Str): Keyboard shortcut that opens the Palette Browser and focuses this search field. Rebindable here or in FNS_HotkeyManager; combos join with '.' and several are separated by spaces.
- **Hide Palette When Idle** (`par.Autohide`, Toggle), default `off`: Close the palette browser after it has gone unused for the number of minutes below. Unused means the mouse is outside the palette and nothing is being typed into the search field. Off by default; the palette stays open until you close it.
- **Hide After (Minutes)** (`par.Autohideminutes`, Float), default `5.0`: Minutes without interaction before the palette browser closes, when Hide Palette When Idle is on. The countdown restarts whenever the mouse enters the palette or the search field is typed into.

### Help

- **Github Page** (`par.Githubpage`, Pulse): Open the upstream project's GitHub page (Yea Chen's TD-SearchPalette) in your browser.
- **Release Notes** (`par.Releasenotes`, Pulse): Open the upstream project's release notes in your browser.
- **Version** (`par.Version`, Str): The vendored component's own version, as its author numbers it. Not the package version the updater compares.
- **TD Build** (`par.Tdbuild`, Str): The TouchDesigner build this component was authored against.
- **Author** (`par.Author`, Str), default `Yea Chen <yeataro@gmail.com>`: Who wrote the component this package vendors.
