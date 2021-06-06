// MOBILE SIDE NAV OPEN RIGHT
$(document).ready(function () {
  $('.sidenav').sidenav({
    edge: "right"
  });
});

// DATE OF BIRTH FORMAT ON REGISTER PAGE
var currYear = (new Date()).getFullYear();

$(document).ready(function () {
  $('.datepicker').datepicker({
    format: 'dd mmm yyyy',
    yearRange: [1900, currYear - 0],
    setDefaultDate: new Date(01, 01, 2021)
  });
});

// DRINKS CARD
$(document).ready(function () {
  $('.collapsible').collapsible();
});


// AUTOMATICALLY INIT ALL JS WITH FUNCTION BELOW
// document.addEventListener('DOMContentLoaded', function () {
//   M.AutoInit();
// });