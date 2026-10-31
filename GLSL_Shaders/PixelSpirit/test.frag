#ifdef GL_ES
precision mediump float;
#endif

#ifndef PI
#define PI 3.1415926535897932384626433832795
#endif


uniform vec2 u_resolution;

float stroke(float x, float s, float w){
	float d = step(s,x+w*.5) - 
			  step(s,x-w*.5);
	return clamp(d, 0., 1.);
}

float fill(float x, float size) {
    return 1.-step(size, x);
}

float rectSDF(vec2 st, vec2 s) {
		st = st*2.-1.; 
    return max( abs(st.x/s.x),
    			abs(st.y/s.y) );
	}

float flip(float v, float pct) {
    return mix(v, 1.-v, pct);
}

vec2 rotate(vec2 st, float a) {
    st = mat2(cos(a),-sin(a),
              sin(a),cos(a))*(st-.5);
    return st+.5;
}

float crossSDF(vec2 st, float s) {
		vec2 size = vec2(.25, s); 
  return min( rectSDF(st , size.xy),
      		  rectSDF(st , size.yx));
	}


float circleSDF (vec2 st) {
	return length(st-.5)*2.;
}

float vesicaSDF(vec2 st, float w) {
    vec2 offset = vec2(w*.5,0.);
    return max( circleSDF(st-offset),
                circleSDF(st+offset));
}

float triSDF(vec2 st) {
    st = (st*2.-1.)*2.;
    return max(abs(st.x) * 0.866025 + st.y * 0.5, -st.y * 0.5);
}

float rhombSDF(vec2 st) {
    return max(triSDF(st),
               triSDF(vec2(st.x,1.-st.y)));
}

void main() {
	vec3 color = vec3(0.);
	vec2 st = gl_FragCoord.xy/u_resolution;
	//color += stroke(st.x, .5, .15);

	//float offset = cos(st.y*PI)*.15;
	//color += stroke(st.x, .28+offset,.1);
	//color += stroke(st.x, .5+offset,.1);
	//color += stroke(st.x, .72+offset,.1);
	
	//float sdf = .5+(st.x-st.y)*.5;
	//color += stroke(sdf,.5,.1);
	//float sdf_inv = (st.x+st.y)*.5;
	//color += stroke(sdf_inv,.5,.1);

	//float circleSDF (vec2 st) {
	//	return length(st-.5)*2.;

	//}

	//color += stroke(circleSDF(st),.5,.05);
	//color += fill(circleSDF(st),.65);
    //vec2 offset = vec2(.1,.05);
    //color -= fill(circleSDF(st-offset),.5);

//float rect = rectSDF(st, vec2(1.));
//color += fill(rect, .5
//	 );
//float cross = crossSDF(st, 1.);
//color *= step(.5,fract(cross*4.));
//color *= step(1., cross);
//color += fill(cross, .5);
//color += stroke(rect, .65, .05);
//color += stroke(rect, .75, .025);

//float rect = rectSDF(st, vec2(.5,1.));
//float diag = (st.x+st.y)*.5;
//color += flip(fill(rect,.6),
//				stroke(diag,.5,.01)); 

//    vec2 offset = vec2(.15,.0);
//    float left = circleSDF(st+offset);
//    float right = circleSDF(st-offset);
//    color += flip(stroke(left,.5,.05),
//                  fill(right,.525));

//float sdf = vesicaSDF(st,.2);
//    color += flip(fill(sdf,.5),
//             step((st.x+st.y)*.5,.5));

//st.y = 1.-st.y;
//    vec2 ts = vec2(st.x,.82-st.y);
//    color += fill(triSDF(st),.7);
//    color -= fill(triSDF(ts),.36);


//float circle = circleSDF(st-vec2(.0,.1));
//   float triangle = triSDF(st+vec2(.0,.1));

//    color += stroke(circle,.45,.1);
//    color *= step(.55,triangle);
//    color += fst = rotate(st, radians(-25.));

st = rotate(vec2(st.x,1.0-st.y),
                radians(45.));
    vec2 s = vec2(1.);
    color += fill(rectSDF(st-.025,s),.4);
    color += fill(rectSDF(st+.025,s),.4);
    color *= step(.38,rectSDF(st+.025,s));

	gl_FragColor = vec4(color,1.0);
}