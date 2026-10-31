# SetSmoothness

Package `FNS_SetSmoothness`.

Set Input/Viewer Smoothness on selected TOPs, or on every TOP in the network.

- Category: Parameters
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-setsmoothness/

## What it does

- **Set smoothness on selected TOPs**: Click the toolbar button, pick a filtering mode, and it is written to the Input and Viewer Smoothness of the selected TOPs.
- **Apply to every TOP in the network**: Hold `Alt` while picking to write it to every TOP in the current network.
- **Change input and viewer smoothness separately**: Set the two values separately on the component and apply them with a pulse or a quick-launch command.
- **Components with their own smoothness**: Components that carry their own Input or Viewer Smoothness parameters, such as RealRamp, are set along with the TOPs.
- **Run from quick-launch**: Smoothness -> selected and Smoothness -> all apply the settings with no toolbar button needed.

## Reach it

`op.SMOOTHNESS_SET` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `OnAll()`: Set the configured smoothness on every operator in the current network.
- `OnSelected()`: Set the configured smoothness on the selected operators; called by the hotkey.
- `SmoothnessAll()`: Apply the smoothness setting to all operators in the network.
- `SmoothnessSelected()`: Apply the smoothness setting to the selected operators.

## Commands

- **Smoothness -> all** (id `smoothnessall`): Apply the smoothness setting to all operators in the network. Method `SmoothnessAll`.
- **Smoothness -> selected** (id `smoothnessselected`): Apply the smoothness setting to the selected operators. Method `SmoothnessSelected`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Input Smoothness** (`par.Inputfiltertype`, Menu), default `linear`, menu `nearest`, `linear`, `mipmap`: The Input Smoothness value written to the TOPs you apply to: how the texture is sampled coming in. 'Use Input' leaves each TOP's existing setting alone.
- **Viewer Smoothness** (`par.Filtertype`, Menu), default `linear`, menu `useinput`, `nearest`, `linear`: The Viewer Smoothness value written to the TOPs you apply to: how the texture is filtered when displayed. 'Use Input' leaves each TOP's existing setting alone.
- **Selected** (`par.Selected`, Pulse): Apply the two smoothness settings above to the currently selected TOPs.
- **All** (`par.All`, Pulse): Apply the two smoothness settings above to every TOP in the current network.
- **Modifier Key** (`par.Keys`, Str): Modifier held while scrolling to set input smoothness on the hovered operator.
