var Common = function () {
    var common = {};
    //Fetch user info from server and return json object
    common.fetchInfo = function (social) {
        $.ajax({
                type: 'GET',
                url: 'http://quadcore.news/api/login/' + social,
            })
            .done(function (data) {
                if (data.result == 0) {
                    return data;
                } else {
                    alert("Fecthing info failed");
                }
            });
    };
    //Fetch news from server and return json object
    common.fetchFeed = function (offset, callback) {
        $.ajax({
            type: 'GET',
            url: 'http://quadcore.news/api/feed?offset=' + offset,
            //offset check
            success: callback
        });
    };

    return common;
};