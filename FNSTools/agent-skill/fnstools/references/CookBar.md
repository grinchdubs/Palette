# CookBar

Draws a bar above every operator in the network you are viewing: its cook time on top, its GPU memory below, so the expensive parts of a network stand out at a glance, with the numbers beside them if you like. A Top List in a corner names the heaviest operators and takes you to one with a click. Its toolbar button switches it on; Ctrl+right-click the button for a global Hog CHOP to stress-test against. Based on Anton Heestand's Cook Bar.

- Category: Network
- Version: 1.0.7
- Access: Free
- Docs: https://functionstore.tools/docs/cookbar/

## What it does

- **Toggle from the toolbar or quick-launch**: Click the toolbar button, run Toggle cook bar from quick-launch or switch Active on; the button lights up while the bars are on.
- **Cook time at a glance**: A bar above each operator shows its CPU plus GPU cook time, green to red up to 1 ms and growing taller past it, with stripes while it cooks.
- **GPU memory at a glance**: A bar below each operator shows the GPU memory it holds, cyan to blue up to 100 MB and growing taller up to 1 GB.
- **COMP totals**: On a COMP, the bars add up the cook time and GPU memory of everything inside it, so you can find the heavy part from the top of a project down.
- **Cooking-off marker**: A COMP whose cooking is switched off gets a grey hatched bar, so a frozen network explains itself.
- **Numeric values beside the bars**: Each bar can write its number beside it, cook time above the operator and GPU memory below.
- **Top List of the heaviest operators**: A corner list names the heaviest operators by cook time or GPU memory; click a row to select that operator and zoom to it.
- **Stress test with a Hog CHOP**: A global Hog CHOP eats part of every frame on purpose, so you can watch how the network copes; the toolbar button turns red while it runs.
- **Overlay that leaves the network untouched**: The bars draw on the shared network overlay, which leaves before every save, so display flags, annotations and operators stay as they were.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('CookBar')`; its promoted methods are called on that COMP.

## Promoted API

- `BarActive()`: Whether the bars are on (the Toggle cook bar chip).
- `HogActive()`: Whether the Global Hog CHOP is on (the Toggle Global Hog CHOP chip).
- `OpenHog()`: Open the Global Hog CHOP's parameters, to eat frame time on purpose while you watch the bars.
- `ToggleCookBar()`: Show or hide each operator's cook time and GPU memory above it in the network editor.
- `ToggleHog()`: Switch the Global Hog CHOP on or off.

## Commands

- **Open Global Hog CHOP** (id `openhog`): Open the Global Hog CHOP's parameters, to eat frame time on purpose while you watch the bars. Method `OpenHog`.
- **Toggle cook bar** (id `togglecookbar`): Show or hide each operator's cook time and GPU memory above it in the network editor. Method `ToggleCookBar`.
- **Toggle Global Hog CHOP** (id `togglehog`): Switch the Global Hog CHOP on or off. It DELIBERATELY eats frame time (stress test). Method `ToggleHog`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_OverlayRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### CookBar

- **Active** (`par.Active`, Toggle), default `on`: Draw a bar above each operator in the network you are viewing: the top bar is its cook time (CPU + GPU, full at 1 ms), the bottom one its GPU memory. Works while the timeline plays.
- **Top List** (`par.Toplist`, Toggle), default `on`: Show a list of the viewed network's heaviest operators in a corner of the network editor while Cook Bar is on. Click a row to go there, or a tab at the top to change what it ranks by.
- **Rank By** (`par.Toprank`, Menu), default `cooktime`, menu `cooktime`, `gpumemory`: What the Top List ranks by: cook time (CPU and GPU per frame, a COMP with everything inside it) or GPU memory.
- **List Corner** (`par.Topcorner`, Menu), default `topleft`, menu `topleft`, `topright`, `bottomleft`, `bottomright`: Which corner of the network editor the Top List sits in.
- **List Margin** (`par.Topmargin`, Int), default `12`: How far the Top List sits from the edges of the network editor, and from any other tool's widget before it in the same corner, in screen points.
- **List Order** (`par.Toporder`, Int), default `100`: The Top List's place among the widgets in the same corner: lower sits nearer the corner. The Overlay tab in FNS_Hub sets it when you drag.
- **List Rows** (`par.Toprows`, Int), default `8`: How many operators the Top List shows, 1 to 12.
- **Top List Collapsed** (`par.Topcollapsed`, Toggle), default `off`: Fold the Top List to its tab row. The arrow at the right of the tabs does the same.
- **Max OPs** (`par.Maxops`, Int), default `100`: The most operators drawn at once, nearest the middle of the view first (up to 250, what the shader holds). Only operators in view count. More costs GPU time: about 0.1 ms at 50, 0.25 ms at 100 and 1.4 ms at 250 for a 1536x700 pane (measured), growing with the pane's size.
- **Values** (`par.Showvalues`, Toggle), default `off`: Write each bar's number next to it: the cook time above the operator and the GPU memory below it. Shown on operators wide enough on screen to fit them.
- **Annotation Alpha** (`par.Annotationalpha`, Float), default `0.2`: While the bars are on, the back colour of every annotation in the network you are viewing is lowered to this alpha so the bars behind it show, and put back when you leave or switch off. An annotation that is already fainter is left as it is.
- **Open Global Hog CHOP** (`par.Openhog`, Pulse): Open the parameters of the Global Hog CHOP, which eats frame time on purpose so you can watch how the network copes. Ctrl+right-click on the toolbar button does the same. The button turns red while the Hog is on.
