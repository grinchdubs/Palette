# VSCodeTools

Package `FNS_VSCodeTools`.

VS Code integration: open externalized scripts, sync files and generate TouchDesigner type stubs.

- Category: Developer
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-vscodetools/

## What it does

- **Open the project in VS Code**: One click creates the project's workspace file and opens it in VS Code or Cursor.
- **Sync a DAT to a file**: `Ctrl+Shift+E` writes the DAT you are on to a file named after it, and from then on the DAT and the file stay in sync both ways.
- **File type and folder picked for you**: The file extension comes from the DAT's language or contents, and an extension's script goes in a subfolder named after its COMP.
- **Choose the name and path**: `Ctrl+Shift+Alt+E` asks for the file's name and path before syncing.
- **Python typing stubs**: Deploys stubs for your extensions and TouchDesigner's built-in Python typings, so the editor autocompletes them, through an integration of Stubser.
- **Clear syncs before shipping**: Drops the syncs and the tool's tags for the selected DATs, a network, or the whole project, so the content lives in the .toe again.

## Reach it

`op.FNS_VSCODETOOLS` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `DeployStubs()`: Deploy TD typing stubs for code completion.
- `ExternalizeSelected()`: Externalize the selected DATs to files.
- `OpenProject()`: Open the project workspace in Visual Studio Code.

## Commands

- **Deploy stubs** (id `deploystubs`): Deploy TD typing stubs for code completion. Method `DeployStubs`.
- **Externalize selected** (id `externalizeselected`): Externalize the selected DATs to files. Method `ExternalizeSelected`.
- **Open project in VSCode** (id `openproject`): Open the project workspace in Visual Studio Code. Method `OpenProject`.

## Hotkeys

- `ctrl.shift.e ctrl.shift.alt.e` (`shortcuts` on `ScriptSyncFile/keyboardin1`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Code.exe** (`par.Codeexe`, File): Path to your editor's executable (code.exe, or Cursor). Auto-detect fills it from TouchDesigner's Preferences text-editor setting, so you usually never touch it.
- **Workspace** (`par.Workspace`, File): Path to the .code-workspace file this project opens. Auto-detect names it after the project file.
- **Auto-detect** (`par.Autodetect`, Toggle), default `off`: Fill Code.exe and Workspace automatically: the editor from TouchDesigner's Preferences, the workspace from the project's name. On by default; turn it off to pin either by hand.
- **Auto-open** (`par.Startup`, Toggle), default `off`: Open the workspace in your editor as soon as the project starts.
- **Open** (`par.Open`, Pulse): Open the workspace now. If none exists yet, one is created in the project root and opened.
- **Sync settings** (`par.Syncsettings`, Header)
- **Script Sync Base Folder** (`par.Folder`, Folder): Where synced scripts are written, relative to the project root. An extension script also gets a subfolder named after the COMP it belongs to.
- **Use Ctrl+Shift+E Shortcut** (`par.Shortcutactive`, Toggle), default `off`: Enable the sync shortcut: it externalizes the selected DAT into the folder above, named after the operator. Add Alt to force the dialog and choose another name or path.
- **Sync File Selected** (`par.Externalizeselected`, Pulse): Sync the selected DAT to a file now, the same action as the shortcut.

### Clear

- **Tags** (`par.Tags`, Str): Read-only. The tags this tool puts on every DAT it syncs, and looks for when clearing: an operator must carry all of them to count as synced.
- **Clear Synced Scripts... (undoable)** (`par.Clear`, Header)
- **selected DATs** (`par.Clearselected`, Pulse): Drop the sync and this tool's tags from the selected DATs, so their content lives in the project file again.
- **in current pane** (`par.Clearcomp`, Pulse): Drop the sync and tags from every DAT in the current pane, not descending into children.
- **in current pane and all children** (`par.Clearcompchildren`, Pulse): Drop the sync and tags from every DAT in the current pane and all of its children.
- **all in project** (`par.Clearall`, Pulse): Drop the sync and tags from every synced DAT in the project. Do this before shipping a .toe without its script files. Otherwise it opens looking for files that are not there.

### Stubs

- **Stubs Tags** (`par.Tags2`, Str), default `TDExtension FNS_externalized`: Read-only. The tags that mark an operator as stub-bearing, the same way the Clear tab's tags mark a synced DAT.
- **Private** (`par.Private`, Toggle), default `off`: Include methods and attributes whose names start with '_' in the generated stubs.
- **Unpromoted** (`par.Unpromoted`, Toggle), default `on`: Include unpromoted members, the lowercase ones that are not reachable straight off the COMP, in the generated stubs.
- **Deploy Stubs** (`par.Deploystubs`, Pulse): Generate Python typing stubs for the selected DATs, or for the selected COMPs' extensions, so your editor can autocomplete them.
- **TD Typings** (`par.Tdtypings`, Header)
- **Install** (`par.Install`, Pulse): Install TouchDesigner's own built-in Python typings, so td module members autocomplete in your editor.
- **Force** (`par.Force`, Pulse): Install the built-in typings even when they are already there, overwriting them. Use it after a TouchDesigner upgrade.

### About

- **README** (`par.Open2`, Pulse): Open this tool's README.
