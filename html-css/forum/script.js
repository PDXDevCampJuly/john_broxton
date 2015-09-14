
var url = 'https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script';

$('#message').on('submit', function(e) {
	e.preventDefault();
	var titleText = $('#title').val(); 
	var msgText = $('#body').val(); 
	var $formData = {"entry_434124687": titleText, "entry_1823097801": msgText};
	$.post('https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse',
		$formData, function(){
			console.log('success');
		}).always( function() {
			window.location.reload(true);
		});	
});

$.ajax({
	type: 'GET',
	url: url,
	async: true,
	contentType: "application/json",
	dataType: 'jsonp',
	success: function(data) {
		var $forum = $('#forum');
		var newContent = "";
		var entryList = data.feed.entry;
		entryList.reverse(); 
		for (var i = 0; entryList.length; i++) {
		   titleText = entryList[i].gsx$posttitle.$t;
		   msgText = entryList[i].gsx$postbody.$t;
		   newContent += '<div id="titlePost">';
		   newContent += titleText+'</div>';
		   newContent += '<div id="msgPost">' + msgText +'</br></br>';
		   newContent += '</div>';

		   $forum.html(newContent); 
		}
		
	}
});

//hidden header function found here: http://jsfiddle.net/mariusc23/s6mLJ/31/

var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('header').outerHeight();

$(window).scroll(function(event){
  didScroll = true;
});
// run hasScrolled() and reset didScroll status
setInterval(function() {
  if (didScroll) {
    hasScrolled();
    didScroll = false;
  }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();
    
    // Make sure they scroll more than delta
    if(Math.abs(lastScrollTop - st) <= delta)
        return;
    
    // If they scrolled down and are past the navbar, add class .nav-up.
    // This is necessary so you never see what is "behind" the navbar.
    if (st > lastScrollTop && st > navbarHeight){
        // Scroll Down
        $('header').removeClass('nav-down').addClass('nav-up');
    } else {
        // Scroll Up
        if(st + $(window).height() < $(document).height()) {
            $('header').removeClass('nav-up').addClass('nav-down');
        }
    }
    
    lastScrollTop = st;
}
