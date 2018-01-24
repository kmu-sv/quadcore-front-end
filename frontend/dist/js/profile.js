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

function auth(firstname, lastname, email, interest) {
    $.ajax({
        type: "POST",
        //SEND TO MY SERVER URL
        url: "eomserver",
        dataType: 'json',
        async: false,
        data: {
            "firstname": firstname, 
            "lastname" : lastname, 
            "email" : email, 
            "interest" : interest
        },
        success: function (response) {
            alert(JSON.stringify(response));
        }
    })
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#selfie').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}
