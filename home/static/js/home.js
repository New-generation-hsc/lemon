
var themes = $("#list_theme > li");
var circles = $(".theme-circle");

const len = themes.length;
var index = 0;

const clearActive = lists => {
	for (var i = 0; i < len; i++) {
		$($(lists)[i]).removeClass('active');
	}
}

const setActive = index => {
	clearActive(themes);
	$(themes[index % len]).addClass('active');
	clearActive(circles);
	$(circles[index % len]).addClass('active');
}

const autoPlay = () => {
	clearActive();
	setActive(index);
	index = (index + 1) % len;
	setTimeout(autoPlay, 2000);
}

$("#project-new").click(function(){
	$("#background").css("display", "block");
	$("#project_color > div").removeClass('active');
	$("#dialog_projects").fadeIn("800", function(){
		$(this).animate({top:"10%"}, 300);
	});
});

$(".close-btn").click(function(event){
	event.preventDefault();
	$("#background").css("display", "none");
	$("#dialog_projects").fadeOut("1500", function(){
		$(this).css("top", "-100%");
	});
});

$("#tags-new").click(function(){
	$("#background").css("display", "block");
	$("#dialog-tags").fadeIn("800", function(){
		$(this).animate({top:"10%"}, 300);
	});
});

$(".tag-close").click(function(){
	$("#background").css("display", "none");
	$("#dialog-tags").fadeOut("1500", function(){
		$(this).css("top", "-100%");
	});
});

$("#project_color div").click(function(){
	$("#project_color > div").removeClass('active');
	$(this).addClass('active');
	var color = $(this).index();
	$("#project_color_index").val(color.toString());
});

$("#tags_color div").click(function(){
	$("#tags_color > div").removeClass('active');
	$(this).addClass('active');
	var color = $(this).index();
	console.log(color);
	$("#tag_color_index").val(color.toString());
});

autoPlay();