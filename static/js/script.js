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
    format: 'dd mm, yyyy',
    yearRange: [1900, currYear - 0],
    setDefaultDate: new Date(01,01,2021)
  });
});