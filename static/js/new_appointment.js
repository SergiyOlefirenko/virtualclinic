$.datetimepicker.setDateFormatter({
    parseDate: function(date, format){
        var d = moment(date, format);
        return d.isValid() ? d.toDate() : false;
    },
    formatDate: function(date, format){
        return moment(date).format(format);
    },
});

jQuery.datetimepicker.setLocale('ua');

jQuery('#start_date_picker').datetimepicker({
     format:"YYYY-MM-DD HH:mm",
     allowTimes:[
        '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
        '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
        '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00'
     ]
});

jQuery('#end_date_picker').datetimepicker({
     format:"YYYY-MM-DD HH:mm",
     allowTimes:[
        '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
        '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
        '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00'
     ]
});