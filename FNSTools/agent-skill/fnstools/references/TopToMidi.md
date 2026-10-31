# TopToMidi

Samples an image at points you define and turns the pixel values into MIDI notes in a musical scale, with trigger gating, retrigger control, a MIDI-learned custom scale and output to a MIDI Out or VST CHOP.

- Category: CHOPs & sensing
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/toptomidi/

## What it does

- **Sample an image at points**: A SOP's points or a TOP's pixels say where the input image is read, and each sample point becomes a note.
- **Index mode**: Each sample point plays its own note whenever its pixel passes the threshold, so a pattern sweeping across the picture plays an arpeggio.
- **Value mode**: The pixel's brightness picks the note, quantised to a number of steps.
- **Scale mapping**: Maps every note into a scale from a root note and octave, from major and minor to the church modes.
- **Trigger gating**: Gate lengths, a minimum sustain and a retrigger delay keep a busy picture from spraying notes.
- **Custom scales**: Type your own scales into a table and they join the Scale menu.
- **Learn a scale from a MIDI keyboard**: With MIDI Scale Learn on, the notes you play one by one become the scale.
- **Play along on a MIDI keyboard**: With MIDI Live on, the scale follows the keys you hold, so you can duet with the picture.
- **Send notes to MIDI Out or a VST**: Sends the notes to a MIDI Out CHOP, an Audio VST CHOP or both, and outputs them as a CHOP for anything else.
- **Sampling preview**: Shows the sample points over the image in a window where you can drag, scale and reset them.
- **Install the mingus dependency**: Install mingus writes a requirements file and hands it to the Python Environment Manager, which installs it into the linked environment in the background.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `topToMidi` (TOP to MIDI) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/TopToMidi.tox`. Its promoted methods are called on the placed copy.

## Promoted API

- `AllNotesOff()`: Silence every note on the MIDI Out and VST outputs.
- `CheckDependencies()`: Look for mingus and write the result to the Status parameter.
- `InstallMingus()`: Install the shipped requirements through the Python Environment Manager, in the background.
- `OpenHelp()`: Open the tool documentation.

## Commands

- **All Notes Off** (id `allnotesoff`): Send note-off for every note on the MIDI and VST outputs Method `AllNotesOff`.
- **Install Mingus** (id `installmingus`): Install the mingus package this tool needs Method `InstallMingus`.
- **Open Help** (id `openhelp`): Open the TopToMidi documentation Method `OpenHelp`.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Input

- **Sampler** (`par.Sampler`, OP): TOP or SOP operator to define the pixel positions for sampling. These can be animated too, of course!
- **Offset 0.5** (`par.Origo`, Toggle), default `off`: By default many SOPs are centered around the origin. This quick toggle shifts the Sampler’s center to (0.5, 0.5).
- **Sample Preview** (`par.Open2`, Pulse): Opens a UI window to visualize and manually adjust the sampling points. Move them around with Left-Click+Dragging ; Scale with Scroll-Wheel (or +-), Reset with Middle-Click. It also has some options on the bottom left to always show the points, toggle Offset 0.5 and Reset the adjustments
- **Sample Channel** (`par.Rgb`, Menu), default `luminance`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`: Which attribute of the input image to perform further processing on.
- **Threshold** (`par.Thresh`, Float x2), default `0.0`: Pre-processes the input image by thresholding between two values. This will also have an effect on when a note is triggered in Index Mapping Mode.
- **Re-Range** (`par.Rerange`, Toggle), default `off`: Re-ranges the thresholded image to 0-1. This parameter is only interesting in Value Mapping Mode.
- **Mapping Mode** (`par.Mode`, Menu), default `0`, menu `Index`, `Value`: This is the most important parameter to determine the mapping of pixel values to MIDI notes, before assigning to a Scale. Index: The point/pixel indices of the Sampler determine the pitch of the notes, upon triggered by the sampled value reaching the Threshold. Notes are sustained while in the range. It is important to set a good Threshold with Index mode.
Important to note that the number of Steps is determined by the number of points. Be careful not to use big textures or SOPs with many points (anyway MIDI is limited to 128 notes).
Value: The sampled values determine the pitch of the notes, where the quantization is determined by the Steps parameter.
It means if you have identical sampled values they will trigged the same note twice.
Re-Range of the Threshold is suggested to be kept on usually.
In this mode you are more free to set more sampling points!
- **Trigger Options** (`par.Triggeroptions`, Header): These parameters can give you more control how often/how long notes are being triggered. Can be very useful in busy scenes.
- **Re-Trigger Gate Length** (`par.Retriggergatelen`, Float), default `0.2`: Overall gate window in seconds. At 0 every trigger passes straight through. Above 0 the sampled pattern is held for this long after a trigger, so a new trigger (or a release) can happen at most once per window; changes that arrive inside the window are applied when it closes.
- **Trigger Gate Length** (`par.Triggergatelength`, Float), default `0.2`: Seconds a sample point has to stay above the threshold before its note turns on. 0 = immediately.
- **Min Sustain Length** (`par.Minsustain`, Float), default `0.0`: Minimum seconds a note stays on once triggered, even if the sample point drops below the threshold sooner.
- **Re-Trigger Delay** (`par.Retrigger`, Float), default `0.0`: Minimum seconds between two triggers of the same note. A new trigger inside this time is ignored.

### Scale

- **Scale** (`par.Scale`, Menu), default `Major`, menu `Major`, `NaturalMinor`, `Chromatic`, `WholeTone`, `HarmonicMajor`, `HarmonicMinor`, `MelodicMinor`, `Bachian`, `MinorNeapolitan`, `Ionian`, `Dorian`, `Phrygian`, `Lydian`, `Mixolydian`, `Aeolian`, `Custom1`, `Custom2`, `Custom31`, `MIDI Scale`: Determines the Scale Mode the triggered notes are mapped to. Scales determine a number of notes in a Scale, starting from a root note (Key). You can also define Custom Scales which will also show up in the dropdown! MIDI Scale is a special one, see later.
- **Key** (`par.Rootnote`, StrMenu), menu `C`, `C#`, `D`, `D#`, `E`, `F`, `F#`, `G`, `G#`, `A`, `A#`, `B`: Sets the musical root note of the Scale.
Can type any musical note notation, even wild things like A#bbb## (thanks to the mingus library). But usually the drop-down list should be more reasonable :)
- **Octave** (`par.Octave`, Int), default `4`: The octave of the root note.
- **Steps** (`par.Steps`, Int), default `1`: Number of MIDI notes to generate.
In Index mode it is fixed to the number of sampling points.
In Value mode it is the "quantization" of the pitch determined by the sampled pixel values.
- **Extend Mode** (`par.Extendmode`, Toggle), default `off`: When having more steps than the number of notes in the Scale, having this on will extend subsequent steps to the next octaves. Otherwise the same scale notes in the starting octave are repeated.
- **Edit Custom Scales** (`par.Open`, Pulse): Opens a Table DAT where in each column you can define a custom scale name where each note can be defined in the rows below using standard musical notation. For example: C#3.
- **Keytrack Lookup** (`par.Velocitylookup`, CHOP): A multi-sample CHOP reference which can define the MIDI velocity based on the pitch.
- **MIDI Scale** (`par.Midiscale`, Header): The parameters below are only relevant if Scale is set to MIDI Scale. They allow you to use this component as a live companion musical instrument.
- **MIDI In CHOP** (`par.Midiref`, CHOP): Optional MIDI In CHOP (a MIDI keyboard) for MIDI Scale learn and live mode. Empty by default; name a sibling MIDI In CHOP, e.g. midiin1.
- **MIDI Scale Learn** (`par.Midilearn`, Toggle), default `off`: Can define a Custom Scale by hitting notes one-by-one on your MIDI In instrument.
- **MIDI Live** (`par.Midilive`, Toggle), default `off`: Follows the keys currently held on the MIDI In CHOP as the scale, in real time (MIDI Scale only), instead of the learned one.
- **Live Octave Offset** (`par.Liveoctaveoffset`, Int), default `0`: Octaves added to the notes taken live from the MIDI In CHOP while MIDI Live is on, so the tool can play along above (or below) the keys you hold.
- **Sync Steps** (`par.Syncsteps`, Toggle), default `off`: Syncs the number of steps to the number of incoming notes. This is not available when Extend Mode is on.
- **Randomize** (`par.Randomize`, Toggle), default `off`: Randomize the order of notes.
- **Seed** (`par.Seed`, Int), default `0`: Seed of the randomization.

### Output

- **MIDI Active** (`par.Active`, Toggle), default `on`: Activates MIDI Out CHOP.
- **MIDI Out CHOP** (`par.Midioutchop`, CHOP): MIDI Out CHOP to send notes to, referenced directly (no Null after it). Empty by default: drop a MIDI Out CHOP beside this tool and name it here, e.g. midiout1 for a sibling.
- **Channel** (`par.Ch`, Int), default `0`: MIDI channel to output notes on.
- **VST Active** (`par.Vstactive`, Toggle), default `off`: Activates VST CHOP.
- **VST CHOP** (`par.Vstchop`, CHOP): Optional Audio VST CHOP to play notes on, referenced directly (no Null after it). Empty by default; name a sibling Audio VST CHOP, e.g. audiovst1.
- **Channel** (`par.Vstchannel`, Int), default `1`: VST channel to output notes on.

### Setup

- **Status** (`par.Status`, Str): Read-only. Whether the Python package mingus (needed for every scale except MIDI Scale) is available, and what to do if it is not.
- **Install mingus** (`par.Install`, Pulse): Installs mingus into the Python environment linked by TouchDesigner's Python Environment Manager, in the background. Needs a linked Python vEnv; the Status line says when one is missing.
- **Re-check** (`par.Recheck`, Pulse): Looks for mingus again, e.g. after installing it by hand from the Python Environment Manager CLI.
- **Python Env Manager Help** (`par.Envhelp`, Pulse): Opens the documentation of TouchDesigner's Python Environment Manager (tdPyEnvManager).

### About

- **Help** (`par.Testopenhelp`, Pulse): Opens documentation.
