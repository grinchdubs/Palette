# HubRegistry

Package `FNS_HubRegistry`.

The registry behind Hub's tab bar: tools contribute native panels, viewers or parameter pages as hub tabs. The raw master, promoted to /sys.

- Category: Core
- Version: 3.2.7
- Access: Free
- Docs: https://functionstore.tools/docs/fns-hubregistry/

## What it does

- **Self-healing Hub tabs**: Keeps one entry per Hub tab with its label, order and visibility, puts a mirror or viewer in the hub for each, and removes tabs whose tool is gone.
- **Arrange tabs**: Drag a tab onto another tab to reorder them; the order roams with your settings.
- **Rename a tab**: Tab Label on the tool's Registry page gives its tab a different label.
- **Hide a tab**: Hiding a tab is written back to its tool's Shown in Hub parameter, so it stays hidden across projects until you show it again.
- **Contribute a tab through a host**: A host copy names the tab: the tool's own panel, a panel inside the tool, or an OP Viewer of a DAT, CHOP, TOP, SOP, POP or MAT.
- **Parameter page tabs**: Tab Parameters shows a Parameter COMP view of chosen pages of the tool, or every page with `*`, as a Hub tab.
- **Python tab API**: RegisterTab(), Tabs(), SetTabDisplayed(), Open(tab=) and OpenDocs() register, list, show and open Hub tabs from Python.
- **Tab exposure callback**: An extension implementing OnHubExposure(exposed) learns when its tab is shown; a palette Web Browser has its Active switched for it.

## Reach it

A registry. `op.FNS_HUBREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Open(tab=None)`: Open FNS_Hub, on `tab` (a canonical name) when given.
- `OpenDocs(canonical)`: Open a tab's registered help page, if it has one.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `RegisterTab(comp, canonical, content=None, params='', label='', order=50, displayed=True, help_url='', source_registry=None)`: Publish a tab.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `SetTabDisplayed(canonical, displayed)`: Show or hide a tab.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `Tabs(include_hidden=False)`: Every live tab in order (an entry whose content is gone is skipped, never shown broken).
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical)`: Remove a contributed Hub tab and resync the tab bar (forwarded to the /sys global).
- `UnregisterTab(canonical)`: Remove a contributed Hub tab and resync the tab bar (forwarded to the /sys global).

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
- **Canonical Name** (`par.Canonicalname`, Str): Unique name of the tab (letters, digits, _ -). It names the hub's mirror (hubtab_<name>). Leave empty to use the tool COMP name.
- **Tab Content** (`par.Tabcontent`, OP): What the tab shows. Empty = the tool COMP itself (it must be a panel). A panel COMP anywhere inside the tool is mirrored into the hub; a DAT/CHOP/TOP/SOP/POP is shown through an OP Viewer. Ignored when Tab Parameters is set.
- **Tab Parameters** (`par.Tabparams`, Str): Show a parameter view of the tool COMP instead of a panel: the page scope to display (e.g. 'Settings', or * for every page). Empty = not a parameter tab.
- **Show in Hub** (`par.Autoregister`, Toggle), default `on`: Publish this tab into FNS_Hub while the component exists. Off = the tool shows nothing in the hub and its panel stays wherever it lives.
- **Register** (`par.Register`, Pulse): Publish once into the hub, even if Show in Hub is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Shown in Hub** (`par.Displayed`, Toggle), default `on`: Show this tab on the hub's tab bar. Off keeps the tab registered but hidden. The hub's tab manager can show it again.
- **Tab Label** (`par.Tablabel`, Str): What the hub's tab bar shows. Empty = the canonical name.
- **Tab Order** (`par.Taborder`, Int), default `50`: Position in the hub's tab bar; the surface configurators sit at 10/20/30, the console viewer at 90; contributions default to 50 and sort by label within an order.
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page; the hub offers it on the tab. Leave empty to skip.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound Registry page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.

### Hub

- **Open Hub** (`par.Open`, Pulse): Open FNS_Hub (the toolkit's one-stop manager window) on this host's tab.
