function reservation_info(status, time) {
    this.status = status;
    this.time = time;
};

function reservation_status(date, reservation_tolerance_minutes){

    function expired(time){
        return new reservation_info("expired", time);
    }

    function valid(time){
        return new reservation_info("valid", time);
    }

    function on_hold(){
        return new reservation_info("on-hold");
    }

    function expired_status(days, hours, minutes) {
        if (days == 1)
            return expired("Ayer".format(days));

        if (days > 0)
            return expired("{0} días".format(days));

        if (hours == 1)
            return expired("{0} hora".format(hours));

        if (hours > 0)
            return expired("{0} hrs".format(hours));

        if (minutes <= reservation_tolerance_minutes)
            return new on_hold();

        return expired("{0} min".format(minutes));
    }

    function valid_status(days, hours, minutes, seconds) {
        if (days == 1)
            return valid("Mañana");

        if (days > 1)
            return valid("{0} días".format(days));

        if (seconds > 0)
            minutes += 1;

        if (minutes > 59)
            hours += 1;

        if (hours == 1)
            return valid("{0} hora".format(hours));

        if (hours > 1)
            return valid("{0} hrs".format(hours));

        if (minutes <= reservation_tolerance_minutes)
            return new on_hold();

        return valid("{0} min".format(minutes));
    }

    function get_lapse_between(initial, final) {

//        console.log("inicial: "+initial);
//        console.log("final: "+final);

        var distance = final - initial;
        var distance_abs = Math.abs(distance);

        var days = Math.floor(distance_abs / (1000.0 * 60.0 * 60.0 * 24.0));
        var hours = Math.floor((distance_abs % (1000.0 * 60.0 * 60.0 * 24.0)) / (1000.0 * 60.0 * 60.0));
        var minutes = Math.floor((distance_abs % (1000.0 * 60.0 * 60.0)) / (1000.0 * 60.0));
        var seconds = Math.floor((distance_abs % (1000.0 * 60.0)) / 1000.0);

        return {
            milliseconds: distance,
            days: days,
            hours: hours,
            minutes: minutes,
            seconds: seconds};
    }

    this.get_lapse = function() {
        var now = new Date().getTime();
        return get_lapse_between(now, date);
    }

    this.get_status = function(lapse){
        if (lapse.milliseconds < 0)
            return expired_status(lapse.days, lapse.hours, lapse.minutes);
        else
            return valid_status(lapse.days, lapse.hours, lapse.minutes, lapse.seconds);
    }
}