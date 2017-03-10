//<<<<<<< HEAD
// Exercise 2.3 Javascript file  //
// Read the instructions.html //

$("html").ready(function(){

//some helpful debug code

$("#javascript_start").html("[OK] Started executing the javascript file");
$("#javascript_end").html("[WAITING]...this far we haven't reached the end... Maybe you should try FireBug?");

// ADD YOUR CODE BETWEEN THESE LINES //

$(".note").attr("class", "note");
$(".test_data").attr("class", "test_data");
$("[href]").attr("class", "external");
$("[href$='.zip']").attr("class", "download");
$("[href$='.xyz']").attr("class", "download");
$("[href$='.doc']").attr("class", "download");
$("[href$='.pdf']").attr("class", "pdf");





// ADD YOUR CODE BETWEEN THESE LINES //

//some helpful debug code

$("#javascript_end").html("[OK] The end of your javascript file was reached. (meaning there were no huge errors) Hopefully your code works too! ");
});
/*
=======
// Exercise 2.3 Javascript file  //
// Read the instructions.html //

//some helpful debug code

$("#javascript_start").html("[OK] Started executing the javascript file");
$("#javascript_end").html("[WAITING]...this far we haven't reached the end... Maybe you should try FireBug?");

// ADD YOUR CODE BETWEEN THESE LINES //







// ADD YOUR CODE BETWEEN THESE LINES //

//some helpful debug code

$("#javascript_end").html("[OK] The end of your javascript file was reached. (meaning there were no huge errors) Hopefully your code works too! ");


>>>>>>> 3aed9094bbe10d43aaa10dca51d21eaafc38aa20

*/
