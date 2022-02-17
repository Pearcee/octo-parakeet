// getText("fetch_info.txt");
const x = document.getElementById("demo");

function myFunction() {
  var x = document.getElementById("demo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}

console.log("about to fetch a poem");
// catchPoem()
//   .then(poem => {
//     document.getElementById('poem').innerText = poem;
//     console.log('yay');
//   })
//   .catch(error => {
//     console.log('error!');
//     console.error(error);
//   });

async function catchPoem() {
  const response = await fetch("poem.txt");
  return await response.text();
}
// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}

// Toggle between showing and hiding the sidebar when clicking the menu icon
var mySidebar = document.getElementById("mySidebar");

function w3_open() {
  if (mySidebar.style.display === "block") {
    mySidebar.style.display = "none";
  } else {
    mySidebar.style.display = "block";
  }
}

// Close the sidebar with the close button
function w3_close() {
  mySidebar.style.display = "none";
}

// async function getText(file) {
//   let x = await fetch(file);
//   let y = await x.text();
//   document.getElementById("demo").innerHTML = y;
// }

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML =
    "Latitude: " +
    position.coords.latitude +
    "<br>Longitude: " +
    position.coords.longitude;
}
