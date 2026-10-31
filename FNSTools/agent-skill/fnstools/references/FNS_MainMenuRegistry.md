# MainMenuRegistry

Package `FNS_MainMenuRegistry`.

TD main-menu surface registry, including project-name display. The raw master, promoted to /sys.

- Category: Core
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-mainmenuregistry/

## What it does

- **Order, hide and place entries**: Holds the order, visibility and left or right placement of every main-menu entry, TouchDesigner's own items and the ones tools publish alike.
- **Edit from the Hub MainMenu tab**: The MainMenu tab of Hub reorders, hides or groups entries, so a tool's entry can sit between TouchDesigner's own items.
- **Restore TouchDesigner's order**: The TD button in that tab puts TouchDesigner's own items back in their original order, all visible.
- **Publish an entry from a tool**: A tool ships a small host copy of the registry beside its widget to get a main-menu entry, reachable globally as op.FNS_MAINMENUREGISTRY.
- **Pin next to a stock item**: Anchor After pins an entry directly after a named TouchDesigner item, such as tutorials, and heals if that item comes and goes.
- **Lifecycle callbacks**: An optional mainmenu_callbacks DAT hears when its entry is registered, unregistered, shown, hidden or moved to the other side.

## Reach it

A registry. `op.FNS_MAINMENUREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `AdoptBarWidget(widget_op, canonical_name, side='left', order=None, display=True)`: Take a panel that is ALREADY in the bar under registry management (TD's built-in items), so it can be ordered, grouped and hidden like any published widget.
- `CreateCallbacks()`: Spawn a `mainmenu_callbacks` DAT into this host's tool and point the host's Callback parameter at it.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `OpenConfigurator()`: Open the MainMenu Configurator (lives in the FNS_MainMenu package).
- `OpenDocs(canonical_name)`: Open the tool's self-reported wiki/help page, if it has one.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PlaceWidgetSequence(canonical_names)`: Manager API for the AUTOMATIC passes (FNS_Hub's boot adoption, its stored-order apply and the group-bracket restore): arrange each side in the given order without moving a published entry or writing to any host.
- `RegisterWidget(widget_op, canonical_name, order=None, side=None, display=True, callback=None, source_registry=None, width=None, help_url=None, anchor=None)`: Publish a panel COMP as a main-menu item under canonical_name.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `SetWidgetAnchor(canonical_name, stock_name)`: Manager API: pin an entry directly after a named stock bar item (e.g.
- `SetWidgetDisplay(canonical_name, visible)`: Manager API: show or hide a registered item.
- `SetWidgetOrder(canonical_name, order)`: Manager API: reposition a registered widget within its side.
- `SetWidgetSequence(canonical_names)`: Manager API for the USER's edit (the Hub's drag, group and restore actions): reassign order 1..N per side from the given sequence and write each number back to its host, which is the user's layout from then on (FNS_ConfigRegistry roams it).
- `SetWidgetSide(canonical_name, side)`: Manager API: dock a widget left or right of the stretchy spacer.
- `SetWidgetWidth(canonical_name, width)`: Manager API: override an entry's bar width (applied to the MIRROR, matchsize off -- the source widget's own size is never touched).
- `SideSequences` (property): Manager API: {'left': [...], 'right': [...]} names in order.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical_name)`: RegistryBase's teardown name for UnregisterWidget.
- `UnregisterWidget(canonical_name)`: Remove a main-menu entry and its mirror from the bar (forwarded to the /sys global).
- `WidgetSequence` (property): Manager API: canonical names -- left entries, then right entries.
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
- **Create Callbacks** (`par.Createcallbacks`, Pulse): Spawn a 'mainmenu_callbacks' DAT into the tool (from the registry's template) and point the Callback parameter at it. Idempotent: an existing DAT is adopted, never overwritten. The hooks are optional lifecycle notifications: onRegistered, onUnregistered, onDisplayChanged, onSideChanged.
- **Auto-register** (`par.Autoregister`, Toggle), default `off`: When on, keep this widget published into the global toolbar registry while this component exists.
- **Register** (`par.Register`, Pulse): Publish once into the global toolbar registry, even if Auto-register is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Menu Bar Order** (`par.Menuorder`, Int), default `-1`: Preferred order among registered widgets, managed by the global registry. -1 = no preference (append at the end).
- **Menu Bar Side** (`par.Align`, Menu), default `right`, menu `left`, `right`: Which side of the pane bar's path area this item docks to. Left sits after TD's own left-hand icons; right sits between the path area and TD's right-hand icons.
- **Anchor After** (`par.Anchor`, Str): Pin this entry into the gap directly AFTER a named stock menu-bar item (e.g. 'tutorials'), overriding the left/right side band. Resolved live each sync: a vanished anchor falls back to the side band and heals if the item returns. Empty = normal side placement.
- **Displayed** (`par.Displayed`, Toggle), default `on`: Default visibility of the widget in the toolbar (managed by the global registry).
- **Bar Width** (`par.Barwidth`, Int), default `0`: Width of this widget in the toolbar. 0 = auto (follow the widget). Persisted here; the registry writes manager edits back.
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page opened from the Configurator (right-click the Name cell). Leave empty to auto-discover from a docsHelper COMP (its Url par) inside the registered panel or its parent.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.
