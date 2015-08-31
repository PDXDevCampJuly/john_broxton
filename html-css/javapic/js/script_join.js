var input = document.getElementsByTagName('input');
var label = document.getElementsByTagName('label');  

function checkName() {
	var nameLabel = document.querySelector('label');
	var named = input[0];
	var textName = named.value; 

	if (this.value.length < 5) {
		nameLabel.innerText = 'please enter your first and last name';
 		named.focus(); 
	} else {
		nameLabel.innerHTML = '<label>welcome, ' + textName + '</label>';
	} 
}


function checkUser() {
	var user = input[1];
	var userValue = user.value; 
	var userLabel = label[2];

	if (this.value.length < 5) {
		userLabel.innerHTML = '<label>please choose a username with at least 5 characters</label>';
 		user.focus(); 
	} else {
		userLabel.innerHTML = '<label>' + userValue + '-- good choice</label>';
	}
}


function checkEmail() {
	var email = input[2];
	var emailValue = email.value;
	var eLabel = label[3];


	if( /(.+)@(.+){2,}\.(.+){2,}/.test(emailValue) ){
		eLabel.innerHTML = '<label>welcome thou</label>';
	} else {
		eLabel.innerHTML = '<label>something seems amiss; please try again</label>';
		email.focus();  
	}
}

window.onload = input[0].focus(); 

input[0].addEventListener('blur', checkName, false);
input[1].addEventListener('blur', checkUser, false);
input[2].addEventListener('blur', checkEmail, false);
