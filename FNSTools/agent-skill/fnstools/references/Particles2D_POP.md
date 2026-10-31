# Particles2D_POP

A 2D particle simulation as a POP loop: a source image emits particles, curl noise and wind effectors steer them with lookup ranges, trails stretch them, and the loop rides out as points for your own render.

- Category: 3D and Particles
- Version: 1.0.6
- Access: Base
- Docs: https://functionstore.tools/docs/particles2d-pop/

## What it does

- **Emit from a source image**: Particles are born from the image on in_source and carry its colours, each with its own life, mass and drag.
- **Curl noise field**: A moving curl noise field swirls the particles, with its strength set per axis and its speed on the Curl page.
- **Wind with variance**: A wind blows the particles along a direction you set, with random variance on top; it starts at zero.
- **Steer forces with images**: Each force reads an image through its own lookup, so a picture or a mask decides where it is strong and where it is off.
- **Motion trails**: Trails stretch the points along their motion.
- **Points out for your own render**: The simulated points come out of out_loopout, ready for a Render TOP with your own material or any POP that takes points.
- **Insert your own POPs into the loop**: out_loopout and in_loopin are the two ends of the simulation loop, so POPs of your own can sit inside it.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `particles2D` (Particles 2D) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/Particles2D_POP.tox`. Its promoted methods are called on the placed copy.

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

- **Particles** (`par.Particles`, Header)
- **Start Pulse** (`par.Startpulse`, Pulse): Start the simulation.
- **Maximum Particles** (`par.Maxparticles`, Int), default `921600`: How many particles can live at once.
- **Birthrate** (`par.Birthrate`, Float), default `50000.0`: How many particles are born per second.
- **Life** (`par.Life`, Float), default `2.0`: How long a particle lives, in seconds.
- **Life Variance** (`par.Lifevariance`, Float), default `0.5`: Random variation of the life of each particle.
- **Initial Mass** (`par.Initmass`, Float), default `2.0`: Mass of a new particle: heavier particles react less to forces.
- **Initial Drag** (`par.Initdrag`, Float), default `1.0`: Drag of a new particle: how quickly it loses speed.
- **Velocity Damping** (`par.Damping`, Float), default `0.1`: Slows every particle down each frame.
- **Speed** (`par.Speed2`, Float), default `1.0`: Overall speed of the simulation.
- **Trails** (`par.Trails`, Header)
- **Length** (`par.Length`, Float), default `0.037`: How far trails stretch the points along their motion.
- **Reset Pulse** (`par.Resetpulse`, Pulse): Clear the simulation.

### Curl

- **Curl** (`par.Curl`, XYZW x3), default `0.5`: Strength of the curl noise field on each axis.
- **Speed** (`par.Speed`, XYZW x4), default `0.04`: How fast the curl noise field moves.
- **Open Curl Noise** (`par.Opennoise`, Pulse): Open the curl noise generator to edit it.
- **Lookup** (`par.Lookup`, Header)
- **Rgb** (`par.Rgb`, Menu), default `luminance`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`, `zero`, `one`: Which channel of the curl effector image is read.
- **Normalize** (`par.Norm`, Toggle), default `off`: Normalize the curl effector image before it is remapped.
- **Fromrange** (`par.Fromrange`, Float x2), default `0.0`: The input range of the curl effector image.
- **Torange** (`par.Torange`, Float x2), default `0.0`: The range the curl effector image is mapped to.
- **Exponent Value** (`par.Expval`, Float), default `1.0`: Exponent applied to the curl effector image: 1 is linear.
- **Update** (`par.Updatecurl`, Toggle), default `on`: Apply the curl effector.

### Wind

- **Wind** (`par.Wind`, XYZW x3), default `0.0`: Wind force on each axis.
- **Variance** (`par.Windvariance`, XYZW x3), default `0.0`: Random variation of the wind on each axis.
- **Wind Variance Speed** (`par.Windvariancespeed`, XYZW x4), default `0.0`: How fast the wind variation changes.
- **Open Variance** (`par.Opennoise2`, Pulse): Open the wind variance noise generator to edit it.
- **Lookup** (`par.Lookup2`, Header)
- **RGB** (`par.Rgbwind`, Menu), default `average`, menu `luminance`, `red`, `green`, `blue`, `alpha`, `rgbaverage`, `average`, `rgbmax`, `max`, `zero`, `one`: Which channel of the wind effector image is read.
- **Normalize** (`par.Normwind`, Toggle), default `on`: Normalize the wind effector image before it is remapped.
- **From Range** (`par.Fromrangewind`, Float x2), default `0.0`: The input range of the wind effector image.
- **To Range** (`par.Torangewind`, Float x2), default `0.0`: The range the wind effector image is mapped to.
- **Exponent Value** (`par.Expvalwind`, Float), default `1.0`: Exponent applied to the wind effector image: 1 is linear.
- **Update** (`par.Updatewind`, Toggle), default `off`: Apply the wind effector.
