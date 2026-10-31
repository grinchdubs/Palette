# ResetPLS

Package `FNS_ResetPLS`.

Reset stateful operators (feedback, cache, timers, counts) across the project, with a pattern-based exception list. Bound to ctrl+0.

- Category: Project
- Version: 3.2.11
- Access: Free
- Docs: https://functionstore.tools/docs/fns-resetpls/

## What it does

- **Restart every feedback loop and timer at once**: One press of `Ctrl+0`, the toolbar button or quick-launch pulses the reset of every matching operator in the project.
- **Operator type toggles**: Switch whole operator types in or out, from Feedback TOPs and Timer CHOPs to particle systems, solvers and MIDI In DATs.
- **Startup reset**: The project can reset itself once as it opens.
- **Rewind the timeline too**: A reset can also send the root timeline back to a chosen frame.
- **Search only part of a project**: Point the search at one component, and cap how deep it looks.
- **Exclude operators by path**: Leave named operators alone, with or without everything inside them.
- **Exceptions by pattern**: A pattern list such as `^*/presets*` for components that should never be reset; with Externalize Tables on, it follows you from project to project.
- **Custom components join the reset**: Your components and Script operators join the reset through a pulse named Reset or Resetpulse, and the list of names is yours to extend.
- **Callback on every reset**: Run your own Python on every reset, for anything a pulse cannot express.

## Reach it

`op.FNS_RPLS` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `EditCustomResetPars()`: Open the custom reset pars editor.
- `EditStaticExceptions()`: Open the static exceptions editor.
- `ResetGenerators()`: Pulse Reset on every enabled generator OP type (the panic button).

## Commands

- **Edit custom reset pars** (id `editcustomresetpars`): Open the custom reset pars editor. Method `EditCustomResetPars`.
- **Edit reset static exceptions** (id `editstaticexceptions`): Open the static exceptions editor. Method `EditStaticExceptions`.
- **Reset all generators** (id `resetgenerators`): Pulse Reset on every enabled generator OP type (the panic button). Method `ResetGenerators`.

## Hotkeys

- `cmd.0 ctrl.0` (`Shortcut` on `FNS_ResetPLS`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Conf

- **Root** (`par.Root`, COMP), default `..`: Where the search for resettable operators starts. Everything under this component is considered, subject to Depth and the exception lists.
- **Limit Depth** (`par.Limitdepth`, Toggle), default `on`: Stop the search at a fixed number of levels below Root instead of walking the whole tree. Worth it in a big project where a full walk is slow.
- **Depth** (`par.Depth`, Int), default `1`: How many levels below Root to search, when Limit Depth is on.
- **Except** (`par.Except`, Str): Operators to leave alone, one pattern per entry. Everything else under Root is reset.
- **Exceptions Limit** (`par.Exceptionslimit`, Toggle), default `off`: For an excepted COMP, also skip everything inside it. Off resets its children even though the COMP itself is excepted.
- **Enable All OPtypes** (`par.Activeall`, Pulse): Switch on every operator-type toggle across the pages, so the reset covers everything this tool knows how to reset.
- **Disable All OPtypes** (`par.Disableall`, Pulse): Switch off every operator-type toggle, so the reset covers nothing until you pick types back.
- **Reset On Startup** (`par.Resetonstartup`, Toggle), default `off`: Fire the reset once, automatically, when the project opens.
- **Reset** (`par.Reset`, Pulse): Reset now: pulse the reset parameter of every included operator under Root. This is what the hotkey and the toolbar button do.
- **Reset Shortcut** (`par.Shortcut`, Str), default `cmd.0 ctrl.0`: Hotkey that pulses Global ResetPLS. Both the Windows and macOS combos are listed.

### TOP

- **Feedback** (`par.Feedbacktop`, Toggle), default `off`: Include Feedback TOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Cache** (`par.Cachetop`, Toggle), default `off`: Include Cache TOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Texture 3D** (`par.Texture3d`, Toggle), default `off`: Include Texture 3D TOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Movie File In** (`par.Moviefilein`, Toggle), default `off`: Include Movie File In TOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Flow** (`par.Flow`, Toggle), default `off`: Include Flow TOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Blob Track** (`par.Blobtrack`, Toggle), default `off`: Include Blob Track TOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Script** (`par.Scripttop`, Toggle), default `off`: Include Script TOPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.

### CHOP

- **LFO** (`par.Lfo`, Toggle), default `off`: Include LFO CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Speed** (`par.Speed`, Toggle), default `off`: Include Speed CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Count** (`par.Count`, Toggle), default `off`: Include Count CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Timer** (`par.Timer`, Toggle), default `off`: Include Timer CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Filter** (`par.Filter`, Toggle), default `off`: Include Filter CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Lag** (`par.Lag`, Toggle), default `off`: Include Lag CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Audio File In** (`par.Audiofilein`, Toggle), default `off`: Include Audio File In CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Audio Oscillator** (`par.Audiooscillator`, Toggle), default `off`: Include Audio Oscillator CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Feedback** (`par.Feedbackchop`, Toggle), default `off`: Include Feedback CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Gesture** (`par.Gesture`, Toggle), default `off`: Include Gesture CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Beat** (`par.Beat`, Toggle), default `off`: Include Beat CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Trail** (`par.Trailchop`, Toggle), default `off`: Include Trail CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Event** (`par.Event`, Toggle), default `off`: Include Event CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Record** (`par.Record`, Toggle), default `off`: Include Record CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Sequencer** (`par.Sequencer`, Toggle), default `off`: Include Sequencer CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Noise** (`par.Noise`, Toggle), default `off`: Include Noise CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Script** (`par.Scriptchop`, Toggle), default `off`: Include Script CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.
- **Spring** (`par.Springchop`, Toggle), default `off`: Include Spring CHOPs in the reset sweep, so their reset parameter is pulsed along with everything else.

### SOP

- **Trail** (`par.Trailsop`, Toggle), default `off`: Include Trail SOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Cache** (`par.Cachesop`, Toggle), default `off`: Include Cache SOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Particle** (`par.Particle`, Toggle), default `off`: Include Particle SOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Creep** (`par.Creep`, Toggle), default `off`: Include Creep SOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Spring** (`par.Springsop`, Toggle), default `off`: Include Spring SOPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Script** (`par.Scriptsop`, Toggle), default `off`: Include Script SOPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.

### POP

- **Cache** (`par.Cachepop`, Toggle), default `off`: Include Cache POPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Trail** (`par.Trailpop`, Toggle), default `off`: Include Trail POPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Feedback** (`par.Feedbackpop`, Toggle), default `off`: Include Feedback POPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Particle** (`par.Particlepop`, Toggle), default `off`: Include Particle POPs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Import Select** (`par.Importselectpop`, Toggle), default `off`: Include Import Select POPs in the reset sweep, so their reset parameter is pulsed along with everything else.

### DAT

- **MIDI In** (`par.Midiin`, Toggle), default `off`: Include MIDI In DATs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **MIDI Event** (`par.Midievent`, Toggle), default `off`: Include MIDI Event DATs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Fifo** (`par.Fifo`, Toggle), default `off`: Include Fifo DATs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Serial** (`par.Serial`, Toggle), default `off`: Include Serial DATs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **OSC In** (`par.Oscin`, Toggle), default `off`: Include OSC In DATs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **OSC Out** (`par.Oscout`, Toggle), default `off`: Include OSC Out DATs in the reset sweep, so their reset parameter is pulsed along with everything else.
- **Script** (`par.Scriptdat`, Toggle), default `off`: Include Script DATs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.

### COMP

- **Replicator** (`par.Replicator`, Toggle), default `off`: Include Replicator COMPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.
- **Flex Solver** (`par.Flexsolver`, Toggle), default `off`: Include Flex Solver COMPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.
- **Actor** (`par.Actor`, Toggle), default `off`: Include Actor COMPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.
- **Bullet Solver** (`par.Bulletsolver`, Toggle), default `off`: Include Bullet Solver COMPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.
- **Base** (`par.Base`, Toggle), default `off`: Include Base COMPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.
- **Container** (`par.Container`, Toggle), default `off`: Include Container COMPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.
- **Geometry** (`par.Geometry`, Toggle), default `off`: Include Geometry COMPs in the reset sweep, so their reset parameter is pulsed along with everything else. Reset here means pulsing a custom parameter named Reset or Resetpulse. The list of names it looks for is editable under Misc, Edit Custom Reset Pars.

### Misc

- **Reset Timeline** (`par.Timeline`, Toggle), default `off`: Also send the root timeline back to Reset Frame when a reset runs.
- **Reset Frame** (`par.Frame`, Int), default `0`: The frame the root timeline jumps to, when Reset Timeline is on.
- **Callback** (`par.Customscript`, Toggle), default `off`: Also run your own callback on each reset, so a tool with no reset parameter can still be handled.
- **Create Callbacks** (`par.Createcallbacks`, Pulse): Create a callbacks DAT beside this component with an onReset stub to fill in, and point the parameter below at it.
- **Callbacks** (`par.Callbacks`, DAT): The DAT holding the onReset callback. It points at the shipped default until you make your own.
- **Static Exceptions** (`par.Open2`, Pulse): Edit the static exception list: name patterns that are never reset, whatever else is set. Prefix each with '^'. Re-save the component after adding rows, or they are lost with the session.
- **Edit Custom Reset Pars** (`par.Open3`, Pulse): Edit the parameter names this tool treats as a reset on COMPs and Script operators. Defaults are Reset and Resetpulse; add your own component's name here to make it resettable.
- **Externalize Tables** (`par.Externalizetables`, Toggle), default `off`: Keep this component's tables in files on disk rather than inside the project, so the same exceptions and reset-parameter names follow you between projects.

### About

- **ReadMe** (`par.Open`, Pulse): Open this tool's README.
