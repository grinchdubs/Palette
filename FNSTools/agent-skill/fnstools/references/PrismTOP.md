# PrismTOP

A kaleidoscopic prism: the input rendered through instanced, rotating polygon facets in up to three ring patterns, with softness, a chromatic distortion pass, fit and transform, and a dry/wet mix. An alternative for the Tile TOP and the Mirror TOP.

- Category: Visual
- Version: 1.0.7
- Access: Base
- Docs: https://functionstore.tools/docs/prismtop/

## What it does

- **Kaleidoscope prism facets**: Maps the input onto polygon facets set in rings around the centre, so the image is repeated, mirrored and rotated at once.
- **Stack up to three ring patterns**: Up to three rings stack, each with its own facet count, radius, size, rotation and opacity.
- **Soften the facet edges**: Softness blurs the seams where the facets meet.
- **Animate the rotation**: Phase turns each ring around the centre, and the whole prism can swing back and forth on a sine.
- **Chromatic distortion**: A chromatic pass splits the colours apart the way real glass does.
- **Mix with the original**: The original image can sit underneath the facets, and Dry/Wet blends the whole result with the input.
- **Replace a Tile or Mirror TOP**: Offered in place of a Tile TOP or Mirror TOP when you create one with the alternatives shortcut held.

## Reach it

No global shortcut. The installer never places it into a network: its tox is in the store at `<user palette>/FNSTools/store/PrismTOP.tox` for the user to place by hand, and its promoted methods are called on that copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

- `mirrorTOP`
- `tileTOP`

## Requires

- `FNS_OpMenuRegistry`

## Parameters

### Custom

- **Res** (`par.Res`, XYZW x2), default `1920.0`: The render resolution of the prism.
- **Operation** (`par.Operand`, Menu), default `under`, menu `add`, `atop`, `average`, `brightest`, `burncolor`, `burnlinear`, `chromadifference`, `color`, `darkercolor`, `difference`, `dimmest`, `divide`, `dodge`, `exclude`, `freeze`, `glow`, `hardlight`, `hardmix`, `heat`, `hue`, `inside`, `insideluminance`, `inverse`, `lightercolor`, `luminancedifference`, `maximum`, `minimum`, `multiply`, `negate`, `outside`, `outsideluminance`, `over`, `overlay`, `pinlight`, `reflect`, `screen`, `softlight`, `linearlight`, `stencilluminance`, `subtract`, `subtractive`, `under`, `vividlight`, `xor`, `yfilm`, `zfilm`: How the facets are composited over the original image.
- **Orig Opac** (`par.Opacity`, Float), default `0.0`: Opacity of the original image underneath the facets.
- **Orig Scale** (`par.Middlescale`, Float), default `1.0`: Scale of the original image underneath the facets.
- **Fit** (`par.Fit`, Menu), default `fitoutside`, menu `fill`, `fithorz`, `fitvert`, `fitbest`, `fitoutside`, `nativeres`: How the input fits the facets: fill, fit horizontally or vertically, best, outside, or native resolution.
- **Translate** (`par.T`, XYZW x2), default `0.0`: Moves the facet layer.
- **Scale** (`par.Scale`, Float), default `1.0`: Scales the facet layer.
- **Rotate** (`par.R`, Float), default `0.0`: Rotates the facet layer, in degrees.
- **Sides** (`par.Sides`, Int), default `6`: The number of sides of each facet's polygon.
- **Softness** (`par.Softness`, Float), default `0.09`: Soft edge of each facet: 0 is a hard cut.
- **Rot Sin Amp** (`par.Rotsinamp`, Float), default `0.0`: Size of a sine swing added to the rotation, in turns: 0 holds the rotation still.
- **Rot Sin Phase** (`par.Rotsinphase`, Float), default `1165.75`: Where the rotation swing sits in its cycle; animate it to swing the prism.
- **Dry/Wet** (`par.Drywet`, Float), default `1.0`: Mixes the prism with the input: 0 is the input alone, 1 the full prism.

### Patterns

- **Pattern** (`par.Pattern`, Sequence), default `0`: Up to three rings of facets, each with its own count, radius, scale, phase and alpha.
- **Instances** (`par.Pattern0instances`, Int), default `6`: How many facets sit in this ring.
- **Radius** (`par.Pattern0radius`, Float), default `1.0`: How far this ring sits from the centre.
- **Instance Scale** (`par.Pattern0amp`, Float), default `1.0`: Size of this ring's facets.
- **Phase** (`par.Pattern0phase`, Float), default `0.0`: Rotates this ring around the centre.
- **Alpha** (`par.Pattern0alpha`, Float), default `1.0`: Opacity of this ring's facets.
- **Instances** (`par.Pattern1instances`, Int), default `6`: How many facets sit in this ring.
- **Radius** (`par.Pattern1radius`, Float), default `1.0`: How far this ring sits from the centre.
- **Instance Scale** (`par.Pattern1amp`, Float), default `1.0`: Size of this ring's facets.
- **Phase** (`par.Pattern1phase`, Float), default `0.0`: Rotates this ring around the centre.
- **Alpha** (`par.Pattern1alpha`, Float), default `1.0`: Opacity of this ring's facets.
- **Instances** (`par.Pattern2instances`, Int), default `6`: How many facets sit in this ring.
- **Radius** (`par.Pattern2radius`, Float), default `1.0`: How far this ring sits from the centre.
- **Instance Scale** (`par.Pattern2amp`, Float), default `1.0`: Size of this ring's facets.
- **Phase** (`par.Pattern2phase`, Float), default `0.0`: Rotates this ring around the centre.
- **Alpha** (`par.Pattern2alpha`, Float), default `1.0`: Opacity of this ring's facets.

### Chroma

- **Layers** (`par.Layers`, Int), default `3`: How many colour layers the chromatic pass splits the image into.
- **Chromatic** (`par.Chromatic`, Float), default `0.0`: How far the colour layers spread apart.
- **Distortion** (`par.Distortion`, Float), default `0.0`: How strongly the chromatic pass bends the image.
