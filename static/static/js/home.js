
var process_get_product = function () {
	var $label_just_clicked_on = $(this);

	// the value of "product_id" attribute 
   var product_id = $label_just_clicked_on.data('product_id');
   document.write(product_id);

  
   var processServerResponse = function ( sersverResponse_data, textStatus_ignored, jqXHR_ignored) {
   	$('#content_product').html(sersverResponse_data);
   }

    var config {
   	url: PRODUCT_URL_ID + product_id + '/',
   	dataType: 'html',
   	success: processServerResponse
   };

   $.ajax(config);

};


$(document).ready(function()  {
  
    $(".change").mouseenter(function(){
        $(this).css({"font-weight" :"bold", "text-decoration": "underline"});
    });
    $(".change").mouseleave(function(){
        $(this).css({"font-weight": "normal", "text-decoration": "none"});
    });

    $(".change").click(process_get_product);
});
