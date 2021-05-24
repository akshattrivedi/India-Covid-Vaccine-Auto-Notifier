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

// API Call for Getting All Districts
$(function () {
    $('#state').change(function () {
        $.get("http://localhost:8000/api/getAllDistricts?state=" + $(this).val(), function (data, status) {
            $('#district').empty()
            for (var i = 0; i < data["districts"].length; i++) {
                $('#district').append($('<option>').text(data["districts"][i]).attr('value', data["districts"][i]));
            }
        });
    });
});

// Show/Hide Fields Based on Check Boxes
$(document).ready(function () {
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


