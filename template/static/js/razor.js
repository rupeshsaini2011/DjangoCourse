
$('.payBtn').click(function () {

    var options = {
        "key": "rzp_test_CGvHyzKvINlM2O", // Enter the Key ID generated from the Dashboard
        "amount":  $('#amount_txt').val()* 100,
        "name": "Schomee",
        "currency":  $('#currency_txt').val(),
        "description": details.first_name + ' joining ' + course.name + ', ' + course.main_teacher.institute.name,
        // "image": "https://example.com/your_logo",
        "order_id":  $('#order_id_txt').val(),//Order ID is generated as Orders API has been implemented. Refer the Checkout form table given below
        "handler": function (response) {
            console.log('Success Paymant Id: ' + response.razorpay_payment_id);

            var pay_details = new Object();
            pay_details.user_id = details.id;
            pay_details.payment_id = response.razorpay_payment_id;
            pay_details.payment_signature = response.razorpay_signature;


            $.ajax({
                url: baseUrl + 'teaching/join_class_complete/' + order_id + '/',
                type: "POST",
                data: JSON.stringify(pay_details),
                "async": true,
                "crossDomain": true,
                "processData": false,
                dataType: "json",
                "headers": {
                    'Content-Type': "application/json",
                    "Authorization": "Bearer " + details.token
                },

                success: function (resp) {
                    console.log(resp);
                    alert('Class Joined!. You will get a mail with instructions soon');
                },
            });
        },
        "prefill": {
            "name": details.first_name + ' ' + details.last_name,
            "email": details.email,
            "contact": details.student.phone,
        },

        "notes": {
            "address": "Pre Approved"
        },

    };

    var rzp1 = new Razorpay(options);
    rzp1.open();


});