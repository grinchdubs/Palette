# OpFamily

Package `FNS_OpFamily`.

The FNS tab in the OP Create dialog: an operator family whose members are FNS tools placed from the store as one node each, with stubs for projects that travel and in-place updates that keep retained parameters and state. Built with TDFam.

- Category: Core
- Version: 0.1.12
- Access: Free
- Docs: https://functionstore.tools/docs/fns-opfamily/

## What it does

- **Create FNS tools from OP Create**: Adds an FNS tab beside COMP, TOP, CHOP and the others; each entry places an FNS tool into the current network as one operator.
- **Remove the FNS tab**: Pick Tools, the FNS Tab in OP Create switch or Remove Operator Family take the tab away, the choice sticks, and the switch brings it back.
- **Members mirrored from the store**: The tab lists exactly the members this machine's store holds, kept in step by the updater, and the same folder shows up in the Palette.
- **Replace a stock operator with a member**: A member can also be offered in place of a stock operator, such as Random when you create a Noise CHOP with the alternatives shortcut held.
- **Stub operators for projects that travel**: Placed members become light placeholders that keep their wiring, position, retained parameters and state, and come back as the real operators wherever the family is installed.
- **Update placed operators in place**: Upgrades every placed member to the newest version in the family folder, keeping its retained parameters and state.
- **Sync, stub and update from quick-launch**: Stub, replace, update and resync from quick-launch without dialogs, for the whole project or only the network you are in.
- **Manifest-declared retention**: Each member's manifest declares which parameters and which state survive a stub or an update.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('FNS_OpFamily')`; its promoted methods are called on that COMP.

## Promoted API

- `AssignedCallbacks` (attribute)
- `Config` (attribute)
- `CreateCallbackDat(owner, template)`: Create a callbacks DAT from template if not already set.
- `DoCallback(callbackName, callbackInfo=None)`: Execute a chained callback - calls BOTH assigned callback and DAT callback.
- `ExportConfig(path: str = None)`: Export config to JSON.
- `FamilyName` (property): The family's name, as a dependency.
- `FindOps(type=None, name=None, path=None, depth=None, maxDepth=None, tags=[], allTags=False, parValue=None, parExpr=None, parName=None, key=None, include_stubs=True, network=None)`: Find placed operators of this family.
- `FolderCache` (property): The cached listing of the family folder's operators, as a dependency.
- `GetMasterOps()`: Get all available operators in this family with full metadata.
- `GetOpSource(lookup_name: str)`: Get operator source for a given name.
- `ImportConfig(source: str | dict)`: Import config from JSON.
- `Install(install: bool = None)`: Install or uninstall the family.
- `InvalidateCallbackCache()`: Force cache refresh on next DoCallback.
- `PassTarget` (attribute)
- `PlaceOp(target, op_type, name=None, x=None, y=None)`: Programmatically place an operator into a target COMP.
- `Properties` (attribute)
- `RemoveOperatorFamily()`: Take the FNS tab out of the OP Create dialog, the tools staying installed; the installer removes it a frame later.
- `ReplaceFamilyStubs(only_current_network: bool = False)`: Bring every FNS stub back as the full operator from the family folder; returns the count and names what the folder lacks.
- `StubFamilyOperators(only_current_network: bool = False)`: Turn every placed FNS operator into a light stub that keeps its wiring and retained parameters; returns the count.
- `StubOp(comp)`: Create a lightweight stub from a placed operator.
- `SyncFamilyFromStore()`: Mirror the store's family members into the family folder now, through FNS_Updater.
- `UpdateFamilyOperators(only_current_network: bool = False)`: Upgrade placed FNS operators to the family folder's newest version, keeping retained parameters and state.
- `UpdateOp(comp)`: Update a single operator to the newest version.

## Commands

- **Remove Operator Family** (id `removeoperatorfamily`): Take the FNS tab out of the OP Create dialog and keep it off; your FNS tools stay installed. Pick Tools turns it back on Method `RemoveOperatorFamily`.
- **Replace Family Stubs** (id `replacefamilystubs`): Bring every FNS stub back as the full operator from the family folder Method `ReplaceFamilyStubs`. Params: `only_current_network: toggle = False`.
- **Stub Family Operators** (id `stubfamilyoperators`): Turn every placed FNS operator into a light stub that keeps its wiring and retained parameters Method `StubFamilyOperators`. Params: `only_current_network: toggle = False`.
- **Sync Family From Store** (id `syncfamilyfromstore`): Mirror the store's family members into the family folder now Method `SyncFamilyFromStore`.
- **Update Family Operators** (id `updatefamilyoperators`): Upgrade placed FNS operators to the newest version in the family folder, keeping retained parameters and state Method `UpdateFamilyOperators`. Params: `only_current_network: toggle = False`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Family

- **Family Name** (`par.Family`, Str): The family name: the tab the operators appear under in the OP Create dialog.
- **Version** (`par.Version`, Str): The version of the family registry.
- **Install** (`par.Install`, Toggle), default `on`: Install the family into the OP Create dialog.
- **Install On Start** (`par.Installonstart`, Toggle), default `on`: Install the family every time the project opens.
- **Color** (`par.Color`, RGBA x3), default `0.569`: The family's colour in the OP Create dialog and on its operators.
- **Index** (`par.Index`, Int), default `9`: Position of the family's tab among the OP Create dialog's tabs.
- **Compatible Op Families** (`par.Compatibletypes`, StrMenu), menu `COMP`, `TOP`, `CHOP`, `SOP`, `POP`, `MAT`, `DAT`, `FNS`: Which operator families the family's operators connect to, for filtering in the dialog.
- **Op Comp** (`par.Opcomp`, COMP): The COMP holding the family's operators.
- **Create Op Comp** (`par.Createopcomp`, Pulse): Create an empty COMP for the family's operators and point Op Comp at it.
- ** [ .tox ] Op Folder** (`par.Opfolder`, Folder): A folder of .tox operators to add to the family.
- **Color .tox from Folder** (`par.Colorfileops`, Toggle), default `off`: Colour the operators loaded from the folder in the family colour.
- **Version Regex Match** (`par.Namingconvention`, StrMenu), menu `(.+)_v(\d+\.\d+\.\d+)\.tox$`, `(.+)_(\d+\.\d+\.\d+)\.tox$`, `(.+)-(\d+\.\d+\.\d+)\.tox$`, `No versioning`: How version numbers are read from .tox file names.
- **Ensure Manifests** (`par.Ensuremanifests`, Pulse): Give every operator in the family a manifest if it lacks one.
- **FamUI COMP** (`par.Famuicomp`, COMP): The COMP that draws the family's UI in the dialog.

### Stubs

- **Create Stubs For All** (`par.Createstuball`, Pulse): Create a stub for every operator in the family.
- **Replace Stubs For All** (`par.Replacestuball`, Pulse): Replace every stub in the project with the current operator.
- **Update All** (`par.Updateall`, Pulse): Update every family operator in the project to the current version.
- **Target Op** (`par.Targetop`, OP): Operator to stub or stub to replace
- **Create Stub For Op** (`par.Createstubop`, Pulse): Create stub for target operator
- **Replace Stub For Op** (`par.Replacestubop`, Pulse): Replace target stub with full operator
- **Update Op** (`par.Updateop`, Pulse): Update the selected operator to the current version.
- **Target Comp** (`par.Targetcomp`, OP): Network container to process
- **Create Stubs In Comp** (`par.Createstubscomp`, Pulse): Stub all operators in target network
- **Replace Stubs In Comp** (`par.Replacestubcomp`, Pulse): Regenerate all stubs in target network
- **Update Ops In Comp** (`par.Updatecomp`, Pulse): Update every family operator inside a COMP.
- **Target Type** (`par.Targettype`, StrMenu): The operator type Update Type acts on.
- **Update Type** (`par.Updatetype`, Pulse): Update every placed operator of Target Type.

### Callbacks

- **Callback DAT** (`par.Callbackdat`, DAT): The DAT holding the family's callbacks.
- **Create Callbacks** (`par.Createcallbacks`, Pulse): Create a callbacks DAT from the template and point Callback DAT at it.

### About

- **About** (`par.About`, Pulse): Show the about text.
- **License** (`par.License`, Pulse): Show the license.
- **Dev Mode** (`par.Devmode`, Toggle), default `off`: Development mode, for authoring the family itself.
- **Support** (`par.Tdfamcreators0support`, Pulse): Open the support page of a TDFam creator.
- **Support** (`par.Tdfamcreators1support`, Pulse): Open the support page of a TDFam creator.
