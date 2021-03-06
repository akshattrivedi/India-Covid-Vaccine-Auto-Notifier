var configJSON = JSON.parse(config);

(function ($) {
    'use strict';
    /*==================================================================
        [ Daterangepicker ]*/
    try {
        $('.js-datepicker').daterangepicker({
            "singleDatePicker": true,
            "showDropdowns": true,
            "autoUpdateInput": false,
            locale: {
                format: 'DD/MM/YYYY'
            },
        });

        var myCalendar = $('.js-datepicker');
        var isClick = 0;

        $(window).on('click', function () {
            isClick = 0;
        });

        $(myCalendar).on('apply.daterangepicker', function (ev, picker) {
            isClick = 0;
            $(this).val(picker.startDate.format('DD/MM/YYYY'));

        });

        $('.js-btn-calendar').on('click', function (e) {
            e.stopPropagation();

            if (isClick === 1) isClick = 0;
            else if (isClick === 0) isClick = 1;

            if (isClick === 1) {
                myCalendar.focus();
            }
        });

        $(myCalendar).on('click', function (e) {
            e.stopPropagation();
            isClick = 1;
        });

        $('.daterangepicker').on('click', function (e) {
            e.stopPropagation();
        });


    } catch (er) { console.log(er); }
    /*[ Select 2 Config ]
        ===========================================================*/

    try {
        var selectSimple = $('.js-select-simple');

        selectSimple.each(function () {
            var that = $(this);
            var selectBox = that.find('select');
            var selectDropdown = that.find('.select-dropdown');
            selectBox.select2({
                dropdownParent: selectDropdown
            });
        });

    } catch (err) {
        console.log(err);
    }


})(jQuery);

// API Call for Getting All Districts When State is Selected
$(function () {
    $('#state').change(function () {
        $.get("http://localhost:8000/api/getAllDistricts?state=" + $(this).val(), function (data) {
            $('#district').empty()
            for (var i = 0; i < data["districts"].length; i++) {
                $('#district').append($('<option>').text(data["districts"][i]).attr('value', data["districts"][i]));
            }
        });
    });
});



// API Call for Finding Slots Through Find Slots Button
$(document).ready(function () {
    var centersString = $('#hidden-slots').val();

    if (centersString == ""){
        document.getElementById('slots-label').innerHTML = "";
        return;
    }

    
    if (centersString == "[]"){
        document.getElementById('slots-label').innerHTML = "NO SLOTS AVAILABLE!";
        return;
    }

    var centersStringJSON = centersString.replace(/'/g, '"');
    var centers = JSON.parse(centersStringJSON);

    createTabularCenters(centers);
    
});

// API Call for Finding Available Slots Through Auto-Refresh of UI Component
$(function () {
    $('#auto-refresh').click(function () {
        var counter = configJSON.autoRefresh / 1000;
        setInterval(function () {
            counter--;
            if (counter >= 0) {
                document.getElementById('auto-refresh-label').innerHTML = "Auto Refreshing in " + counter + " seconds";
            }
            else {
                $.get('http://localhost:8000/api/getSlots', {
                    state: $('#state').val(),
                    district: $('#district').val(),
                    pincode: $('#pincode').val(),
                    age: $('#age').val(),
                    date: $('#date').val(),
                    vaccineType: $('#vaccineType').val(),
                    dose: $('#dose').val()
                },
                    function (data) {
                        var centers = data["slots"];
                        createTabularCenters(centers);
                    });
                counter = configJSON.autoRefresh / 1000;
                document.getElementById('auto-refresh-label').innerHTML = "Auto Refreshing in " + counter + " seconds";
            }
        }, 1000);
    });
});

function createTabularCenters(centers){
    if(centers[0] == "Input Error!"){
        document.getElementById('slots-label').innerHTML = "Input Error!";
        return;
    }

    if (centers.length > 0) {
        var slotsTable = "<table>";

        slotsTable += "<tr>";
        slotsTable += "<th>" + "S.NO." + "</th>";
        slotsTable += "<th>" + "NAME" + "</th>";
        slotsTable += "<th>" + "ADDRESS" + "</th>";
        slotsTable += "<th>" + "STATE" + "</th>";
        slotsTable += "<th>" + "DISTRICT" + "</th>";
        slotsTable += "<th>" + "BLOCK" + "</th>";
        slotsTable += "<th>" + "PINCODE" + "</th>";
        slotsTable += "<th>" + "FEE" + "</th>";
        slotsTable += "<th>" + "DATE" + "</th>";
        slotsTable += "<th>" + "TOTAL AVAILABILITY" + "</th>";
        slotsTable += "<th>" + "AGE" + "</th>";
        slotsTable += "<th>" + "VACCINE" + "</th>";
        slotsTable += "<th>" + "DOSE 1 AVAILABILITY" + "</th>";
        slotsTable += "<th>" + "DOSE 2 AVAILABILITY" + "</th>";
        slotsTable += "</tr>";

        for (var i = 0; i < centers.length; i++) {
            var center = centers[i];
            var sessions = center["sessions"];

            slotsTable += '<tr>';
            slotsTable += '<td rowspan="' + sessions.length + '">' + (i+1) + '</td>';
            slotsTable += '<td rowspan="' + sessions.length + '">' + center["name"] + '</td>';
            slotsTable += '<td rowspan="' + sessions.length + '">' + center["address"] + '</td>';
            slotsTable += '<td rowspan="' + sessions.length + '">' + center["state_name"] + '</td>';
            slotsTable += '<td rowspan="' + sessions.length + '">' + center["district_name"] + '</td>';
            slotsTable += '<td rowspan="' + sessions.length + '">' + center["block_name"] + '</td>';
            slotsTable += '<td rowspan="' + sessions.length + '">' + center["pincode"] + '</td>';
            slotsTable += '<td rowspan="' + sessions.length + '">' + center["fee_type"] + '</td>';

            for (var j = 0; j < sessions.length; j++) {
                var session = sessions[j];

                if (j!=0){
                    slotsTable += '<tr>';
                }
                slotsTable += '<td>' + session['date'] + '</td>';
                slotsTable += '<td>' + session['available_capacity'] + '</td>';
                slotsTable += '<td>' + session['min_age_limit'] + '</td>';
                slotsTable += '<td>' + session['vaccine'] + '</td>';
                slotsTable += '<td>' + session['available_capacity_dose1'] + '</td>';
                slotsTable += '<td>' + session['available_capacity_dose2'] + '</td>';
                slotsTable += '</tr>';
            }

            // slotsTable += '</tr>';
        }

        slotsTable += "</table>";
        document.getElementById('slots-label').innerHTML = slotsTable;

        // Notification Sound if slots are available
        var audioUrl = $('#hidden-audio-url').val();
        const audio = new Audio(audioUrl);
        audio.play();
    }
    else {
        document.getElementById('slots-label').innerHTML = "NO SLOTS AVAILABLE!";
    }
}


// Show/Hide Form Fields Based on Check Boxes
$(document).ready(function () {
    $("#form-pincode").hide();

    $("#rdb-region").click(function () {
        if ($("#rdb-region").is(':checked')) {
            $("#form-region").show();
            $("#form-pincode").hide();
        }
        else {
            $("#form-region").hide();
            $("#form-pincode").show();
        }
    });

    $("#rdb-pincode").click(function () {
        if ($("#rdb-pincode").is(':checked')) {
            $("#form-pincode").show();
            $("#form-region").hide();
        }
        else {
            $("#form-pincode").hide();
            $("#form-region").show();
        }
    });

    $("#cb-age").click(function () {
        if ($("#cb-age").is(':checked'))
            $("#form-age").show();
        else
            $("#form-age").hide();
    });

    $("#cb-date").click(function () {
        if ($("#cb-date").is(':checked'))
            $("#form-date").show();
        else
            $("#form-date").hide();
    });

    $("#cb-vaccine-type").click(function () {
        if ($("#cb-vaccine-type").is(':checked'))
            $("#form-vaccine-type").show();
        else
            $("#form-vaccine-type").hide();
    });

    $("#cb-dose").click(function () {
        if ($("#cb-dose").is(':checked'))
            $("#form-dose").show();
        else
            $("#form-dose").hide();
    });
});
