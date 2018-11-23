(function($){
	$("#task_plus").click(function(){
        $("#new_task_window").animate({right : "0"}, 1000);
    });

    $("#cancle_window").click(function(){
        $("#new_task_window").animate({right : "-450px"}, 1000);
    });
}(jQuery));