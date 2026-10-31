# OpMenuRegistry

Package `FNS_OpMenuRegistry`.

OP Create dialog surface registry: search words, row decorations, right-click items, filter stages. The raw master, promoted to /sys.

- Category: Core
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-opmenuregistry/

## What it does

- **Shared OP Create dialog surface**: Arbitrates between the tools that change the OP Create dialog, and the dialog goes back to stock when those tools are removed.
- **Arrange contributions in Hub**: Hub's OpMenu tab reorders what the tools add to the dialog and switches any contribution off without uninstalling its tool.
- **Replace a stock operator with an alternative**: Create a stock operator type with the alternatives shortcut held and installed alternatives are offered; one is placed with its wiring restored, several open a picker.
- **Alternatives from the store**: Alternatives from tools downloaded to your store but not in the project are offered below a divider and placed from disk; >> marks such types.
- **Search word contributions**: Tools add extra words that match an operator type, so searching music finds Audio File In.
- **Row decorations**: Tools relabel rows in the operator list, such as the >>> OpTemplates puts beside every type you have a template for.
- **Right-click menu items**: Tools add entries after TouchDesigner's own three in the dialog's right-click menu, such as OpTemplates' Edit Templates.
- **Filter-chain stages**: Tools splice Script DATs into the operator list's filter chain to filter or rewrite the list itself.
- **Panel injection**: Tools wire Panel COMPs into the dialog at a named anchor.
- **Callbacks DAT inside each tool**: A tool's whole contribution is one opmenu_callbacks DAT inside the tool, so its menu behaviour travels in its own .tox.

## Reach it

A registry. `op.FNS_OPMENUREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `Alternatives` (property): Merged {opType: [alternative, ...]} from every contributor.
- `Contributors` (property): Manager API: snapshot of all registered contributor entries.
- `CreateCallbacks()`: Spawn an `opmenu_callbacks` DAT into this host's tool and point the host's Callback parameter at it.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `DecorateLabel(optype, label)`: Run every contributor's row decorator over a node-table label.
- `Decorators` (property): [(canonical, fn)] label decorators, resolved ONCE.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `InvokeMenuItem(index, optype)`: Dispatch a right-click menu click (index is already offset past TD's stock items) back to the tool that published it.
- `MarkAlternatives(optype, label)`: Append the alternatives mark to one node-table label.
- `MenuItems` (property): [(canonical, label)] appended after TD's stock right-click items.
- `OpenDocs(canonical_name)`: Open the tool's self-reported wiki/help page, if it has one.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PlaceAlternative(orig_op, alternative)`: Replace `orig_op` in place with one alternative (a dict from Alternatives, or a bare OP), restoring its input and output wiring.
- `RefreshStoreAlternatives()`: Drop the cached store scan; the next read rescans the folder.
- `RegisterContributor(comp, canonical_name, callback=None, order=None, display=True, source_registry=None, help_url=None, panel=None, panel_anchor=None)`: Publish a COMP's op-menu contributions under canonical_name.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `Resync()`: Public: re-apply the whole surface now.
- `SearchWords` (property): Merged {opType: [word, ...]} from every contributor.
- `SetContributorDisplay(canonical_name, visible)`: Manager API: enable or disable a tool's contributions.
- `SetContributorOrder(canonical_name, order)`: Manager API: reorder a contributor's menu items.
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterContributor(canonical_name)`: Remove a contributor's menu items, search words and alternatives and resync the dialog (forwarded to the /sys global).
- `UnregisterPanel(canonical_name)`: RegistryBase's teardown name for UnregisterContributor.

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

- **Widget COMP** (`par.Comp`, COMP), default `..`: Panel COMP published as the toolbar widget. Defaults to the parent component.
- **Canonical Name** (`par.Canonicalname`, Str): Unique name for this widget in the global toolbar registry.
- **Callback DAT** (`par.Callback`, DAT): Optional DAT with toolbar callbacks for this widget.
- **Create Callbacks** (`par.Createcallbacks`, Pulse): Spawn an 'opmenu_callbacks' DAT into this tool from the registry's template and wire this host's Callback parameter to it. Safe to pulse again: an existing DAT is adopted, never overwritten.
- **Panel** (`par.Panel`, COMP): A Panel COMP to inject into /ui/dialogs/menu_op. The zero-code way to contribute a panel, with no callbacks DAT needed. Combined with anything onPanels() returns, not overridden by it.
- **Panel Anchor** (`par.Panelanchor`, Str), default `searchpanel`: Name of a panel inside /ui/dialogs/menu_op whose output the injected panel's input is wired to. Without it the panel drops out of the dialog's layout flow. Default: searchpanel.
- **Auto-register** (`par.Autoregister`, Toggle), default `off`: When on, keep this widget published into the global toolbar registry while this component exists.
- **Register** (`par.Register`, Pulse): Publish once into the global toolbar registry, even if Auto-register is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Contribution Order** (`par.Menuorder`, Int), default `-1`: Preferred order among registered widgets, managed by the global registry. -1 = no preference (append at the end).
- **Displayed** (`par.Displayed`, Toggle), default `on`: Default visibility of the widget in the toolbar (managed by the global registry).
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page opened from the Configurator (right-click the Name cell). Leave empty to auto-discover from a docsHelper COMP (its Url par) inside the registered panel or its parent.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.

### Alternatives

- **Alternatives Shortcut** (`par.Shortcutalternatives`, Str), default `alt ctrl`: Modifier keys to hold while creating an operator to be offered the alternatives registered for its type (space-separated: alt, ctrl, shift, cmd). Without the keys the operator is created as normal. Applies on the /sys global; the master holds the value the global is promoted with.
