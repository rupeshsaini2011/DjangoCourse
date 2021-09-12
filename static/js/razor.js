



$('.payBtn').click(function () {

    var options = {
        "key": "rzp_test_CGvHyzKvINlM2O", // Enter the Key ID generated from the Dashboard
        "amount":  $('#amount_txt').val()* 100,
        "name":  $('#name_txt').val(),
        "currency": $('#currency_txt').val(),
        "description": "Payment for Course",
        // "image": "https://example.com/your_logo",nt
        "order_id": $('#order_id_txt').val(),//Order ID is generated as Orders API has been implemented. Refer the Checkout form table given below
        "handler": function (response) {
            console.log('Success Paymant Id: ' + response.razorpay_payment_id);

            var pay_details = new Object();
            pay_details.user_id = $('#order_id_txt').val();
            pay_details.payment_id = response.razorpay_payment_id;
            pay_details.payment_signature = response.razorpay_signature;


            $.ajax({
                url: 'payment-status/' +  $('#order_id_txt').val() + '/',
                type: "POST",
                data: JSON.stringify(pay_details),
                "async": true,
                "crossDomain": true,
                "processData": false,
                dataType: "json",
                "headers": {
                    'Content-Type': "application/json",
                    "Authorization": "Bearer " 
                },

                success: function (resp) {
                    console.log(resp);
                    alert('Class Joined!. You will get a mail with instructions soon');
                },
            });
        },
       

        "notes": {
            "address": "Pre Approved"
        },

    };

    var rzp1 = new Razorpay(options);
    rzp1.open();


});