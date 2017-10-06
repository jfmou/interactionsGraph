'use strict';

// Get data through XHR
$.getJSON('data.json').done(function(data) {
  var redTeamsData = _getTeamsByColor(data, '#ff0000'),
      orangeTeamsData = _getTeamsByColor(data, '#ff9900');

  _renderTable('#red-teams', 'Red interactions', redTeamsData);
  _renderTable('#orange-teams', 'Orange interactions', orangeTeamsData);
});

// Get an array of teams from data with a specified color of interaction
function _getTeamsByColor(data, color) {
  var results = [];

  data.links.forEach(function(link, idx) {
    if (link.value === color) {
      results.push(link);
    }
  });

  return results;
}

// Generic helping function to build an html table
function _renderTable(container, title, items) {
  var $container = $(container);

  var html = '<h1>' + title + '</h1><table class="striped"><thead><tr><th>Source</th><th>Destination</th></tr></thead><tbody>';

  items.forEach(function(item, idx) {
    html += '<tr><td>' + item.source + '</td><td>' + item.target + '</td></tr>';
  });

  html += '</tbody></table>';

  $container.append(html);
}
