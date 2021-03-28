var unirest = require("unirest");

var name = "iphone12" + " " + "price";
var numResult = "4";

var req = unirest("GET", "https://google-search3.p.rapidapi.com/api/v1/search/q=" + name + "&num=" + numResult + "&lr=lang_en");

req.headers({
	"x-rapidapi-key": "6702144403msha01bc39f5b65ee2p1d17aejsn39dbb6fb0748",
	"x-rapidapi-host": "google-search3.p.rapidapi.com",
	"useQueryString": true
});


req.end(function (res) {
	if (res.error) throw new Error(res.error);

	console.log(res.body);
});