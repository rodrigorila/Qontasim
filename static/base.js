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

function offset_date_from_today_as_string(days_from_today){
    var d = new Date();

    d.setDate(d.getDate() + days_from_today);

    return d.toDateString();
};

function offset_date_as_string(date_string, days_offset){
    var ms = Date.parse(date_string);

    if (isNaN(ms))
        return; // returns undefined!

    var d = new Date(ms);

    d.setDate(d.getDate() + days_offset);

    return d.toDateString();
};

function is_valid_date(date_string){
    var ms = Date.parse(date_string);
    return !isNaN(ms)
};

