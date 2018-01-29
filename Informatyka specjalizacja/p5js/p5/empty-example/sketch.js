function setup() {
  // put setup code here
    createCanvas(10000, 10000);
}

// function draw() {
//   // put drawing code here
//   stroke('#fae');
//   strokeWeight(4);
//   fill(255, 0, 0);
//   ellipse(50, 50, 80, 80);
//   fill(0, 255, 0);
//   ellipse(100, 100, 200, 80);
//   fill(0, 0, 255);
//   rect(30, 22, 55, 55);
//
//   stroke('#0040FF');
//   strokeWeight(7);
//   fill(255, 0, 0);
//   ellipse(250, 250, 160, 160);
//
//   stroke('#FF803E');
//   strokeWeight(7);
//   fill(255, 0, 0);
//   rect(500, 400, 160, 160);
//
//   stroke('#FF803E');
//   strokeWeight(7);
//   fill(255, 0, 0);
//   rect(800, 400, 160, 160);


// strokeWeight('20');
// stroke('green');
function draw(){

  r = random(255);
  g = random(255);
  b = random(255);
noFill();
noStroke();

if (mouseIsPressed) {


if (mouseButton === LEFT){
  strokeWeight(20);
  stroke(r, g, b);
  fill(r, g ,b, 127)

}

if (mouseButton === CENTER){
strokeweight(20);
fill(255, 255, 255);
stroke(255, 255, 255);

}
} else {
  noFill();
  noStroke();

}
point(mouseX, mouseY)

}
//
//     fill('green');
//   } else {
//     fill('red');
//   }
//   point(mouseX, mouseY);
// }
