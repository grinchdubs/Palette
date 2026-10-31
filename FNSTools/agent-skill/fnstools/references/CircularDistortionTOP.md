# CircularDistortionTOP

A circular distortion for images: rings of displacement around a centre you place, with phase, frequency, amplitude and a mode blend, and a choice of how the input extends past its edge.

- Category: Visual
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/circulardistortiontop/

## What it does

- **Ring distortion around a centre you place**: Pushes the image in rings around any point: the middle of the frame, a face, a logo.
- **Animate the rings with Phase**: Animating Phase sends the rings outward or inward; a step of 1 moves them by one ring.
- **Round on any aspect**: The rings stay circular on a 16:9 frame or any other non-square image.
- **Blend between two distortion modes**: Mode blends between a push that grows with the distance from the centre and one that is the same strength everywhere.
- **Edge handling**: Choose what shows where the rings pull in pixels from past the image edge: hold, zero, repeat or mirror.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `circularDistortion` (Circular Distortion) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/CircularDistortionTOP.tox`. Its promoted methods are called on the placed copy.

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

- **Center** (`par.Center`, XYZW x2), default `0.5`: The point the rings are centred on, in UV: 0.5, 0.5 is the middle of the image.
- **Phase** (`par.Phase`, Float), default `0.5`: Shifts the rings outward or inward; one full step (0 to 1) moves them one ring. Animate it to make them travel.
- **Frequency** (`par.Frequency`, Float), default `0.5`: How tightly the rings are packed: higher values put more rings across the image.
- **Amplitude** (`par.Amplitude`, Float), default `0.5`: How far the rings displace the image. 0 leaves it untouched.
- **Mode** (`par.Mode`, Float), default `1.0`: Blends two ways of distorting: 0 scales the image radially around the centre, 1 pushes each pixel along its direction from the centre.
- **Input Extend Mode Uv** (`par.Inputextenduv`, Menu), default `mirror`, menu `hold`, `zero`, `repeat`, `mirror`: What a displaced sample returns outside the image: hold the edge, zero, repeat or mirror.
