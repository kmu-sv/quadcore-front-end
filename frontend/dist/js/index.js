$(document).ready(function () {

  //Save and modify user's interest
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

  // Real time feed
  var options = [{
      selector: '#staggered-test',
      offset: 500,
      callback: function (el) {
        Materialize.showStaggeredList($(el));
      }
    }, {
      selector: '#image-test',
      offset: 500,
      callback: function (el) {
        Materialize.fadeInImage($(el));
      }
    }];

  Materialize.scrollFire(options);

  // Detect sroll end
  var _throttleTimer = null;
  var _throttleDelay = 100;
  var $window = $(window);
  var $document = $(document);

  $window
          .off('scroll', ScrollHandler)
          .on('scroll', ScrollHandler);

  function ScrollHandler(e) {
      clearTimeout(_throttleTimer);
      _throttleTimer = setTimeout(function () {
          console.log('scroll');
          if ($window.scrollTop() + $window.height() > $document.height() - 100) {
              alert("getting feed!");
          }

      }, _throttleDelay);
    }
  });
