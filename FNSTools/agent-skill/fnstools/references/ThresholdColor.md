# ThresholdColor

A Threshold TOP that keeps the colour: pixels that pass the test come through in their original colour with a soft edge. An alternative for the Threshold TOP.

- Category: Visual
- Version: 1.0.6
- Access: Free
- Docs: https://functionstore.tools/docs/thresholdcolor/

## What it does

- **Colour-keeping threshold**: Pixels the Comparator removes go black while every other pixel keeps its exact RGB.
- **Test luminance, a channel or RGB**: Tests luminance, one channel, or the average or maximum of RGB or RGBA against the threshold.
- **Soften the edge**: Soften feathers the boundary between kept and removed pixels.
- **Alpha cut-outs for compositing**: Removed pixels can also turn transparent, ready to composite over something else.
- **Replace a Threshold TOP**: Create a Threshold TOP with the alternatives shortcut held and ThresholdColor is offered in its place, wired into the same spot.

## Reach it

No global shortcut. The installer never places it into a network: its tox is in the store at `<user palette>/FNSTools/store/ThresholdColor.tox` for the user to place by hand, and its promoted methods are called on that copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

- `thresholdTOP`

## Requires

- `FNS_OpMenuRegistry`

## Parameters

### Custom

- **Comparator** (`par.Comparator`, Menu), default `less`, menu `less`, `greater`, `lessorequal`, `greaterorequal`, `equal`, `notequal`: The test that REMOVES a pixel (sets it to black): with Less, every pixel whose tested value is below Threshold goes black and the rest keep their colour. Same semantics as the Threshold TOP.
- **RGB** (`par.Rgb`, Menu), default `luminance`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`: Which value of each pixel is compared against Threshold: luminance, one channel, the RGB or RGBA average, or the RGB or RGBA maximum.
- **Threshold** (`par.Threshold`, Float), default `0.5`: The value each pixel is compared against with the Comparator.
- **Alpha** (`par.Alpha`, Menu), default `same`, menu `same`, `one`: Output alpha: Same as RGB multiplies the input alpha by the pass/fail matte (removed pixels become transparent); One keeps the input alpha untouched.
- **Soften** (`par.Soften`, Float), default `0.0`: Width of the soft edge around the threshold; pixels near it fade between their colour and black instead of cutting hard. 0 is a hard cut.
