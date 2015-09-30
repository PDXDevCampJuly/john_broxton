$(function() {

	var img =  ["url('../static/images/pdxcg_01.jpg')",
				"url('../static/images/pdxcg_10.jpg')",
				"url('../static/images/pdxcg_12.jpg')",
				"url('../static/images/pdxcg_21.jpg')",
				"url('../static/images/pdxcg_26.jpg')",
				"url('../static/images/pdxcg_28.jpg')",
				"url('../static/images/pdxcg_33.jpg')",
				"url('../static/images/pdxcg_35.jpg')",
				"url('../static/images/pdxcg_49.jpg')",
				"url('../static/images/pdxcg_50.jpg')",];

	var i = 0; 	
	
	setInterval(function() { 
	  	$('#jumbotron')
	    .css('background-image', img[i++%img.length])
	},  3000);


});




