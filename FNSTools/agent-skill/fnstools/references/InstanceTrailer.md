# InstanceTrailer

Turns one moving image into a trail of its recent frames: a cache laid out in a row or column with exponent-shaped spacing, plus the offsets as a CHOP for instancing.

- Category: Visual
- Version: 1.0.4
- Access: Base
- Docs: https://functionstore.tools/docs/instancetrailer/

## What it does

- **Trail of recent frames**: Caches incoming frames while an input is wired and lays the latest copies side by side, oldest at one end, newest at the other.
- **Reach and copy count**: Set how many copies the trail holds and how many frames back the oldest one reaches.
- **Shape the time spacing**: An exponent spaces the delays, so the copies bunch up near the present or fan out evenly into the past.
- **Row or column layout**: Lays the copies out left to right, right to left, top to bottom or bottom to top.
- **CHOP output for instancing**: A second output carries the trail as a CHOP in the same layout as the texture, for instanced geometry or CHOP-side use.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `instanceTrailer` (Instance Trailer) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/InstanceTrailer.tox`. Its promoted methods are called on the placed copy.

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

- **Depth** (`par.Depth`, Int), default `10`: Number of delayed copies (instances) drawn in the trail, the live frame included.
- **Max Cache Size** (`par.Maxcachesize`, Int), default `300`: Frames the cache holds. The trail cannot reach further back than this; larger values use more GPU memory.
- **Cache Size** (`par.Cachesize`, Int), default `300`: How many frames back the oldest copy reaches. Clamped to Max Cache Size: the cache holds nothing further back, so a larger value would read empty slots.
- **Direction** (`par.Direction`, Float), default `1.0`: Direction and strength of the time offset, -1 to 1. Positive values delay the copies into the past, negative values reverse the order; at +-1 the oldest copy reaches Cache Size frames back.
- **Exponent Value** (`par.Expval`, Float), default `1.0`: Exponent that spaces the delays: 1 is even spacing, higher values bunch the copies near the live frame. 0 puts every copy on the same frame.
- **Align** (`par.Align`, Menu), default `verttb`, menu `horizlr`, `horizrl`, `verttb`, `vertbt`: How the copies are arranged in the output layout.
- **Recreate All Operators** (`par.Recreateall`, Pulse): Rebuild every replicated copy, for example after changing Depth by a large amount.
