$(function () {
    let searchParams = new URLSearchParams(window.location.search);

    var $msg = $(".msg");
    var $progress = $(".progress");
    var $msg_content = $(".msg > p");

    function show_msg(msg){
        $msg_content.text(msg);
        $msg.animate({
            bottom : '50px',
        }, 250, function(){
            $progress.animate({
                width : "100%",
            }, 3000, function(){
                $msg.animate({
                    bottom : '-40px'
                }, 250, function(){
                    $progress.css('width', "0");
                });
            });
        });
    }

    if(searchParams.has('msg')){
        show_msg(searchParams.get('msg'));
    }
});