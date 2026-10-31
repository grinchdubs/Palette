# Quick-launch commands

Every quick-launch command the public packages declare, by package. A command is run through the command registry by its key, the declaring COMP's path, `#`, and the id shown on its line: for a package's own command `op.FNS_COMMANDREGISTRY.Run(op.FNS.op('FNS_Updater').path + '#checkforupdates')`, and for a command a COMP inside the package declares (the line says "Method X on `<path under the package>`") `op.FNS_COMMANDREGISTRY.Run(op.FNS.op('FNS_CommandRegistry/FNS_BuiltinCommands/TD_Session').path + '#togglerealtime')`. `op.FNS_COMMANDREGISTRY.Commands()` lists the live commands with their keys (`key`, `tool`, `id`, `label`, `help`, `path`). The method named on the line is the command's implementation and can be called on the declaring COMP directly. The built-in TouchDesigner commands (toggle realtime, open a dialog, ...) are declared by COMPs under FNS_CommandRegistry.

## CookBar

- **Open Global Hog CHOP** (id `openhog`): Open the Global Hog CHOP's parameters, to eat frame time on purpose while you watch the bars. Method `OpenHog`.
- **Toggle cook bar** (id `togglecookbar`): Show or hide each operator's cook time and GPU memory above it in the network editor. Method `ToggleCookBar`.
- **Toggle Global Hog CHOP** (id `togglehog`): Switch the Global Hog CHOP on or off. It DELIBERATELY eats frame time (stress test). Method `ToggleHog`.

## FNS_AltSelect

- **Toggle AltSelect** (id `toggleactive`): Enable or disable AltSelect. Method `ToggleActive`.

## FNS_AutoCombine

- **Toggle AutoCombine** (id `toggleactive`): Enable or disable AutoCombine. Method `ToggleActive`.

## FNS_AutoRes

- **Toggle AutoRes** (id `toggleactive`): Enable or disable AutoRes. Method `ToggleActive`.

## FNS_BorderlessTD

- **Toggle borderless** (id `toggleborderless`): Toggle the borderless TouchDesigner main window. Method `ToggleBorderless` on `BorderlessWindow`.
- **Toggle fullscreen** (id `togglefullscreen`): Toggle fullscreen on the TouchDesigner main window. Method `ToggleFullscreen` on `BorderlessWindow`.
- **Toggle timeline** (id `toggletimeline`): Show or hide the timeline bar. Method `ToggleTimeline` on `HideTimeline`.

## FNS_ColorUI

- **Export color palette** (id `exportpalette`): Export the current UI colors to file. Method `ExportPalette`.
- **Import color palette** (id `importpalette`): Import a UI color palette from file. Method `ImportPalette`.
- **Open color UI** (id `opencolorui`): Open the TouchDesigner UI color editor. Method `OpenColorUI`.
- **Randomize colors** (id `randomizecolors`): Randomize the UI colors. Method `RandomizeColors`.
- **Reset all colors** (id `resetallcolors`): Reset every UI color to its default. Method `ResetAllColors`.
- **Undo randomize** (id `undorandomize`): Undo the last color randomization. Method `UndoRandomize`.

## FNS_CommandRegistry

- **Add Embody** (id `addembody`): Download the latest Embody release and add it to the project root. Method `AddEmbody` on `FNS_BuiltinCommands/TD_Components`.
- **Add TDX Launcher Utility** (id `addlauncherutility`): Download the latest TDX Launcher Utility and add it to the project root. Method `AddLauncherUtility` on `FNS_BuiltinCommands/TD_Components`.
- **Add TDMCP** (id `addtdmcp`): Download the latest TDMCP release (Derivative's MCP server) and add it to the project root. Method `AddTdmcp` on `FNS_BuiltinCommands/TD_Components`.
- **Export Movie** (id `exportmovie`): Open the Export Movie dialog, optionally preloaded with a TOP path. Method `ExportMovie` on `FNS_BuiltinCommands/TD_Dialogs`. Params: `top: str = ''`.
- **Floating copy of pane** (id `floatingpanecopy`): Open a floating copy of the current pane. Method `FloatingPaneCopy` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Home network view** (id `homenetwork`): Home the current network editor's view. Method `HomeNetwork` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Import File** (id `importfile`): Open TD's Import File dialog. Method `ImportFile` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Maximize Pane** (id `maximizepane`): Toggle maximize on the current pane. Method `MaximizePane` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Beat** (id `openbeat`): Open the beat / tap-tempo dialog. Method `OpenBeat` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Bookmarks** (id `openbookmarks`): Open the Bookmarks dialog. Method `OpenBookmarks` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Console** (id `openconsole`): Open the OS console window (not the Textport). Method `OpenConsole` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Errors** (id `openerrors`): Open the Errors dialog. Method `OpenErrors` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Key Manager** (id `openkeymanager`): Open the Key Manager dialog. Method `OpenKeyManager` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open MIDI Device Mapper** (id `openmidimapper`): Open the MIDI Device Mapper dialog. Method `OpenMidiMapper` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Palette Browser** (id `openpalettebrowser`): Open the Palette Browser. Method `OpenPaletteBrowser` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Performance Monitor** (id `openperformancemonitor`): Open the Performance Monitor. Method `OpenPerformanceMonitor` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Preferences** (id `openpreferences`): Open the Preferences dialog. Method `OpenPreferences` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Search** (id `opensearch`): Open the Search / Replace dialog. Method `OpenSearch` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Operator Snippets** (id `opensnippets`): Open Operator Snippets, optionally for one type (e.g. noiseTOP). Method `OpenSnippets` on `FNS_BuiltinCommands/TD_Dialogs`. Params: `optype: str = ''`.
- **Open Textport** (id `opentextport`): Open the Textport. Method `OpenTextport` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Version** (id `openversion`): Open the version / about dialog. Method `OpenVersion` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Open Window Placement** (id `openwindowplacement`): Open the Window Placement dialog. Method `OpenWindowPlacement` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Set pane type** (id `setpanetype`): Change the current pane to another pane type. Method `SetPaneType` on `FNS_BuiltinCommands/TD_Dialogs`. Params: `kind: menu (required)`.
- **Show op in floating pane** (id `showop`): Open a floating network pane on an operator path. Method `ShowOp` on `FNS_BuiltinCommands/TD_Dialogs`. Params: `path: str (required)`.
- **Tear away pane** (id `tearawaypane`): Tear the current pane into its own OS window. Method `TearAwayPane` on `FNS_BuiltinCommands/TD_Dialogs`.
- **Copy op path** (id `copyoppath`): Copy the selected operator's path to the clipboard. Method `CopyOpPath` on `FNS_BuiltinCommands/TD_Session`.
- **Customize op** (id `customizeop`): Open the Component Editor on the selected component, to add custom parameters. Method `CustomizeOp` on `FNS_BuiltinCommands/TD_Session`.
- **Customize parent** (id `customizeparent`): Open the Component Editor on the component whose network you are in, to add custom parameters. Method `CustomizeParent` on `FNS_BuiltinCommands/TD_Session`.
- **Load recent file** (id `loadrecent`): Load a File > Recent entry (1 = most recent). CLOSES this project. Method `LoadRecent` on `FNS_BuiltinCommands/TD_Session`. Params: `index: int = 1`.
- **Open op parameters** (id `openopparameters`): Open a floating parameter dialog for the selected operator. Method `OpenOpParameters` on `FNS_BuiltinCommands/TD_Session`.
- **Open op viewer** (id `openopviewer`): Open the selected operator's viewer window. Method `OpenOpViewer` on `FNS_BuiltinCommands/TD_Session`.
- **Open parent parameters** (id `openparentparameters`): Open a floating parameter dialog for the component whose network you are in. Method `OpenParentParameters` on `FNS_BuiltinCommands/TD_Session`.
- **Open Project Folder** (id `openprojectfolder`): Show the project's folder in Explorer / Finder. Method `OpenProjectFolder` on `FNS_BuiltinCommands/TD_Session`.
- **Open TD folder** (id `opentdfolder`): Show one of TD's own folders in Explorer / Finder. Method `OpenTdFolder` on `FNS_BuiltinCommands/TD_Session`. Params: `folder: menu (required)`.
- **Quit TouchDesigner** (id `quittouchdesigner`): Quit TD (prompts about unsaved changes first). Method `QuitTouchDesigner` on `FNS_BuiltinCommands/TD_Session`.
- **Save Project** (id `saveproject`): Save the project (respects the Increment Filename preference). Method `SaveProject` on `FNS_BuiltinCommands/TD_Session`.
- **Save project + external toxes** (id `saveprojectwithtoxes`): Save the project AND write all dirty external .tox files. Method `SaveProjectWithToxes` on `FNS_BuiltinCommands/TD_Session`.
- **Set Cook Rate** (id `setcookrate`): Set the project cook rate (advanced). Method `SetCookRate` on `FNS_BuiltinCommands/TD_Session`. Params: `fps: float (required)`.
- **Set master volume** (id `setmastervolume`): Set TD's master audio volume (0-1). Method `SetMasterVolume` on `FNS_BuiltinCommands/TD_Session`. Params: `level: float (required)`.
- **Toggle Perform Mode** (id `toggleperformmode`): Toggle perform mode. Method `TogglePerformMode` on `FNS_BuiltinCommands/TD_Session`.
- **Toggle perform on start** (id `toggleperformonstart`): Toggle whether this project opens straight into perform mode. Method `TogglePerformOnStart` on `FNS_BuiltinCommands/TD_Session`.
- **Toggle Power** (id `togglepower`): MASTER power switch - off halts ALL processing (advanced). Method `TogglePower` on `FNS_BuiltinCommands/TD_Session`.
- **Toggle Realtime** (id `togglerealtime`): Toggle realtime playback mode. Method `ToggleRealtime` on `FNS_BuiltinCommands/TD_Session`.
- **Toggle window on top** (id `togglewindowontop`): Toggle keep-on-top for TD's main window. Method `ToggleWindowOnTop` on `FNS_BuiltinCommands/TD_Session`.

## FNS_ConfigHost

- **Load all tool configs** (id `loadallconfigs`): Load every registered tool's config. Method `LoadAllConfigs`.
- **Open FNS settings** (id `openconfigsettings`): Open the FNS_Config settings UI. Method `OpenConfigSettings`.
- **Save all tool configs** (id `saveallconfigs`): Save every registered tool's config. Method `SaveAllConfigs`.

## FNS_ConfigRegistry

- **Load all tool configs** (id `loadallconfigs`): Load every registered tool's config. Method `LoadAllConfigs`.
- **Open FNS settings** (id `openconfigsettings`): Open the FNS_Config settings UI. Method `OpenConfigSettings`.
- **Save all tool configs** (id `saveallconfigs`): Save every registered tool's config. Method `SaveAllConfigs`.

## FNS_CustomParTools

- **Customize current COMP** (id `customizecurrentcomp`): Open the component editor on the selected operator. Method `CustomizeCurrentComp`.
- **Customize parent COMP** (id `customizeparentcomp`): Open the component editor on the current network's COMP. Method `CustomizeParentComp`.
- **Open current COMP parameters** (id `opencurrentparameters`): Open a floating parameter dialog for the selected operator. Method `OpenCurrentParameters`.
- **Open parent COMP parameters** (id `openparentparameters`): Open a floating parameter dialog for the current network's COMP. Method `OpenParentParameters`.
- **Promote pars of selected** (id `promoteselected`): Promote custom parameters of the selected operators. Method `PromoteSelected`.
- **Clear custom pars of selected** (id `clearselectedpars`): Remove ALL custom parameters from the selected operators (undoable). Method `ClearSelectedPars` on `ClearPars`.
- **Create extension on current** (id `createextoncurrent`): Run QuickExt's extension creator on the current COMP. Method `CreateExtOnCurrent` on `QuickExt`.
- **Toggle QuickParCustom** (id `toggleactive`): Enable or disable QuickParCustom. Method `ToggleActive` on `QuickParCustom`.
- **Add parent shortcut** (id `addshortcuttocurrent`): Add a parent shortcut to the current COMP (prompts for the name). Method `AddShortcutToCurrent` on `QuickParent`.

## FNS_ExprHotStrings

- **Open hot-strings editor** (id `openhotstrings`): Open the expression hot-strings editor. Method `OpenHotStrings`.

## FNS_GlobalVolControl

- **Set volume** (id `setvolume`): Set the global output volume (0-1). Method `SetVolume`. Params: `level: float (required)`.
- **Toggle mute** (id `togglemute`): Mute or unmute the global audio output. Method `ToggleMute`.

## FNS_HotkeyManager

- **Load hotkeys** (id `loadhotkeyscmd`): Load the saved hotkey bindings. Method `LoadHotkeysCmd`.
- **Open hotkey UI** (id `openhotkeyui`): Open the hotkey manager lister. Method `OpenHotkeyUI`.
- **Save hotkeys** (id `savehotkeyscmd`): Save the current hotkey bindings. Method `SaveHotkeysCmd`.

## FNS_Hub

- **Open FNS Hub** (id `openhub`): Open the FNS Hub window: every registry's configurator, the console, and any tab a tool contributes. Method `OpenHub`.
- **Open main-menu configurator** (id `openmainmenuconfigurator`): Open FNS Hub on the Main Menu tab (the configurator lives in the hub). Method `OpenMainMenuConfigurator`.
- **Toggle FNSTools perform mode** (id `toggleperform`): Toggle FNSTools Perform Mode: the tools that only serve the network editor stop, and come back as they were. Method `TogglePerform`.

## FNS_HydroHomie

- **Set HydroHomie interval** (id `setinterval`): Set the hydration reminder interval in minutes. Method `SetInterval`. Params: `minutes: float = 45`.
- **Toggle HydroHomie** (id `toggle`): Show or hide the hydration reminder overlay. Method `Toggle`.

## FNS_Misc

- **Open toolbar configurator** (id `opentoolbarconfigurator`): Open FNS_Hub on the Toolbar tab (the configurator lives in the hub). Method `OpenToolbarConfigurator`.
- **Toggle global mouse input** (id `toggleglobalmouse`): Toggle the Global Mouse CHOP used for mappings. Method `ToggleGlobalMouse`.

## FNS_OpFamily

- **Remove Operator Family** (id `removeoperatorfamily`): Take the FNS tab out of the OP Create dialog and keep it off; your FNS tools stay installed. Pick Tools turns it back on Method `RemoveOperatorFamily`.
- **Replace Family Stubs** (id `replacefamilystubs`): Bring every FNS stub back as the full operator from the family folder Method `ReplaceFamilyStubs`. Params: `only_current_network: toggle = False`.
- **Stub Family Operators** (id `stubfamilyoperators`): Turn every placed FNS operator into a light stub that keeps its wiring and retained parameters Method `StubFamilyOperators`. Params: `only_current_network: toggle = False`.
- **Sync Family From Store** (id `syncfamilyfromstore`): Mirror the store's family members into the family folder now Method `SyncFamilyFromStore`.
- **Update Family Operators** (id `updatefamilyoperators`): Upgrade placed FNS operators to the newest version in the family folder, keeping retained parameters and state Method `UpdateFamilyOperators`. Params: `only_current_network: toggle = False`.

## FNS_OpMenuMods

- **Resync op menu** (id `resyncopmenu`): Re-collect the op-menu contributions from all tools. Method `ResyncOpMenu`.

## FNS_OpTemplates

- **Add selection to templates** (id `addtotemplates`): Save the current selection as a new template. Method `AddToTemplates`.
- **Open templates** (id `opentemplates`): Open the OP templates browser (floating). Method `OpenTemplates`.
- **Refresh templates** (id `refreshtemplatescmd`): Reload the templates from disk. Method `RefreshTemplatesCmd`.
- **Save templates** (id `savetemplates`): Write the templates tox to disk. Method `SaveTemplates`.

## FNS_OpToClipboard

- **Copy op to clipboard** (id `copyoptoclipboard`): Copy the current operator to the OS clipboard. Method `CopyOpToClipboard`.
- **Toggle OpToClipboard** (id `toggleactive`): Enable or disable OpToClipboard. Method `ToggleActive`.

## FNS_OpenExt

- **Open extension of current** (id `opencurrentext`): Open the extension code of the current COMP. Method `OpenCurrentExt`.

## FNS_Output

- **Toggle NDI output** (id `togglendi`): Enable or disable the NDI output stream. Method `ToggleNdi`.
- **Toggle perform window** (id `toggleperformwindow`): Open or close the FNS perform output window. Method `TogglePerformWindow`.
- **Toggle Spout/Syphon output** (id `togglespout`): Enable or disable the Spout/Syphon output (sender TD_FNS_OUT). Method `ToggleSpout`.

## FNS_PaneTypeRegistry

- **Floating network editor** (id `floatingnetworkeditor`): Open a floating network editor on the current network. Method `FloatingNetworkEditor`.

## FNS_ParOPDrop

- **Toggle ParOPDrop** (id `toggleactive`): Enable or disable ParOPDrop. Method `ToggleActive`.

## FNS_ParRandomizer

- **Randomize pars of op** (id `randomizeop`): Randomize all parameters of the current operator. Method `RandomizeOp`.
- **Randomize rollover par** (id `randomizerollover`): Randomize the parameter under the mouse. Method `RandomizeRollover`.
- **Reset custom pars to defaults** (id `resetcustomdefaults`): Reset the current op's custom parameters to their defaults. Method `ResetCustomDefaults`.
- **Save custom defaults** (id `savecustomdefaults`): Store the current custom parameter values as defaults. Method `SaveCustomDefaults`.
- **Toggle ParRandomizer** (id `toggleactive`): Enable or disable ParRandomizer. Method `ToggleActive`.

## FNS_QuickCollapse

- **Collapse selected** (id `collapseselected`): Collapse the selected operators into a container. Method `CollapseSelected`.
- **Toggle QuickCollapse** (id `toggleactive`): Enable or disable QuickCollapse. Method `ToggleActive`.

## FNS_QuickPane

- **Split pane** (id `splitpane`): Split the current pane in the given direction. Method `SplitPane`. Params: `dir: menu = 'right'`.
- **Toggle QuickPane** (id `toggleactive`): Enable or disable QuickPane. Method `ToggleActive`.

## FNS_QuickTime

- **Reset timer** (id `resettimer`): Reset the QuickTime timer. Method `ResetTimer`.

## FNS_ResetPLS

- **Edit custom reset pars** (id `editcustomresetpars`): Open the custom reset pars editor. Method `EditCustomResetPars`.
- **Edit reset static exceptions** (id `editstaticexceptions`): Open the static exceptions editor. Method `EditStaticExceptions`.
- **Reset all generators** (id `resetgenerators`): Pulse Reset on every enabled generator OP type (the panic button). Method `ResetGenerators`.

## FNS_SearchFix

- **Repatch find bars** (id `repatchfindbars`): Apply the search to every find bar again, for example after TouchDesigner rebuilt one. Method `RepatchFindBars`.
- **Toggle SearchFix** (id `toggleactive`): Switch the Python find-bar search on or off; off is TouchDesigner's own find bar. Method `ToggleActive`.
- **Toggle fuzzy find** (id `togglefuzzy`): Also match loosely in the find bar: first letters of words, a typo or two. Method `ToggleFuzzy`.
- **Toggle legacy find** (id `togglelegacy`): Search like TouchDesigner's own find bar: names that start with the text, case-sensitive. Method `ToggleLegacy`.

## FNS_SetSmoothness

- **Smoothness -> all** (id `smoothnessall`): Apply the smoothness setting to all operators in the network. Method `SmoothnessAll`.
- **Smoothness -> selected** (id `smoothnessselected`): Apply the smoothness setting to the selected operators. Method `SmoothnessSelected`.

## FNS_SwapOps

- **Swap selected ops** (id `swapselected`): Swap the connections of the selected operators. Method `SwapSelected`.

## FNS_SwitchOPs

- **Toggle SwitchOPs** (id `toggleactive`): Enable or disable SwitchOPs. Method `ToggleActive`.

## FNS_Updater

- **Check for updates** (id `checkforupdates`): Check the store for FunctionStore tool updates. Method `CheckForUpdates`.
- **Install agent skill** (id `installagentskill`): Copy the FNSTools agent skill into this project or your user skills folder Method `InstallAgentSkill`. Params: `where: menu = 'project'`, `agents_md: toggle = False`.
- **Update tools** (id `updatetools`): Download and install available tool updates. Method `UpdateTools`.

## FNS_VSCodeTools

- **Deploy stubs** (id `deploystubs`): Deploy TD typing stubs for code completion. Method `DeployStubs`.
- **Externalize selected** (id `externalizeselected`): Externalize the selected DATs to files. Method `ExternalizeSelected`.
- **Open project in VSCode** (id `openproject`): Open the project workspace in Visual Studio Code. Method `OpenProject`.

## PasteFromClipboard

- **Paste as annotate** (id `pasteannotate`): Paste the clipboard image into an annotate. Method `PasteAnnotate`.
- **Paste image** (id `pasteimage`): Paste the clipboard image into the network. Method `PasteImage`.
- **Paste as Script TOP** (id `pastescripttop`): Paste the clipboard image as a Script TOP. Method `PasteScriptTop`.

## QuickMarks

- **Clear quickmark** (id `clearmark`): Clear the quickmark stored in the given slot. Method `ClearMark`. Params: `slot: int (required)`.
- **Go to quickmark** (id `gotomark`): Jump to the quickmark stored in the given slot. Method `GoToMark`. Params: `slot: int (required)`.
- **List quickmarks** (id `listmarks`): List every populated quickmark slot with its name and network. Method `ListMarks`.
- **Name quickmark** (id `namemark`): Set the label shown for a quickmark slot. Method `NameMark`. Params: `slot: int (required)`, `name: str = ''`.
- **Store quickmark** (id `storemark`): Store the current network location in the given slot. Method `StoreMark`. Params: `slot: int (required)`.
- **Toggle QuickMarks** (id `toggleactive`): Enable or disable QuickMarks. Method `ToggleActive`.
- **Toggle QuickMarks overlay** (id `toggleoverlay`): Show or hide the mark list and the outlines; marks and Ctrl+number keep working. Method `ToggleOverlay`.

## TopToMidi

- **All Notes Off** (id `allnotesoff`): Send note-off for every note on the MIDI and VST outputs Method `AllNotesOff`.
- **Install Mingus** (id `installmingus`): Install the mingus package this tool needs Method `InstallMingus`.
- **Open Help** (id `openhelp`): Open the TopToMidi documentation Method `OpenHelp`.
