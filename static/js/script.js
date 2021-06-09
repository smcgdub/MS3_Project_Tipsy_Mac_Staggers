// AUTOMATICALLY INIT ALL JS WITH FUNCTION BELOW
document.addEventListener('DOMContentLoaded', function () {
  M.AutoInit();
});

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
    setDefaultDate: new Date(01, 01, 2021),
    showClearBtn: true
  });
});

// DRINKS CARD OPEN & CLOSE
$(document).ready(function () {
  $('.collapsible').collapsible();
});

// PAGE HEADERS FADEIN
$(document).ready(function () {
  $('h3.tipsys_drinks').slideDown(1000),
    $('h3.profile_username_h3').slideDown(1000),
    $('h2.register_text').slideDown(1000),
    $('p.register_p').slideDown(1000),
    $('h3.add_drink').slideDown(1000),
    $('ul.drinks_cards').slideDown(1000),
    $('h3.edit_drink').slideDown(1000),
    $('form.edit_drink_form').slideDown(1000),
    $('form.add_drink_form').slideDown(1000),
    $('form.register_page_form').slideDown(1000),
    $('form.login_page_form').slideDown(1000)
});

// CHARACTER COUNTER FOR ADD DRINK PAGE - INGREDIENTS AND INSTRUCTIONS INPUT
$(document).ready(function () {
  $('textarea#drink_ingredients').characterCounter();
  $('textarea#drink_instructions').characterCounter();
});

// OPEN MODAL ON LOAD

$(document).ready(function () {
  $('.modal').modal();
  $('#modal1').modal('open');
  $('#cls').click(function () {
    $('#modal1').modal('close');
  });
});