$(function() {
  $(document).on('click', '#getex1', function (event) {
    event.preventDefault();
    $('#ex1').html("request sent...");
    $.ajax({
      url: '/docs/ex1',
      method: 'get'
    }).done(function (response) {
      $('#ex1').html(response)
    })
  });

  $(document).on('click', '#getex2', function (event) {
    event.preventDefault();
    $('#ex2').html("request sent...");
    $.ajax({
      url: '/docs/ex2',
      method: 'get'
    }).done(function (response) {
      $('#ex2').html(response)
    })
  });
});
