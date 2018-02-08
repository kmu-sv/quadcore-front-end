$(document).ready(function () {
    var common = new Common();
    var offset = 50;
    //change background image
    var thumbnail = common.fetchFeed(offset, function (data) {
        var index = 0;
        var thumbnails = [];
        var $body = $("body");
        data.articles.forEach(function (v, i, a) {
            if (v.thumbnail != "") {
                thumbnails.push('url(' + v.thumbnail + ')');
                $body.append('<img class="preload" src="' + v.thumbnail + '">');
            }
        });
        setInterval(function () {
            $body.css("background-image", thumbnails[index]);
            index = (index + 1) % 10;
        }, 3000);
    });
});
