# ColorGen

A colour palette generator: a lookup of any length shaped by a phase step per channel and per channel exponents, with a lookup ramp as a second output.

- Category: Visual
- Version: 1.0.4
- Access: Base
- Docs: https://functionstore.tools/docs/colorgen/

## What it does

- **Palette from a formula**: Red, green and blue follow one curve, offset from each other by a phase step and bent by an exponent each, so a few values give a whole family of gradients.
- **Animate with one Phase**: One Phase value scrolls the palette and lands back where it started at 1, so it loops cleanly when you animate it.
- **Palette strip**: out_col is the palette as a colour strip, as many pixels wide as the palette has colours, ready for a Lookup TOP.
- **Colour an image through the palette**: out_lookup colours the input image through the palette; with nothing wired, a built-in 0 to 1 ramp shows the palette.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `colorGen` (Color Gen) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/ColorGen.tox`. Its promoted methods are called on the placed copy.

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

- **Length** (`par.Length`, Int), default `255`: Number of colours in the palette: the width in pixels of out_col, and of the fallback ramp that feeds the lookup when nothing is connected to the input.
- **Phase Step per Channel** (`par.Phasestep`, Float), default `0.101`: Phase offset between the R, G and B curves: R stays put, B is shifted by twice this many palette cycles, G by a share of that set by Exponent Shift. 0 keeps the channels in step (greys).
- **Phase** (`par.Phase`, Float), default `0.0`: Scrolls all three curves along the palette. 1 is one full cycle and lands back where it started; 0.5 mirrors the palette. Animate it to cycle the colours.
- **Exponent Shift** (`par.Expval`, Float), default `1.0`: Exponent that places G's phase between R and B: 1 puts it halfway, higher values move it toward R, values below 1 toward B.
- **Exponent R** (`par.Expval1`, Float), default `1.0`: Exponent shaping the red curve along the palette: 1 is linear, higher values keep the channel dark for longer, below 1 brightens it early.
- **Exponent G** (`par.Expval2`, Float), default `1.0`: Exponent shaping the green curve along the palette: 1 is linear, higher values keep the channel dark for longer, below 1 brightens it early.
- **Exponent B** (`par.Expval3`, Float), default `1.0`: Exponent shaping the blue curve along the palette: 1 is linear, higher values keep the channel dark for longer, below 1 brightens it early.
