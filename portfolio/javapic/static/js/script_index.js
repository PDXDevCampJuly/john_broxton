window.onload = function() {	
	var jumbo = document.getElementById('jumbotron');
	var i = 0; 
	var img = ["01", "05", "10", "12", "21", "26", "32", "33", "39", "49", "54"];
	var interval = 20000;

	function slideShow() {
		jumbo.style.backgroundImage = "url('../static/images/pdxcg_" + img[i++%img.length] + ".jpg')";
	}

	setInterval(slideShow, interval)
}


