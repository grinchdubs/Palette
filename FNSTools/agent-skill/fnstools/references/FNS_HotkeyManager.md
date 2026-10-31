# HotkeyManager

Package `FNS_HotkeyManager`.

Unified hotkey discovery, conflict detection and rebinding UI across the whole toolkit.

- Category: Interface
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-hotkeymanager/

## What it does

- **Find every hotkey in the project**: Scans the whole project, toolkit tools and your own components alike, for Keyboard In CHOPs and DATs and shortcut parameters, one row per binding.
- **Rebind by pressing keys**: Click a Hotkey cell and press the new keys; a combo already in use asks you to press it again to take it.
- **Reset a binding**: Right-click a Hotkey cell to put that binding back to its default.
- **Conflict detection**: Combos bound by more than one tool are flagged CONFLICT, and clicking the flag jumps between the rows that share it.
- **Copies listed once**: A component copied around the project is one row, and rebinding it rewrites every copy.
- **Persist bindings across projects**: Toolkit hotkeys follow you to other projects and through updates, and any other binding can opt in with a tag or a click.
- **Save, load and defaults**: Save, reload or put back the default bindings, or force the defaults on every load to get a machine back to a known state.
- **Discovery rules for tool authors**: Where to put a binding so it is found and gets a default that survives renames and moves.

## Reach it

`op.FNS_HOTKEY_MANAGER` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `AllHotkeyPars()`: (operator, parameter_name) tuples for the parexec watcher.
- `ApplyBinding(display_path: str, par_name: str, combo: str)`: Write a new combo onto a binding.
- `BeginCapture(display_path: str, par_name: str)`: Arm the capture keyboardin; next non-modifier keypress becomes the binding.
- `CancelCapture()`: Abandon a key capture in progress and refresh the UI.
- `ComputeConflicts()`: combo -> [records] for every combo bound by more than one tool.
- `ConfigLoadRows(data)`: Merge config rows into the gathered table -- update by path+par, insert unknown, remember unresolvable rows as orphans, leave every project-local row untouched -- then apply through the standard load path (watch suppressed).
- `ConfigSaveRows()`: Declared rows of the gathered table, for config_callbacks onConfigSave.
- `Discover()`: Scan every top-level COMP (minus excluded roots) for hotkey-bearing parameters.
- `JumpToConflictPartner(display_path: str, par_name: str)`: Select and scroll to the partner row of this row's conflicted combo; repeated clicks cycle through partners when there are several.
- `LoadHotkeysCmd()`: Load the saved hotkey bindings.
- `OnCaptureKey(key, character, alt, ctrl, shift, state, cmd=False)`: Called by the capture keyboardin's onKey callback.
- `OpenHotkeyUI()`: Open the hotkey manager lister.
- `OpenUI()`: Open the hotkey manager window, refreshing the bindings and the conflict list first.
- `RefreshAll()`: Full re-scan + UI rebuild (UI Refresh button).
- `RefreshUI()`: Rebuild the UI table the lister displays.
- `ResetToDefault(display_path: str, par_name: str)`: Restore one binding to its default.
- `SaveHotkeys()`: Externalize the current live bindings into the gathered table.
- `SaveHotkeysCmd()`: Save the current hotkey bindings.
- `ShowConflictPartners(display_path: str, par_name: str)`: Surface who else binds this row's conflicted combo in the hint bar.
- `TogglePersist(display_path: str, par_name: str)`: Persist-column click: flip the CONFIG_TAG on the row's source op.

## Commands

- **Load hotkeys** (id `loadhotkeyscmd`): Load the saved hotkey bindings. Method `LoadHotkeysCmd`.
- **Open hotkey UI** (id `openhotkeyui`): Open the hotkey manager lister. Method `OpenHotkeyUI`.
- **Save hotkeys** (id `savehotkeyscmd`): Save the current hotkey bindings. Method `SaveHotkeysCmd`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_HubRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn hotkey management on or off. Off leaves every binding as it is but stops the manager applying, saving or restoring them.
- **Save Hotkeys** (`par.Savehotkeys`, Pulse): Write the declared bindings to your user palette now, so they survive project files and updates. Toolkit hotkeys are always declared; anything else has to be tagged FNS_hotkeys or ticked in the lister's Persist column.
- **Load Hotkeys** (`par.Loadhotkeys`, Pulse): Re-apply the saved bindings from your user palette over what is bound right now.
- **Load Default** (`par.Loaddefault`, Pulse): Put every discovered binding back to the default its own parameter declares, discarding your saved bindings for this session.
- **Force Default** (`par.Forcedefault`, Toggle), default `off`: Ignore saved bindings entirely and use each parameter's declared default on every load. Use it to get a machine back to a known state; leave it off to keep your own bindings.
- **Excluded Roots** (`par.Excluderoots`, Str), default `ui sys local`: Space-separated names of top-level components to SKIP during project-wide hotkey discovery. TD's own ui/sys/local are excluded by default; add other roots here to silence them.
- **Open Hotkey UI** (`par.Openui`, Pulse): Open the hotkey configurator panel: every discovered binding grouped by tool, click a Hotkey cell to rebind via key capture, right-click to reset to default. Conflicts are flagged in the Status column.
