# RealRamp

A ramp with a true phase and period and its colour keys as parameters: vertical, horizontal, radial or circular, holding, zeroing, repeating or mirroring past its ends, so a driven phase never drifts or snaps the way a keyed Ramp TOP can. An alternative for the Ramp TOP.

- Category: Visual
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/realramp/

## What it does

- **Colour keys as parameters**: Each key's position and colour is a parameter on the operator, so it can take an expression, an export or a CHOP like any other.
- **Phase and period ramp**: Computes the gradient in a shader from a phase and a period, so driving Phase from a CHOP cycles the ramp smoothly forever.
- **Radial, circular, vertical or horizontal ramps**: Draws the ramp vertical, horizontal, radial or circular, with Radial starting at 3 o'clock like the Ramp TOP.
- **Repeat or mirror past the ends**: Holds the end colours, goes to zero, repeats or mirrors past the ends of the ramp.
- **Interpolate between keys like the Ramp TOP**: Step, Linear, Ease In Ease Out and Hermite blending between keys, matched against the stock Ramp TOP.
- **Banding-free output**: Outputs 32-bit float by default, so a slow gradient shows no steps.
- **Resolution from an input**: With an input connected the ramp takes its resolution, and the image itself is never sampled; without one, Resolution sets the size.
- **Replace a Ramp TOP**: Offered in place of a Ramp TOP created with the alternatives shortcut held, wired into the same spot.

## Reach it

No global shortcut. The installer never places it into a network: its tox is in the store at `<user palette>/FNSTools/store/RealRamp.tox` for the user to place by hand, and its promoted methods are called on that copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

- `rampTOP`

## Requires

- `FNS_OpMenuRegistry`

## Parameters

### Custom

- **Resolution** (`par.Resolution`, Int x2), default `256`: Output width and height in pixels when nothing is wired into the input. With an input connected, the ramp takes the input resolution.
- **Type** (`par.Type`, Menu), default `horiz`, menu `vert`, `horiz`, `rad`, `circ`: Direction of the ramp. Radial runs round the centre starting at 3 o'clock, like the Ramp TOP; Circular grows outward from the centre.
- **Phase** (`par.Phase`, Float), default `0.0`: Offsets the ramp along its direction, in periods. Constant 0 by default; drive it with an expression or CHOP (e.g. absTime.seconds*0.2) to scroll the ramp.
- **Period** (`par.Period`, Float), default `1.0`: Length of one ramp cycle in UV units; smaller values repeat the ramp more often. 0 outputs black.
- **Extend** (`par.Extend`, Menu), default `repeat`, menu `hold`, `zero`, `repeat`, `mirror`: What the ramp does past its ends: Hold keeps the end colours, Zero goes transparent black, Repeat starts over, Mirror runs back.
- **Interpolate** (`par.Interpolate`, Menu), default `linear`, menu `step`, `linear`, `easeineaseout`, `hermite`: How colours blend between keys, as on the Ramp TOP: Step holds each key, Linear blends straight, Ease In Ease Out slows at each key, Hermite curves through them.
- **Curve Tension** (`par.Tension`, Float), default `0.0`: Hermite only: bends the curve between keys. 0 is a smooth curve through every key.
- **Input Smoothness** (`par.Inputfiltertype`, Menu), default `nearest`, menu `nearest`, `linear`, `mipmap`: Filtering used when sampling a wired input. The ramp itself never samples the input (only its resolution and format are used), so this is kept for SetSmoothness and has no visible effect.
- **Viewer Smoothness** (`par.Filtertype`, Menu), default `nearest`, menu `nearest`, `linear`, `mipmap`: Filtering used when the output is displayed at another resolution.
- **Pixel Format** (`par.Format`, Menu), default `rgba32float`, menu `useinput`, `rgba8fixed`, `rgba16float`, `rgba32float`, `rgb10a2fixed`, `rgba16fixed`, `rgba11float`, `mono8fixed`, `mono16fixed`, `mono16float`, `mono32float`, `rg8fixed`, `rg16fixed`, `rg16float`, `rg32float`, `a8fixed`, `a16fixed`, `a16float`, `a32float`, `monoalpha8fixed`, `monoalpha16fixed`, `monoalpha16float`, `monoalpha32float`: Pixel format of the output. Defaults to 32-bit float, which keeps the ramp free of banding; 16-bit float is usually enough, 8-bit shows visible steps. Use Input follows the wired input (8-bit when nothing is wired).

### Keys

- **Keys** (`par.Key`, Sequence), default `0`: Colour keys along the ramp. Add or remove keys with + and -. Keys may be in any order; they are sorted by position.
- **Position** (`par.Key0pos`, Float), default `0.0`: Where this key sits on the ramp, 0 at the start and 1 at the end.
- **Color** (`par.Key0color`, RGBA x4), default `0.0`: Colour and alpha of this key.
- **Position** (`par.Key1pos`, Float), default `0.0`: Where this key sits on the ramp, 0 at the start and 1 at the end.
- **Color** (`par.Key1color`, RGBA x4), default `0.0`: Colour and alpha of this key.
