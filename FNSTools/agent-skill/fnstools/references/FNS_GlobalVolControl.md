# GlobalVolControl

Package `FNS_GlobalVolControl`.

Global audio volume control.

- Category: Show & output
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/fns-globalvolcontrol/

## What it does

- **Master volume slider**: Sets TouchDesigner's application-wide output level from the toolbar, leaving the Volume on every Audio Device Out and Audio Play CHOP unchanged.
- **Mute**: The speaker button silences output without moving the slider, so unmuting returns to the same level.
- **Set volume or toggle mute from quick-launch**: The Set volume command takes a level from 0 to 1, and Toggle mute mutes and unmutes.
- **Restore the level at startup**: The level and the mute state are applied again as the project starts.

## Reach it

`op.FNS_VolControl` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `GetVolume()`: Current global output volume (0-1).
- `SetVolume(level: float)`: Set the global output volume (0-1).
- `ToggleMute()`: Mute or unmute the global audio output.

## Commands

- **Set volume** (id `setvolume`): Set the global output volume (0-1). Method `SetVolume`. Params: `level: float (required)`.
- **Toggle mute** (id `togglemute`): Mute or unmute the global audio output. Method `ToggleMute`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Volume** (`par.Volume`, Float), default `1.0`: TouchDesigner's overall output volume, 0 to 1. This is the application-wide level, not a per-operator one.
- **Mute** (`par.Mute`, Toggle), default `off`: Silence TouchDesigner's audio output without losing the Volume setting.
