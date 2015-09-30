var input = document.getElementsByTagName('input');
var label = document.getElementsByTagName('label');  
var form = document.getElementById('signup');

window.onload = input[0].focus(); 

function checkName() {
	var nameLabel = document.querySelector('label');
	
	var textName = input[0].value; 

	if (this.value.length < 5) {
		nameLabel.innerText = 'please enter your first and last name';
 		input[0].focus(); 
 		
	} else {
		nameLabel.innerHTML = '<label>welcome, ' + textName + '</label>';
		sessionStorage.setItem('userName', input[0].value);	
	} 
}

function checkUser() {
	var user = input[1];
	var userValue = user.value; 
	var userLabel = document.querySelector('label').nextSibling.nextSibling.nextSibling.nextSibling;

	if (this.value.length < 5) {
		userLabel.innerText = 'please choose a username with at least 5 characters';
 		user.focus(); 
	} else {
		userLabel.innerHTML = '<label>' + userValue + '-- good choice</label>';
	}
}

function checkEmail() {
	var email = input[2];
	var emailValue = email.value;
	var eLabel = document.querySelector('label').nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling;

	if( /(.+)@(.+){2,}\.(.+){2,}/.test(emailValue) ){
		eLabel.innerHTML = '<label>welcome thou</label>';

		// submit.focus();		  
	} else {
		eLabel.innerText = 'something seems amiss; please try again';
		email.focus();  
	}
}


function toGallery(e) {
	e.preventDefault();
	window.location.href = 'gallery.html';			 
}

input[0].addEventListener('blur', checkName, false);
input[1].addEventListener('blur', checkUser, false);
input[2].addEventListener('blur', checkEmail, false);
form.addEventListener('submit', toGallery, false);








