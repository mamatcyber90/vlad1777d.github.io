var colors = new Array(
  [84,118,155],  // по умолчанию темный голубой
  [100,120,130],  // темный почти серый
  [100,120,130],  // темный почти серый
  [100,100,130],  // темный почти синий\фиолетовый
  [95,110,82],  // темно лаймовый
  [203, 199, 80]);  // темно серый

var step = 0;
//color table indices for:
// current color left
// next color left
// current color right
// next color right
var colorIndices = [0,1,2,3];

//transition speed
var gradientSpeed = 0.02;

function updateGradient() {
	//if ( $===undefined ) return;

	var c0_0 = colors[colorIndices[0]];
	var c0_1 = colors[colorIndices[1]];
	var c1_0 = colors[colorIndices[2]];
	var c1_1 = colors[colorIndices[3]];

	var istep = 1 - step;
	var r1 = Math.round(istep * c0_0[0] + step * c0_1[0]);
	var g1 = Math.round(istep * c0_0[1] + step * c0_1[1]);
	var b1 = Math.round(istep * c0_0[2] + step * c0_1[2]);
	var color1 = "rgb("+r1+","+g1+","+b1+")";

	var r2 = Math.round(istep * c1_0[0] + step * c1_1[0]);
	var g2 = Math.round(istep * c1_0[1] + step * c1_1[1]);
	var b2 = Math.round(istep * c1_0[2] + step * c1_1[2]);
	var color2 = "rgb("+r2+","+g2+","+b2+")";

	//$('.changeable_background_gradient').css({
	//	'background-image': "-webkit-gradient(linear, left bottom, right top, from('rgb(50, 50, 50)'), to("+color1+"))"}).css({
	//	'background-image': "linear-gradient(to top right, rgb(50, 50, 50) 0%,  "+color1+" 70%)"});
	document.getElementById("changeable_background_gradient").style['background-image'] = "-webkit-gradient(linear, left bottom, right top, from('rgb(50, 50, 50)'), to("+color1+"))";
	document.getElementById("changeable_background_gradient").style['background-image'] = "linear-gradient(to top right, rgb(50, 50, 50) 0%,  "+color1+" 70%)"

	step += gradientSpeed;
	if ( step >= 1 ) {
		step %= 1;
		colorIndices[0] = colorIndices[1];
		colorIndices[2] = colorIndices[3];

		//pick two new target color indices
		//do not pick the same as the current one
		colorIndices[1] = ( colorIndices[1] + Math.floor( 1 + Math.random() * (colors.length - 1))) % colors.length;
		colorIndices[3] = ( colorIndices[3] + Math.floor( 1 + Math.random() * (colors.length - 1))) % colors.length;
  }
}

setInterval(updateGradient, 100);
