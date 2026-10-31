# ParticlesGpuUltimate

A GPU particle system driven by images: a thresholded source emits particles, and look, life, turbulence, wind and force fields shape them, each optionally read from its own image, with a feedback pass for trails and one rendered output.

- Category: 3D and Particles
- Version: 2.0.4
- Access: Pro
- Docs: https://functionstore.tools/docs/particlesgpuultimate/

## What it does

- **Emit particles from an image**: The source image is thresholded to decide where particles are born and what colour they carry.
- **Material and particle shape**: Pick the material, the SOP shape for each particle and the maximum particle size on the Look page.
- **Fade particles over their life**: Set how long particles live, fade them in and out at either end of their life, and shrink or dim them as they age.
- **Turbulence and wind**: Turbulence and wind act differently on the dark and the bright parts of an image, so a picture decides where particles swirl or drift.
- **Steer each effector with its own image**: Life, turbulence and wind can each read their own image, apart from the one that emits the particles.
- **Force fields you place**: Radial, axial, vortex and spiral fields that you place, each with its own reach and strength.
- **Feedback trails**: A feedback pass draws trails behind the particles, mixed in with Dry / Wet, over the source or a background colour.
- **Replace the position and colour maps**: Position and colour maps of your own replace the ones derived from the source image.
- **Optical flow movement**: An optical-flow map pushes the particles, as hard as Optical Flow Magnitude sets.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `particlesGpuUltimate` (Particles GPU Ultimate) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/ParticlesGpuUltimate.tox`. Its promoted methods are called on the placed copy.

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

### Source

- **Source Res** (`par.Sourceres`, XYZW x2), default `0.0`: Resolution the source image is sampled at.
- **Interpolate Source Point Position** (`par.Interpolatepoint`, Toggle), default `on`: When using a low resolution source object, toggling this parameter will spawn particles from interpolated positions of the original source.
- **Source Thresh** (`par.Sourcethresh`, Header)
- **Comparator** (`par.Comparator`, Menu), default `less`, menu `less`, `greater`, `lessorequal`, `greaterorequal`, `equal`, `notequal`: How pixels are compared with the threshold to decide where particles are born.
- **RGB** (`par.Rgb2`, Menu), default `luminance`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`: Which channel of the source image is compared with Source Threshold.
- **Source Threshold** (`par.Sourcethreshold`, Float), default `0.5`: The brightness a pixel needs, by the comparator, to emit particles.
- **Source Mix** (`par.Sourcemix`, Header)
- **OverUnderLay Source** (`par.Menu`, Menu), default `Input`, menu `Input`, `Thresholded`: What is composited with the particles: the input image or the thresholded source.
- **Under Opac** (`par.Sourceunderopac`, Float), default `1.0`: Opacity of the source image underneath the particles.
- **Operation** (`par.Operand`, Menu), default `multiply`, menu `add`, `atop`, `average`, `brightest`, `burncolor`, `burnlinear`, `chromadifference`, `color`, `darkercolor`, `difference`, `dimmest`, `divide`, `dodge`, `exclude`, `freeze`, `glow`, `hardlight`, `hardmix`, `heat`, `hue`, `inside`, `insideluminance`, `inverse`, `lightercolor`, `luminancedifference`, `maximum`, `minimum`, `multiply`, `negate`, `outside`, `outsideluminance`, `over`, `overlay`, `pinlight`, `reflect`, `screen`, `softlight`, `linearlight`, `stencilluminance`, `subtract`, `subtractive`, `under`, `vividlight`, `xor`, `yfilm`, `zfilm`: How the source and the particles are composited.
- **Opac** (`par.Opacity2`, Float), default `1.0`: Opacity of the composited source.
- **Comp Over Background Color** (`par.Compover`, Toggle), default `off`: Composite the result over the background colour.
- **Bgcolor** (`par.Bgcolor`, RGBA x4), default `0.0`: The background colour.

### pGpu

- **Render Res** (`par.Res`, XYZW x2), default `0.0`: The render resolution.
- **Create** (`par.Create`, Menu), default `name1`, menu `numParticles`, `perFrame`: Specify how particles are being created. You can either create a certain number of particles all at once or create a certain number of particles on a per frame basis.
- **Max Particles in Simulation** (`par.Maxparticles`, Int), default `409600`: How many particles the simulation holds at once.
- **Birth** (`par.Birth`, Int), default `10000`: The number of particles spawned each frame. Only available when the Create parameter is set to "By Particles per Frame".
- **Random InitPos** (`par.Randominitpos`, Toggle), default `on`: Birth particles at random positions inside the source instead of in order.
- **Camera** (`par.Camera`, COMP): The camera the particles are rendered through.
- **Projection Blend** (`par.Projectionblend`, Float), default `0.0`: Blend between perspective (0) and orthographic (1) projection.
- **Light** (`par.Light`, COMP), default `light1`: The light used when rendering the particles.
- **Hit Behaviour** (`par.Hit`, Menu), default `bounce`, menu `none`, `die`, `bounce`, `avoid`, `stick`, `fade`: Specify what the particle should do when leaving the bounding box.
- **Speed** (`par.Speed`, Float), default `1.0`: Overall speed of the simulation.
- **Drag** (`par.Drag`, Float), default `1.0`: How quickly particles lose speed.
- **Optical Flow Magnitude** (`par.Optflowmag`, Float), default `0.01`: Magnitude of the optical flow input force.
- **Optical Flow Size Remap** (`par.Optflowremap`, XYZW x2), default `1.0`: Remaps the size of the optical flow input to help adjust to the systems aspect ratio.
- **Pause** (`par.Pause`, Toggle), default `off`: Freeze the simulation.
- **Reset** (`par.Reset`, Pulse): Reset the particle system.

### Look

- **Material** (`par.Material`, Menu), default `constant`, menu `constant`, `phong`, `line`, `pbr`: Select which material type should be used for the particle system render.
- **Open MAT** (`par.Open`, Pulse): Open the particle material to edit it.
- **SOP** (`par.Sop`, Menu), default `Point`, menu `Point`, `Box`: The shape drawn for each particle: a point or a box.
- **Particle Size Max** (`par.Particlesizemax`, Float), default `1.0`: Specify the maximum size of the particle.
- **Compositing** (`par.Compositing`, Menu), default `independent`, menu `coverage`, `discard`, `independent`, `nodepth`: How particle transparency is resolved when rendering.
- **Alpha Threshold** (`par.Alphathreshold`, Float), default `0.8`: Pixels of a particle below this alpha are discarded.
- **Fade** (`par.Fade`, Header)
- **Fade In** (`par.Fadein`, Float), default `0.001`: Specify the time in seconds a particle fades in after being spawned.
- **Fade Out** (`par.Fadeout`, Float), default `1.0`: Specify the time in seconds a particle fades out before dying.
- **Fade to Color (Mult Alpha)** (`par.Fadetocolor`, Float), default `1.0`: How far particles fade toward black (multiplied alpha) over their life.
- **Fade to Alpha** (`par.Alphafade`, Float), default `0.0`: How far particles fade out over their life.
- **Fade to Size** (`par.Fadetosize`, Float), default `0.0`: How far particles shrink over their life.
- **Col to Size Map** (`par.Coltosizemap`, Menu), default `red`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`, `zero`, `one`: Which channel of the source colour sets particle size.
- **Col to Size Cross** (`par.Lumtosize`, Float), default `0.0`: Blend between a fixed size and a size taken from the source colour.
- **Normalize** (`par.Norm4`, Toggle), default `off`: Stretch the source colour to the full 0 to 1 range before it sets particle size.
- **Exponent Value** (`par.Expval`, Float), default `2.0`: Exponent on the colour-to-size mapping: 1 is linear.
- **Size Mod Invert** (`par.Sizemodinvert`, Float), default `0.0`: Invert the colour-to-size mapping, so darker areas give bigger particles.

### Life

- **Life Type** (`par.Lifetype`, Menu), default `constant`, menu `constant`, `random`, `Effector`: How life is set: the same for every particle, random, or read from an effector image.
- **Life** (`par.Life`, Float), default `2.0`: The number of seconds a particle will be alive.
- **Life Max** (`par.Lifemax`, Float), default `0.0`: The longest a particle can live, in seconds.
- **Lifevariance** (`par.Lifevariance`, Float), default `2.0`: A delta number of seconds that will be added or subtracted from the expected lifetime, specified in the Life parameter, of a particle.
- **RGB** (`par.Rgb`, Menu), default `red`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`, `zero`, `one`: Which channel of the life effector image is read.
- **Normalize** (`par.Norm3`, Toggle), default `off`: Stretch the life effector image to the full 0 to 1 range before it is mapped.
- **Exponent Value** (`par.Expval2`, Float), default `2.0`: Exponent on the life effector mapping: 1 is linear.
- **To Range (dark/bright)** (`par.Torange`, Float x2), default `0.0`: The range the life effector is mapped to.
- **Works only with Random InitPos=Off** (`par.Worksonlywithrandominitposoff`, Header)
- **Random InitPos** (`par.Randominitpos2`, Toggle), default `on`: Birth particles at random positions (mirrors Random InitPos on the pGpu page).
- **InitPos/CurrPos** (`par.Effectorswitchlife`, Toggle), default `on`: Where the effector image is sampled: at the position a particle was born (off) or where it is now (on).

### Turb

- **Turb Gain** (`par.Turbgain`, Float), default `1.0`: Overall strength of the turbulence.
- **Trub Effector Exponent** (`par.Turbexpval`, Float), default `2.0`: Exponent on the turbulence effector image: 1 is linear.
- **Turb Seed** (`par.Turbseed1`, Int), default `0`: Random seed of the turbulence noise.
- **Turb Trans Speed** (`par.Turbtrans`, XYZW x3), default `0.0`: How fast the turbulence noise moves on each axis.
- **Rgb** (`par.Rgbturb`, Menu), default `luminance`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`, `zero`, `one`: Which channel of the turbulence effector image is read.
- **Normalize** (`par.Norm`, Toggle), default `off`: Stretch the turbulence effector image to the full 0 to 1 range before it is mapped.
- **Dark Side** (`par.Darkside`, Header)
- **Turb** (`par.Turb`, XYZW x3), default `0.0`: Turbulence on the dark side of the effector image, per axis.
- **Turb Period** (`par.Turbperiod1`, Float), default `0.5`: Scale of the turbulence noise: larger periods give broader swirls.
- **Turb Mag** (`par.Turbmag`, Float), default `0.0`: Strength of the dark-side turbulence.
- **Bright Side** (`par.Brightside`, Header)
- **Turb** (`par.Turb1`, XYZW x3), default `0.0`: Turbulence on the bright side of the effector image, per axis.
- **Turb Period2** (`par.Turbperiod2`, Float), default `0.5`: Scale of the bright-side turbulence noise: larger periods give broader swirls.
- **Turb Mag** (`par.Turbmag1`, Float), default `0.0`: Strength of the bright-side turbulence.
- **InitPos/CurrPos** (`par.Effectorswitchturb`, Toggle), default `on`: Where the effector image is sampled: at the position a particle was born (off) or where it is now (on).

### Wind

- **Windgain** (`par.Windgain`, Float), default `0.0`: Overall strength of the wind.
- **Wind Effector Exponent** (`par.Windexpval`, Float), default `2.0`: Exponent on the wind effector image: 1 is linear.
- **Rgb** (`par.Rgbwind`, Menu), default `luminance`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`, `zero`, `one`: Which channel of the wind effector image is read.
- **Normalize** (`par.Norm2`, Toggle), default `off`: Stretch the wind effector image to the full 0 to 1 range before it is mapped.
- **Dark Side** (`par.Darkside2`, Header)
- **Wind** (`par.Wind1`, XYZW x3), default `0.0`: Wind direction on the dark side of the effector image.
- **WindMag** (`par.Windmag1`, Float), default `0.0`: Strength of the dark-side wind.
- **Wind Variance** (`par.Windvariance`, Float), default `0.0`: Random variation of the dark-side wind.
- **Bright Side** (`par.Brightside2`, Header)
- **Wind** (`par.Wind`, XYZW x3), default `0.0`: Wind direction on the bright side of the effector image.
- **WindMag** (`par.Windmag`, Float), default `0.0`: Strength of the bright-side wind.
- **Wind Variance** (`par.Windvariance1`, Float), default `0.0`: Random variation of the bright-side wind.
- **InitPos/CurrPos** (`par.Effectorswitchwind`, Toggle), default `on`: Where the effector image is sampled: at the position a particle was born (off) or where it is now (on).

### Forces

- **Forces** (`par.Forces`, Sequence), default `0`: Extra forces placed in the scene, one block each.
- **Force Type** (`par.Forces0forcetype`, Menu), default `2`, menu `Radial`, `Axial`, `Vortex`, `Spiral`: The shape of this force: Radial acts outward from its position (inward with a negative amount), Axial along its direction, Vortex around its direction, Spiral around and inward at once.
- **Forcepos** (`par.Forces0forcepos`, XYZW x3), default `0.0`: Where this force sits in particle space.
- **Force Radius** (`par.Forces0forceradius`, Float), default `1.0`: How far this force reaches from its position.
- **Force Amount** (`par.Forces0forceamount`, Float), default `0.0`: Strength of this force; a negative amount reverses it.
- **Forcedir** (`par.Forces0forcedir`, XYZW x3), default `0.0`: The axis this force acts along (Axial) or around (Vortex, Spiral).
- **Force Type** (`par.Forces1forcetype`, Menu), default `2`, menu `Radial`, `Axial`, `Vortex`, `Spiral`: The shape of this force: Radial acts outward from its position (inward with a negative amount), Axial along its direction, Vortex around its direction, Spiral around and inward at once.
- **Forcepos** (`par.Forces1forcepos`, XYZW x3), default `0.0`: Where this force sits in particle space.
- **Force Radius** (`par.Forces1forceradius`, Float), default `1.0`: How far this force reaches from its position.
- **Force Amount** (`par.Forces1forceamount`, Float), default `0.0`: Strength of this force; a negative amount reverses it.
- **Forcedir** (`par.Forces1forcedir`, XYZW x3), default `0.0`: The axis this force acts along (Axial) or around (Vortex, Spiral).

### Post

- **Operation** (`par.Operand1`, Menu), default `multiply`, menu `add`, `atop`, `average`, `brightest`, `burncolor`, `burnlinear`, `chromadifference`, `color`, `darkercolor`, `difference`, `dimmest`, `divide`, `dodge`, `exclude`, `freeze`, `glow`, `hardlight`, `hardmix`, `heat`, `hue`, `inside`, `insideluminance`, `inverse`, `lightercolor`, `luminancedifference`, `maximum`, `minimum`, `multiply`, `negate`, `outside`, `outsideluminance`, `over`, `overlay`, `pinlight`, `reflect`, `screen`, `softlight`, `linearlight`, `stencilluminance`, `subtract`, `subtractive`, `under`, `vividlight`, `xor`, `yfilm`, `zfilm`: How the feedback trail is combined with the new frame.
- **Opacity** (`par.Opacity`, Float), default `0.9`: Opacity of the feedback trail.
- **Filter Size** (`par.Size`, Int), default `7`: Blur applied to the feedback trail each frame, in pixels.
- **Reset** (`par.Reset1`, Momentary), default `off`: Clear the feedback trail.
- **Dry / Wet Mix** (`par.Drywet`, Float), default `1.0`: Mix between the plain render (0) and the render with its feedback trail (1).
