var fs = require('fs');
var parse = require('csv-parse');

var parser = parse({delimiter: ',', columns: true}, function(err, data){
  if (!!err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

fs.createReadStream(__dirname+'/data.csv').pipe(parser);
