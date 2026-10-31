# CommandRegistry

Package `FNS_CommandRegistry`.

Collects the commands your tools declare and serves them to whatever can run them: the in-TouchDesigner command palette and the TDX launcher. Discovery is by tag, so a tool installed before any consumer still appears the moment one arrives.

- Category: Core
- Version: 3.2.11
- Access: Free
- Docs: https://functionstore.tools/docs/fns-commandregistry/

## What it does

- **Share one list across palettes**: The CommandPalette and TDX Launcher Ultra read the same commands, and favourites, hidden commands and presets made in one show in the other.
- **Tag-based tool discovery**: Finds tools tagged fnscommands and harvests their commands, so a tool installed before any palette or launcher still appears when one arrives.
- **Curation that survives moves**: Favourites, hidden flags and presets are keyed on tool name and command id, so they survive a tool being moved in the network.
- **Presets per copy or pinned**: A preset runs on every copy of a tool, or is pinned to one instance label and waits quietly where no copy carries it.
- **Built-in TouchDesigner commands**: Serves TouchDesigner's own actions, such as the Textport, dialogs, pane changes, saving, recent files, realtime, perform mode and cook rate, badged TD in the palette.
- **Newest version wins for duplicates**: When two packages offer the same canonical command, the newest package version is served and the other set aside, so the list never doubles.
- **Tools work without it**: Every call a tool makes is guarded, so with no registry in the session nothing happens and nothing errors.
- **Commands derived from methods**: Builds each command's label, help and prompted parameters from the method's name, docstring and signature, with type hints setting input styles.
- **Declared context, surface and state**: Tools declare what a command acts on, where it is offered, where its live value lives, its capability group and a cross-package canonical id.
- **Commands for each tool copy**: Each copy of a multi-copy tool registers its commands under its own path, labelled by FnsInstance() and grouped under one name by FnsToolName().
- **Declaration validation**: Enforces limits at harvest (24 commands per tool, 6 parameters, 5 contexts, 8 surfaces) and rejects malformed declarations with a reason.
- **Consumer API**: Commands(), Run(key, args), RescanTools(), Shadowed(), Rev() and Version() let a palette or launcher list, run and re-harvest commands and check the contract version.

## Reach it

A registry. `op.FNS_COMMANDREGISTRY` is its global shortcut, promoted into /sys/FNS_Registries while the toolkit runs: call its promoted methods on that object from anywhere in the project, never on the master inside the toolkit root. See registries.md.

## Promoted API

- `Commands()`: Flat wire-ready list; prunes registrations whose tool is gone.
- `Register(owner, commands=None)`: Replace OWNER's registered command set.
- `Repromote()`: Dev helper: replace the /sys global with a fresh copy of THIS shipper, migrating registrations — regardless of version.
- `RescanTools()`: Collect commands from every COMP tagged TOOL_TAG: its promoted FnsCommands() spec list when it has one, else its decorated (`_fns_command`-marked) methods.
- `Rev()`: Monotonic change counter - bumps on every registry mutation.
- `Run(key, args=None, kwargs=None)`: Execute one registered command by key ('<owner path>#<id>').
- `Shadowed()`: Commands withheld because another package won their canonical id.
- `Unregister(owner)`: Drop OWNER's commands (COMP or path).
- `Version()`: This instance's registry version (family version-compare).

## Commands

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

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Command Registry

- **Rescan Tools** (`par.Rescan`, Pulse): Re-collect commands from COMPs tagged 'fnscommands' that promote FnsCommands(). Runs automatically on init; pulse after dropping a tool in by hand.
- **Status** (`par.Status`, Str): Read-only summary of the current registry: command and tool counts plus the change revision.
