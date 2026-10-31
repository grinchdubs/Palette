# CustomParTools

Package `FNS_CustomParTools`.

Promote parameters to a parent with binds or expressions, customize name/label/range on drop, plus extension creation, parent shortcuts, parameter clearing and IOP promotion. Also carries the pane-bar drag-drop hijack and path-cell injection, and four stock-TouchDesigner shortcuts for opening parameters and the COMP editor.

- Category: Parameters
- Version: 3.2.15
- Access: Free
- Docs: https://functionstore.tools/docs/fns-custompartools/

## What it does

- **Promote by drop**: Drop a parameter on the button or on a parent in the path bar and it becomes a custom parameter there, bound back to the original.
- **Customise as you promote**: Hold `Ctrl` while dropping to set the name, label, range, clamping and default before the parameter is created.
- **Menu parameter from a table**: Drop a Table DAT and the parent gets a menu parameter that takes its entries from the table.
- **Promote the hovered parameter**: `Alt+X` promotes the parameter under the mouse and `Alt+\` opens it in the Component Editor, with nothing to select or drag.
- **Clear dangling binds and expressions**: Switches parameters with a dangling bind or a failing expression back to constant and clears script errors, on the selected COMP and its immediate children.
- **Add a parent shortcut**: Gives a COMP a parent shortcut from the button or quick-launch, starting from its name or the shortcut it already has.
- **Internal OPs by drop**: A `Ctrl+Alt` drop adds an operator to the parent, or to a parent in the path bar, as an iop.
- **Open parameters and the Component Editor**: Open the parameter dialog or the Component Editor for the selected operator or the current network's COMP from the button, the keyboard or quick-launch.
- **Create an extension in one click**: QuickExt gives a COMP a Python extension with the starting code written, ExtUtils docked and the extension slot filled in.
- **Switch parts off**: Each part switches off on its own, and its button or pane-bar widget goes away with it.
- **Parameters as extension properties**: CustomParHelper gives an extension `self.evalSpeed` and `self.parSpeed` for every custom parameter.
- **Callbacks by parameter name**: A method named `onParSpeed` runs when the Speed parameter changes, with matching names for pulses, parameter groups and sequences.
- **Declare parameters in code**: Helpers such as `CustomParHelper.Float` and `CustomParHelper.Menu` create custom parameters from `__init__`, with page, range and help text.
- **Name your own handlers**: `@CustomParHelper.onPar('Speed')` binds any method to a parameter, and a mistyped parameter name is reported in the log.
- **Execute callbacks without nodes**: NoNode registers CHOP, DAT and parameter execute callbacks from extension code or from decorators on the methods, with no execute DATs in the network.
- **Keyboard shortcuts from code**: `NoNode.RegisterKeyboardShortcut` binds a key such as `ctrl.k` to an extension method, and `DeregisterKeyboardShortcut` removes it.

## Reach it

`op.FNS_CPP` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `CustomizeCurrentComp()`: Open the component editor on the selected operator.
- `CustomizeParentComp()`: Open the component editor on the current network's COMP.
- `DoPromoteAll(exceptions=None)`: Promote every parameter of the reference operator's current page onto the target.
- `IsParGroup(par)`: Whether a parameter belongs to a multi-component group, so the whole group is promoted.
- `ModuleEnabled(module)`: True when `module` is switched on, on the Modules page.
- `OnCustomizeCallback(info)`: Called when the customize dialog closes; promotes the parameter with the entered name, label and range when OK was pressed.
- `OnCustomizeParameterDropped(dropParam)`: Open the customize dialog for a parameter or group dropped on the tool; called by the drop handler.
- `OnEditText(field, text)`: Called by the customize dialog on text entry; remembers the typed parameter name.
- `OpenCurrentParameters()`: Open a floating parameter dialog for the selected operator.
- `OpenParentParameters()`: Open a floating parameter dialog for the current network's COMP.
- `PromotePar(_par, page_name, target=None, refBind=None, parName=None, parLabel=None, parMin=None, parMax=None, clamp=None, parDefault=None)`: Promote one parameter onto the target as a custom parameter bound, or referenced, back to the original.
- `PromoteParGroup(_parGroup, page_name, target=None, refBind=None, parName=None, parLabel=None)`: Promote one parameter group (a vector or a color) onto the target as a custom parameter group bound back to the reference.
- `PromoteSelected()`: Promote custom parameters of the selected operators.
- `Reference` (property): The operator whose parameters are promoted (settable by OP or path).
- `SetTableMenu(_table, _target)`: Create a menu custom parameter on the target from a table DAT's rows (name and label columns).
- `Target` (property): The COMP the promoted parameters are created on (settable by COMP or path; a non-COMP clears it).

## Commands

- **Customize current COMP** (id `customizecurrentcomp`): Open the component editor on the selected operator. Method `CustomizeCurrentComp`.
- **Customize parent COMP** (id `customizeparentcomp`): Open the component editor on the current network's COMP. Method `CustomizeParentComp`.
- **Open current COMP parameters** (id `opencurrentparameters`): Open a floating parameter dialog for the selected operator. Method `OpenCurrentParameters`.
- **Open parent COMP parameters** (id `openparentparameters`): Open a floating parameter dialog for the current network's COMP. Method `OpenParentParameters`.
- **Promote pars of selected** (id `promoteselected`): Promote custom parameters of the selected operators. Method `PromoteSelected`.
- **Clear custom pars of selected** (id `clearselectedpars`): Remove ALL custom parameters from the selected operators (undoable). Method `ClearSelectedPars` on `ClearPars`.
- **Create extension on current** (id `createextoncurrent`): Run QuickExt's extension creator on the current COMP. Method `CreateExtOnCurrent` on `QuickExt`.
- **Toggle QuickParCustom** (id `toggleactive`): Enable or disable QuickParCustom. Method `ToggleActive` on `QuickParCustom`.
- **Add parent shortcut** (id `addshortcuttocurrent`): Add a parent shortcut to the current COMP (prompts for the name). Method `AddShortcutToCurrent` on `QuickParent`.

## Hotkeys

- `alt.\` (`Shortcutrollovercustomize` on `QuickParCustom`)
- `alt.x` (`Shortcutrolloverpromote` on `QuickParCustom`)
- `ctrl.alt.\` (`Shortcutrolloverswitchparmode` on `QuickParCustom`)
- `ctrl.alt.q` (`Shortcutparentpars` on `FNS_CustomParTools`)
- `ctrl.alt.w` (`Shortcutparentcomp` on `FNS_CustomParTools`)
- `shift.alt.q` (`Shortcutcurrentpars` on `FNS_CustomParTools`)
- `shift.alt.w` (`Shortcutcurrentcomp` on `FNS_CustomParTools`)
- `shift.alt.x` (`Shortcutrolloverpromotemod` on `QuickParCustom`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_NavbarRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Ref/Bind** (`par.Refbind`, Toggle), default `off`: How a promoted parameter is linked back to the original. On binds the two (either end can be edited and both follow); off leaves the original in expression mode pointing at the promoted one. Holding the modifier while promoting inverts this for that one action.
- **Promote All** (`par.Promote`, Pulse): Promote every custom parameter on the current page of the referenced COMP to the target COMP at once, linked according to Ref/Bind.
- **Params: Selected** (`par.Shortcutcurrentpars`, Str), default `shift.alt.q`: Hotkey that opens the parameter dialog for the SELECTED operator. Rebindable here or in FNS_HotkeyManager.
- **Params: Current COMP** (`par.Shortcutparentpars`, Str), default `ctrl.alt.q`: Hotkey that opens the parameter dialog for the COMP whose network is showing.
- **Editor: Selected** (`par.Shortcutcurrentcomp`, Str), default `shift.alt.w`: Hotkey that opens the component editor for the SELECTED operator.
- **Editor: Current COMP** (`par.Shortcutparentcomp`, Str), default `ctrl.alt.w`: Hotkey that opens the component editor for the COMP whose network is showing.

### Modules

- **Parameter Promotion** (`par.Activeparpromote`, Toggle), default `on`: Drop a parameter onto the CustomParTools button to promote it onto the current network COMP. The core action of the tool.
- **QuickExt** (`par.Activequickext`, Toggle), default `on`: Create an extension on the current COMP from the button.
- **QuickParent** (`par.Activequickparent`, Toggle), default `on`: Set a parent shortcut on the current COMP from the button.
- **ClearPars** (`par.Activeclearpars`, Toggle), default `on`: Alt-click (Cmd on macOS) the button to clear the custom parameters of the current child.
- **IOP Promoter** (`par.Activeioppromoter`, Toggle), default `on`: Hold the modifier while dropping an operator on the button to promote it as an Internal OP instead of promoting parameters.
- **Navbar Drag/Drop** (`par.Activehijackdragdrop`, Toggle), default `on`: Accept operator and parameter drops anywhere on the pane navigation bar. Off UNREGISTERS the widget, removing it from every bar.
- **Navbar Path Cell Click** (`par.Activepathcellclickinject`, Toggle), default `on`: Open parameters for the operator whose path cell you click in the pane bar. Off UNREGISTERS the widget, removing it from every bar.
- **QuickParCustom** (`par.Activequickparcustom`, Toggle), default `on`: Rollover hotkeys for promoting and customizing the parameter under the mouse. Bound to QuickParCustom's own Active switch.
- **Parameter/Editor Hotkeys** (`par.Activetdshortcuts`, Toggle), default `on`: The four stock-TouchDesigner hotkeys on the Custom page (open parameters, open component editor). Off deactivates the keyboardins; the matching quick-launch commands stay available.
