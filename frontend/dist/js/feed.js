$(document).ready(function () {

    var common = new Common();
    var info = {
        "firstname" : "SeungWoo",
        "lastname" : "Jeong",
        "username" : "swzoey",
        "email" : "tmddnnim2da@gmail.com",
        "interest" : ["c++", "c", "python"]
    };
    
    var scrollBehaviour = function () {
        if ($window.scrollTop() + $window.height() > $document.height() - 1200) {
            feedToDom(offset);
            offset += 10;
        }
    };

    //  Use objects, arrays, and strings as arguments
    String.prototype.formatUnicorn = String.prototype.formatUnicorn ||
        function () {
            "use strict";
            var str = this.toString();
            if (arguments.length) {
                var t = typeof arguments[0];
                var key;
                var args = ("string" === t || "number" === t) ?
                    Array.prototype.slice.call(arguments) :
                    arguments[0];

                for (key in args) {
                    str = str.replace(new RegExp("\\{" + key + "\\}", "gi"), args[key]);
                }
            }

            return str;
        }

    // Real time feed
    var offset = 10;
    var template_news = "" +
        '<div class="article-wrapper">' +
        '<div class="card z-depth-4 qc-article-card sticky-action">' +
        '<div class="card-content">' +
        '<span class="card-title activator grey-text text-darken-4">{title}' +
        '<i class="material-icons right">more_vert</i>' +
        '</span>' +
        '<span class="qc-article-meta">{published} /' +
        '<a href="{link}" target="_blank">{newspaper}</a>' +
        '</span>' +
        '<hr>' +
        '{thumbnail_wrapper}' +
        '<p class="qc-article-brief">{content}</p>' +
        '</div>' +
        '</div>' +
        '</div>';

    var template_thumbnail = '<div class="card-image waves-effect waves-block waves-light">'
    + '<img class="qc-article-image activator" src="{thumbnail}">'
    + '</div>'
    + '<hr>';

    function feedToDom(offset) {
        $window.off("scroll");
        // Loading circle show
        var $feed_wrapper = $(".feed-wrapper");
        var data = common.fetchFeed(offset, function (data) {
            data.articles.forEach(function (v, i, a) {
                if (v.thumbnail != "") {
                    v.thumbnail_wrapper = template_thumbnail.formatUnicorn(v);
                } else {
                    v.thumbnail_wrapper = "";
                }
                $feed_wrapper.append(template_news.formatUnicorn(v));
            }); 
            $window.on("scroll", scrollBehaviour);
            // Loading circle hide
        });
    }

    $window = $(window);
    $document = $(document);

    //Detect when scrolling is near the bottom
    $window.on("scroll", scrollBehaviour);

    feedToDom(offset);
});