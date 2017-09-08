/* source: https://www.clicktorelease.com/blog/how-to-make-clouds-with-css-3d/ */

(function() {
	var lastTime = 0;
	var vendors = ['ms', 'moz', 'webkit', 'o'];
	for(var x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
		window.requestAnimationFrame = window[vendors[x]+'RequestAnimationFrame'];
		window.cancelRequestAnimationFrame = window[vendors[x]+
		  'CancelRequestAnimationFrame'];
	}

	if (!window.requestAnimationFrame)
		window.requestAnimationFrame = function(callback, element) {
			var currTime = new Date().getTime();
			var timeToCall = Math.max(0, 16 - (currTime - lastTime));
			var id = window.setTimeout(function() { callback(currTime + timeToCall); },
			  timeToCall);
			lastTime = currTime + timeToCall;
			return id;
		};

	if (!window.cancelAnimationFrame)
		window.cancelAnimationFrame = function(id) {
			clearTimeout(id);
		};
}())


/*
  objects is an array of cloud bases
  layers is an array of cloud layers
*/
var layers = [],
	objects = [],


	/*
	  Defining our variables
	  world and viewport are DOM elements,
	  worldXAngle and worldYAngle are floats that hold the world rotations,
	  d is an int that defines the distance of the world from the camera
	*/
	world = document.getElementById( 'world' ),
	viewport = document.getElementById( 'viewport' ),

	d = 0,
	//p = "10000px",
	worldXAngle = 0,
	worldYAngle = 0;


/*viewport.style.webkitPerspective = p;
viewport.style.MozPerspective = p;
viewport.style.oPerspective = p;
viewport.style.Perspective = p;*/


generate();


/*
  Creates a single cloud base and adds several cloud layers.
  Each cloud layer has random position ( x, y, z ), rotation (a)
  and rotation speed (s). layers[] keeps track of those divs.
*/
function createCloud() {

	var div = document.createElement( 'div'  );
	div.className = 'cloudBase';
	var x = 256 - ( Math.random() * 1024 );
	var y = 256 - ( Math.random() * 512 );
	var z = 256 - ( Math.random() * 768 );
	var t = 'translateX( ' + x + 'px ) translateY( ' + y + 'px ) translateZ( ' + z + 'px )';
	div.style.webkitTransform = t;
	div.style.MozTransform = t;
	div.style.oTransform = t;
	div.style.Transform = t;
	world.appendChild( div );

	for( var j = 0; j < 5 + Math.round( Math.random() * 10 ); j++ ) {
		var cloud = document.createElement( 'img' );
		cloud.style.opacity = 0;
		var r = Math.random();
		if (document.location.pathname.includes("/en/")) {
			var src = '../theme/images/cloud_v2.png';
		}
		else {
			var src = './theme/images/cloud_v2.png';
		}
		( function( img ) { img.addEventListener( 'load', function() {
			img.style.opacity = 0.8;
		} ) } )( cloud );
		cloud.setAttribute( 'src', src );
		cloud.className = 'cloudLayer';

		var x = 256 - ( Math.random() * 512 );
		var y = 256 - ( Math.random() * 512 );
		var z = 100 - ( Math.random() * 200 );
		var a = Math.random() * 360;
		var s = .25 + Math.random();
		x *= .2; y *= .2;
		cloud.data = {
			x: x,
			y: y,
			z: z,
			a: a,
			s: s,
			speed: 0.2 * Math.random()
		};
		var t = 'translateX( ' + x + 'px ) translateY( ' + y + 'px ) translateZ( ' + z + 'px ) rotateZ( ' + a + 'deg ) scale( ' + s + ' )';
		cloud.style.webkitTransform = t;
		cloud.style.MozTransform = t;
		cloud.style.oTransform = t;
		cloud.style.Transform = t;

		div.appendChild( cloud );
		layers.push( cloud );
	}

	return div;
}


/*window.addEventListener( 'mousewheel', onContainerMouseWheel );*/
/*window.addEventListener( 'DOMMouseScroll', onContainerMouseWheel );*/
/*
  Event listener to transform mouse position into angles
  from -180 to 180 degress, both vertically and horizontally
*/
header___element = document.getElementById("header");
header___element.addEventListener( 'mousemove', on_mouse_move );
header___element.addEventListener( 'touchmove', on_touch_move );


function on_mouse_move ( event ) {

	var x = event.clientX;
	var y = event.clientY;

	worldYAngle = -( .5 - ( x / window.innerWidth ) ) * 10;
	worldXAngle = ( .5 - ( y / window.innerHeight ) ) * 5;
	updateView();
	event.preventDefault();

}


function on_touch_move ( event ) {

	var x = event.touches[ 0 ].clientX;
	var y = event.touches[ 0 ].clientY;

	worldYAngle = -( .5 - ( x / window.innerWidth ) ) * 15;
	worldXAngle = ( .5 - ( y / window.innerHeight ) ) * 10;
	updateView();
	//event.preventDefault();

}


/* Disabled */
function onContainerMouseWheel( event ) {

	event = event ? event : window.event;
	d = d - ( event.detail ? event.detail * -5 : event.wheelDelta / 8 );
	updateView();
	event.preventDefault();

}


/*
  Clears the DOM of previous clouds bases
  and generates a new set of cloud bases
*/
function generate() {

	objects = [];

	if ( world.hasChildNodes() ) {
		while ( world.childNodes.length >= 1 ) {
			world.removeChild( world.firstChild );
		}
	}

	for( var j = 0; j < 5; j++ ) {
		objects.push( createCloud() );
	}

}


/*
  Changes the transform property of world to be
  translated in the Z axis by d pixels,
  rotated in the X axis by worldXAngle degrees and
  rotated in the Y axis by worldYAngle degrees.
*/
function updateView() {
	var t = 'translateZ( ' + d + 'px ) rotateX( ' + worldXAngle + 'deg) rotateY( ' + worldYAngle + 'deg)';
	world.style.webkitTransform = t;
	world.style.MozTransform = t;
	world.style.oTransform = t;
	world.style.Transform = t;
}


/*
  Rotates clouds to create "live" effect.
  Iterate layers[], update the rotation and apply the
  inverse transformation currently applied to the world.
  Notice the order in which rotations are applied.
*/
function update (){

	for( var j = 0; j < layers.length; j++ ) {
		var layer = layers[ j ];
		layer.data.a += layer.data.speed;
		var t = 'translateX( ' + layer.data.x + 'px ) translateY( ' + layer.data.y + 'px ) translateZ( ' + layer.data.z + 'px ) rotateY( ' + ( - worldYAngle ) + 'deg ) rotateX( ' + ( - worldXAngle ) + 'deg ) rotateZ( ' + layer.data.a + 'deg ) scale( ' + layer.data.s + ')';
		layer.style.webkitTransform = t;
		layer.style.MozTransform = t;
		layer.style.oTransform = t;
		layer.style.Transform = t;
	}

	requestAnimationFrame( update );

}


update();
