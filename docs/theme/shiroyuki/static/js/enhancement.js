function theme_replace_head_img() {
    var $target = $('.container article:first > img:first-child');
    var offset  = $(window).innerHeight();
    var content;

    if ($target.length === 0) {
        return;
    }

    $target
        .closest('.off-canvas-content')
        .prepend('<div class="cover" style="background-image: url(' + $target.attr('src') + ');"></div>');

    $target.remove();

    switch (true) {
        case offset >= 940: offset = 300; break;
        case offset >= 720: offset = 200; break;
        default:            offset = 200; break;
    }

    setTimeout(function() {
        window.scrollTo(0, offset);
    }, 50);
}

function group_photos() {
    var $section = $(this),
        $adjacents = $section.children(),
        sequences = [],
        seq_index = -1,
        prevTagName = null
    ;

    // Gather the images.
    $adjacents.each(function () {
        var $adjacent = $(this),
            tagName   = $adjacent.prop('tagName'),
            data
        ;

        if (tagName !== 'IMG') {
            prevTagName = tagName;

            return;
        }

        if (prevTagName !== tagName) {
            sequences[++seq_index] = {
                parent: $section,
                images: []
            };

            $adjacent.attr('data-group', seq_index);
            $adjacent.addClass('photo-group-beacon');
        }

        sequences[seq_index].images.push($adjacent.prop('outerHTML'));

        prevTagName = tagName;
    });

    // Remove most of original placements.
    $section.children('.photo-group-beacon').each(function () {
        var $groupBeacon = $(this);
        var groupId      = parseInt($groupBeacon.data('group'), 10);
        var sequence     = sequences[groupId];

        $groupBeacon.before([
            '<div class="photo-group" data-group="', groupId, '" data-count="', sequence.images.length, '">',
            sequence.images.join(''),
            '</div>'
        ].join(''));

        $groupBeacon.remove();
    });

    $section.find('.photo-group ~ img').remove();
}

$(function () {
    // Enhance tables
    $('table').each(function () {
        $(this).addClass('table table-bordered');
    });

    // Make all first paragraphs a subtitle.
    $('body').not('[data-path="misc/resume"]').find('.section > p:first').addClass('lead');

    $('.section').each(group_photos);

    // Emphasize the first image.
    theme_replace_head_img();
});
