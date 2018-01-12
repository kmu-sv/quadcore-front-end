$(document).ready(function () {
    $("#signin").click(function () {
        //collect userName and password entered by users
        var username = $("#username").val();
        var password = $("#password").val();

        auth(userName, password);
    });
});

function auth(userName, password) {
    $.ajax({
        type: "POST",
        //SEND TO MY SERVER URL
        url: "quadcore.news",
        dataType: 'json',
        async: false,
        data: '{"username": "' + username + '", "password" : "' + password + '"}',
        success: function (response) {
            alert(JSON.stringify(response));
        }
    })
}