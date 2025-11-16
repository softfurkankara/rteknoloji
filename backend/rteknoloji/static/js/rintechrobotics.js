//  region jquery ready function
$(document).ready(function () {

    // region HomePages
    // region Revolution Sliders
    // region Corporate
    if ($("#rev_slider_home_corporate").length > 0 && $("#rev_slider_home_corporate").revolution == undefined) {
        revslider_showDoubleJqueryError("#rev_slider_1078_1");
    } else if ($("#rev_slider_home_corporate").length > 0) {
        let $slider = $("#rev_slider_home_corporate");

        $slider.show().revolution({
            sliderType: "standard",
            jsFileLocation: "/static/revolution/js/",
            sliderLayout: "fullscreen",
            dottedOverlay: "none",
            delay: 9000,
            navigation: {
                keyboardNavigation: "on",
                keyboard_direction: "horizontal",
                mouseScrollNavigation: "off",
                mouseScrollReverse: "default",
                onHoverStop: "off",
                touch: {
                    touchenabled: "on",
                    swipe_threshold: 75,
                    swipe_min_touches: 1,
                    swipe_direction: "horizontal",
                    drag_block_vertical: false
                }
                ,
                arrows: {
                    style: "zeus",
                    enable: true,
                    hide_onmobile: true,
                    hide_under: 600,
                    hide_onleave: true,
                    hide_delay: 200,
                    hide_delay_mobile: 1200,
                    tmp: '<div class="tp-title-wrap">  	<div class="tp-arr-imgholder"></div> </div>',
                    left: {
                        h_align: "left",
                        v_align: "center",
                        h_offset: 30,
                        v_offset: 0
                    },
                    right: {
                        h_align: "right",
                        v_align: "center",
                        h_offset: 30,
                        v_offset: 0
                    }
                }
                ,
                bullets: {
                    enable: true,
                    hide_onmobile: false,
                    hide_under: 300,
                    style: "hermes",
                    hide_onleave: false,
                    hide_delay: 200,
                    hide_delay_mobile: 1200,
                    direction: "horizontal",
                    h_align: "center",
                    v_align: "bottom",
                    h_offset: 0,
                    v_offset: 30,
                    space: 8,
                    tmp: '<span class="tp-bullet-img-wrap">  <span class="tp-bullet-image"></span></span><span class="tp-bullet-title">{{title}}</span>'
                }
            },
            viewPort: {
                enable: true,
                outof: "pause",
                visible_area: "80%",
                presize: false
            },
            responsiveLevels: [1240, 1024, 778, 480],
            visibilityLevels: [1240, 1024, 778, 480],
            gridwidth: [1240, 1024, 778, 480],
            gridheight: [600, 600, 500, 400],
            lazyType: "none",
            parallax: {
                type: "mouse",
                origo: "slidercenter",
                speed: 2000,
                levels: [2, 3, 4, 5, 6, 7, 12, 16, 10, 50, 46, 47, 48, 49, 50, 55]
            },
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,
            shuffle: "off",
            autoHeight: "off",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
                simplifyAll: "off",
                nextSlideOnWindowFocus: "off",
                disableFocusListener: false
            }
        });

        function findBgVideo() {
            return $slider.find('.tp-bgvideo')[0] ||
                $slider.find('.rs-background-video-layer video')[0] ||
                null;
        }

        function primeAndPlay(videoEl) {
            videoEl.muted = true;
            videoEl.setAttribute('muted', '');
            videoEl.setAttribute('autoplay', '');
            videoEl.setAttribute('playsinline', '');
            videoEl.removeAttribute('controls');

            $slider.find('.rev-slidebg').addClass('rev-slidebg-visible');

            try {
                videoEl.currentTime = 0.01;
            } catch (e) {
            }
            var tryPlay = function () {
                videoEl.play().catch(function () {
                    videoEl.addEventListener('loadeddata', function once() {
                        videoEl.removeEventListener('loadeddata', once);
                        videoEl.play().catch(function () { /* swallow */
                        });
                    }, {once: true});
                });
            };
            tryPlay();
        }

        $slider.on('revolution.slide.onafterswap', function () {
                let tries = 40; // ~4s
                (function wait() {
                    var v = findBgVideo();
                    if (v) return primeAndPlay(v);
                    if (--tries <= 0) return;
                    setTimeout(wait, 100);
                })();
            });
    }
    // endregion Corporate
    // endregion Revolution Sliders
    // region HomePages
});
// endregion jquery ready function