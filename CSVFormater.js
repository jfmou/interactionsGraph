var CSVFormater = function (data) {
  if (!data) {
    return
  }
  this.rawData = data;
  this.sourceData = data.slice(1, data.length - 6)// remove first and last fifth rows;
  this.targetOrdered = data[0];
  this.targetOrdered.shift();
  this.sourceOrdered = [];
  this.cleanData = this.isolateSourceAndData();


  return this;
};

CSVFormater.prototype.getTargetsOrdered = function () {
 return this.targetOrdered;
};

CSVFormater.prototype.getTarget = function (idx) {
 return this.targetOrdered[idx];
};

CSVFormater.prototype.getSourcesOrderedLength = function () {
  var length = this.getSourcesOrdered().length;
  return length;
};

CSVFormater.prototype.isolateSourceAndData = function () {
  var data = [];

  for (var i = 0; i < this.sourceData.length; i++) {

    this.sourceOrdered.push(this.sourceData[i].shift()); // Source is always on first col of each row

    data.push(this.sourceData[i]);
  }

  return data;
};

CSVFormater.prototype.getSourcesOrdered = function () {

  return this.sourceOrdered;
};

CSVFormater.prototype.getSource = function (idx) {
 return this.getSourcesOrdered()[idx];
};

CSVFormater.prototype._getSourceLength = function () {
  return Array.isArray(this.sourceData) && this.sourceData.length
};

CSVFormater.prototype.getInteractionValueFromIndex = function (sourceIdx, destinationIdx) {

  return this.cleanData[sourceIdx][destinationIdx];
};

module.exports = CSVFormater;
