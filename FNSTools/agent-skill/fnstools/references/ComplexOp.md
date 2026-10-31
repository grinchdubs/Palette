# ComplexOp

Treats the image plane as the complex plane and applies a complex function to it: square, root, exp, log, the trigonometric and hyperbolic families, with iteration, a pre and post transform and a choice of edge handling.

- Category: Visual
- Version: 1.0.4
- Access: Free
- Docs: https://functionstore.tools/docs/complexop/

## What it does

- **Warp an image through a complex function**: Reads each pixel's UV as a complex number, runs it through the chosen function and samples the input image at the result.
- **Function menu: square, root, exp, log, sin and more**: Offers square, root, exp, log, inverse, power, and the trigonometric and hyperbolic families with their inverses.
- **Iteration**: Applies the function up to 64 times in a row, with an escape radius that can stop it early.
- **Transform before and after the function**: A transform before and after the function moves the point of interest to where the function does something worth seeing.
- **Edge handling**: Extend picks what fills the frame where the warped coordinates leave the image: hold the edge, zero, repeat or mirror.
- **Border mask output**: The borders output keeps the mapped image only near the edges of each repeated tile, with Borders setting where that soft edge starts.
- **Chain functions through the UV output**: A second output carries the mapped UV field, for a second ComplexOp, ComplexMix or a Remap TOP.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `complexOp` (Complex Op) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/ComplexOp.tox`. Its promoted methods are called on the placed copy.

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

- **Operand/Map** (`par.Uv`, Toggle), default `off`: On: the input is an image, warped through the function over a screen-space complex plane (Center/Aspect apply). Off: the input red/green channels ARE the complex operand, for chaining the UV output of another Complex Op.
- **Op** (`par.Op`, Menu), default `none`, menu `none`, `csqr`, `csqrt`, `cexp`, `clog`, `cinv`, `cabs2`, `cconj`, `csin`, `ccos`, `ctan`, `ccot`, `csinh`, `ccosh`, `ctanh`, `ccoth`, `casin`, `cacos`, `catan`, `cacot`, `casinh`, `cacosh`, `catanh`, `cacoth`, `cpolar`, `cpow`, `cconst`: The complex function applied to z. None passes z through, so only the transforms and Extend act.
- **Power** (`par.Power`, Float), default `2.0`: Base of the logarithm for Logarithm, or the exponent n for Power (z^n). Enabled only for those two functions.
- **Const** (`par.Const`, Float x2), default `0.0`: Real and imaginary part of the constant returned by the Constant function (enabled only for Constant).
- **Op Iter** (`par.Opiter`, Int), default `1`: How many times the function is applied in a row (1-64). Higher values fold the image further; Boundary can stop the iteration early.
- **Center UV** (`par.Center`, Toggle), default `off`: Map mode only. Puts the complex origin at the image centre (z runs -1..1) instead of the bottom-left corner (0..1). With Op None the result is the image tiled by the Extend mode.
- **Aspect** (`par.Aspect`, Toggle), default `off`: Map mode only. Scales the complex plane by the image aspect so circles stay round on non-square images.
- **Transform Order** (`par.Xord`, Menu), default `srt`, menu `srt`, `str`, `rst`, `rts`, `tsr`, `trs`: Order in which the pre transform applies scale, rotate and translate to z before the function.
- **Trans** (`par.Optrans`, Float x2), default `0.0`: Pre transform: moves z along x and y before the function.
- **Rot** (`par.Rot`, Float), default `0.0`: Pre transform: rotates z by this many degrees before the function.
- **Scale** (`par.Opscale`, Float x2), default `1.0`: Pre transform: scales z along x and y before the function.
- **Pivot** (`par.Pivot`, Float x2), default `0.0`: Pre transform pivot (x, y): the point that rotation and scale happen around.
- **Post Transform Order** (`par.Xord2`, Menu), default `srt`, menu `srt`, `str`, `rst`, `rts`, `tsr`, `trs`: Order in which the post transform applies scale, rotate and translate to the result of the function.
- **Post Trans** (`par.Posttrans`, Float x2), default `0.0`: Post transform: moves the result along x and y after the function.
- **Post Rot** (`par.Postrot`, Float), default `0.0`: Post transform: rotates the result by this many degrees after the function.
- **Post Scale** (`par.Postscale`, Float x2), default `1.0`: Post transform: scales the result along x and y after the function.
- **Post Pivot** (`par.Postpivot`, Float x2), default `0.0`: Post transform pivot (x, y): the point that rotation and scale happen around.
- **Boundary** (`par.Boundary`, Float), default `0.0`: Escape radius: iteration stops once |z| exceeds this value, keeping the last value inside. 0 disables the test.
- **Borders** (`par.Borders`, Float x2), default `0.0`: Start of the soft edge for the borders output (third output), which shows the mapped image only near the edges of each repeated tile: 0.5 is the tile centre, 1 the tile edge.
- **Extend** (`par.Mode`, Menu), default `Mirror`, menu `Hold`, `Zero`, `Repeat`, `Mirror`: How the image is sampled where the warped coordinates leave 0..1: Hold the edge pixels, Zero (transparent black), Repeat the image, or Mirror it.
- **Blend** (`par.Blend`, Float), default `1.0`: Mix between the unwarped coordinates (0) and the warped ones (1).

### Common

- **Resolution** (`par.Resolution`, Int x2), default `1280`: Width and height of the built-in UV map used when nothing is wired into the input. Disabled while an input is connected; the output then takes the input resolution.
- **Input Smoothness** (`par.Inputfiltertype`, Menu), default `linear`, menu `nearest`, `linear`, `mipmap`: Filtering used when sampling the input image.
- **Viewer Smoothness** (`par.Filtertype`, Menu), default `linear`, menu `useinput`, `nearest`, `linear`, `mipmap`: Filtering used when the output is displayed at another resolution.
- **Pixel Format** (`par.Format`, Menu), default `useinput`, menu `useinput`, `rgba8fixed`, `rgba16float`, `rgba32float`, `rgb10a2fixed`, `rgba16fixed`, `rgba11float`, `mono8fixed`, `mono16fixed`, `mono16float`, `mono32float`, `rg8fixed`, `rg16fixed`, `rg16float`, `rg32float`, `a8fixed`, `a16fixed`, `a16float`, `a32float`, `monoalpha8fixed`, `monoalpha16fixed`, `monoalpha16float`, `monoalpha32float`: Pixel format of the outputs. Keep a float format when the UV output feeds another Complex Op or a Remap, or the coordinates are quantised.
