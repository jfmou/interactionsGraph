var fs = require('fs');
var parse = require('csv-parse');
var CSVFormater = require('./CSVFormater');

var parser = parse({delimiter: ','}, function(err, data){
  if (!!err) {
    return console.error(err);
  }
  var results = {};

  // init CSVFormater
  CSVFormater = new CSVFormater(data);

  results['nodes'] = _nodesCreator();
  results['links'] = _linksCreator();

  fs.writeFile('./public/data.json', JSON.stringify(results));
});

fs.createReadStream(__dirname+'/data.csv').pipe(parser);

function _nodesCreator() {
  var nodes = [];
  var length = CSVFormater.getSourcesOrderedLength();

  for (var i = 0; i < length; i++) {
    var obj = {};
    obj['id'] = CSVFormater.getTarget(i);
    obj['group'] = Math.floor(Math.random(1,4)).toString();

    nodes.push(obj);
  }

  return nodes;
}

function _linksCreator() {
  var links = [];
  //rows
  for (var sourceIdx = 0; sourceIdx < CSVFormater.sourceData.length; sourceIdx++) {

    // Columns
    for (var targetIdx = 1; targetIdx < CSVFormater.sourceData.length; targetIdx++) {
      if (sourceIdx !== targetIdx) {
        var obj = {};
        var colorHexa = _colorPicker(CSVFormater.getInteractionValueFromIndex(sourceIdx, targetIdx));

        obj['source'] = CSVFormater.getSource(sourceIdx);
        obj['target'] = CSVFormater.getTarget(targetIdx);
        obj['value'] = colorHexa;

        links.push(obj);
      } else {
        continue;
      }
    }
  }

  return links;
}


function _colorPicker (value) {
  var color = '';

  switch(value) {
    case 'OK':
      color = '#00ff00'
      break;

    case 'Moyen':
      color = '#ff9900'
      break;

    case 'Pas d\'interaction':
      color = '#fff'
      break;

    case 'NOK':
      color: '#ff0000'
      break;

    default:
      color: '#f3f3f3'
      break;
  }

  return color;
}
