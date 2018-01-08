$(document).ready(function () {
  $(".modal").modal();

  $("#edit-interests").click(function (e) {
    e.preventDefault();
    $("#modal-edit-interests").modal("open");
  });

  $('.chips').material_chip();
  $('.chips-initial').material_chip({
    data: [{
      tag: 'C++',
    }, {
      tag: 'Python',
    }, {
      tag: 'Google',
    }, {
      tag: 'Machine Learning'
    }],
  });
  $('.chips-placeholder').material_chip({
    placeholder: 'Enter your interest',
    secondaryPlaceholder: '+Tag',
  });
  $('.chips-autocomplete').material_chip({
    autocompleteOptions: {
      data: {
        'Apple': null,
        'Microsoft': null,
        'Google': null,
        'C++': null,
        'Python': null,
        'Machine Learning': null,
      },
      limit: Infinity,
      minLength: 1
    }
  });
});