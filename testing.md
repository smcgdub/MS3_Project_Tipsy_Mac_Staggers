# **Tipsy Mac Staggers** #
![Image of people drinking](assets/images/readme_images/people_drinking.jpg)
>
## **Table of contents** ##

### **1. Automated Testing** ###

* 1.1 HTML Code Validating 
* 1.2 CSS Code Validating 
* 1.3 JavaScript Validating
* 1.4 Python Validating

### **2. Manual Testing** ###

* 2.1 Manual testing desktop
* 2.2 Manual testing mobile

>

### **1. Automated Testing** ###

**1.1 HTML Code Validating**

* All of the HTML files were tested on the [W3C HTML Markup Validation website](https://validator.w3.org/)
* All of the files came back clear with the result of **"Document checking completed. No errors or warnings to show"**

**1.2 CSS Code Validating**

* The main CSS files were tested on the [W3C CSS  Validation website](https://jigsaw.w3.org/css-validator/) 
* All of the files came back clear with the result of **"Congratulations! No Error Found."**

**1.3 JavaScript Code Validating**

The testing for the script.js file was carried out on [JShint.com](https://jshint.com/) The results from the test were as follows:

**1.4 Python Code Validating**

>

### **2. Manual Testing** ###

**2.1 Manual testing desktop**

All desktop testing was carried out on Chrome, FireFox and Safari. 

**1. Navbar**

* Have clicked on the Tipsy's text on the left hand side of the Navbar. Can confirm it brings the user back to the drinks.html landing page.
* Have clicked on each item in the Navbar and can confirm the page then brings to user to that section.
* Can confirm on smaller screen sizes and mobile devices the list items in the Navbar collapse and now appear as a hamburger menu. When pressed the menu expands to show items. 

<!-- **9. Contact Us Form**

* I have used Email JS for this contact us form. When the user sends an email via the website they will receive a pop up notification confirming their message has been sent. 
* I will also receive an email with the users message and details. First name and e-mail address are required fields and the message will not send unless these fields have been populated. 
* The user will also receive an automated email from the site confirming their message has been received and confirms someone will be in contact with them soon.
* I have also added a spell check to the free text message box on the contact us form. 

**Note:** - Once the user message has been submitted via the site, the auto reply can sometimes vary in the speed of the response being sent to the user. Sometimes i have tested it and the response is immediate, other times it may take several minutes to be sent. I have set it so Email JS should send the automated email reply immediately. Any delay is entirely down to Email JS and is out of my control. All of the pages contact us forms use the exact same JS code from the email.js file so there is no error there. Also all of the incoming and outgoing emails in the Email JS dashboard have been set up correctly. 

I am using the free Email JS service and not the paid subscription one so one factor i thought that may be causing this could be the day/time that the email is sent/replied to. At peak times there may be a lot of sites using the service and this could be leading to the delay. 

The incoming message that the site receives from the user is always received straight away. -->

**10. The Footer**

* The footer of each page contains the social media icons and the links to those social media sites. 
* I have tested all of the social media links behind the icons on each page and they all point to the correct social media site relative to the icon. When clicked the social media site will open in a new tab/window 

>

**2.1 Manual testing mobile**

**1. Navbar**

* When viewing on a tablet horizontally the Navbar will display all of the list items the same as a desktop. 
* When held vertically on a tablet the Navbar will display with the hamburger menu in place. 
* On mobile phones whether held horizontally or vertically the Navbar will always appear as a hamburger menu. When pressed the hamburger menu expands to show the list items. 
* Have clicked on the Tipsy's text on the left of the Navbar. Can confirm it brings the user back to the drinks.html landing page.

**9. Contact Us Form**

* The contact us form works exactly the same on mobiles and tablets as it does on desktops. 

**Note:** Please refer to the in the desktop testing section for the functionality notes highlighted. Its not written here to avoid repetition. 

**10. The Footer**

* The footer works exactly the same on mobiles and tablets as it does on desktops.  

>

### **B) The email.js file** ###

This file contains the JavaScript for the Email JS contact us form. 

**TESTING OF THE EMAIL.JS FILE**

The testing for the app.js file was carried out on [JShint.com](https://jshint.com/) The results from the test were as follows:

>

### **D) Console Testing** ###

I have tested each page of the site on the console and upon loading none of the pages are showing errors or warnings. 

>

**5.1 - Contact Us Form**

If the user uses the auto complete function on their device the following error seems to pop up in the console. 

![Image of autofill function error message console results](assets/readme-images/contact-us-error-1.png)

**CAUSE:**

From what ive been able to establish this is being caused when a user uses the auto complete function in their browser to complete the form.

**SOLUTION: ON GOING**

I came across this post from W3 docs [click here](https://www.w3docs.com/snippets/html/how-to-disable-browser-autocomplete-and-autofill-on-html-form-and-input-fields.html) that gave 4 or 5 different solutions you can use to disable autocomplete. I have tried every one of the solutions listed without success.

However i do know that these options do work because as part of the testing i created an input filed at the base of the contact us form to test (Screenshot below)

![Image of autofill function error message console results](assets/readme-images/contact-us-test-field.png)

When i click on this input and start typing the auto complete function doesn't pre populate the form. However, when i click on the first name field in the contact us form the information does auto populate (Screenshot below)

![Image of autofill function error message console results](assets/readme-images/contact-us-error-2.png)

I have also tried to do a hard reset of the browsers, deleted the cache and the issue still persists. I have spoken with the tutors at Code Institute and after looking at solutions and we have narrowed it down to the Email JS contact form that is causing this. All of my code was checked and reviewed and came back with no errors. I have tested the form for thoroughly for functionality and this error doesn't impact the functionality of the page or the email function in anyway for the user. I have marked this down to be looked at in future to try and resolve. 
>

