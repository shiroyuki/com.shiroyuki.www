function theme_replace_head_img() {
    var $target = $('.container article:first > img:first-child'),
        content
    ;

    if ($target.length === 0) {
        return;
    }

    $target
        .closest('.off-canvas-content')
        .prepend('<div class="cover" style="background-image: url(' + $target.attr('src') + ');"></div>');

    $target.remove();
}

$(function () {
    // Enhance tables
    $('table').each(function () {
        $(this).addClass('table table-bordered');
    });

    // Make all first paragraphs a subtitle.
    $('.section > p:first').addClass('lead');

    // Emphasize the first image.
    theme_replace_head_img();
});