# ColorUI

Package `FNS_ColorUI`.

Operator and family colour palettes, with the active palette roaming through config.

- Category: Interface
- Version: 3.2.12
- Access: Free
- Docs: https://functionstore.tools/docs/fns-colorui/

## What it does

- **Recolour UI elements**: Every colour in TouchDesigner's interface in one list, each with its default and a reset.
- **Operator family colours**: Recolour whole operator families, POPs included.
- **Save and reapply your colours**: Your colours are stored in the component, applied as the project opens, and follow you to other projects and through updates.
- **Filter the list**: Narrow the list by name with wildcards, to changed colours only, or to colours close to a reference colour.
- **Change many at once**: Give one colour to everything listed, or to a whole group, and reset a group in one go.
- **Randomize and undo**: Throw random colours at the whole interface, then put your own colours back with one click.
- **Share your colours as JSON**: Export writes only the colours you changed to a JSON file, to keep with a project, commit or send to someone.
- **Import a JSON palette**: Import applies such a file; its colours take precedence over the ones stored locally, and elements this build does not know are skipped.
- **Open from Hub or quick-launch**: The colour editor opens from the OpColor tab of Hub (the FNS button in the main-menu bar), Open color UI in quick-launch, or Open UI on the component.
- **Console tab in the browser**: With Expose to Console on, the same editor is served in the browser as the ColorUI tab of Console, the toolkit's web front.

## Reach it

`op.FNS_COLOR_UI` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `ApplyOverrides()`: Write every stored override into ui.colors.
- `ConsoleCommand(msg)`: One page->TD message, same vocabulary as the title bridge (_dispatch), answered with the resulting state plus any toasts the command raised.
- `ConsoleState()`: The page state as the console tab's HTTP answer: {'ok', 'state'}.
- `DoExport(dialog=False)`: Save the stored overrides as JSON to the File parameter's path, or one chosen in a dialog.
- `DoImport(dialog=False)`: Load UI colors from the JSON file the File parameter names, or one chosen in a dialog, and apply them.
- `ExportPalette()`: Export the current UI colors to file.
- `ImportPalette()`: Import a UI color palette from file.
- `OnBrowserTitle(raw)`: Called by watch_browser when the page rewrites document.title.
- `OnConsoleExposure(exposed)`: FNS_Console hand-off: the host calls this instead of flipping the renderer itself, so the viewer rule above stays the single owner.
- `OnHubExposure(exposed)`: FNS_Hub hand-off: our panel is the hub's OpColor tab; the hub calls this as the tab is shown/hidden.
- `OnStart()`: Project start (execute1 onStart/onCreate).
- `OpenColorUI()`: Open the TouchDesigner UI color editor.
- `OpenUI()`: Served by the console: open its ColorUI tab.
- `Overrides` (property): The UI color overrides this tool stores on its COMP, element name to RGB.
- `Randomize()`: Give every UI color a random value (UndoRandom takes it back).
- `RandomizeColors()`: Randomize the UI colors.
- `ResetAll()`: Reset every UI color to TouchDesigner's defaults and drop the stored overrides.
- `ResetAllColors()`: Reset every UI color to its default.
- `SendState()`: Push the current color state to the page in the in-TD browser.
- `SyncLocalBrowser()`: The local Web Render runs only while someone can see it: the viewer is open AND the console is not serving the page.
- `Toast(text)`: Show a short message on the page; a console request in flight collects it for its answer.
- `UndoRandom()`: Undo Randomize: TouchDesigner's defaults with the stored overrides applied again.
- `UndoRandomize()`: Undo the last color randomization.

## Commands

- **Export color palette** (id `exportpalette`): Export the current UI colors to file. Method `ExportPalette`.
- **Import color palette** (id `importpalette`): Import a UI color palette from file. Method `ImportPalette`.
- **Open color UI** (id `opencolorui`): Open the TouchDesigner UI color editor. Method `OpenColorUI`.
- **Randomize colors** (id `randomizecolors`): Randomize the UI colors. Method `RandomizeColors`.
- **Reset all colors** (id `resetallcolors`): Reset every UI color to its default. Method `ResetAllColors`.
- **Undo randomize** (id `undorandomize`): Undo the last color randomization. Method `UndoRandomize`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_Console`
- `FNS_HubRegistry`

## Parameters

### ColorUI

- **Open UI** (`par.Openui`, Pulse): Open the colour editor. It is also the OpColor tab of FNS_Hub, and, with Expose on the Registry page, a tab of FNS_Console in the browser.
- **File (.json)** (`par.File`, FileSave): Where Export writes and Import reads. A .json file you can keep in a project, commit, or hand to someone else.
- **Import** (`par.Import`, Pulse): Read colours from the file above and apply them. Imported colours take precedence over the ones saved locally in the component.
- **Export** (`par.Export`, Pulse): Write the current colours to the file above, so they can be shared or version-controlled.
- **Auto-Load Colors** (`par.Autoload`, Toggle), default `on`: Apply the colours saved in this component when the project opens. Off leaves TouchDesigner's own colours until you open the UI and apply.
- **Group By** (`par.Groupby`, Menu), default `prefix`, menu `prefix`, `role`: How the editor's list is organised: Prefix groups elements by the name they start with, Role groups them by what they are used for.
