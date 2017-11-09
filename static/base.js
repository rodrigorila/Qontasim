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

    var date_time_string = '1970-01-01T{0}Z'.format(time_string);

    var ms = Date.parse(date_time_string);

    if (isNaN(ms))
        return; // returns undefined!

    var d = new Date(ms);

    d.setHours(d.getHours() + hours_offset);

    return d.toTimeString();
};

function datetime_strings(){

    var d = new Date();

    this.time = function() {
        return "{0}:{1}".format(d.getHours(), d.getMinutes());
    };

    this.year = function() {
        return "{0}".format(d.getFullYear());
    };

    this.day = function() {
        switch(d.getDay()){
            case 0: return "Domingo {0}".format(d.getDate());
            case 1: return "Lunes {0}".format(d.getDate());
            case 2: return "Martes {0}".format(d.getDate());
            case 3: return "Miércoles {0}".format(d.getDate());
            case 4: return "Jueves {0}".format(d.getDate());
            case 5: return "Viernes {0}".format(d.getDate());
            case 6: return "Sábado {0}".format(d.getDate());
        }

        return; //returns undefined
    };

    this.month = function() {
        switch(d.getMonth()){
            case 0: return "Enero {0}".format(d.getFullYear());
            case 1: return "Febrero {0}".format(d.getFullYear());
            case 2: return "Marzo {0}".format(d.getFullYear());
            case 3: return "Abril {0}".format(d.getFullYear());
            case 4: return "Mayo {0}".format(d.getFullYear());
            case 5: return "Junio {0}".format(d.getFullYear());
            case 6: return "Julio {0}".format(d.getFullYear());
            case 7: return "Agosto {0}".format(d.getFullYear());
            case 8: return "Septiembre {0}".format(d.getFullYear());
            case 9: return "Octubre {0}".format(d.getFullYear());
            case 10: return "Noviembre {0}".format(d.getFullYear());
            case 11: return "Diciembre {0}".format(d.getFullYear());
        };

        return; //returns undefined
    }
}

function is_valid_date(date_string){
    var ms = Date.parse(date_string);
    return !isNaN(ms)
};

