$(function() {

	var img =  ["url('images/pdxcg_01.jpg')",
				"url('images/pdxcg_10.jpg')",
				"url('images/pdxcg_12.jpg')",
				"url('images/pdxcg_21.jpg')",
				"url('images/pdxcg_26.jpg')",
				"url('images/pdxcg_32.jpg')",
				"url('images/pdxcg_33.jpg')",
				"url('images/pdxcg_39.jpg')",
				"url('images/pdxcg_49.jpg')",
				"url('images/pdxcg_54.jpg')",]; 

	var i = 0; 	
	
	setInterval(function() { 
	  	$('#jumbotron')
	    .css('background-image', img[i++%img.length])
	},  3000);


});




