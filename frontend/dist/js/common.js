var Common = function () {
    var common = {};
    //Fetch user info from server and return json object
    common.fetchInfo = function () {
        $.ajax({
            type: 'GET',
            url: '',
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
            url: 'http://quadcore.news/api/feed?offset='+ offset,
            success: callback
        });
    };

    /*Make alert 
    var makeAlert = function (message, theme) {
        $.ajax({
                type: 'GET',
                url: '',
            })
            .done(function (data) {
                if (message == data.message) {
                    return theme;
                }
            })
    };*/

    return common;
};