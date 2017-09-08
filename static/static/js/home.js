function get_product(name) {
    document.getElementById("number").innerHTML = "get_product";
}

function get_best_seller(list_product){

	document.getElementById("number").innerHTML = JSON.stringify(list_product);
}