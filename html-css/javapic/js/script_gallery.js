var gallery = document.getElementById('gallery');
var main = document.querySelector('.gallery_page');
var imageGallery = [];
var imgSrc = [];

function createSrc() {		
		for (var i=1; i < 61; i++){
			if (i < 10) {
				var src = 'images/pdxcg_0' +i+ '.jpg';
			} else {
				var src = 'images/pdxcg_' +i+ '.jpg';
			}
			imgSrc.push(src);
		}		 
}

function populateGallery() {
	for (var i=0; i < imgSrc.length; i++){
		var listItem = document.createElement('li'); 
		var newImg = document.createElement('img');
		newImg.src = imgSrc[i];
		listItem.appendChild(newImg);
		gallery.appendChild(listItem);
	}
}	

function getTarget(e) {
	if (!e) {
		e = window.event;
	}
	return e.target || e.srcElement;
}


function enlargeImg(e) {
	var target = getTarget(e);
	var targetSrc = target.getAttribute('src');
	var imageShow = document.getElementById('image_show');
	var targetImage = imageShow.firstChild;

	targetImage.setAttribute('src', targetSrc);
	imageShow.className = 'display_img';
}

function reduceImg(e) {
	var imageReduce = document.getElementById('image_show'); 
	imageReduce.className = 'display_none';

	if (e.preventDefault) {
		e.preventDefault();
	} else {
		e.returnValue = false;
	}
}

function changeName() {
	var tagline = document.getElementsByClassName('tagline')[0];
	console.log(tagline)
	thing=sessionStorage.getItem('userName');
	tagline.innerText = 'develop something beautiful, ' + thing;
}

createSrc();
populateGallery();
changeName(); 

if (gallery.addEventListener) {
	gallery.addEventListener('click', function(e) {enlargeImg(e);}, false);
} else {
	gallery.attachEvent('onclick', function(e) {enlargeImg(e);});
}

if (main.addEventListener) {
	main.addEventListener('click', function(e) {reduceImg(e);}, true); 
} else {
	main.attachEvent('onclick', function(e) {reduceImg(e);}); 
}
 
