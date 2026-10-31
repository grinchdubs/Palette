# CommandPalette

Package `FNS_CommandPalette`.

A command palette inside TouchDesigner: every command your FNS tools declare and TouchDesigner's own palette components in one ranked list, opened with a hotkey and aware of what you are looking at. Manage favourites and hidden commands from its tab in Hub.

- Category: Interface
- Version: 3.2.18
- Access: Free
- Docs: https://functionstore.tools/docs/fns-commandpalette/

## What it does

- **Find any command on one key**: Opens over the network you are in with every command your FNS tools declare, TouchDesigner's built-in commands and its palette components in one ranked list.
- **Context-aware ranking**: Commands about the parameter under your mouse, the selected operator or the current network come first.
- **Typo-tolerant search**: Initials, typos, letters in order and British or American spellings all find a command, with strict matches ranked first.
- **Search by what a command does**: A word from a command's help or its tool's documentation finds it, so `copy` finds PasteFromClipboard, and the row says why it matched.
- **Actions first for words like copy**: A word that starts command titles, such as copy, open or reset, lists the commands that start with it first, then components named with it.
- **Scoping prefixes**: A leading character narrows the list to commands, tool commands, components or one tool's commands.
- **Navigate the network**: `/` is the root, `./` where you came from and each `..` a level up; Right drills into a row and Left backs out.
- **Step through a command's values**: A command that takes values asks for them one at a time: a menu as pick rows, anything else as a field naming its type and default.
- **Presets that run on Enter**: `Alt+S` saves a command with its values as a preset row, which runs on Enter without prompting.
- **Place palette components**: TouchDesigner's palette components, your own folders included, land on your mouse ready to place, or drag into any pane.
- **Stars and hidden commands**: Star commands with `Ctrl+D` to lead their tier, and hide the ones you never use with `Ctrl+H`.
- **Rank by usage**: Commands you run often rank higher, the lift fading over a couple of weeks unused; Rank By Usage switches it off.
- **Query history**: `Alt+Up` and `Alt+Down` cycle through the queries you have run before.
- **Commands tab in Hub**: Every registered command, hidden ones included, with Star and Hidden toggles shared with TDX Launcher Ultra.
- **Install from the palette**: A tool you can install but have not yet shows as an Install row; Enter installs it.
- **Call extension methods**: `~` lists the public methods of a COMP's extensions and calls them with the arguments you type.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('FNS_CommandPalette')`; its promoted methods are called on that COMP.

## Promoted API

- `Activate(row: dict, args: dict = None)`: Enter on a row.
- `ActivateSelected()`: Enter.
- `CaptureContext()`: Snapshot what the user is looking at, BEFORE the window opens.
- `Catalogue(rebuild: bool = False)`: Every row the palette can offer, commands first.
- `Choose(onChosen, title: str = None)`: Open the palette as a picker: Enter or a click on a command or a preset hands it to onChosen instead of running it, as a dict {'key', 'label', 'kwargs'}; closing without a pick calls onChosen(None).
- `ClearUsage()`: Forget this palette's usage history.
- `Context()`: The active snapshot, capturing one now if the palette never opened.
- `DeletePreset(preset_id: str)`: Remove a saved preset by id; False when there is none.
- `Dismiss()`: Close the palette and stop listening for keys.
- `Favourites()`: Identities (tool#id) starred with Ctrl+D here or in the launcher.
- `History()`: Executed queries, oldest first.
- `IsHidden(key: str)`: Whether a command is hidden from the palette's listing, by the user's override or the tool's own default.
- `IsOpen()`: Whether the palette window is open right now.
- `ListPresets()`: Every saved preset: label, target command and baked arguments.
- `OnHubExposure(exposed: bool)`: FNS_Hub tells a tab's component when it is shown; rebuild then.
- `OnInputBlur()`: The input lost keyboard focus (panel/input_callbacks onFocusEnd).
- `OnKey(key, ctrl=False, alt=False, shift=False)`: Raw key names from the Keyboard In DAT while the palette is open.
- `OnManagerButton(name: str)`: The toolbar buttons on the Commands tab.
- `OnQuery(text)`: Every keystroke in the input lands here (editablecontinuous).
- `OnRowClick(index: int)`: A mouse click on a row (panel/panelexec_rows): select it, then do exactly what Enter does, so clicks and keys can never diverge.
- `Rank(query: str = '', limit: int = None)`: The rows to show, best first.
- `RefreshManager()`: Rebuild the Commands tab's table: every registry command, hidden ones included, with the star and hidden state from the prefs.
- `SavePreset(ident: str, args: dict, label: str)`: Add a preset over the command with identity `ident` (tool#id), `args` baked in.
- `Summon()`: Open the palette over whatever the user is looking at right now.
- `ToggleFavourite(key: str)`: Flip a command's favourite flag in the curation; returns the new state.
- `ToggleHidden(key: str)`: Flip a command's visibility.
- `UsageBonus(key: str)`: The current ranking bonus (0..8) for a command identity, tool#id.

## Commands

No commands recorded for this package.

## Hotkeys

- `ctrl.shift.p` (`Hotkey` on `FNS_CommandPalette`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_HubRegistry`

## Parameters

### Palette

- **Hotkey** (`par.Hotkey`, Str), default `ctrl.shift.p`: Keyboard shortcut that opens the palette. Space-separated combos, parts joined with a dot, e.g. ctrl.shift.p. Rebind it from FNS_HotkeyManager.
- **Justify and Offset To...** (`par.Justifyoffsetto`, Menu), default `specifydisplay`, menu `primarydisplay`, `specifydisplay`, `alldisplays`: Which display the palette window is placed on: the primary one, the one set on the window, or the bounds of all displays.
- **Ignore Taskbar** (`par.Ignoretaskbar`, Toggle), default `on`: Place the palette as if the taskbar were not there.
- **DPI Scaling** (`par.Dpiscaling`, Menu), default `usedpiscale`, menu `native`, `usedpiscale`: Size the palette in native pixels, or scaled with the display DPI.
- **Shift to Single Display** (`par.Single`, Menu), default `off`, menu `off`, `singledisplay`, `cursordisplay`: Keep the palette on one display: off, on a single display, or on the display with the cursor.
- **Favourite keys** (`par.Favouritekeys`, Str), default `[]`: Legacy store of starred command identities (tool#id) from before the shared curation file; adopted into that file on first read, then emptied.
- **Query history** (`par.Queryhistory`, Str), default `[]`: JSON list of executed palette queries, oldest first, recalled with Alt+Up / Alt+Down. Persisted by the config host.
- **Visibility overrides** (`par.Visibilityoverrides`, Str), default `{}`: Legacy store of visibility overrides (tool#id -> hidden or shown) from before the shared curation file; adopted into that file on first read, then emptied.
- **Presets** (`par.Presets`, Str), default `[]`: Legacy store of presets from before the shared curation file; adopted into that file on first read, then emptied.
- **Rank By Usage** (`par.Rankbyusage`, Toggle), default `on`: Commands you run often rank higher: a small bonus that fades with a 14-day half-life and breaks ties between similar matches, never above a better match or a favourite. Usage is shared with the TDXLU launcher (command-usage.json) and recorded even when this is off.
