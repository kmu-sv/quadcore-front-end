String.prototype.formatUnicorn = String.prototype.formatUnicorn ||
function () {
    "use strict";
    var str = this.toString();
    if (arguments.length) {
        var t = typeof arguments[0];
        var key;
        var args = ("string" === t || "number" === t) ?
            Array.prototype.slice.call(arguments)
            : arguments[0];

        for (key in args) {
            str = str.replace(new RegExp("\\{" + key + "\\}", "gi"), args[key]);
        }
    }

    return str;
};

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

  var offset = 10;
  var template_news = ""
    + '<div class="article-wrapper">'
    + '<div class="card z-depth-4 qc-article-card sticky-action">'
    + '<div class="card-content">'
    + '<span class="card-title activator grey-text text-darken-4">{title}'
    + '<i class="material-icons right">more_vert</i>'
    + '</span>'
    + '<span class="qc-article-meta">{published} /'
    + '<a href="{link}" target="_blank">{newspaper}</a>'
    + '</span>'
    + '<hr>'
    + '<p class="qc-article-brief">{content}</p>'
    + '</div>'
    + '</div>'
    + '</div>';

  function feedNews(offset) {
    var $feed_wrapper = $(".feed-wrapper");

    $.ajax({
      method: "GET",
      url: "http://quadcore.news/api/feed?offset=" + offset
    }).done(function (data) {
      data.articles.forEach(function (v, i, a) {
        $feed_wrapper.append(template_news.formatUnicorn(v));
      });
    });
  }

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
        feedNews(offset);
        offset += 10;
      }
    }, _throttleDelay);
  }  

  feedNews(offset);

  $.ajax({
    method: "GET",
    url: "http://quadcore.news/api/user/username"
  }).done(function (data) {
    if (data.result == 0) {
      $("#username").html(data.username);
    } else {
      $("#username").html("Temporary User");
    }
  });
});