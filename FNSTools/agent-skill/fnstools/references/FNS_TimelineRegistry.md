# TimelineRegistry

Package `FNS_TimelineRegistry`.

Publish a widget into TouchDesigner's timeline bar: transport controls beside the stock ones, an entry on the time-properties block, or a full-width strip in the frame-ruler band that gets its own row.

- Category: Core
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-timelineregistry/

## What it does

- **Stock bar when unused**: With nothing contributed the timeline bar stays stock, and it returns to its stock height when the last widget goes.
- **Background zone adds a row**: The background zone makes the bar taller by its own height, recomputed from the stock height each time so the bar never creeps taller.
- **Publish widgets to the timeline bar**: A tool publishes a panel COMP and it appears in the timeline bar, shown through mirrors so the stock blocks stay as they are.
- **Transport, ruler and graph-heading zones**: A widget sits at the right end of the transport row, as a full-width strip under the frame-ruler numbers, or in the Animation editor's graph heading.
- **Register through a host copy**: A tool ships a small host copy whose Registration page names the COMP, canonical name, zone, order and whether it is displayed.
- **Python registration API**: RegisterWidget, UnregisterWidget and SetWidgetZone on op.FNS_TIMELINEREGISTRY add, remove and move widgets from Python; the zone settles a frame later.

## Reach it

A registry. `op.FNS_TIMELINEREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `AdoptTimelineWidget(widget_op, canonical_name, order=None, display=True)`: Take a panel that is ALREADY in the timeline under registry management (TD's built-in transport controls), so it can be reordered, grouped and hidden like any published widget.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `EnsureSection(host, name, height=18, spec=None)`: Create or update a managed section container inside `host`.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `OpenConfigurator()`: No dedicated configurator yet -- the timeline surface is managed through the registry API (and, once it ships a hub tab, through FNS_Hub).
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PlaceWidgetSequence(canonical_names)`: Manager API for the AUTOMATIC passes (FNS_Hub's boot adoption, its stored-order apply and the group-bracket restore): arrange the bar in the given order without moving a published tool or writing to any host.
- `RegisterDivider(canonical_name, order=None, width=None, display=True, zone=None)`: Publish a VIRTUAL divider -- a registry-owned blank separator with no backing widget.
- `RegisterWidget(widget_op, canonical_name, order=None, display=True, callback=None, source_registry=None, width=None, height=None, help_url=None, zone=None)`: Publish a panel COMP into the timeline under canonical_name.
- `RemoveDivider(canonical_name)`: Remove a registered divider by name; False when the name is not a divider.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `SetWidgetDisplay(canonical_name, visible)`: Manager API: show or hide a registered widget.
- `SetWidgetOrder(canonical_name, order)`: Manager API: reposition a registered widget.
- `SetWidgetSequence(canonical_names)`: Manager API for the USER's edit (the Hub's drag, group, divider and restore actions): reassign order 1..N from the given full sequence and write each number back to its host, which is the user's layout from then on (FNS_ConfigRegistry roams
- `SetWidgetWidth(canonical_name, width)`: Manager API: override an entry's width (applied to the MIRROR, matchsize off -- the source widget's own size is never touched).
- `SetWidgetZone(canonical_name, zone)`: Manager API: move a registered entry to another timeline zone.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical_name)`: RegistryBase's teardown name for UnregisterWidget.
- `UnregisterWidget(canonical_name)`: Remove a timeline entry; an adopted native control gets its visibility back (forwarded to the /sys global).
- `WidgetSequence` (property): Manager API: canonical names in current order.
- `WidgetTarget(canonical)`: Resolve the live widget COMP for a registered canonical name.
- `Widgets` (property): Manager API: snapshot of all registered entries.

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
- **Timeline Order** (`par.Menuorder`, Int), default `-1`: Preferred order among registered widgets, managed by the global registry. -1 = no preference (append at the end).
- **Displayed** (`par.Displayed`, Toggle), default `on`: Default visibility of the widget in the toolbar (managed by the global registry).
- **Bar Width** (`par.Barwidth`, Int), default `0`: Width of this widget in the toolbar. 0 = auto (follow the widget). Persisted here; the registry writes manager edits back.
- **Bar Height** (`par.Barheight`, Int), default `0`: Height of this widget in its zone. 0 = the zone's own row height. The registry sizes the SOURCE panel to this, because a mirror is a window onto the widget and not a scaler, so an oversized source shows only its top-left corner in the slot.
- **Timeline Zone** (`par.Zone`, Menu), default `transport`, menu `transport`, `background`, `graphheading`: Which part of TD's timeline this widget is published into. 'Transport row' appends it after the native play/stop controls. 'Properties block' places it in the left 279px column. 'Background strip' spans the full width in the frame-ruler band and is drawn UNDERNEATH the ruler. The ruler's own background is transparent, so it shows through.
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page opened from the Configurator (right-click the Name cell). Leave empty to auto-discover from a docsHelper COMP (its Url par) inside the registered panel or its parent.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.
