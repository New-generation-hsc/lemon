(function($){
	$("#task_plus").click(function(){
        $("#new_task_window").animate({right : "0"}, 1000);
    });

    $("#cancel_window").click(function(){
        $("#new_task_window").animate({right : "-450px"}, 1000);
    });

    $(".edit").dblclick(function(){
        $element = $(this);
        $element.attr("contenteditable", "true");
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
                window.location.href = '/?msg='+response['msg'];
            }
        });
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $(".task-edit").click(function(){
        $target = $(this);
        context = {
            'pk' : $target.attr("value"),
            'csrfmiddlewaretoken' :  getCookie('csrftoken')
        };
        $.ajax({
            type: "POST",
            url: 'update/finish',
            data : context,
            success : function(response){ 
                window.location.href = '/?msg='+response['msg'];
            }
        });
    });

    /** add a new project submit */
    $("#newproject_form").submit(function(event){
        event.preventDefault();
        var $form = $(this);
        var context = {};
        $form.serializeArray().forEach(element => {
            context[element['name']] = element['value'];
        });

        $.ajax({
            type: "POST",
            url: $form.attr('action'),
            data : context,
            success : function(response){
                window.location.href = '/?msg='+response['msg'];
            }
        });
    });

    /** add a new tag submit */
    $("#newtag_form").submit(function(event){
        event.preventDefault();
        var $form = $(this);
        var context = {};
        $form.serializeArray().forEach(element => {
            context[element['name']] = element['value'];
        });

        $.ajax({
            type: "POST",
            url: $form.attr('action'),
            data : context,
            success : function(response){
                window.location.href = '/?msg='+response['msg'];
            }
        });
    });

    $(".update_btn").click(function(event){
        event.preventDefault();
        var $btn = $(this);
        var $content = $btn.prev();
        $content.removeAttr("contenteditable");

        var context = {
            'content' : $content.text(),
            'pk' : $content.attr("id"),
            'csrfmiddlewaretoken' :  getCookie('csrftoken')
        };

        $.ajax({
            type: "POST",
            url: 'update/content',
            data : context,
            success : function(response){
                window.location.href = '/?msg='+response['msg'];
            }
        });

    });
}(jQuery));