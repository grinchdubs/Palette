# PaneTypeRegistry

Package `FNS_PaneTypeRegistry`.

Named, persistent pane-type entries for TD's panebar: any COMP can appear in the pane-type dropdown and be recalled with configurable owner, type, window actions and callbacks.

- Category: Core
- Version: 3.2.9
- Access: Free
- Docs: https://functionstore.tools/docs/fns-panetyperegistry/

## What it does

- **Recall a COMP from the pane-type dropdown**: A COMP joins the pane bar's pane-type dropdown; picking it turns the pane into that COMP with the entry's owner, pane type, window behaviour and callbacks.
- **Register a COMP from the dropdown**: Right-click a built-in row to register the network the pane shows as a new entry of that type, kept with the project.
- **Run one action on right-click**: Right-click a registered row to run one step on its own, such as Set Owner, Tear Away or Open Floating Network Editor, or to unregister it.
- **Open a floating network editor**: The Floating network editor quick-launch command opens a floating network editor on the network you are in.
- **Register a tool as a pane type**: A tool ships a host copy of the registry and registers on load, declaring its COMP, pane type, and the window actions or callback to run on recall.
- **Callback on recall**: An optional callback runs after the built-in actions, for what they cannot express: focusing a field, opening a panel, restoring state.

## Reach it

A registry. `op.FNS_PANETYPEREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `ActionMenuSource` (property): Legacy MenuSource (Action parameter removed in 0.0.6).
- `CreateCallbacks()`: Deploy a callbacks DAT skeleton into the TOOL and assign Callback.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `EnsureHostRegistry(owner, canonical, pane_type='PANEL')`: Ensure owner has a PaneTypeRegistry child for this menu entry.
- `FloatingNetworkEditor()`: Open a floating network editor on the current network.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `OnPaneTypeContextSelect(infoDict)`: popMenu onSelect handler for panetype right-click menu.
- `OpenFloatingNetworkEditor(owner_op, name=None)`: Open a floating Network Editor pointed at owner_op.
- `OpenPaneTypeContextMenu(panetype_comp, canonical_name)`: Right-click menu for a panebar panetype dropdown row.
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `PanetypeMenuSource` (property): MenuSource for the Panetype parameter.
- `RecallPanel(pane, canonical_name, flags=None, run_callback=None)`: Apply a registered entry to a UI pane.
- `RegisterCurrentOwnerAsBuiltin(pane_comp, pane_type, builtin_label=None, owner=None)`: Register the pane's current owner as a custom panebar entry for pane_type.
- `RegisterPanel(panel_op, canonical_name, pane_type=None, action=None, set_owner=None, change_type=None, maximize=False, tear_away=False, float_pane=False, open_parameters=False, callback=None, source_registry=None, menu_order=None)`: Register a COMP for the panebar menu.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `UnregisterPanel(canonical_name)`: Remove a panebar menu entry.

## Commands

- **Floating network editor** (id `floatingnetworkeditor`): Open a floating network editor on the current network. Method `FloatingNetworkEditor`.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Registration

- **COMP** (`par.Comp`, COMP), default `..`: COMP to register as the pane owner. Defaults to parent (..). PANEL requires a Panel COMP (isPanel); other pane types accept any COMP.
- **Canonical Name** (`par.Canonicalname`, Str): Name shown in the panebar menu. Leave empty to use the host COMP name.
- **Callback** (`par.Callback`, DAT): Optional Text DAT with onPaneRecall(ctx). Invoked after built-in recall actions. Use Create Callback for a skeleton.
- **Create Callback** (`par.Createcallbacks`, Pulse): Create a callbacks Text DAT with a default onPaneRecall(ctx) skeleton and assign it to Callback. Will not overwrite non-empty existing callbacks text.
- **Auto-register** (`par.Autoregister`, Toggle), default `off`: When on, register the host COMP immediately and keep recall flags / callback in sync when settings change. When off, use Register or Python RegisterPanel.
- **Register** (`par.Register`, Pulse): Register the host COMP now (even if Auto-register is off). Validates COMP type against Pane Type.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Status** (`par.Regstatus`, Str), default `Idle`: Read-only status of host auto-registration (Idle, Registered, Skipped under /sys or /ui, Error).
- **Menu Order** (`par.Menuorder`, Int), default `-1`: Preferred order among registered panebar entries. -1 = no preference (append, default). 0 = first among custom entries, 1 = second, and so on. Built-in rows are not moved.
- **Pane Type** (`par.Panetype`, Menu), default `PANEL`, menu `PANEL`, `NETWORKEDITOR`, `GEOMETRYVIEWER`, `TOPVIEWER`, `CHOPVIEWER`, `ANIMATIONEDITOR`, `PARAMETERS`, `TEXTPORT`, `OPBROWSER`: Pane type applied when this entry is selected in the panebar. PANEL is typical for containerCOMP UIs.
- **Default Actions** (`par.Defaultactions`, Header)
- **Set Owner** (`par.Setowner`, Toggle), default `on`: When on, set the pane owner to the registered COMP when this entry is selected.
- **Change Type** (`par.Changetype`, Toggle), default `on`: When on, change the pane to the selected Pane Type. changeType returns a new Pane object; Maximize/Float/Callback run after.
- **Maximize** (`par.Maximize`, Toggle), default `off`: When on, maximize the pane after recall (pane.maximize = True).
- **Tear Away** (`par.Tearaway`, Toggle), default `off`: When on, tear the pane into a floating window after recall (pane.tearAway()).
- **Float** (`par.Float`, Toggle), default `off`: Open the registered COMP in a floating window. PANEL/Geometry/TOP/CHOP -> openViewer(); PARAMETERS -> openParameters(); Network Editor and other tool types -> showInPane Floating.
- **Open Parameters** (`par.Openparameters`, Toggle), default `off`: When on, open a floating parameter dialog for the registered COMP (op.openParameters()). Available for any pane type.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.
- **Pre-Save Heal** (`par.Presaveheal`, Toggle), default `on`: Before each project save, re-check this registry: update entries whose component moved, drop entries whose component is gone, and republish a host that initialised before the global registry existed. Off skips the sweep for this registry only.

### About

- **View Readme** (`par.Viewreadme`, Pulse): Open the PaneTypeRegistry developer README as a styled markdown annotate in this network (uses the bundled md viewer).
