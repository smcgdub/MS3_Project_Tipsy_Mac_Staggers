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

// PAGE HEADERS FADE IN
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
    $('form.login_page_form').slideDown(1000),
    $('form.search_bar').slideDown(1000),
    $('div.shop_div').slideDown(1000),
    $('p.all_inputs_p').slideDown(1000),
    $('p.occasion-p').slideDown(1000),
    $('h4.all_drinks_h4').slideDown(1000),
    $('div.welcome_back_col').slideDown(1000);
});

// CHARACTER COUNTER FOR ADD DRINK PAGE - INGREDIENTS AND INSTRUCTIONS INPUT
$(document).ready(function () {
  $('textarea#drink_ingredients').characterCounter();
  $('textarea#drink_instructions').characterCounter();
});

// VALIDATOR FOR SELECT INPUTS
// CODE WAS FOUND ON GITHUB HERE: https://github.com/Dogfalo/materialize/issues/1861#issuecomment-275121774
$(document).ready(function () {
  $('select[required]').css({
    display: 'inline',
    position: 'absolute',
    float: 'center',
    padding: 0,
    margin: 0,
    border: '1px solid rgba(255,255,255,0)',
    height: 0,
    width: 0,
    top: '2em',
    left: '3em'
  });
});


// $('select[required]').css({
//   display: 'inline',
//   position: 'absolute',
//   float: 'center',
//   padding: 0,
//   margin: 0,
//   border: '1px solid rgba(255,255,255,0)',
//   height: 0, 
//   width: 0,
//   top: '2em',
//   left: '3em'
// });