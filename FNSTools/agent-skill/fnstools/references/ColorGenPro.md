# ColorGenPro

A cosine palette generator in GLSL: the full coefficient set per channel, an RGB and D mode, blackout and soft regions, and a lookup ramp as a second output.

- Category: Visual
- Version: 1.0.4
- Access: Pro
- Docs: https://functionstore.tools/docs/colorgenpro/

## What it does

- **Cosine palette with every coefficient**: Offset, amplitude, period, phase and exponent for red, green and blue, for smooth gradients that loop cleanly.
- **RGB and D mode**: Drives the three phases from one Offset, Amplitude and Exponent, so a single value scrolls the whole palette.
- **Blackout region**: Keeps the start of the palette black, added to the length or taken from the colours, with a soft edge you shape.
- **Palette strip output**: out_col is the palette as a colour strip, and Length sets how many colours it holds.
- **Colour an image through the palette**: out_lookup colours the input image through the palette; with nothing wired a built-in 0 to 1 ramp shows the palette.
- **Reset to the shipped coefficients**: Default restores the shipped coefficients and leaves any parameter driven by an expression alone.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `colorGenPro` (Color Gen Pro) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/ColorGenPro.tox`. Its promoted methods are called on the placed copy.

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

- **Length** (`par.Length`, Int), default `256`: Number of colours in the palette (the width of out_col). Blackout with Reductive at 0 adds its share on top of this.
- **Input Smoothness** (`par.Inputfiltertype`, Menu), default `linear`, menu `nearest`, `linear`, `mipmap`: Sampling filter the lookup uses on the input image: Nearest picks exact palette entries, Linear blends between neighbours.
- **Blackout** (`par.Blackout`, Float), default `0.0`: Share of the palette (0 to 1) that fades to black at its start. Reductive decides whether that share is added to the length or taken from the colours; above 0 it enables the Soften parameters.
- **Reductive** (`par.Lensubtract`, Float), default `0.0`: How Blackout makes room: 0 extends the palette by the blackout share, 1 keeps Length and takes the blackout from the colours.
- **Soften Black** (`par.Blacksoften`, Float), default `0.5`: Width of the fade from black into the palette, as a share of the blackout region. 0 is a hard edge, 1 fades across the whole region.
- **Soften Exponent** (`par.Softenexponent`, Float), default `1.0`: Curve of the black fade: 1 is linear, higher values stay dark longer, below 1 brighten early.
- **Soften Extend** (`par.Softenextend`, Menu), default `Zero`, menu `Mirror`, `Zero`, `Repeat`: What the palette does inside the blackout region under the fade: Mirror reflects it, Zero/Hold holds the first colour, Repeat continues the cycle backwards.
- **pow(a + b*cos( 2PI * (c*t+d) ), e)** (`par.Header`, Header): The cosine palette formula each channel follows; t runs 0 to 1 along the palette.
- **a (Offset)** (`par.A`, Float x3), default `0.5`: a (Offset) for red, green, blue: the base brightness the cosine swings around.
- **b (Amplitude)** (`par.B`, Float x3), default `0.5`: b (Amplitude) for red, green, blue: how far the cosine swings above and below a. Values above a clip to black at the troughs.
- **c (Period)** (`par.C`, Float x3), default `1.0`: c (Period) for red, green, blue: how many colour cycles fit along the palette.
- **d (Phase)** (`par.D`, Float x3), default `0.0`: d (Phase) for red, green, blue: shifts each channel's cycle; offsetting the three is what makes hues. Driven by Offset, Amplitude and Exponent while RGBD Mode is on.
- **e (Exponent)** (`par.E`, Float x3), default `1.0`: e (Exponent) for red, green, blue: gamma on each channel; above 1 deepens, below 1 lifts.
- **RGBD Mode** (`par.Rgbdmode`, Toggle), default `off`: Drive the three d (Phase) values from Offset, Amplitude and Exponent instead of setting them by hand. Switching it on restores the shipped coefficients first.
- **Offset** (`par.Offset`, Float), default `0.0`: RGBD Mode: phase of the red channel; green and blue follow from it.
- **Amplitude** (`par.Amplitude`, Float), default `0.2`: RGBD Mode: phase spread from red to blue. 0 puts all three channels in phase (greys).
- **Exponent** (`par.Exponent`, Float), default `1.0`: RGBD Mode: where green sits between red and blue in the spread: 1 halfway, higher values toward red.
- **Default** (`par.Default`, Pulse): Restore the shipped coefficients (a, b, c, d, e) and the RGBD Offset, Amplitude and Exponent. Parameters driven by an expression are left alone.
