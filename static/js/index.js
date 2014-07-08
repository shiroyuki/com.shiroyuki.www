function enableFeatureVideo() {
    videoSelector = '.feature .video-player';
    videoCode = '<iframe class="video-player" width="100%" height="100%" src="//www.youtube.com/embed/vdvp3DExCF4" frameborder="0" allowfullscreen></iframe>';
    $video = null;
    $body = $('body');
    $window = $(window);
    $feature = $('.feature');
    $videoCloser = $('a.video-done');

    $('a.video-trigger').on('click', function (e) {
        e.preventDefault();

        if ($window.outerWidth() < $window.outerHeight()) {
            alert('Cannot play the video in the portrait mode.');
            return;
        }

        $feature.append(videoCode);
        $video = $(videoSelector);

        $video.fadeIn(
            500,
            function () {
                $videoCloser.fadeIn(250);
            }
        );
    });

    $videoCloser.on('click', function (e) {
        e.preventDefault();

        if (!$video) {
            return;
        }

        $video.fadeOut(
            500,
            function () {
                $video.remove();
                $videoCloser.fadeOut(250);
            }
        );
    });
}

function main() {
    // NOP
}

$(document).ready(main);