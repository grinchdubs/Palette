# LayerSep3D

Slices an image into depth layers by a channel threshold and instances them as a stack in 3D, with per layer threshold, softness, mix, position, scale and rotation driven by curves or CHOPs.

- Category: 3D and Particles
- Version: 1.0.4
- Access: Base
- Docs: https://functionstore.tools/docs/layersep3d/

## What it does

- **Slice an image into layers**: Each layer takes the part of the image that passes its threshold on the channel you pick, with a soft edge to its neighbours.
- **Instance the layers as a 3D stack**: The layers are instanced as planes along Z in one Geometry COMP, so a camera pointed at it sees a flat picture with depth.
- **Shape each value with a curve**: Threshold, softness, mix, depth, scale and rotation each follow a curve over the layers, set by offset, amplitude, power and phase.
- **Shuffle the layer order**: Reverse, repeat, phase-shift or randomise which layer each plane shows, or show one layer on every plane.
- **Drive layers from CHOPs**: CHOPs with one sample per layer take over the threshold, softness or mix curves.
- **Instancing overrides**: Per-layer Z, scale and rotation can also be overridden in the instancing.
- **Colour the layers from another image**: Slice one image and draw another on the layers, such as a depth map cutting up the camera feed it came from.
- **Output the layers as a texture**: out_layers gives the layer stack as a 2D texture array or 3D texture for your own instancing.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `layerSep3D` (Layer Sep 3D) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/LayerSep3D.tox`. Its promoted methods are called on the placed copy.

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

- **Layers** (`par.Layers`, Int), default `10`: Number of layers the input is split into (the depth of the output texture and the number of instanced quads). The threshold range is divided into this many equal bands, one per layer. Minimum 2.
- **Reverse Layer Order** (`par.Reverse`, Toggle), default `off`: Flips the order of the layers in the output texture: layer 0 becomes the brightest band instead of the darkest.
- **Open Material** (`par.Open`, Pulse): Opens the parameter dialog of the material the layers are rendered with.
- **Mode** (`par.Mode`, Menu), default `luminanc`, menu `luminanc`, `red`, `green`, `blue`, `alpha`, `rgbavg`, `rgbaavg`, `rgbmax`, `rgbamax`, `rgbmin`, `rgbamin`: Which value of the mask pixel is compared against the thresholds: luminance, a single channel, or an average, maximum or minimum of the channels.
- **Threshold Offset** (`par.Thoffs`, Float), default `0.0`: Added to every layer threshold before the range mapping. Positive values push all band edges up.
- **Threshold Amplitude** (`par.Thamp`, Float), default `1.0`: Scales the spread of the thresholds. 1 spreads the bands over the whole range, smaller values squeeze them toward the bottom, negative values reverse the ramp.
- **Threshold Range** (`par.Thrange`, Float x2), default `0.0`: Mask values (min, max) the layers are spread across. The range is split into Layers equal bands: the first layer also takes everything below the range, the last layer everything above its lower edge.
- **Threshold Power** (`par.Threshpow`, Float), default `1.0`: Exponent applied to the threshold ramp. 1 = equal bands, above 1 = thinner bands at the bottom, below 1 = thinner bands at the top.
- **Threshold Phase** (`par.Thphase`, Float), default `0.0`: Rotates the threshold ramp across the layers (0 to 1), so the band order wraps around.
- **Threshold CHOP (override)** (`par.Threshold`, CHOP), default `None`: Optional CHOP with one sample per layer that replaces the generated thresholds. Leave empty to use the Threshold parameters above (a CHOP wired to the threshold input also overrides them).
- **Softness Offset** (`par.Softoffset`, Float), default `0.0`: Softness added to every layer edge. Softness is the width of the blend between neighbouring layers, in mask units.
- **Softness Amplitude** (`par.Softamp`, Float), default `0.0`: How much the softness ramps across the layers, from 0 at the first layer to this value at the last.
- **Softness Power** (`par.Softpow`, Float), default `1.0`: Exponent applied to the softness ramp across the layers.
- **Softness Phase** (`par.Softphase`, Float), default `0.0`: Rotates the softness ramp across the layers (0 to 1).
- **Softness CHOP (override)** (`par.Softness`, CHOP), default `None`: Optional CHOP with one sample per layer that replaces the generated softness values.
- **Mix Amplitude** (`par.Mixamp`, Float), default `0.0`: How much of the content above each layer is left in it, ramped across the layers. 0 = each layer holds only its own band.
- **Mix Offset** (`par.Mixoffset`, Float), default `0.0`: Mix added to every layer. 1 keeps everything from the layer upward in each slice.
- **Mix Power** (`par.Mixpow`, Float), default `1.0`: Exponent applied to the mix ramp across the layers.
- **Mix Phase** (`par.Mixphase`, Float), default `0.0`: Rotates the mix ramp across the layers (0 to 1).
- **Mix CHOP (override)** (`par.Mix`, CHOP), default `None`: Optional CHOP with one sample per layer that replaces the generated mix values.
- **Texture Index** (`par.Lookupindex`, Header)
- **Invert Texture Index** (`par.Invert2`, Float), default `0.0`: Blends the texture index each quad samples from normal (0) to reversed (1), so the quad order and the layer order can run against each other.
- **Texture Index Phase** (`par.Phase`, Float), default `0.0`: Shifts which layer each instanced quad samples, as a phase of the index ramp.
- **Texture Index Exponent** (`par.Expval`, Float), default `1.0`: Exponent applied to the texture index ramp. 1 = one layer per quad in order; other values bunch the layers toward one end.
- **Texture Index Period** (`par.Period`, Float), default `1.0`: Period of the texture index ramp across the quads. 1 = each layer once; smaller values repeat the layer sequence.
- **Randomize Seed** (`par.Randomize`, Float), default `0.0`: When above 0, shuffles which layer each quad samples, using this value as the seed. 0 = no shuffle.
- **Single Layer** (`par.Single`, Toggle), default `off`: Every quad samples the same layer, chosen by Select.
- **Select Layer** (`par.Select`, Float), default `0.0`: The layer every quad shows while Single Layer is on (0 = first layer).

### Transform

- **These can be overridden in the instancing...** (`par.Thesecanbeoverriddenintheinstancing`, Header)
- **Z Offset** (`par.Tzoffset`, Float), default `0.0`: Z position added to every quad.
- **Z Amplitude** (`par.Tzamplitude`, Float), default `1.0`: Total Z spread of the quads, from the first layer to the last.
- **Z Power** (`par.Tzpow`, Float), default `1.0`: Exponent applied to the Z spread, so the quads bunch toward the front or the back.
- **Z Phase** (`par.Tzphase`, Float), default `0.0`: Rotates the Z ramp across the quads (0 to 1).
- **Scale Offset** (`par.Scaleoffset`, Float), default `1.0`: Uniform scale of every quad (1 = original size).
- **Scale Amplitude** (`par.Scaleamplitude`, Float), default `0.0`: How much the scale ramps across the quads, added on top of Scale Offset.
- **Scale Power** (`par.Scalepow`, Float), default `1.0`: Exponent applied to the scale ramp across the quads.
- **Scale Phase** (`par.Scalephase`, Float), default `0.0`: Rotates the scale ramp across the quads (0 to 1).
- **Rotation Offset** (`par.Rotoffset`, Float), default `0.0`: Z rotation in degrees added to every quad.
- **Rotation Amplitude** (`par.Rotamplitude`, Float), default `0.0`: How many degrees the rotation ramps across the quads.
- **Rotation Power** (`par.Rotpow`, Float), default `1.0`: Exponent applied to the rotation ramp across the quads.
- **Rotation Invert** (`par.Rotinvert`, Float), default `0.0`: Blends the rotation ramp from normal (0) to reversed (1).

### Common

- **Output Type** (`par.Type`, Menu), default `texture2darray`, menu `texture2darray`, `texture3d`: 2D Texture Array keeps each layer as its own slice (smooth mipmaps); 3D Texture lets the instance texture index interpolate between layers.
- **^ 2D: allows for smooth Mipmap pixels** (`par.Header`, Header)
- **^ 3D: allows for layer interpolation (Tex Idx)** (`par.Header2`, Header)
- **Filter** (`par.Instancetexfilter`, Menu), default `mipmaplinear`, menu `nearest`, `linear`, `mipmaplinear`: Texture filtering used when the quads sample the layer texture.
- **Author** (`par.Authorname`, Str), default `Function Store (@function.str)`: Author of the component.
- **Author Link** (`par.Openauthor`, Pulse): Opens the author page in the browser.
