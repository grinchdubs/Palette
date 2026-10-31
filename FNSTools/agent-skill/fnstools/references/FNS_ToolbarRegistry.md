# ToolbarRegistry

Package `FNS_ToolbarRegistry`.

The toolbar surface registry and mirror rail. The raw master, promoted to /sys; clone it to put your own tools on the bar.

- Category: Core
- Version: 3.2.9
- Access: Free
- Docs: https://functionstore.tools/docs/fns-toolbarregistry/

## What it does

- **Bookmark bar slots, order and visibility**: Keeps which widgets sit on TouchDesigner's bookmark bar, in what order and which are shown, so installing or removing a tool never leaves a hole or a dead button.
- **Mirror rail**: Each button on the bar is a live view of the widget inside its tool, so no button COMP is ever copied into the bar.
- **Arrange the bar in Hub**: The Toolbar tab of Hub reorders and groups widgets, sets their width and adds dividers between them.
- **Hide buttons you never use**: Hiding a button from its row in Hub takes it off the bar while the tool stays installed.
- **Layout follows you**: Your arrangement is saved with your settings and comes with you to every project.
- **Reset the toolbar layout**: Reset toolbar puts every tool back in the slot it shipped in.
- **Drop a panel on the FNS button**: Dropping any panel COMP on the FNS button gives it a self-registering host and puts it on the bar, the quickest way to add a tool of your own.
- **Register from a host or from Python**: A host copy inside a tool registers it on load; RegisterWidget(), SetWidgetDisplay() and WidgetTarget() do the same work from code.

## Reach it

A registry. `op.FNS_TOOLBARREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `AddDivider(after=None, width=None)`: Manager API: insert a new virtual divider after the given canonical name (or at the end).
- `AdoptBarWidget(widget_op, canonical_name, order=None, display=True, source_registry=None)`: Take a panel that is ALREADY in the bar under registry management (TD's built-in icons), so it can be ordered, grouped and hidden like any published widget.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `OpenConfigurator()`: Open the Toolbar Configurator (lives in the FNS_Toolbar package).
- `OpenDocs(canonical_name)`: Open the tool's self-reported wiki/help page, if it has one.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PlaceWidgetSequence(canonical_names)`: Manager API for the AUTOMATIC passes (FNS_Hub's boot adoption, its stored-order apply and the group-bracket restore): arrange the bar in the given order without moving a published tool or writing to any host.
- `RegisterDivider(canonical_name, order=None, width=None, display=True)`: Publish a VIRTUAL divider -- a registry-owned blank separator with no backing widget.
- `RegisterWidget(widget_op, canonical_name, order=None, display=True, callback=None, source_registry=None, width=None, help_url=None)`: Publish a panel COMP as a toolbar widget under canonical_name.
- `RemoveDivider(canonical_name)`: Manager API: remove a divider (virtual, or a legacy widget-based one, which also destroys its DIVIDER_TAG-owned widget).
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SetDividerWidth(canonical_name, width)`: Set a divider's width (the same as SetWidgetWidth).
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `SetWidgetDisplay(canonical_name, visible)`: Manager API: show or hide a registered widget.
- `SetWidgetOrder(canonical_name, order)`: Manager API: reposition a registered widget in the bar.
- `SetWidgetSequence(canonical_names)`: Manager API for the USER's edit (the Hub's drag, group, divider and restore actions): reassign order 1..N from the given full sequence and write each number back to its host, which is the user's layout from then on (FNS_ConfigRegistry roams
- `SetWidgetWidth(canonical_name, width)`: Manager API: override any entry's bar width (applied to the MIRROR, matchsize off -- the source widget's own size is never touched).
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical_name)`: RegistryBase's teardown name for UnregisterWidget.
- `UnregisterWidget(canonical_name)`: Remove a toolbar widget and its mirror from the bar (forwarded to the /sys global).
- `WidgetSequence` (property): Manager API: canonical names in current bar order.
- `WidgetTarget(canonical)`: Resolve the live widget COMP for a registered canonical name.
- `Widgets` (property): Manager API: snapshot of all registered widget entries.

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
- **Auto-register** (`par.Autoregister`, Toggle), default `off`: When on, keep this widget published into the global toolbar registry while this component exists.
- **Register** (`par.Register`, Pulse): Publish once into the global toolbar registry, even if Auto-register is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Toolbar Order** (`par.Menuorder`, Int), default `-1`: Preferred order among registered widgets, managed by the global registry. -1 = no preference (append at the end).
- **Displayed** (`par.Displayed`, Toggle), default `on`: Default visibility of the widget in the toolbar (managed by the global registry).
- **Bar Width** (`par.Barwidth`, Int), default `0`: Width of this widget in the toolbar. 0 = auto (follow the widget). Persisted here; the registry writes manager edits back.
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page opened from the Configurator (right-click the Name cell). Leave empty to auto-discover from a docsHelper COMP (its Url par) inside the registered panel or its parent.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.
