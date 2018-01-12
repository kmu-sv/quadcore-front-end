$(document).ready(function () {
    $("#submit").click(function () {
        //collect userName and password entered by users
        var firstname = $("#firstname").val();
        var lastname = $("#lastname").val();
        var username = $("#username").val();
        var password = $("#password").val();
        auth(firstname, lastname, userName, password);
    });
});

function auth(firstname, lastname, userName, password) {
    $.ajax({
        type: "POST",
        //SEND TO MY SERVER URL
        url: "eomserver",
        dataType: 'json',
        async: false,
        data: '{"firstname": "' + firstname + '", "lastname" : "' + lastname + '", "username" : "' + username + '", "password" : "' + password + '"}',
        success: function (response) {
            alert(JSON.stringify(response));
        }
    })
}

