# PaletteRegistry

Package `FNS_PaletteRegistry`.

Contribute tabs to TouchDesigner's Palette Browser: a tool publishes a native panel COMP and it appears beside the stock Palette tab, sized to the slot and notified on every tab change.

- Category: Core
- Version: 3.2.7
- Access: Free
- Docs: https://functionstore.tools/docs/fns-paletteregistry/

## What it does

- **Tabs in the Palette Browser**: Adds a tab strip above the Palette Browser's list, with TouchDesigner's own Palette tab first and one tab per contributed panel.
- **Stock palette left intact**: With nothing contributed the palette stays as TouchDesigner ships it; the strip appears with the first registration and goes with the last.
- **Switch back to the Palette tab**: SearchPalette's `Ctrl+Shift+F` switches to the stock Palette tab before focusing its search field; other tools can call ShowTab('palette') the same way.
- **Register a tab from a host**: A tool ships a small host copy whose Registration page sets the tab's tool, canonical name, panel, label, order and visibility.
- **Tab API from Python**: RegisterTab(), Tabs(), SetTabDisplayed(), ShowTab(), CurrentTab() and UnregisterTab() on op.FNS_PALETTEREGISTRY manage tabs from code.
- **Tab change callback**: An optional Callbacks DAT gets onPaletteTab(canonical, previous) on every tab change.
- **Panels fitted to the slot**: A registered panel is resized to the slot, restored when the tab goes away, and keeps its state across tab switches, Web Render included.
- **Extra tabs from one tool**: The Extra Tabs sequence adds one tab per block, and a block without its own panel reuses the first tab's panel.

## Reach it

A registry. `op.FNS_PALETTEREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `CurrentTab()`: The canonical name of the tab the palette shows now, the stock tab by default.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PanelTarget(canonical)`: Live panel for a tab (the mirrors' selectpanel expression).
- `RegisterTab(comp, canonical, panel=None, label='', order=50, displayed=True, callback=None, source_registry=None)`: Publish a tab: `panel` (a panel COMP in the project) is shown in the Palette Browser under a tab named `label`.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RemoveSurface()`: Take the strip and every mirror out of the dialog and show the stock palette.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `Resync()`: Rebuild the palette strip and the mirrors from the registered tabs.
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `SetTabDisplayed(canonical, displayed)`: Show or hide a contributed tab; written back to the contributing host's Displayed par (compare-before-set) so it persists with the tool.
- `ShowTab(canonical)`: Select a tab: TD's own ('palette') or a registered canonical.
- `SlotHeight()`: Height of a tab's slot -- exactly where TD's own list stands.
- `SlotWidth()`: Width of a tab's slot -- the palette column.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `Tabs(include_hidden=False)`: Every tab, in strip order: TD's own Palette first, then the live contributions (an entry whose panel is gone is skipped, never shown broken).
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical)`: Remove a contributed palette tab, giving its panel its size back, and resync the strip (forwarded to the /sys global).
- `UnregisterTab(canonical)`: Remove a contributed palette tab, giving its panel its size back, and resync the strip (forwarded to the /sys global).

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
- **Canonical Name** (`par.Canonicalname`, Str): Unique name of the tab (letters, digits, _ -). Leave empty to use the tool COMP name. "palette" is TD's own tab and cannot be taken.
- **Tab Panel** (`par.Panel`, PanelCOMP): The panel COMP shown when this tab is selected. Shown in place through a Select COMP, never copied, and sized to the tab slot by the registry (its w/h become slot expressions while registered). Defaults to the tool itself.
- **Callbacks DAT** (`par.Callback`, DAT): Optional Python DAT. onPaletteTab(canonical, previous) fires on every tab change so the tool can react (e.g. route a shared panel). Raise-contained.
- **Expose in Palette** (`par.Autoregister`, Toggle), default `on`: Publish this tab into TouchDesigner's Palette Browser while the component exists. Off = the tool contributes nothing.
- **Register** (`par.Register`, Pulse): Publish once into the Palette Browser, even if Expose is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Shown in Palette** (`par.Displayed`, Toggle), default `on`: Show this tab on the Palette Browser's tab strip. Off keeps it registered but hidden; the registry writes its choice back here so it persists with the tool.
- **Tab Label** (`par.Tablabel`, Str): What the tab strip shows. Empty = the canonical name.
- **Tab Order** (`par.Taborder`, Int), default `50`: Position on the strip after TD's own Palette tab (always first). Contributions default to 50 and sort by this, then by label.
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page. Informational; leave empty to skip.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound Registry page (Pl* pars). Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.
- **Extra Tabs** (`par.Tab`, Sequence), default `0`: Additional tabs published by this one host. The Registration pars above define the FIRST tab; each block here adds one more, so a tool can put several tabs on the strip (optionally over the same panel) without stamping a second host.
- **Canonical Name** (`par.Tab0name`, Str): Unique name of this extra tab (letters, digits, _ -). Required; the block is skipped while it is empty. "palette" is TD's own tab and cannot be taken.
- **Tab Panel** (`par.Tab0source`, PanelCOMP): Panel COMP shown for this tab. Leave empty to reuse the Tab Panel above. That is how one panel serves several tabs, routed by onPaletteTab.
- **Tab Label** (`par.Tab0label`, Str): What the tab strip shows for this tab. Empty = the canonical name.
- **Tab Order** (`par.Tab0order`, Int), default `50`: Position on the strip after TD's own Palette tab. Contributions sort by this, then by label.
- **Shown in Palette** (`par.Tab0shown`, Toggle), default `on`: Show this tab on the strip. Off keeps it registered but hidden.
