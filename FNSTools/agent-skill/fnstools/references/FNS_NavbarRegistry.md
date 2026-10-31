# NavbarRegistry

Package `FNS_NavbarRegistry`.

The pane-bar surface registry. The raw master, promoted to /sys; clone it to add your own pane-bar widgets.

- Category: Core
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-navbarregistry/

## What it does

- **Widgets in every pane bar**: Registered widgets are placed in every pane bar TouchDesigner has open and in the default bar new panes start from, so they show in panes you open later too.
- **Navbar layout in Hub**: Hub's Navbar tab reorders pane-bar items, flips them between the left and right side, groups them and shows or hides them.
- **Layout follows you**: Your pane-bar arrangement is saved with your settings and comes with you to every project.
- **Panel COMP to navbar package**: Dropping any panel COMP on the FNS button registers it as its own self-installing navbar package.
- **Host copy registration**: A tool that wants a pane-bar widget ships a host copy of this registry, picks a side and a kind, and registers on load.
- **Widget copy in each pane**: Each pane bar gets its own copy of a widget, so a breadcrumb can show its own pane's path; RefreshWidget() re-copies after you edit it.

## Reach it

A registry. `op.FNS_NAVBARREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `AdoptBarWidget(canonical_name, side='left', order=None, display=True)`: Take one of TD's stock pane-bar buttons under management so it can be ordered, grouped and hidden like a published widget.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `OpenConfigurator()`: Open the Navbar Configurator (lives in the FNS_Navbar package).
- `OpenDocs(canonical_name)`: Open the tool's self-reported wiki/help page, if it has one.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PlaceWidgetSequence(canonical_names)`: Manager API for the AUTOMATIC passes (FNS_Hub's boot adoption, its stored-order apply and the group-bracket restore): arrange each side in the given order without moving a published widget or writing to any host.
- `RefreshWidget(canonical)`: Manager API: re-stamp an entry's instances from its live source (after the source widget itself was edited).
- `RegisterWidget(widget_op, canonical_name, order=None, side=None, kind=None, display=True, callback=None, source_registry=None, width=None, help_url=None)`: Publish a COMP as a navbar item under canonical_name.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `SetWidgetDisplay(canonical_name, visible)`: Manager API: show or hide a registered item.
- `SetWidgetOrder(canonical_name, order)`: Manager API: reposition a registered widget within its side.
- `SetWidgetSequence(canonical_names)`: Manager API for the USER's edit (the Hub's drag, group and restore actions): reassign order 1..N per side from the given sequence and write each number back to its host, which is the user's layout from then on (FNS_ConfigRegistry roams it).
- `SetWidgetSide(canonical_name, side)`: Manager API: dock a widget left or right of the path area.
- `SetWidgetWidth(canonical_name, width)`: Manager API: override a widget's bar width (applied to the managed copies; the source widget is never touched).
- `SideSequences` (property): Manager API: {'left': [...], 'right': [...]} widget names in order.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical_name)`: RegistryBase's teardown name for UnregisterWidget.
- `UnregisterWidget(canonical_name)`: Remove a pane-bar item and its instances from every bar (forwarded to the /sys global).
- `WidgetSequence` (property): Manager API: canonical names -- left widgets, right widgets, then overlay/logic entries.
- `WidgetTarget(canonical)`: Resolve the live source COMP for a registered canonical name.
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
- **Navbar Order** (`par.Menuorder`, Int), default `-1`: Preferred order among registered widgets, managed by the global registry. -1 = no preference (append at the end).
- **Navbar Side** (`par.Align`, Menu), default `right`, menu `left`, `right`: Which side of the pane bar's path area this item docks to. Left sits after TD's own left-hand icons; right sits between the path area and TD's right-hand icons.
- **Item Kind** (`par.Kind`, Menu), default `widget`, menu `widget`, `overlay`, `logic`: What the registered COMP is. Widget: a panel placed in the bar's left/right flow. Overlay: an out-of-flow panel (e.g. a click-through layer over the path cells), shown but never re-ordered. Logic: a non-panel COMP that just needs a running copy inside every pane bar.
- **Displayed** (`par.Displayed`, Toggle), default `on`: Default visibility of the widget in the toolbar (managed by the global registry).
- **Bar Width** (`par.Barwidth`, Int), default `0`: Width of this widget in the toolbar. 0 = auto (follow the widget). Persisted here; the registry writes manager edits back.
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page opened from the Configurator (right-click the Name cell). Leave empty to auto-discover from a docsHelper COMP (its Url par) inside the registered panel or its parent.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.
