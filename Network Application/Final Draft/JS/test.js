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