# EaseInterpolator

Crossfades between two CHOPs through an easing curve: thirty classic easings from sine to bounce, or a custom curve from a third input, all driven by one Select value.

- Category: CHOPs & sensing
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/easeinterpolator/

## What it does

- **Crossfade two CHOPs along a curve**: Moves from the first input to the second as Select runs from 0 to 1, along an easing curve.
- **Easing curves from sine to bounce**: Linear, or sine, quad, cubic, quart, quint, expo, circ, back, elastic and bounce curves in In, Out and In-Out forms.
- **Drive the move from one value**: Select runs the whole transition, so a timer, an LFO or a slider can drive it.
- **Custom ease from a CHOP**: Reads the curve from an optional third input, so any shape drawn in a CHOP becomes the transition.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `easeInterpolator` (Ease Interpolator) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/EaseInterpolator.tox`. Its promoted methods are called on the placed copy.

## Promoted API

- `CustomEaseChop` (attribute)
- `Easings` (attribute)
- `ModSel(sel)`: Wrap a preset index into 1..numPresets, inclusive at the top.
- `OnSelect2(cross)`: Interpolate between preset A and preset B at position cross; called when the selector moves.
- `UpdateSplineCoefs()`: Recompute the spline coefficients of every parameter column when Spline interpolation is on.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Seq

- **Easing** (`par.Easing`, Menu), default `Linear`, menu `Linear`, `InSine`, `OutSine`, `InOutSine`, `InQuad`, `OutQuad`, `InOutQuad`, `InCubic`, `OutCubic`, `InOutCubic`, `InQuart`, `OutQuart`, `InOutQuart`, `InQuint`, `OutQuint`, `InOutQuint`, `InExpo`, `OutExpo`, `InOutExpo`, `InCirc`, `OutCirc`, `InOutCirc`, `InBack`, `OutBack`, `InOutBack`, `InElastic`, `OutElastic`, `InOutElastic`, `InBounce`, `OutBounce`, `InOutBounce`, `CustomEase`: The curve the blend follows between the two inputs: Linear, the In, Out and In-Out forms of the classic easings, or Custom Ease from the third input.
- **Select** (`par.Select`, Float), default `0.0`: Where the blend sits: 0 is the first input, 1 the second, values between follow the easing curve.
