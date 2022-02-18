function currentTime() {
  var date = new Date(); /* creating object of Date class */
  var year = date.getFullYear(); /* getting current year */
  var month = date.getMonth()+1; /* getting current month */
  var day = date.getDate(); /* getting current date */
  var hour = date.getHours();
  var min = date.getMinutes();
  var sec = date.getSeconds();
  hour = updateTime(hour);
  min = updateTime(min);
  sec = updateTime(sec);
  month = updateTime(month);
  day = updateTime(day);
  document.getElementById("clock").innerText =
    year +
    "/" +
    month +
    "/" +
    day +
    "  " +
    hour +
    ":" +
    min +
    ":" +
    sec; /* adding time to the div */
  var t = setTimeout(function () {
    currentTime();
  }, 1000); /* setting timer */
}

function updateTime(k) {
  if (k < 10) {
    return "0" + k;
  } else {
    return k;
  }
}

currentTime(); /* calling currentTime() function to initiate the process */
