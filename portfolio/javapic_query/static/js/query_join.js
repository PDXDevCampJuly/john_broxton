$(function() {
	var $input = $('input');
	var $label = $('label');  
	var $form = $('#signup');

	window.onload = $input[0].focus(); 

	function checkName() {
		var $this = $(this);
		
		if  ($('input').eq(0).val().length < 5) {
			$('label').eq(0).text('please enter your first and last name');

	 		console.log($('input').eq(0))
	 		$('input').eq(0).focus(); 
	 		
		} else {
			$('label').eq(0).html('<label>welcome, ' + $('input').eq(0).val() + '</label>');
			sessionStorage.setItem('userName', $('input').eq(0).val());	
		} 
	}

	function checkUser() {

		if ($('input').eq(1).val().length < 5) {
			$('label').eq(2).text('please choose a username with at least 5 characters');
	 		$('input').eq(1).focus(); 
		} else {
			$('label').eq(2).html('<label>' + $('input').eq(1).val() + '-- nice</label>');
		}
	}

	function checkEmail() {
		var $email = $("input[type='email']");
		console.log($email);
		var $emailValue = $email.val();
		console.log($emailValue);
		var $eLabel = $("label[for='email']");
		console.log($eLabel);

		if( /(.+)@(.+){2,}\.(.+){2,}/.test($emailValue) ){
			$eLabel.html('<label>welcome thou</label>');

			$("input[type='submit']").focus();	  
		} else {
			$eLabel.text('something seems amiss; please try again');
			$email.focus();  
		}
	}

	$('input').eq(0).on('blur', function() {
		checkName();
	});

	$('input').eq(1).on('blur', function() {
		checkUser();
	});
	
	$("input[type='email']").on('blur', function() {
		checkEmail();
	});
	
	$("form[id='signup']").on('submit', function(e) {
		e.preventDefault();
		window.location.href = 'query_gallery.html';
	});

});










