# OpTemplates

Package `FNS_OpTemplates`.

A library of preconfigured operator templates to drop into a network.

- Category: Network
- Version: 3.2.14
- Access: Free
- Docs: https://functionstore.tools/docs/fns-optemplates/

## What it does

- **Template by drag and drop**: Drop an operator set up the way you like onto the toolbar icon and it becomes a template for its type.
- **Place a template on create**: Hold the alternatives shortcut (`Ctrl+Alt` by default) while placing an operator marked >>> in the OP Create dialog, and your template goes down in its place with the wiring kept.
- **Variants of one operator type**: Keep as many named variants of one operator type as you like and pick one from a menu as you place it.
- **Operator chains as templates**: Operators wired after the template operator are placed together with it, such as the shipped LFO, Math and Null.
- **Network snippets as templates**: A Base COMP in the type's template holds a whole network, such as a Render TOP with its geometry, camera and light, placed as one template.
- **Substitute a COMP for the operator**: A Base COMP inside a snippet's Base COMP makes the template land as that COMP.
- **Insert into a connection**: Templates, chains and networks drop into an existing wire, with In and Out operators marking where a network connects.
- **Shared alternatives menu**: Other tools that offer themselves for the same operator type are listed beside your templates, with tools from your store below a divider.
- **Global or per-project library**: Keep one library for every project on the machine or one inside the project file, or follow the toolkit's Config Scope.
- **Push project templates to global**: Push To Global copies the project set to the global file whenever you like, asking first when the file exists.
- **Save the templates**: Under global scope, middle-click the toolbar icon or press Save Templates; under project scope, saving the project saves them.
- **Open the library**: Left-click the toolbar icon, or run Open templates from quick-launch, to browse or edit the library in a floating network editor.
- **Edit one type's templates**: Right-click a type in the OP Create dialog and pick Edit Templates... to work on its templates.
- **Starter set**: Ships with templates for 18 operator types to start from.
- **Library kept across upgrades**: On the first start after an upgrade it finds the newest library you saved under an older name, and keeps the file it replaces beside it.

## Reach it

`op.FNS_OPTEMPLATES` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `AddToTemplates()`: Save the current selection as a new template.
- `ColorBaseCOMPbyName(_op)`: Color a template base by the operator family its name contains.
- `DropOp(_op)`: Store a dropped operator as a template for its operator type.
- `ExternalChange(onSave=False, startup=False, enable=None)`: Retired with the External toggle; the scope decides now.
- `ExternalPath` (property): The global library file's path, evaluated.
- `ExternalPathExpr(name=None)`: The expression for the global library file's path under the palette, for the externaltox parameter.
- `OnNewOp(_op: td.OP)`: Kept for callers; the engine lives in FNS_OpMenuRegistry now.
- `OnTemplatesUpdate(new_ops)`: Called when the templates network changes: refresh the cache and color the new bases.
- `OpenTemplateBase(optype)`: Open the template base of an operator type in a floating network editor, creating it when needed.
- `OpenTemplates()`: Open the OP templates browser (floating).
- `OpenTemplatesFloating()`: Open the templates network in a floating network editor.
- `PlaceTemplate(orig_op=None, template_ops=None)`: Place a template through the registry (kept for the popMenu callbacks and any external caller).
- `PushToGlobal()`: Write the active library to the palette file (asks before an overwrite).
- `RefreshCachedTemplates()`: Drop the cached Templates listing so the next read rebuilds it.
- `RefreshTemplates()`: Reload the active library: from the palette file under global scope; the project library has nothing to reload, its cache is refreshed.
- `RefreshTemplatesCmd()`: Reload the templates from disk.
- `SaveTemplates()`: Write the templates tox to disk.
- `TemplateSave()`: Persist the active library: the palette file under global scope, the project itself under project scope.

## Commands

- **Add selection to templates** (id `addtotemplates`): Save the current selection as a new template. Method `AddToTemplates`.
- **Open templates** (id `opentemplates`): Open the OP templates browser (floating). Method `OpenTemplates`.
- **Refresh templates** (id `refreshtemplatescmd`): Reload the templates from disk. Method `RefreshTemplatesCmd`.
- **Save templates** (id `savetemplates`): Write the templates tox to disk. Method `SaveTemplates`.

## Hotkeys

None.

## Alternative for

- `analyzeCHOP`
- `analyzeTOP`
- `audiodeviceinCHOP`
- `baseCOMP`
- `circleTOP`
- `compTOP`
- `dattoCHOP`
- `displaceTOP`
- `filterCHOP`
- `lfoCHOP`
- `limitCHOP`
- `moviefileoutTOP`
- `noiseTOP`
- `rampTOP`
- `renderTOP`
- `scurveCHOP`
- `speedCHOP`
- `triggerCHOP`

## Requires

- `FNS_ConfigRegistry`
- `FNS_OpMenuRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Root** (`par.Target`, COMP), default `x`: The component whose network is watched for newly created operators. '/' watches the whole project; narrow it if you want templates to apply in one branch only.
- **Library Scope** (`par.Libraryscope`, Menu), default `follow`, menu `follow`, `global`, `project`: Where the active templates library lives. Global: one .tox in your user palette folder, shared by every project on this machine. Project: a component at the network root outside FNSTools, saved with this .toe and kept across toolkit updates. Follow: whatever the toolkit's Config Scope says. A missing library is created from the set that is loaded now; the shipped templates are only the seed.
- **Library Folder** (`par.Libraryfolder`, Str): Folder under <user palette>/FNSTools that holds the global library. Empty uses OpTemplates, which is right for everyone except a development project that must keep its curated set apart from the one it uses day to day. Global scope only; cleared on export, so it never ships.
- **Templates** (`par.Templates`, COMP): The library the scope resolved to. Read-only: change Library Scope instead.
- **Open Templates** (`par.Opentemplates`, Pulse): Open the templates component in a floating network, to add or edit templates by hand.
- **Save Templates** (`par.Savetemplates`, Pulse): Write the templates to disk: to the external .tox when External is on, otherwise by saving the project. It confirms first, because it overwrites what is already there.
- **Push To Global** (`par.Pushtoglobal`, Pulse): Write the active library to the global palette file, so a set built in this project becomes the one every project on this machine loads. Asks before overwriting an existing file.
- **Refresh Templates** (`par.Refreshtemplates`, Pulse): Reload the templates component from its external .tox, discarding unsaved edits made in this session.
- **Keys** (`par.Keys`, Str): Mirrors the Alternatives Shortcut on FNS_OpMenuRegistry, which is where the alternatives are offered from now. Change it there.
