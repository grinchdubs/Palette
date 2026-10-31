# MoveDetectDir

Reads which way things move in a camera or any image with optical flow and turns it into left/right and down/up channels, with thresholds, inversion and filtering, for swipe and gesture triggers.

- Category: CHOPs & sensing
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/movedetectdir/

## What it does

- **Optical flow direction**: Runs optical flow on the input image and measures how much of the flow points left, right, down and up.
- **Direction channels**: Outputs LR and DU channels that swing toward the direction of movement once it passes a threshold, for swipe and gesture triggers.
- **Filter out noise and small motion**: Blur on the input, a flow threshold and a movement threshold per axis keep camera noise and small motion from firing it.
- **Invert a direction for mirrored cameras**: Flips either direction for a mirrored camera.
- **Smooth the channels**: Smooths the direction channels over a time you set.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `moveDetectDir` (Move Detect Dir) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/MoveDetectDir.tox`. Its promoted methods are called on the placed copy.

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

- **Input Filter Size** (`par.Size`, Int), default `7`: Blur applied to the input before the optical flow, in pixels. More blur ignores small noise.
- **Optflow Lambda** (`par.Lambda`, Float), default `0.1`: Smoothing of the optical flow: higher values give a steadier, less detailed flow.
- **OptFlow Threshold** (`par.Threshold`, Float), default `0.0`: The smallest flow that counts as movement; weaker flow is ignored.
- **Move Threshold X** (`par.Movethresholdx`, Float), default `300.0`: How much horizontal movement it takes before LR swings left or right.
- **Move Threshold Y** (`par.Movethresholdy`, Float), default `300.0`: How much vertical movement it takes before DU swings down or up.
- **Inverse X** (`par.Inversex`, Toggle), default `off`: Flip the left/right direction, for a mirrored camera.
- **Inverse Y** (`par.Inversey`, Toggle), default `off`: Flip the down/up direction.
- **Filter Width** (`par.Width`, Float), default `0.2`: How long the output channels are smoothed over, in seconds.
