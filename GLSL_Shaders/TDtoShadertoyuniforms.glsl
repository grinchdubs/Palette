//Common Uniforms
uniform vec2 iResolution;
uniform vec2 iMouse;

uniform float iTime;
uniform float iFrame;

#define iChannelTime iTime
#define iChannelResolution iResolution
#define iChannel0 sTD2DInputs[0]
#define iChannel1 sTD2DInputs[1]
#define fragCoord gl_FragCoord

out vec4 fragColor;


//Shader
