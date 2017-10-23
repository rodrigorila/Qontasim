"use strict";

// String.format
if (!String.prototype.format) { //CHECK IF ALREADY IMPLEMENTED!!!
  String.prototype.format = function() {
      var args = arguments;
      return this.replace(/{(\d+)}/g, function(match, number) {
          return typeof args[number] != 'undefined'
            ? args[number]
            : match;
      });
  };
};

// toInt
function toInt(n){
    return Math.round(Number(n));
};