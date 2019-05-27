// Auto-Scroll
function scroll_to(clicked_link, nav_height) {
        var element_class = clicked_link.attr('href').replace('#', '.');
        var scroll_to = 0;
        if(element_class != '.top-content') {
            element_class += '-container';
            scroll_to = $(element_class).offset().top - nav_height;
        }
        if($(window).scrollTop() != scroll_to) {
            $('html, body').stop().animate({scrollTop: scroll_to}, 1000);
        }
}

jQuery(document).ready(function() {

        /*
            Navigation
        */
        $('a.scroll-link').on('click', function(e) {
                e.preventDefault();
                scroll_to($(this), $('nav').outerHeight());
        });
        // toggle "navbar-no-bg" class
        $('.top-content .text').waypoint(function() {
                $('nav').toggleClass('navbar-no-bg');
        });

    /*
        Wow
    */
    new WOW().init();

});


// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Get the Session modal
var sessionmodal = document.getElementById('mySessionModal');

// Get the button that opens the modal
var sessionbtn = document.getElementById("mySessionBtn");
//

// Get the <span> element that closes the modal
var sessionspan = document.getElementsByClassName("sessionclose")[0];

// When the user clicks on the button, open the modal
sessionbtn.onclick = function() {
  sessionmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
sessionspan.onclick = function() {
  sessionmodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == sessionmodal) {
    sessionmodal.style.display = "none";
  }
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Get the Session modal
var prevsessionmodal = document.getElementById('myPrevSessionModal');

// Get the button that opens the modal
var prevsessionbtn = document.getElementById("myPrevSessionBtn");
//

// Get the <span> element that closes the modal
var prevsessionspan = document.getElementsByClassName("prevsessionclose")[0];

// When the user clicks on the button, open the modal
prevsessionbtn.onclick = function() {
  prevsessionmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
prevsessionspan.onclick = function() {
  prevsessionmodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == prevsessionmodal) {
    prevsessionmodal.style.display = "none";
  }
  if (event.target == sessionmodal) {
    sessionmodal.style.display = "none";
  }
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

$(document).ready(function(){
    $("#dd").on('click', function(){
        $(this).toggleClass("active");
        event.stopPropagation();
    });
});

$(document).ready(function(){
    $(".toggler").on('click', function(){
        $("#dd").removeClass("active");
    });
});

$(document).ready(function(){
    $("#checkAll").click(function(){
        $('input:checkbox').not(this).prop('checked', this.checked);
    });
});

bootstrap_alert = function() {}
bootstrap_alert.warning = function(message) {
            $('#alert_placeholder').html('<div class="alert alert-danger custom-alerts animated bounceInDown bounceOutUp"><span>'+message+'</span></div>')
        }
jQuery(function ($) {
    $('#selectedchecks').submit(function (e) {
        if (!$('.selectedchecks').is(':checked')) {
            bootstrap_alert.warning('Please select at least one question');
            e.preventDefault();
        }
    });
});

$(document).ready(function() {
    strPath = '../static/extractor/output/extractor.output'

    if(document.getElementById('downloadfile') != null) {
        var iframe;
        iframe = document.getElementById("hiddenDownloader");

        if (iframe == null) {
            iframe = document.createElement('iframe');
            iframe.id = "hiddenDownloader";
            iframe.style.visibility = 'hidden';
            document.body.appendChild(iframe);
        }
        iframe.src = strPath;
    }
});


