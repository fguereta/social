$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: '/ajax/',
        success: function (result) {

            if (result.status == "success") {
                if (result['data']) {
                    jQuery.each(result['data'], function (i, val) {

                        $('.myTable').append(
                            '<tr><td id="presentacion">'+val['presentacion']+'</td>' +
                            '<td id="generico">'+val['generico']+'</td></tr>');

                    });
                }
            }
        }
    })

});