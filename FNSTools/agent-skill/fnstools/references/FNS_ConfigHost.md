# ConfigHost

Package `FNS_ConfigHost`.

A standalone ConfigRegistry host. Drop it into a component to give it roaming settings; its parameters save and reload with your config, with per-parameter and per-page exclusions.

- Category: Developer
- Version: 3.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-confighost/

## What it does

- **Roaming settings for any component**: Drop it inside a component and that component's custom parameters are written into the shared settings file and restored on load.
- **Parameter and page exclusions**: Name patterns, or whole parameter pages, stay out of what is saved, for parameters that must boot at their defaults.
- **Registry page on the parent**: The host's key settings are mirrored onto the component as a Registry page, so it can be configured without opening the host.
- **Edit on the settings page**: With the toolkit installed, the component is listed on the FNS settings page beside every FNS tool, its parameters editable there.
- **Named settings section**: The canonical name is the section the settings are stored under, defaulting to the component's name; renaming it orphans values saved under the old name.
- **Global or per project**: Follows the toolkit's choice between one settings file shared by every project and settings kept in the .toe.
- **Save and load callbacks**: onConfigSave and onConfigLoad save and restore anything JSON-serializable, such as table rows; a pulse writes the starter DAT.

## Reach it

A registry. `op.FNS_CONFIGREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `AcceptsDrop(items)`: True when at least one dropped item could become a host here.
- `CloseSettingsUI()`: Close the console, the settings UI, when it is up.
- `ConfigData` (property): Parsed, schema-gated, mtime-cached view of the file.
- `ConfigPath` (property): Absolute path of the aggregated config file.
- `ConfigScopeChanged(par, prev)`: Confirm the risky flip.
- `CreateCallbacks()`: Spawn a `config_callbacks` DAT into this host's tool and point the host's Callback parameter at it.
- `CreateGroup(first, last=None, label=None)`: Manager API: wrap the run from `first` to `last` (inclusive, in current bar order) in a new group.
- `GroupPath(canonical_name)`: Manager API: 'outer / inner' label path for an entry, '' if loose.
- `GroupVisibility` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `GroupVisible(group_id)`: Manager API: is this group expanded (default yes).
- `Groups` (property): Manager API: {group_id: {'label', 'members', 'parent', 'visible'}}.
- `HostCanonical` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `LoadAll()`: Explicitly re-apply every registered tool's saved section.
- `LoadAllConfigs()`: Load every registered tool's config.
- `LoadTool(canonical_name, force=False)`: Apply a tool's saved section onto the live tool now.
- `OpenConfigSettings()`: Open the FNS_Config settings UI.
- `OpenSettingsUI(tab=None, panel=True)`: Open the FNS console on its Settings tab (or `tab`).
- `PackageDrop(comp)`: Turn a dropped panel COMP into a self-registering host of this surface.
- `PaneRegistry` (stored item: a value the extension keeps on the COMP, read as an attribute)
- `RegisterTool(comp, canonical_name, callback=None, autoload=True, persist_pars=True, exclude_pars='', exclude_pages='', source_registry=None)`: Publish a tool COMP for settings persistence under canonical_name.
- `RemoveGroup(group_id)`: Manager API: dissolve a group -- both markers go, members stay exactly where they are and keep their own display flags, so anything the group was hiding comes back.
- `RenameGroup(group_id, label)`: Manager API: relabel a group (id and markers untouched).
- `SaveAll()`: Snapshot every registered tool into the aggregated file (the ONLY code path that writes it).
- `SaveAllConfigs()`: Save every registered tool's config.
- `SaveTool(canonical_name)`: Read-merge-write a single tool's section.
- `ScopeAudit()`: [(path, problem)] for every copy of this registry that does not carry the guarded Configscope: 'missing', 'bind' or 'unguarded'.
- `SetConfigScope(value, prompt=False)`: Flip the config scope programmatically ('global' / 'project').
- `SetGroupVisible(group_id, visible)`: Manager API: expand/collapse a group WITHOUT touching any member's own display flag, so expanding restores exactly what was showing.
- `StampHost(target_comp, canonical_name=None, autoregister=True, promote_pars=True, par_values=None)`: Copy THIS master into `target_comp` as a configured host.
- `ToggleGroup(group_id)`: Manager API: flip a group; returns the new state.
- `Tools` (property): Manager API: snapshot of all registered tool entries.
- `UiExport(save=True)`: A portable config document snapshotted from the LIVE tools.
- `UiImport(data)`: Apply an exported/roamed config document from the page.
- `UiScope(value=None, mode=None)`: Read or flip the config scope from the console.
- `UiSet(canonical_name, par_name, value)`: Set ONE par from the page and persist it through SaveTool.
- `UiState()`: Everything the settings page needs, in one call.
- `UnregisterPanel(canonical_name)`: RegistryBase's teardown name for UnregisterTool.
- `UnregisterTool(canonical_name)`: Remove a tool's registration from the settings registry (forwarded to the /sys global).

## Commands

- **Load all tool configs** (id `loadallconfigs`): Load every registered tool's config. Method `LoadAllConfigs`.
- **Open FNS settings** (id `openconfigsettings`): Open the FNS_Config settings UI. Method `OpenConfigSettings`.
- **Save all tool configs** (id `saveallconfigs`): Save every registered tool's config. Method `SaveAllConfigs`.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Registration

- **Tool COMP** (`par.Comp`, COMP), default `..`: Tool COMP whose settings are persisted. Defaults to the parent component (the host lives inside the tool it publishes).
- **Canonical Name** (`par.Canonicalname`, Str): Unique name for this tool's section in the config file.
- **Callback DAT** (`par.Callback`, DAT): Optional config_callbacks DAT for state beyond parameters (onConfigSave/onConfigLoad).
- **Create Callbacks** (`par.Createcallbacks`, Pulse): Spawn a 'config_callbacks' DAT into this tool from the registry's template and wire this host's Callback parameter to it. Safe to pulse again: an existing DAT is adopted, never overwritten.
- **Auto-register** (`par.Autoregister`, Toggle), default `off`: When on, keep this tool published into the global config registry while this component exists.
- **Register** (`par.Register`, Pulse): Publish once into the global config registry, even if Auto-register is off.
- **Unregister** (`par.Unregister`, Pulse): Take this tool's contribution back out of the registry and turn Autoregister off, so it stays out. Register puts it back.
- **Registration Status** (`par.Regstatus`, Str): Read-only status of this host registration.
- **Auto-load** (`par.Autoload`, Toggle), default `on`: Apply this tool's saved section from the config file once per session, shortly after the tool registers. Turn off for a tool whose settings should stay project-local.
- **Persist Parameters** (`par.Persistpars`, Toggle), default `on`: Snapshot and restore the tool COMP's custom parameters (value, expression, bind + mode). Meta pages (About, Version Ctrl, Info, Callbacks, Common) are always skipped; missing parameters are never created on load.
- **Exclude Pars** (`par.Excludepars`, Str): Space-separated name patterns (tdu.match) of custom parameters to leave out of persistence, e.g. 'Spoutactive Ndi*'. Use for parameters that must boot at their defaults.
- **Exclude Pages** (`par.Excludepages`, Str): Space-separated page-name patterns to leave out of persistence entirely.
- **Help URL** (`par.Helpurl`, Str): The tool's wiki/help page. Informational for config; leave empty to skip.
- **Promote Parameters** (`par.Promotepars`, Toggle), default `on`: When on, the host mirrors its key Registration parameters onto the parent tool as a bound 'Registry' page. Turn off before shipping a tool that should not expose registry controls.

### Config

- **Config Scope** (`par.Configscope`, Menu), default `global`, menu `global`, `project`: Follows the toolkit root's Config Scope (op.FNS, FNSTools page) through a guarded expression, and reads 'project' when there is no root: a standalone tool release keeps its settings in the .toe. Author on the root; the root par is the record.
- **Config File** (`par.Configfile`, File): Override the config file location. Empty = the user palette default (FNSTools/config/FNStools_config.json). Evaluated by the /sys global; set it on the FNS_Config master so promotion carries it.
- **Save All Now** (`par.Saveall`, Pulse): Snapshot every registered tool into the config file now (forwards to the global).
- **Load All Now** (`par.Loadall`, Pulse): Re-apply every registered tool's saved section now (forwards to the global).
