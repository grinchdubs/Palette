# Console

Package `FNS_Console`.

The toolkit's web front, served from inside your project: every tool's settings on one page, the install picker, and any tab a tool contributes. The raw master, promoted to /sys.

- Category: Core
- Version: 3.2.19
- Access: Free
- Docs: https://functionstore.tools/docs/fns-console/

## What it does

- **Settings for every tool on one page**: Each installed tool appears as a card with its parameters grouped by page, with a jump list and a search across all of them.
- **Open on any tab**: Open Settings, Pick Tools and Open Console open it in Hub, the toolkit root's panel or your system browser, and the tab sits in the address so a reload or a link keeps it.
- **Install and remove**: The installer's picker in a tab: check a tool to install it, uncheck an installed one to remove it, and its settings are kept for next time.
- **Updates in one list**: Compares what you have installed with what the store publishes, shows each update's notes, and applies one update or all of them.
- **Community tools**: Lists tools by other creators, and places some of them straight into the network you are working in.
- **Config scope, global or project**: The Settings header switches your settings between global and project scope.
- **Export settings**: Writes every tool's settings to one JSON file in the config folder and offers it as a download.
- **Import settings**: Applies a settings file to the tools you have now and keeps the sections for tools you install later.
- **Show or hide tabs**: The ⋯ button shows or hides each contributed tab, and the choice is saved on the tool that contributed it.
- **Runs only while in use**: Served on 127.0.0.1 from inside your project; it starts when you open it and stops after ten idle minutes.
- **Contribute a tab**: A stamped FNS_Console host publishes a tool's own HTML page as a console tab, with an optional Python DAT answering its requests.
- **Browser hand-off**: While a tool's tab is exposed, the console switches the tool's own web render off, and back on when the exposure ends.
- **HTTP API**: Routes on the console's port list and show tabs, read and set settings, export and import them, and drive updates from another page.
- **Python API**: `op.FNS_CONSOLE` opens and closes the console, lists and shows tabs, and registers a tab without a host.
- **Hot-synced sources**: Disk edits to the externalized console sources reach the running console on its next request.

## Reach it

A registry. `op.FNS_CONSOLE` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `Close()`: Stop serving the console: its web server goes inactive.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Open(tab=None, panel=True)`: Serve the console and show it.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `RegisterTab(comp, canonical, page=None, api_dat=None, label='', order=50, displayed=True, source_registry=None)`: Publish a tab: `page` (text DAT) is served as-is under /t/<canonical>/; `api_dat` (optional) answers /t/<canonical>/api/* through its onConsoleRequest(action, method, body).
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `Serve(tab=None)`: Make sure the console is being served and return its URL (with the tab fragment when given) -- WITHOUT showing it anywhere.
- `ServeTab(canonical, subpath='', method='GET', body=None)`: Answer one request under /t/<canonical>/: '' -> the page, 'api/<action>' -> the api DAT.
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `SetTabDisplayed(canonical, displayed)`: Show or hide a contributed tab.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `Tabs(include_hidden=False)`: Every tab, in order: the built-ins (always displayed), then the live contributions (a registration whose page DAT is gone is skipped, never shown broken).
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UiBaseCss()`: The shared UI base, served at /base.css for contributed tabs.
- `UiUpdates()`: The Updates tab's whole state in one answer: Compare() rows (no network -- the store manifest already on disk), per-package release notes from that manifest, and whether a check/update pass is live.
- `UiUpdatesApply(names=None)`: Kick UpdateProject() for `names` (or everything that differs when empty).
- `UiUpdatesCheck()`: Kick CheckUpdates() -- manifest only, deliberately cheap.
- `UiUpdatesStatus()`: The live pass, for the page's poll: stage, the updater's own narration, and -- once settled -- the per-package results.
- `UiUpdatesTakeOver(path=None, confirm=False)`: Bring a standalone copy of a global tool under the toolkit (FNS_Updater.TakeOver, docs/StandaloneTakeover.md).
- `UnregisterPanel(canonical)`: Remove a contributed console tab (forwarded to the /sys global).
- `UnregisterTab(canonical)`: Remove a contributed console tab (forwarded to the /sys global).
- `Url()`: The console's URL if it is serving right now, else None.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Registration

- **Tool COMP** (`par.Comp`, COMP), default `..`: The tool that contributes this tab. Defaults to the parent component (the host lives inside the tool it publishes).
- **Canonical Name** (`par.Canonicalname`, Str): Unique, URL-safe name of the tab (letters, digits, _ -). It is the path: /t/<name>/. Leave empty to use the tool COMP name.
- **Tab Page** (`par.Tabpage`, DAT): Text DAT holding the tab's HTML. Served verbatim in the console under /t/<name>/. Inline its CSS and JS; relative fetches resolve under that path.
- **Tab API** (`par.Tabapi`, DAT): Optional Python DAT defining onConsoleRequest(action, method, body) -> JSON-able. Answers /t/<name>/api/<action>; body is the parsed JSON of a POST, else None.
- **Local Browser** (`par.Localbrowser`, COMP): Optional: the tool's own web browser panel (a palette webBrowser COMP) rendering the same page. While this tab is exposed the console serves the page, so the console switches that browser's Active off, a renderer nobody looks at, and back on when the exposure ends.
- **Expose to Console** (`par.Autoregister`, Toggle), default `on`: Publish this tab into the console while the component exists. Off = the tool runs only its own local interface and contributes nothing.
- **Register** (`par.Register`, Pulse): Publish once into the console, even if Expose is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Shown in Console** (`par.Displayed`, Toggle), default `on`: Show this tab on the console's tab bar. Off keeps the tab registered but hidden. It stays listed in the console's tab manager, which writes its choice back here.
- **Tab Label** (`par.Tablabel`, Str): What the console's tab bar shows. Empty = the canonical name.
- **Tab Order** (`par.Taborder`, Int), default `50`: Position in the tab bar. Built-ins sit at 0 (Settings) and 10 (Install & remove); contributions default to 50 and sort by this, then by label.
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page. Informational; leave empty to skip.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound Registry page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.

### Console

- **Open Console** (`par.Open`, Pulse): Serve the console (on the first free port of 36710-36759) and show it, in the toolkit root's webBrowser panel when there is one, else your system browser.
