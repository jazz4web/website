$(function() {
  "use strict";
  let dt = luxon.DateTime.now();
  $.ajax({
    method: 'GET',
    url: '/api/captcha',
    success: function(data) {
      let form = Mustache.render($('#logint').html(), data);
      $('#mc').append(form);
      if ($('.today-field').length) renderTF('.today-field', dt);
      checkPC(860);
    },
    dataType: 'json'
  });
});
