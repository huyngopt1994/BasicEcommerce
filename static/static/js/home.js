function get_product(name) {
    document.getElementById("number").innerHTML = "get_product";
}


function get_best_seller(){

	document.getElementById("number").innerHTML = "best seller";
}

$(document).ready(function(){
    $("li").mouseenter(function(){
        $(this).css("font-weight", "bold");
    });
    $("li").mouseleave(function(){
        $(this).css("font-weight","light");
    });
});