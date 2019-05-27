var page = $("html, body");

$(document).ready(function () {
    page.on("scroll mousedown wheel DOMMouseScroll mousewheel keyup touchmove", function(){
        page.stop();
    });
    page.animate({ scrollTop: $('#output-container').offset().top - 70 }, 1000, function(){
        page.off("scroll mousedown wheel DOMMouseScroll mousewheel keyup touchmove");
    });

    return false;
});
