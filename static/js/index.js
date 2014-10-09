function extendFullHeight(selector) {
    var $window = $(window),
        height  = $window.innerHeight()
    ;

    $(selector).height(height);
}

function main() {
    var $body = $('body'),
        $window  = $(window),
        $info    = $('.info'),
        $feature = $('.feature');

    extendFullHeight('.info, .feature');

    $window.on('resize', function (e) {
        extendFullHeight('.info, .feature');
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
}

$(document).ready(main);