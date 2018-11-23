(function($){
	$("#task_plus").click(function(){
        $("#new_task_window").animate({right : "0"}, 1000);
    });

    $("#cancle_window").click(function(){
        $("#new_task_window").animate({right : "-450px"}, 1000);
    });

    $("#newtask_form").submit(function(event){
        event.preventDefault();
        var $form = $(this);
        // var $csrf = $("input[name='csrfmiddlewaretoken']", $form);
        var $content = $("#task_content");
        var $time = $("#remind_time");
        var context = {
            'content' : $content.text(),
            'remind_time' : $time.val(),
        }
        $form.serializeArray().forEach(element => {
            context[element['name']] = element['value'];
        });

        $.ajax({
            type: "POST",
            url: $form.attr('action'),
            data : context,
            success : function(response){
                window.location.href = '/';
            }
        });
    });
}(jQuery));