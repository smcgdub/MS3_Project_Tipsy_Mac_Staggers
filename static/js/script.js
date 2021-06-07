// AUTOMATICALLY INIT ALL JS WITH FUNCTION BELOW
// document.addEventListener('DOMContentLoaded', function () {
//   M.AutoInit();
// });

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

// DRINKS CARD OPEN & CLOSE
$(document).ready(function () {
  $('.collapsible').collapsible();
});

// PAGE HEADERS FADEIN
$(document).ready(function () {
  $('h3.tipsys_drinks').slideDown(1000),
  $('h3.profile_username_h3').slideDown(1000)
  $('h2.register_text').slideDown(1000)
  $('p.register_p').slideDown(1000)
  $('h3.add_drink').slideDown(1000)
});