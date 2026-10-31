# PaneSearchRegistry

Package `FNS_PaneSearchRegistry`.

Publish a control into the find bar of every network editor pane: it sits beside the bar's own Home toggle, one copy per pane, and appears in panes opened later too.

- Category: Core
- Version: 0.1.6
- Access: Free
- Docs: https://functionstore.tools/docs/fns-panesearchregistry/

## What it does

- **Controls in every find bar**: Copies a published panel COMP into every network editor pane's find bar after Home, one copy per pane, including panes that open their bar later.
- **Stock find bar when unused**: With nothing contributed, every find bar stays as TouchDesigner made it, and the search itself is always left to the bar or to SearchFix.
- **Register through a host copy**: A tool ships a host copy whose Registration page names the panel COMP, a canonical name, its order and whether it is displayed.
- **Python widget API**: RegisterWidget(), UnregisterWidget(), RefreshWidget() and Instance() add, remove, refresh and find a find bar contribution from Python.
- **Reach the find bar's operators**: A script in the contributed panel reaches the bar's search field and the pane's network path through me.parent(2).

## Reach it

A registry. `op.FNS_PANESEARCHREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `Instance(bar, canonical)`: The copy of `canonical` in one find bar, or None.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `RefreshWidget(canonical)`: Replace every find bar's copy of `canonical` with a fresh copy of its source, after the source changed.
- `RegisterWidget(widget_op, canonical_name, order=None, display=True, callback=None, source_registry=None)`: Publish a panel COMP into every pane's find bar under canonical_name.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: RegistryBase.StampHost, then shaped like every other registry host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical_name)`: RegistryBase's teardown name for UnregisterWidget.
- `UnregisterWidget(canonical_name)`: Remove a find-bar control and its instance from every pane (forwarded to the /sys global).
- `WidgetTarget(canonical)`: The live source panel registered under `canonical`, or None.
- `Widgets()`: The registered names, in bar order.

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

- **Widget COMP** (`par.Comp`, COMP), default `..`: Panel COMP published as every find bar widget. Defaults to the parent component.
- **Canonical Name** (`par.Canonicalname`, Str): Unique name for this widget in the find bar registry.
- **Callback DAT** (`par.Callback`, DAT): Optional DAT with find bar callbacks for this widget.
- **Auto-register** (`par.Autoregister`, Toggle), default `off`: When on, keep this widget published into the find bar registry while this component exists.
- **Register** (`par.Register`, Pulse): Publish once into the find bar registry, even if Auto-register is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Find Bar Order** (`par.Menuorder`, Int), default `-1`: Preferred order among registered widgets, managed by the global registry. -1 = no preference (append at the end).
- **Displayed** (`par.Displayed`, Toggle), default `on`: Default visibility of the widget in every find bar (managed by the global registry).
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.
