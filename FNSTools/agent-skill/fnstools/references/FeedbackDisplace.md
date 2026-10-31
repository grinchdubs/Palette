# FeedbackDisplace

A feedback loop with a displace stage inside it: opacity, crossfade, filter size, displacement driven by a built-in noise or a second input, a per-pass transform, reset and a dry/wet mix. An alternative for the Feedback TOP.

- Category: Visual
- Version: 1.0.7
- Access: Base
- Docs: https://functionstore.tools/docs/feedbackdisplace/

## What it does

- **Trails with opacity and blur**: Each pass is composited over the input with an opacity and a blur, so trails, smears and echoes come straight from the parameters.
- **Noise or image displacement**: Warps every pass by a built-in animated noise, or by a displacement map wired into the in_displace input.
- **Zoom, spin and drift each pass**: Applies a transform on every pass for drift, zoom and spin, including infinite zooms.
- **Reset the loop**: Hold Reset to clear the loop, including the faint ghost an 8-bit loop at a high opacity leaves behind.
- **Mix dry and wet**: Dry / Wet Mix blends the whole effect with the input, and Cross fades between the fresh input and the loop.
- **Replace a Feedback TOP**: Offered in place of a Feedback TOP created with the alternatives shortcut held, wired into the same spot; also on the OP Create dialog's FNS tab.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `feedbackDisplace` (Feedback Displace) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/FeedbackDisplace.tox`. Its promoted methods are called on the placed copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

- `feedbackTOP`

## Requires

- `FNS_OpMenuRegistry`

## Parameters

### Feedback

- **Operation** (`par.Operand`, Menu), default `multiply`, menu `add`, `atop`, `average`, `brightest`, `burncolor`, `burnlinear`, `chromadifference`, `color`, `darkercolor`, `difference`, `dimmest`, `divide`, `dodge`, `exclude`, `freeze`, `glow`, `hardlight`, `hardmix`, `heat`, `hue`, `inside`, `insideluminance`, `inverse`, `lightercolor`, `luminancedifference`, `maximum`, `minimum`, `multiply`, `negate`, `outside`, `outsideluminance`, `over`, `overlay`, `pinlight`, `reflect`, `screen`, `softlight`, `linearlight`, `stencilluminance`, `subtract`, `subtractive`, `under`, `vividlight`, `xor`, `yfilm`, `zfilm`: How each pass of the feedback is composited over the input.
- **Opacity** (`par.Opacity`, Float), default `0.9`: How much of the previous frame survives each pass: higher values leave longer trails.
- **Cross** (`par.Cross`, Float), default `0.0`: Crossfades between the fresh input (0) and the feedback loop (1).
- **Filter Size** (`par.Size`, Int), default `1`: Blur on the loop each pass, in pixels.
- **Aspect Correct** (`par.Aspectcorrect`, Toggle), default `on`: Keep the displacement square on non-square images.
- **Displace Weight** (`par.Displaceweight`, XYZW x2), default `0.0`: How far the displacement pushes the image, per axis.
- **Source Midpoint** (`par.Midpoint`, XYZW x2), default `0.5`: The displacement value that means no movement; the default 0.5 centres it.
- **UV Weight** (`par.Uvweight`, Float), default `1.0`: Blend of the displacement into the image coordinates: 0 leaves them untouched.
- **Displace Period** (`par.Period`, Float), default `1.0`: Scale of the built-in noise that drives the displacement: larger periods give broader shapes.
- **Displace Amplitude** (`par.Amp`, Float), default `0.0`: Strength of the built-in noise that drives the displacement.
- **Displace Speed** (`par.Displacespeed`, Float), default `0.0`: How fast the built-in noise moves.
- **T** (`par.T`, XYZW x2), default `0.0`: Translate applied to the loop each pass.
- **Rotate** (`par.Rotate`, XYZW), default `0.0`: Rotation applied to the loop each pass, in degrees.
- **Scale** (`par.S`, XYZW x2), default `1.0`: Scale applied to the loop each pass: a little above 1 zooms the trails outward.
- **Reset** (`par.Reset`, Momentary), default `off`: Clear the feedback loop while held.
- **Dry / Wet Mix** (`par.Drywet`, Float), default `1.0`: Mixes the effect with the input: 0 is the input alone, 1 the full effect.

### About

- **Help** (`par.Help`, Pulse): Open the help for this tool.
