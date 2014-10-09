function extendFullHeight(selector) {
    var $window = $(window),
        height  = $window.innerHeight()
    ;
    
    $(selector).height(height);
}

function main() {
    var $window = $(window);
    
    extendFullHeight('.info');
    
    $window.on('resize', function (e) {
        extendFullHeight('.info');
    });
}

$(document).ready(main);