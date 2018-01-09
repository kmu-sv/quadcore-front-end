$(document).ready(function () {
    $("#submit").click(function () {
        //collect userName and password entered by users
        var userName = $("#username").val();
        var password = $("#password").val();

        auth(userName, password);
    });
});

function auth(userName, password) {
    $.ajax
        ({
            type: "POST",
            //SEND TO MY SERVER URL
            url: "eomserver",
            dataType: 'json',
            async: false,
            data: '{"userName": "' + userName + '", "password" : "' + password + '"}',
            success: function (response) {
                alert(JSON.stringify(response));
            }
        })
}