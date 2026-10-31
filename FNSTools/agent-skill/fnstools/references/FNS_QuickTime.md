# QuickTime

Package `FNS_QuickTime`.

A toolbar clock that hands out drag-and-drop time references for parameters: resettable and scalable absTime and absFrame, frame, and a progress value for perfect loops.

- Category: Time & sequencing
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-quicktime/

## What it does

- **Drag-and-drop time references**: Click the toolbar icon for absTime, absFrame, frame and progress, ready to drag onto a parameter.
- **Reset the clock**: Middle-click the icon, or run Reset timer, to send QuickTime's absTime and absFrame back to zero.
- **Scale the clock speed**: Multiplier scales absTime and absFrame: 1 is real time, 0.5 is half speed.
- **Progress for perfect loops**: The current frame divided by the end frame, for lookups and loops that close exactly.

## Reach it

`op.FNS_QUICKTIME` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `ResetTimer()`: Reset the QuickTime timer.

## Commands

- **Reset timer** (id `resettimer`): Reset the QuickTime timer. Method `ResetTimer`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Multiplier** (`par.Multiplier`, Float), default `0.0`: Scales the absTime and absFrame references QuickTime hands out: 1 is real time, 0.5 runs them at half speed.
- **Reset** (`par.Reset`, Pulse): Set QuickTime's internal timers back to zero. Middle-clicking the toolbar icon does the same thing.
