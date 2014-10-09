function extendFullHeight(selector) {
    var $window = $(window),
        height  = $window.innerHeight()
    ;
    
    $(selector).height(height);
}

function main() {
    var $window = $(window);
    
    extendFullHeight('.info, .feature');
    
    $window.on('resize', function (e) {
        extendFullHeight('.info, .feature');
    });
}

$(document).ready(main);