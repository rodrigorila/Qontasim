/// This class holds the Date-DueDate pairs of cells of a table
function ReservationsTable(table, date_prefix, due_time_prefix){

    var rows = getTableDataRows(table);

    function getTableDataRows(table) {
        var list = null;

        // Serarches for date_prefixN and due_time_prefixN pairs
        // in a table there will be a maximum of N-rows pairs
        for (var i=0, len=table.rows.length; i<len; i++) {
            var date = document.getElementById("{0}{1}".format(date_prefix, i+1));
            var dueTime = document.getElementById("{0}{1}".format(due_time_prefix, i+1));

            if (date == null || dueTime == null)
                continue;

            console.log("Found:" + i);

            if (list == null)
                list = new Array({Date:date, DueTime: dueTime});
            else
                list.push({Date:date, DueTime: dueTime});
        }

        return list;
    }

    this.count = (rows == null) ? 0 : rows.length;

    this.date = function(index){
        return rows[index].Date;
    }

    this.dueTime = function(index){
        return rows[index].DueTime;
    }
}