# AutoCombine

Package `FNS_AutoCombine`.

Hold Alt while placing a generator TOP to have it come in pre-set to composite over its input.

- Category: Network
- Version: 3.2.11
- Access: Free
- Docs: https://functionstore.tools/docs/fns-autocombine/

## What it does

- **Composite as you place**: Hold `Alt` while placing a generator TOP such as a Noise, Circle or Rectangle onto a chain, and it comes in set to combine with its input.
- **Blend and format defaults**: The Combine with Input mode, the Operation, the Pixel Format and the Noise TOP's RGB mode all come from your settings on AutoCombine.
- **Alt or another modifier key**: Pick the key that arms the gesture; the default chooses the right one per platform.
- **Skip reloads and large batches**: Acts only on the operator that just appeared in the network you are looking at; operators surfacing deeper down and large batches are left alone.
- **Toggle from quick-launch**: The Toggle AutoCombine command switches it off and on without opening its parameters.

## Reach it

`op.AUTO_COMBINE` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `SetCombine(_op)`: Apply the tool's combine settings (operand, RGB and the rest) to a newly created operator that has inputs, while the tool is active; called for each new operator.
- `ToggleActive()`: Enable or disable AutoCombine.

## Commands

- **Toggle AutoCombine** (id `toggleactive`): Enable or disable AutoCombine. Method `ToggleActive`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn AutoCombine on or off. When on, dropping a generator TOP (noise, circle, rectangle...) with the modifier held applies the defaults below to it. Off leaves the component installed but idle.
- **Combine with Input** (`par.Combineinput`, Menu), default `compres`, menu `res`, `compres`: The Combine with Input mode written onto a generator TOP dropped this way: how it merges with the TOP it landed on.
- **Operation** (`par.Operand`, Menu), default `multiply`, menu `add`, `atop`, `average`, `brightest`, `burncolor`, `burnlinear`, `chromadifference`, `color`, `darkercolor`, `difference`, `dimmest`, `divide`, `dodge`, `exclude`, `freeze`, `glow`, `hardlight`, `hardmix`, `heat`, `hue`, `inside`, `insideluminance`, `inverse`, `lightercolor`, `luminancedifference`, `maximum`, `minimum`, `multiply`, `negate`, `outside`, `outsideluminance`, `over`, `overlay`, `pinlight`, `reflect`, `screen`, `softlight`, `linearlight`, `stencilluminance`, `subtract`, `subtractive`, `under`, `vividlight`, `xor`, `yfilm`, `zfilm`: The Operation written onto the dropped TOP: the maths used to combine it with its input.
- **RGB** (`par.Rgb`, Menu), default `add`, menu `noise`, `multiply`, `add`, `subtract`: The RGB mode written onto generator TOPs that have one (the Noise TOP): whether the noise replaces, multiplies, adds to or subtracts from the input.
- **Pixel Format** (`par.Format`, Menu), default `useinput`, menu `useinput`, `rgba8fixed`, `srgba8fixed`, `rgba16float`, `rgba32float`, `_separator_`, `rgb10a2fixed`, `rgba16fixed`, `rgba11float`, `rgb16float`, `rgb32float`, `mono8fixed`, `mono16fixed`, `mono16float`, `mono32float`, `rg8fixed`, `rg16fixed`, `rg16float`, `rg32float`, `a8fixed`, `a16fixed`, `a16float`, `a32float`, `monoalpha8fixed`, `monoalpha16fixed`, `monoalpha16float`, `monoalpha32float`: The Pixel Format written onto the dropped TOP. 'Use Input' leaves TouchDesigner's own default alone.
- **Keys** (`par.Keys`, Str): The modifier keys held to trigger this gesture, space-separated (TouchDesigner key names). The default is an expression that picks the right keys per platform. Typing a plain value over it pins the tool to one OS.
