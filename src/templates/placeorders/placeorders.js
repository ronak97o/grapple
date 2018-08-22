function initMap() {
	/****** Change latitude and longitude here ******/
	var myLatlng = new google.maps.LatLng(37.422021, -122.084079);

	/****** Map Options *******/
	var mapOptions = {
		zoom: 14,
		center: myLatlng
	};

	var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	/****** Info Window Contents *******/
	var contentString = '<div id="content">'+
		'<div id="siteNotice">'+
		'</div>'+
		'<h1 id="firstHeading" class="firstHeading">Googleplex</h1>'+
		'<div id="bodyContent">'+ '<div style="float:left; width:20%;"><img src="image.jpg" width="120" height="80"/></div>' +
		'<div style="float:right; width:80%;margin-top: -19px;"><p>The <b>Googleplex</b> is the corporate headquarters complex of <b>Google, Inc.</b>, located at <b>Googleplex, 1600 Amphitheatre Pkwy, Mountain View, CA 94043, United States</b>. <br/>' +
		'The original complex with 2 million square feet of office space is the company\'s second largest square footage '+
		'assemblage of Google buildings (The largest Google building is the 2.9 million square foot building in New York City '+
		'which Google bought in 2010) '+
		'<p>Attribution: Googleplex, <a href="http://en.wikipedia.org/wiki/Googleplex">'+
		'http://en.wikipedia.org/wiki/Googleplex</a> '+
		'.</p></div>'+
		'</div>'+
		'</div>';

	var infowindow = new google.maps.InfoWindow({
		content: contentString
	});

	/****** Map Marker Options *******/
	var marker = new google.maps.Marker({
		position: myLatlng,
		map: map,
		title: 'Googleplex (CodexWorld)'
	});

	/****** Info Window With Click *******/
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map,marker);
	});

	/****** Info Window Without Click *******/
	infowindow.open(map,marker);
}