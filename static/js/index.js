function extendFullHeight(selector) {
    var $window = $(window),
        height  = $window.innerHeight()
    ;

    $(selector).height(height);
}

function main() {
    var $body    = $('body');
    var $window  = $(window);
    var $info    = $('.info');
    var $feature = $('.feature:first');
    var $video   = $('.feature:first video');
    var video;

    if (navigator.userAgent.match(/android.+mobile/i)) {
        $video.hide();
    } else if ($video.length !== 0) {
        video = $video[0];

        video.play();
    }

    extendFullHeight('.info, .feature');

    $window.on('resize', function (e) {
        extendFullHeight('.info, .feature');
    });

    $window.on('focus', function (e) {
        if (!video) {
            return;
        }

        video.play();
    });

    $window.on('blur', function (e) {
        if (!video) {
            return;
        }

        video.pause();
    });

    $('header h1').on('click', function (e) {
        var target = 0;
        e.preventDefault();
        //window.scrollTo(0, target);
        $body.animate({scrollTop: target});
    });

    $('header nav a[href=#feature]').on('click', function (e) {
        var target = $info.outerHeight();
        e.preventDefault();
        //window.scrollTo(0, $info.outerHeight());
        $body.animate({scrollTop: target});
    });

    $('header nav a[href=#feature]').trigger('click');

    if (video) {
        setInterval(function () {
            if (video.ended) {
                $video.fadeOut();
            }
        }, 250);
    }
}

$(document).ready(main);
