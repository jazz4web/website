$(function() {
  "use strict";
  let dt = luxon.DateTime.now();
  if ($('.today-field').length) renderTF('.today-field', dt);
  checkPC(860);
});
