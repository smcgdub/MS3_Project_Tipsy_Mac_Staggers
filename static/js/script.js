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
    $('div.shop_div').slideDown(1000)
  $('div.welcome_back_col').slideDown(1000)
});

// CHARACTER COUNTER FOR ADD DRINK PAGE - INGREDIENTS AND INSTRUCTIONS INPUT
$(document).ready(function () {
  $('textarea#drink_ingredients').characterCounter();
  $('textarea#drink_instructions').characterCounter();
});


// function scrollToTop() {
//   window.scrollTo(0, 0);
// }


// PHOTO UPLOADER WIDGET
// var myWidget = cloudinary.createUploadWidget({
//   cloudName: 'my_cloud_name',
//   uploadPreset: 'my_preset'
// }, (error, result) => {
//   if (!error && result && result.event === "success") {
//     console.log('Done! Here is the image info: ', result.info);
//   }
// })

// document.getElementById("upload_widget").addEventListener("click", function () {
//   myWidget.open();
// }, false);


// cloudinary callback. Sets upload image url input
// function imageUploaded(error, result) {
//   $( '<preview img tag>' ).prop("src", result[0].secure_url);
//   $( '<hidden form input>' ).val(result[0].secure_url);
// }
// // Shows the cloudinary image upload widget
// $( <image upload button> ).click(function(event) {
//   event.preventDefault();
//   cloudinary.openUploadWidget(
//     {
//       cloud_name: '<your cloud name here>',
//       upload_preset: '<your preset here>'
//     },
//     imageUploaded);
// });