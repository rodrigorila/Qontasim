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

function offset_time_as_string(time_string, hours_offset){

    var date_time_string = new Date('1970-01-01T' + time_string + 'Z');

    var ms = Date.parse(date_time_string);

    if (isNaN(ms))
        return; // returns undefined!

    var d = new Date(ms);

    d.setHours(d.getHours() + hours_offset);

    return d.toTimeString();
};

function is_valid_date(date_string){
    var ms = Date.parse(date_string);
    return !isNaN(ms)
};

