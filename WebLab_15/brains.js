function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.strokeStyle = "yellow";

    canvas.beginPath();
    canvas.moveTo(120, 180);
    canvas.lineTo(155, 80);
    canvas.lineTo(180, 175);
    canvas.lineTo(290, 160);
    canvas.lineTo(220, 240);
    canvas.lineTo(330, 260);
    canvas.lineTo(220, 300);
    canvas.lineTo(290, 390);
    canvas.lineTo(190, 350);
    canvas.lineTo(150, 440);
    canvas.lineTo(110, 350);
    canvas.lineTo(25, 390);
    canvas.lineTo(80, 300);
    canvas.lineTo(1, 270);
    canvas.lineTo(90, 240);
    canvas.lineTo(15, 160);
    canvas.closePath();
    canvas.stroke();

    var g = canvas.createLinearGradient(10, 10, 300, 200);
    g.addColorStop(.7, "white");
    g.addColorStop(1, "yellow");

    canvas.fillStyle = g;
    canvas.fill();

}

window.addEventListener("load", shapes, false);
