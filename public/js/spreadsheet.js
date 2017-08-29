$('.add-team').click(function () {
  $(this).addClass('hide');
  $('.card-team').removeClass('hide');
});

$('.icon-close').click(function () {
  $('.card-team').addClass('hide');
  $('.add-team').removeClass('hide');
});

$(".container").on("click", ".delete-team", function () {
  $(this).parent().remove();
  if ($('ul.teams li').length < 2) {
    $("#next").addClass('hide');
  }

  return false;
});

$('.textarea-card-team').keypress(function (e) {
  if (e.which == 13 && !e.shiftKey) {
    $('#add-team-action').click();
    e.preventDefault();
    return false;
  }
});

$('#add-team-action').click(function () {
  var team = $('.textarea-card-team').val();
  $('ul.teams').append(
    $('<li>').attr('rel', team).append(
      team,
      $('<a>').attr('href', '#').attr('class', 'delete-team').append("x")
    )
  );
  if ($('ul.teams li').length > 1) {
    $('#next').removeClass('hide');
  }
  $('.textarea-card-team').val('');
});

$('#next').click(function () {
  var teams = {};
  $('ul.teams li').each(function(index) {
    teams[index] = $(this).attr('rel');
  });
  localStorage.setItem('teams', JSON.stringify(teams));
});