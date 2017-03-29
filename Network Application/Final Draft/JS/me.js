function reveal() {
    document.getElementById("items").style.visibility = "visible";
  }
  function hide() {
    document.getElementById("items").style.visibility = "hidden";
  }
  
  function reveal1() {
    document.getElementById("items1").style.visibility = "visible";
  }
  function hide1() {
    document.getElementById("items1").style.visibility = "hidden";
  }
  
  function reveal2() {
    document.getElementById("items2").style.visibility = "visible";
  }
  function hide2() {
    document.getElementById("items2").style.visibility = "hidden";
  }
  
  function reveal3() {
    document.getElementById("items3").style.visibility = "visible";
  }
  function hide3() {
    document.getElementById("items3").style.visibility = "hidden";
  }
  
    function reveal4() {
    document.getElementById("items4").style.visibility = "visible";
  }
  function hide4() {
    document.getElementById("items4").style.visibility = "hidden";
  }
function be(){
	$( "#push" ).css({
    borderStyle: "inset",
    cursor: "wait"
  });
    $( "#test" ).slideDown( 1000, function() {
    $( this )
      .css( "border", "2px red inset" )
      .filter( ".middle" )
        .css( "background", "yellow" )
        .focus();
    $( "#tes" ).css( "visibility", "hidden" );
  });

		
	}
 
    var num1 = document.getElementById("num1");
    var num2 = document.getElementById("num2");
    num1.innerHTML = Math.floor(Math.random()*10+1);
    num2.innerHTML = Math.floor(Math.random()*10+1);

function checkMath() {
    var num1 = parseInt(document.getElementById("num1").innerHTML, 10);
    var num2 = parseInt(document.getElementById("num2").innerHTML, 10);
    var answer = parseInt(document.getElementById("answer").value, 10);
    if (answer === num1 + num2) {
         $("#check1").html("Correct answer");
    } else {
        $("#check1").html("Incorrect answer");
    }
    randomNum();
}   
function be(){
	$( "#push" ).css({
    borderStyle: "inset",
    cursor: "wait"
  });
    $( "#test" ).slideDown( 1000, function() {
    $( this )
      .css( "border", "2px red inset" )
      .filter( ".middle" )
        .css( "background", "yellow" )
        .focus();
    $( "#tes" ).css( "visibility", "hidden" );
  });
  $( "#tes" ).hide();

		
	}
 
    var num1 = document.getElementById("num1");
    var num2 = document.getElementById("num2");
    num1.innerHTML = Math.floor(Math.random()*10+1);
    num2.innerHTML = Math.floor(Math.random()*10+1);

function checkMath() {
    var num1 = parseInt(document.getElementById("num1").innerHTML, 10);
    var num2 = parseInt(document.getElementById("num2").innerHTML, 10);
    var answer = parseInt(document.getElementById("answer").value, 10);
    if (answer === num1 + num2) {
         $("#check1").html("Correct answer");
    } else {
        $("#check1").html("Incorrect answer");
    }
    randomNum();
}   
   
   
function checkPasswordMatch() {
    var password = $("#pass").val();
    var confirmPassword = $("#conf").val();

    if (password != confirmPassword)
        $("#check").html("Passwords do not match!");
    else
        $("#check").html("Passwords match.");
}

$(document).ready(function () {
   $("#conf").keyup(checkPasswordMatch);
});

function check(form){
	var me = $("#userid").val();
 /*the following code checkes whether the entered userid and password are matching*/

  	if( form.pswrd.value == "1234"){
        window.open('server.php?username='+ me);
         window.location.assign('chat.xhtml?username='+ me);
  } else
  {
   alert("Error Password")/*displays error message*/
  }
}
   
   
function checkPasswordMatch() {
    var password = $("#pass").val();
    var confirmPassword = $("#conf").val();

    if (password != confirmPassword)
        $("#check").html("Passwords do not match!");
    else
        $("#check").html("Passwords match.");
}

$(document).ready(function () {
   $("#conf").keyup(checkPasswordMatch);
});

function check(form){
	var me = $("#userid").val();
 /*the following code checkes whether the entered userid and password are matching*/

  	if( form.pswrd.value == "1234"){
        window.open('server.php?username='+ me);
         window.location.assign('chat.xhtml?username='+ me);
  } else
  {
   alert("Error Password")/*displays error message*/
  }
}