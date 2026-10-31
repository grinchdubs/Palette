# FloatDataRecorder

Records a float texture such as a depth point cloud, a colour texture and a CHOP to files in sync, then plays the three back together against the timeline with a frame offset.

- Category: Show & output
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/floatdatarecorder/

## What it does

- **Record a point cloud, colour and CHOP together**: Rec writes a float texture such as a depth point cloud, a colour texture and a CHOP such as skeleton data to files at once.
- **Play back in step with the timeline**: Plays the three files back in step with the timeline, with a frame offset to line them up, as textures and channels.
- **Live pass-through**: With Play off, and always while recording, the outputs carry the live inputs, so nothing downstream has to be rewired.
- **Timeline fitted to the take**: Sets the timeline's end to the length of the recording in one pulse.
- **Reload a new take**: Reload picks up a take recorded over the same files and looks again for a missing CHOP file; until that file exists the CHOP player stays off, so a fresh node shows no error.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `floatDataRecorder` (Float Data Recorder) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/FloatDataRecorder.tox`. Its promoted methods are called on the placed copy.

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

- **Record** (`par.Recordheader`, Header)
- **Texture File** (`par.Texfile`, File), default `'TDMovieOut' + me.fileSuffix`: The movie the float texture (first input) is recorded to.
- **Color Texture File** (`par.Texfile2`, File), default `'TDMovieOut' + me.fileSuffix`: The movie the colour texture (third input) is recorded to.
- **CHOP File** (`par.Chopfile`, File): Where the recorded channels are saved when Rec turns off. A name with no extension gets .bclip.
- **Rec** (`par.Rec`, Toggle), default `off`: Record all three inputs while on. Turning it off saves the channels to the CHOP File. Playback is paused while recording.
- **Play** (`par.Playheader`, Header)
- **Texture File** (`par.Opentexforplay`, File): The recorded float texture movie to play back.
- **Color Texture File** (`par.Opentexforplay2`, File): The recorded colour texture movie to play back.
- **CHOP File** (`par.Openchopforplay`, File): The recorded channel clip to play back. The CHOP player stays off until this file exists.
- **Play Offset Frames** (`par.Offset`, Int), default `0`: Shifts playback against the timeline by this many frames, to line the recording up.
- **Reload** (`par.Reload`, Pulse): Reload the three playback files, and look again for a CHOP file that was missing.
- **Sync Timeline** (`par.Synctimeline`, Pulse): Set the timeline's end to the length of the recording.
- **Play** (`par.Play`, Toggle), default `off`: Output the recordings. Off, and always while recording, the outputs pass the live inputs through.
