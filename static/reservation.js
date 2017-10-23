
function Reservation(date){

    function overdue_text(days, hours, minutes) {

        if (days == 1)
            return "Vencida: Ayer".format(days);

        if (days > 0)
            return "Vencida: {0} días".format(days);

        if (hours == 1)
            return "Vencida: {0} hora".format(hours);

        if (hours > 0)
            return "Vencida: {0} horas".format(hours);

        if (minutes < 15)
            return "En espera";

        return "Vencida: {0} minutos".format(minutes);
    }

    function waiting_text(days, hours, minutes, seconds) {
        if (days == 1)
            return "Mañana";

        if (days > 1)
            return "{0} días".format(days);

        if (seconds > 0)
            minutes += 1;

        if (minutes > 59)
            hours += 1;

        if (hours == 1)
            return "{0} hora".format(hours);

        if (hours > 1)
            return "{0} horas".format(hours);

        if (minutes < 15)
            return "En espera";

        return "{0} minutos".format(minutes);
    }

    function get_lapse_between(initial, final) {

        var distance = final - initial;
        var distance_abs = Math.abs(distance);

        var days = Math.floor(distance_abs / (1000.0 * 60.0 * 60.0 * 24.0));
        var hours = Math.floor((distance_abs % (1000.0 * 60.0 * 60.0 * 24.0)) / (1000.0 * 60.0 * 60.0));
        var minutes = Math.floor((distance_abs % (1000.0 * 60.0 * 60.0)) / (1000.0 * 60.0));
        var seconds = Math.floor((distance_abs % (1000.0 * 60.0)) / 1000.0);

        return {milliseconds: distance, days: days, hours: hours, minutes: minutes, seconds: seconds};
    }

    this.get_lapse = function() {
        var now = new Date().getTime();
        return get_lapse_between(now, date);
    }

    this.get_status = function(lapse){
        if (lapse.milliseconds < 0)
            return overdue_text(lapse.days, lapse.hours, lapse.minutes);
        else
            return waiting_text(lapse.days, lapse.hours, lapse.minutes, lapse.seconds);
    }
}