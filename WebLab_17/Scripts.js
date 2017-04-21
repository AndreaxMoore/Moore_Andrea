function drag() {
    cat = document.getElementById("cat");
    leftbox = document.getElementById("leftBox");

    cat.addEventListener("dragstart", startDrag, false);
    cat.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);

}

function startDrag(e) {
    var pic = '<img id = "cat" src = "https://s-media-cache-ak0.pinimg.com/736x/72/38/00/723800cf0bf6b9d52a78908ef3a73634.jpg">';
    e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e){
    e.preventDefault();
    leftbox.style.background = "pink";
    leftbox.style.border = "3px solid red";
}

function dragLeave(e){
    e.preventDefault();
    leftbox.style.background = "white"
    leftbox.style.border = "3px solid purple";
}

function drop(e){
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e){
    pic = e.target
    pic.style.visibility = "hidden";
}
    window.addEventListener("load", drag, false);
