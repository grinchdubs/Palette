# SwitchTools

Package `FNS_SwitchTools`.

A companion for any Switch, Cross or multi-input operator: index by slider, menu or bind, loop or clamp, colour the live input, cook only the inputs in use and unload the rest from the GPU, plus reorder, reverse, randomize and align the inputs.

- Category: Show & output
- Version: 1.1.9
- Access: Base
- Docs: https://functionstore.tools/docs/fns-switchtools/

## What it does

- **Drive the switch index**: Binds the switch's index to its own Index, so a slider, a menu of input names, a CHOP or a bound parameter drives it.
- **Loop, clamp or zigzag**: Decides what happens when the index runs past the last input: clamp at the ends, loop round to the first, or zigzag back.
- **Crossfade between inputs**: With Blend on, index values between two inputs crossfade between them.
- **Colour the live input**: Colours the input on screen in the network editor and the rest in a second colour.
- **Cook only what is on screen**: Input components the switch is not showing stop cooking until they are selected again.
- **Release unused memory**: Frees the CPU and GPU memory of inputs that went off screen, spread over several frames so the switch does not hitch.
- **Reverse or shuffle the inputs**: Flips or shuffles the input order in one click, and Restore Original goes back to the saved wiring.
- **Reorder inputs to match the layout**: Rewires the switch so the top node is the first input, or moves the nodes to match the wiring.
- **Align and rename input nodes**: Lines the input nodes up beside the switch and renames them so their digits match their index.
- **Callbacks on cook and selection changes**: Run your own Python when inputs start or stop cooking, or are selected and unselected.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `switchTools` (Switch Tools) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/FNS_SwitchTools.tox`. Its promoted methods are called on the placed copy.

## Promoted API

- `NumInputs` (attribute)
- `SwitchOP` (attribute)

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Custom

- **Switch OP** (`par.Switchop`, OP): The Switch, Cross or multi-input operator to drive. Dropping the tool next to it or docking it sets this too.
- **Bind** (`par.Bind`, Toggle), default `off`: Bind the switch operator's index (or Cross) to this tool's Index, so either one moves the other.
- **Control** (`par.Control`, Header)
- **Index** (`par.Index`, Float), default `0.0`: Which input is shown. With Blend on, values between inputs crossfade.
- **Blend** (`par.Blend`, Toggle), default `off`: Turn on the switch operator's blending between inputs, so fractional indexes crossfade.
- **Loop Type** (`par.Type`, Menu), default `off`, menu `off`, `clamp`, `loop`, `zigzag`: What happens when Index runs past the first or last input: off, clamp at the ends, loop round, or zigzag back.
- **Select** (`par.Select`, Menu): Pick an input by name; sets Index.
- **Current Select** (`par.Currentselect`, Menu): Read-only: the input currently shown.
- **Out Index** (`par.Outindex`, Float), default `0.0`: Read-only: the index actually sent to the switch operator after Loop Type.
- **Num Inputs** (`par.Numinputs`, Int), default `0`: Read-only: how many inputs the switch operator has.
- **Cooker** (`par.Cooker`, Header)
- **Control Cook (COMPs)** (`par.Controlcook`, Toggle), default `off`: Let only the input COMPs in use cook; the rest stop cooking until selected.
- **Unload GPU** (`par.Unloadgpu`, Toggle), default `off`: When an input stops being used, release its COMP's CPU/GPU memory a few frames later (cancelled if it is selected again first), paced by Unload Method and Unload Budget.
- **Unload Method** (`par.Unloadmethod`, Menu), default `progressive`, menu `progressive`, `legacy`: How an unused input COMP's memory is released. Progressive uses COMP.progressiveUnload() paced by Unload Budget and covers every node type including POPs. Immediate calls unload() on each unlocked TOP in one frame (the previous behaviour).
- **Unload Budget (ms/frame)** (`par.Unloadbudget`, Float), default `2.0`: Milliseconds per frame spent releasing an unused input's memory (COMP.progressiveUnload). Spreads the unload over several frames so a heavy input never hitches the frame it stops being used. 0 unloads everything in a single frame.
- **Colorize** (`par.Colorize`, Toggle), default `off`: Colour input nodes by state: On Color for the one in use, Off Color for the rest.
- **On Color** (`par.Oncolor`, RGBA x3), default `0.0`: Node colour of the input in use, with Colorize on.
- **Off Color** (`par.Offcolor`, RGBA x3), default `1.0`: Node colour of the inputs not in use, with Colorize on.
- **Active** (`par.Active`, Toggle), default `on`: Turn the tool off without removing it: the switch operator is unbound and left as it is.

### Inputs

- **Reverse Inputs** (`par.Reverseinputs`, Pulse): Reverse the order the inputs are wired in.
- **Randomize Inputs** (`par.Randomize`, Pulse): Rewire the inputs in a random order.
- **Order to NodeY (swap)** (`par.Reorderswitchops`, Pulse): Move the input nodes so their vertical position follows their input order.
- **NodeY to Order (reconnect)** (`par.Reorderswitchinputs`, Pulse): Rewire the inputs so their order follows the nodes' vertical position.
- **^(automatic)^** (`par.Positiontoorder`, Toggle), default `off`: Rewire automatically whenever an input node is moved, so the order always follows the layout.
- **Re-Digitize Inputs (rename)** (`par.Redigitizeinputs`, Pulse): Change the digits of the inputs to match the select index
- **^1 based index^** (`par.Onebasedindex`, Toggle), default `off`: Number inputs from 1 instead of 0 when renaming them.
- **Align Inputs (retoggle)** (`par.Aligninputs`, Toggle), default `off`: Re-toggle to re-align
- **Alignment Mode** (`par.Alignmentmode`, Menu), default `Center`, menu `Top`, `Center`, `Bottom`: How Align Inputs lines the input nodes up: top, centre or bottom.
- **Adjust Offset (X, Y, YGap)** (`par.Adjust`, Float x3), default `0.0`: Offsets used when aligning inputs: horizontal offset, vertical offset and the gap between nodes.
- **Save as Original** (`par.Save`, Pulse): Remember the current input wiring as the original.
- **Restore Original** (`par.Restore`, Pulse): Rewire the inputs back to the saved original.
- **Disconnect All Inputs** (`par.Disconnectall`, Pulse): Disconnect every input of the switch operator.
- **First == Last** (`par.Firstlast`, Toggle), default `off`: The last input repeats the first, so a loop closes cleanly; it is left out of reordering.

### Callbacks

- **Callbacks** (`par.Callbacks`, DAT): The DAT holding your callbacks: onCookingChange and onSelectionChange.
- **Create Callbacks** (`par.Createcallbacks`, Pulse): Create a callbacks DAT beside the tool and point Callbacks at it.

### About

- **Show Builtin Pages** (`par.Builtinpages`, Toggle), default `off`: Show the component's built-in parameter pages.
