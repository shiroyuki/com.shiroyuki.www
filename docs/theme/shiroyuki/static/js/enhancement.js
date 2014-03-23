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

    setTimeout(function() {
        window.scrollTo(0, 400);
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
    $section.children('.photo-group-beacon ~ img').remove();
    $section.children('.photo-group-beacon').each(function () {
        var $groupBeacon = $(this)
            groupId = parseInt($groupBeacon.data('group'), 10)
        ;

        $groupBeacon.before([
            '<div class="photo-group" data-group="', groupId, '">',
            sequences[groupId].images.join(''),
            '</div>'
        ].join(''));

        $groupBeacon.remove();
    });

    console.log(sequences);
}

$(function () {
    // Enhance tables
    $('table').each(function () {
        $(this).addClass('table table-bordered');
    });

    // Make all first paragraphs a subtitle.
    $('.section > p:first').addClass('lead');

    $('.section').each(group_photos);

    // Emphasize the first image.
    theme_replace_head_img();
});