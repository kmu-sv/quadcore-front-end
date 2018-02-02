$(document).ready(function () {

    //var common = new Common();
    var checkUsername = 0;
    var info = {
        "firstname" : "SeungWoo",
        "lastname" : "Jeong",
        "username" : "swzoey",
        "email" : "tmddnnim2da@gmail.com",
        "interest" : ["c++", "c", "python"]
    };
    //Set profile from social
    function setProfile() {
        $('#firstname').attr('value', info.firstname);
        $('#lastname').attr('value', info.lastname);
        $('#profile-username').attr('value', info.username);
        $('#username').text(info.username);
        $('#email').attr('value', info.email);

    }

    // Edit profile
    function editProfile() {
        var interest = info.interest.map(function (data) {
            return {
                tag: data
            }
        });

        $(".modal").modal();
        $("#edit-profile").click(function (e) {
            e.preventDefault();
            $("#modal-edit-profile").modal("open");
        });

        $('.chips').material_chip();

        $('.chips-initial').material_chip({ 
            data: interest
        });
        return 
    }

    // Save modification of profile
    function saveProfile() {
        $("#save").click(function () {
            if (checkUsername() == 0) {
                $.ajax({
                    type: 'POST',
                    //url: 'http://quadcore.news/api/register',
                    dataType: 'json',
                    data: {
                        'fisrtname': $('#fisrtname').val(),
                        'lastname': $('#lastname').val(),
                        'profile-username': $('profile-username').val(),
                        'email': $('email').val()
                    },
                })
                .done(function () {
                    setProfile();
                });
            } else {
                $('#save').addClass('disabled');
            }
        });
    }

    //check user's name
    function checkUsername() {
        $.ajax({
            type: 'POST',
            url: '', //where
            data: "profile-username=" + $(this).attr("value"),
            success: function (data) {
                if (data.result != 0) {
                    $("#username-check").text("Your username is already exist");
                } else {
                    return 0;
                }
            }
        })
    }


    editProfile();
    saveProfile();
    setProfile();
});
