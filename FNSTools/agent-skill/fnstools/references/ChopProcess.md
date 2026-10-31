# ChopProcess

Shapes channels in one node: limit, remap between ranges with an exponent curve, zero at the bottom, lag, and an optional speed mode that turns the result into a running total. An alternative for the Math CHOP.

- Category: CHOPs & sensing
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/chopprocess/

## What it does

- **Limit and remap with a curve**: Limits incoming values to a range and remaps that range onto another through an exponent curve.
- **Zero Below**: Makes the bottom of the input range output 0, so a fader switches fully off at its lowest point yet starts usefully once moved.
- **Lag smoothing**: Glides toward new values with a lag.
- **Speed mode**: Treats the result as a speed and outputs its running total, which can be clamped, looped or bounced between limits.
- **Shape a whole fader bank in one node**: Every input channel goes through the same chain, so one node shapes a whole fader bank; with nothing connected, the Value parameter is processed.
- **Replace a Math CHOP**: Create a Math CHOP with the alternatives shortcut held and ChopProcess is offered in its place, wired into the same spot.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `chopProcess` (Chop Process) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/ChopProcess.tox`. Its promoted methods are called on the placed copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

- `mathCHOP`

## Requires

- `FNS_OpMenuRegistry`

## Parameters

### Custom

- **Value** (`par.Value`, Float), default `0.0`: The value to process when nothing is wired into the input.
- **Name** (`par.Name`, Str): Rename the output channels: names separated by spaces, one per channel, or a pattern like chan[1-4]. Empty keeps the input's names.
- **Type** (`par.Type`, Menu), default `off`, menu `off`, `clamp`, `loop`, `zigzag`: What happens outside the From Range: off lets values through, clamp holds them at the ends, loop wraps them round, zigzag bounces them back.
- **From Range** (`par.Fromrange`, Float x2), default `-1.0`: The input range. With Type set to clamp, loop or zigzag this is also the limit.
- **To Range** (`par.Torange`, Float x2), default `0.0`: The output range the From Range maps onto.
- **Zero Below** (`par.Zerobelow`, Toggle), default `off`: Output 0 while the input sits at the bottom of the From Range, instead of the bottom of the To Range. Only with Type set to clamp.
- **Exponent Value** (`par.Expval`, Float), default `2.0`: Exponent for the curve between the ranges: 1 is linear, above 1 eases in, below 1 eases out.
- **Lag** (`par.Lag`, Float x2), default `0.2`: Seconds to glide up and down toward a new value.
- **Speed** (`par.Speed`, Header)
- **Is Speed** (`par.Isspeed`, Toggle), default `off`: Treat the processed value as a speed and output its running total instead, so a held input keeps moving.
- **Limit Type** (`par.Limittype`, Menu), default `off`, menu `off`, `clamp`, `loop`, `zigzag`: What happens when the running total leaves Minimum and Maximum.
- **Minimum** (`par.Min`, Float), default `0.0`: Lower limit for the running total.
- **Maximum** (`par.Max`, Float), default `1.0`: Upper limit for the running total.
- **Reset Value** (`par.Resetvalue`, Float), default `0.0`: The value the running total returns to on reset.
- **Reset** (`par.Reset`, Toggle), default `off`: Hold the running total at the Reset Value while on.
- **Reset Pulse** (`par.Resetpulse`, Pulse): Return the running total to the Reset Value once.
