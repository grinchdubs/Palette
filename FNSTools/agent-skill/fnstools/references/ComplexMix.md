# ComplexMix

Combines two UV fields as complex numbers: add, subtract, multiply, divide or raise one to the other, optionally weighted by a third input, then samples an image through the result.

- Category: Visual
- Version: 1.0.4
- Access: Free
- Docs: https://functionstore.tools/docs/complexmix/

## What it does

- **Combine two UV fields as complex numbers**: Treats each pixel pair of two UV fields as complex numbers and adds, subtracts, multiplies, divides or raises one to the other.
- **Weighting between the operands**: Fn Weight balances the two operands before they combine, so with Add one warp can morph into the other.
- **Sample an image through the result**: Samples the in1 image through the combined coordinates, so two ComplexOp warps become their sum, product or quotient.
- **Transform the combined coordinates**: Moves, rotates and scales the combined coordinates, with Aspect keeping rotation and scale round on a non-square output.
- **Blend the effect in**: Blend fades from the plain image to the full combination; animate it to bring the warp in on a cue.
- **Chain the combined UV field**: out2 outputs the combined UV field for chaining into another sampler.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `complexMix` (Complex Mix) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/ComplexMix.tox`. Its promoted methods are called on the placed copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

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

- **Operation** (`par.Operation`, Menu), default `Add`, menu `Op1`, `Op2`, `Add`, `Subtract`, `Multiply`, `Divide`, `Power1**2`, `Power2**1`: How the two complex operands (input 2 = Op1, input 3 = Op2, read from their red/green channels) combine: either one alone, or complex add, subtract, multiply, divide or power.
- **Weighting** (`par.Weighting`, Toggle), default `off`: Scales Op1 by (1 - Fn Weight) and Op2 by Fn Weight before they combine. Not used by Op1 only / Op2 only.
- **Fn Weight** (`par.Fnweight`, Float), default `0.5`: Balance between the operands when Weighting is on: 0 is all Op1, 1 is all Op2.
- **Aspect** (`par.Aspect`, Toggle), default `off`: Applies the transform in aspect-corrected space so rotation and scale stay round on non-square outputs.
- **Transform Order** (`par.Xord`, Menu), default `srt`, menu `srt`, `str`, `rst`, `rts`, `tsr`, `trs`: Order in which the transform applies scale, rotate and translate to the combined coordinates.
- **Trans** (`par.Mixtrans`, Float x2), default `0.0`: Moves the combined coordinates along x and y.
- **Rot** (`par.Rot`, Float), default `0.0`: Rotates the combined coordinates by this many degrees around the pivot.
- **Scale** (`par.Mixscale`, Float x2), default `1.0`: Scales the combined coordinates along x and y; larger values zoom in.
- **Pivot** (`par.Pivot`, Float x2), default `0.0`: Pivot (x, y): the point that rotation and scale happen around.
- **Extend** (`par.Mode`, Menu), default `Mirror`, menu `Hold`, `Zero`, `Repeat`, `Mirror`: How input 1 is sampled where the coordinates leave 0..1: Hold the edge pixels, Zero (transparent black), Repeat the image, or Mirror it.
- **Blend** (`par.Blend`, Float), default `1.0`: Mix between plain screen coordinates (0, input 1 unchanged) and the combined, transformed coordinates (1).

### Common

- **Resolution** (`par.Resolution`, Int x2), default `1280`: Width and height of the built-in UV map used when nothing is wired into input 1. Disabled while input 1 is connected; the output then takes its resolution.
- **Input Smoothness** (`par.Inputfiltertype`, Menu), default `linear`, menu `nearest`, `linear`, `mipmap`: Filtering used when sampling the inputs.
- **Viewer Smoothness** (`par.Filtertype`, Menu), default `linear`, menu `useinput`, `nearest`, `linear`, `mipmap`: Filtering used when the output is displayed at another resolution.
- **Pixel Format** (`par.Format`, Menu), default `useinput`, menu `useinput`, `rgba8fixed`, `rgba16float`, `rgba32float`, `rgb10a2fixed`, `rgba16fixed`, `rgba11float`, `mono8fixed`, `mono16fixed`, `mono16float`, `mono32float`, `rg8fixed`, `rg16fixed`, `rg16float`, `rg32float`, `a8fixed`, `a16fixed`, `a16float`, `a32float`, `monoalpha8fixed`, `monoalpha16fixed`, `monoalpha16float`, `monoalpha32float`: Pixel format of the outputs. Keep a float format when the UV output feeds another Complex tool or a Remap, or the coordinates are quantised.
