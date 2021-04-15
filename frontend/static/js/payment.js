var paymentForm = document.getElementById('paymentForm');

// paymentForm.addEventListener('submit', payWithPaystack, false);

function payWithPaystack() {

    var handler = PaystackPop.setup({
        key: `{process.env.PAYSTACK_PUBLIC_KEY}`,
        email: document.getElementById('email-address').value,
        amount: document.getElementById('amount').value * 100,
        metadata: {
            custom_fields: [
                {
                    display_name: "Mobile Number",
                    variable_name: "mobile_number",
                    value: "" //customer's mobile number
                }
            ]
        },
        // currency: 'NGN', // Use GHS for Ghana Cedis or USD for US Dollars
        // ref: 'YOUR_REFERENCE', // Replace with a reference you generated
        callback: function (response) {
            //this happens after the payment is completed successfully
            // var reference = response.reference;
            alert('Payment complete! Reference: ');
            // Make an AJAX call to your server with the reference to verify the transaction
        },
        onClose: function () {
            alert('Transaction was not completed, window closed.');
        },
    });
    handler.openIframe();
}