var productModal = $("#productModal");
$(function () {

    //JSON data by API call
    // $.get means we are calling http and productListApiUrl we get from common.js as an API call
    $.get(productListApiUrl, function (response) {
        if (response) {
            var table = '';
            // here we're iterating the json file to make it display on teh UI
            $.each(response, function (index, product) {
                table += '<tr data-id="' + product.product_id + '" data-name="' + product.name + '" data-unit="' + product.uom_id + '" data-price="' + product.price_per_unit + '">' +
                    '<td>' + product.name + '</td>' +
                    '<td>' + product.uom_name + '</td>' +
                    '<td>' + product.price_per_unit + '</td>' +
                    '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});

// Save Product, insert product
$("#saveProduct").on("click", function () {
    // If we found id value in form then update product detail
    var data = $("#productForm").serializeArray();
    var requestPayload = {
        product_name: null,
        uom_id: null,
        price_per_unit: null
    };
    // below loop is used to iterate through object we get from after save button is pressed on UI which get converted into seriealized array  from ablove and when we iterate  and get a name we put teh value of 'name' in array to requestPayload 'product_name' and similar for teh others  
    for (var i = 0; i < data.length; ++i) {
        var element = data[i];
        switch (element.name) {
            case 'name':
                requestPayload.product_name = element.value;
                break;
            case 'uoms':
                requestPayload.uom_id = element.value;
                break;
            case 'price':
                requestPayload.price_per_unit = element.value;
                break;
        }
    }
    // callapi function is a generic ajax function, ajax is used in UI to call backend, to call Http: taken from 'common.js'
    callApi("POST", productSaveApiUrl, {
        // sinc eabove we get a immutable dict which is not convinent for flasjk we convert that to a string and send it to backend
        'data': JSON.stringify(requestPayload)
    });
});


// delete of a product from database
$(document).on("click", ".delete-product", function () {
    var tr = $(this).closest('tr');
    var data = {
        product_id: tr.data('id')
    };
    var isDelete = confirm("Are you sure to delete " + tr.data('name') + " item?");
    if (isDelete) {
        callApi("POST", productDeleteApiUrl, data);
    }
});


//Add new product pop-up  functions

// hide the add new product model
productModal.on('hide.bs.modal', function () {
    $("#id").val('0');
    $("#name, #unit, #price").val('');
    productModal.find('.modal-title').text('Add New Product');
});

// add new product  moddel open
productModal.on('show.bs.modal', function () {
    //JSON data by API call
    $.get(uomListApiUrl, function (response) {
        if (response) {
            var options = '<option value="">--Select--</option>';
            $.each(response, function (index, uom) {
                options += '<option value="' + uom.uom_id + '">' + uom.uom_name + '</option>';
            });
            $("#uoms").empty().html(options);
        }
    });
});