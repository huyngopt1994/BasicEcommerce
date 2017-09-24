
var process_get_product = function () {

	var $label_just_clicked_on = $(this);

	// the value of "product_id" attribute 
   var product_id = $label_just_clicked_on.data('product_id');
  
   var processServerResponse = function ( sersverResponse_data, textStatus_ignored, jqXHR_ignored ) {
       	$('#content_product').html(sersverResponse_data);
   }
   
    var config = {
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

$(document).on('mouseenter', ".block-image",function() { 
        $(this).find(".middle").css({"opacity" :1});
        $(this).find(".my-img").css({"opacity" :0.3});} );

$(document).on('mouseleave',".block-image", function() { 
        $(this).find(".middle").css({"opacity" :0});
        $(this).find(".my-img").css({"opacity" :1});
      });
});


