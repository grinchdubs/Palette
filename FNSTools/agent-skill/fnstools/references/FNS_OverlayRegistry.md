# OverlayRegistry

Package `FNS_OverlayRegistry`.

One overlay over the network editor you are working in, composited from every tool that draws there: each tool hands over its own image, and this registry fits it over your view, stacks it with the rest and shows it above the nodes, without touching your network's display flags or annotations.

- Category: Core
- Version: 0.2.4
- Access: Free
- Docs: https://functionstore.tools/docs/fns-overlayregistry/

## What it does

- **Stack every tool's drawing in one overlay**: Stacks every tool's drawing into one image shown above the nodes of the network editor you work in; with nothing drawing, nothing runs.
- **Follows the view**: Pan, zoom or open another network and the overlay follows, keeping everything in place at any zoom and sharp on high DPI screens.
- **Leaves your network untouched**: Switches no display flag, dims no annotation, and is taken out before every project save.
- **Corner widgets**: Tools can pin small clickable panels to a corner of the network editor that keep their size at any zoom and stack without overlapping.
- **Manage layers and widgets in Hub**: FNS_Hub's Overlay tab lists every layer and widget: reorder them, hide one without switching its tool off, or move a widget to another corner.
- **Publish a layer**: A tool hands over one TOP through a host copy of the registry, or from Python with RegisterWidget(), and the registry composites it with the rest.
- **View data for layers**: The View page and View() give the covered network rectangle, render resolution, units per pixel and zoom; NetworkToPixel() converts network positions to pixels.
- **Panel widget API**: RegisterPanelWidget() pins a tool's panel COMP to a corner with an order and margin; UnregisterPanelWidget() takes it away.

## Reach it

A registry. `op.FNS_OVERLAYREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `Cursor()`: The mouse over a network editor as (network, x, y) in network units, or None when it is over no network editor of this TD's main window.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `LayerEntries()`: Every registered layer as {canonical: entry}, bottom first: panel_path, display (the user's), active (the tool's), menu_order, source_registry (its host).
- `NetworkToPixel(x, y)`: A point in network units to layer pixels (origin bottom left).
- `Overlay` (property): The annotation showing the composite, or None.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PanelWidgets()`: The registered widget names.
- `RegisterPanelWidget(panel, canonical, anchor='topleft', order=None, margin=None, shown=True, active=True, tool=None, pars=None, at=None)`: Show `panel` (a panel COMP) as an interactive widget pinned to a corner of the network editor you work in, at its own size on screen.
- `RegisterWidget(widget_op, canonical_name, order=None, display=True, callback=None, source_registry=None, active=True)`: Publish a TOP as a layer of the network overlay under canonical_name.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: RegistryBase.StampHost, then shaped like every other registry host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical_name)`: RegistryBase's teardown name for UnregisterWidget.
- `UnregisterPanelWidget(canonical)`: Take a widget off the network editor.
- `UnregisterWidget(canonical_name)`: Remove a layer from the overlay and recomposite (forwarded to the /sys global).
- `View()`: Everything a client layer needs to render, as one dict.
- `WidgetRect(canonical)`: (network, x, y, width, height) of a widget as placed now, in network units of the network it shows in, or None while it is not shown.
- `WidgetSpecs()`: Every registered widget as {canonical: spec}: panel_path, anchor, order, margin, shown, active, tool_path and pars (the overlay manager's view; a copy, editing it changes nothing).
- `WidgetTarget(canonical)`: The live layer TOP registered under `canonical`, or None.
- `Widgets()`: The registered names, bottom layer first.

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

- **Widget COMP** (`par.Comp`, COMP), default `..`: The tool this layer belongs to. Defaults to the parent component; it names the layer when Canonical Name is empty.
- **Layer TOP** (`par.Layer`, TOP): The TOP this tool adds to the network overlay. It renders over the registry's View (op.FNS_OVERLAYREGISTRY.View()), premultiplied, transparent where it draws nothing.
- **Canonical Name** (`par.Canonicalname`, Str): Unique name for this layer in the overlay registry.
- **Callback DAT** (`par.Callback`, DAT): Optional DAT with find bar callbacks for this widget.
- **Auto-register** (`par.Autoregister`, Toggle), default `off`: When on, keep this widget published into the find bar registry while this component exists.
- **Register** (`par.Register`, Pulse): Publish once into the find bar registry, even if Auto-register is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Layer Order** (`par.Menuorder`, Int), default `-1`: Stacking order among layers: higher draws on top. -1 = no preference (bottom).
- **Displayed** (`par.Displayed`, Toggle), default `on`: Whether the layer is in the overlay. Bind it to the tool's own on switch.
- **Layer Active** (`par.Layeractive`, Toggle), default `off`: The tool's own half of whether its layer is drawn: an expression on the tool's on/off switch (Active unless the tool says otherwise). The layer shows only when this AND Displayed are on; Displayed is yours.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.
