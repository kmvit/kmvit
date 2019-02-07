jQuery(function($) {
    "use strict";

    var SLZ = window.SLZ || {};


    /*============================================
    =            PAGE LOADER FUNCTION            =
    =============================================*/

    SLZ.pageLoader = function() {
        var logo_curtain = $(".logo-curtain"),
            logo_curtain_div = $(".logo-curtain div"),
            preload = $(".preload");

        logo_curtain.animate({
            opacity: 1
        }, 500, function() {
            logo_curtain_div.animate({
                top: 0
            }, 2000, function() {
                preload.animate({
                    opacity: 0
                }, 500, function() {
                    preload.css("visibility", "hidden");
                });
            });
        });
        new WOW().init();
    };

    SLZ.mainLayout = function() {

        $(window).on('scroll load', function(event) {
            if ($(window).scrollTop() > $(window).height()) {
                $(".header:not(.header-sourcecode)").addClass('header-fixed fadeInDown animated');
            } else {
                $(".header:not(.header-sourcecode)").removeClass('header-fixed fadeInDown animated');
            }
        });

        // Slider homepage
        if ($('.slider-img-banner').length) {
            $('.slider-img-banner:not(.with-nav)').slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                speed: 800,
                arrows: false,
                dots: false,
                autoplay: true,
                autoplaySpeed: 7000,
                fade: true,
                cssEase: 'linear'
            });
            $('.slider-img-banner.with-nav').slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                speed: 800,
                arrows: true,
                dots: false,
                autoplay: true,
                autoplaySpeed: 7000,
                fade: true,
                cssEase: 'linear'
            });
        }

        $('.dropdown > a').on('click', function() {
            $(this).parent().parent().addClass('moves-out');
            $(this).next().removeClass('is-hidden');
        });
        $('.goback').on('click', function() {
            $(this).parent().parent().parent().removeClass('moves-out');
            $(this).parent().addClass('is-hidden');
        });

        // Click to open search box
        $('.btn-search').on('click', function() {
            if ($('.form-search').hasClass('display-none')) {
                $('.form-search').removeClass('display-none');
            } else
                $('.form-search').addClass('display-none');
        });

        // Click to open mmenu-hamburger
        $('.hamburger-menu-wrapper').on('click', function() {
            $('html').css('overflow', 'hidden');
            $('body').addClass('drawer-open');
        });

        // Click to close menu
        $(document).on('click', '.drawer-overlay', '.drawer-overlay i', function() {
            $('html').css('overflow', '');
            $('body').removeClass('drawer-open');
            $('.navigation .nav-links').removeClass('moves-out');
            $('.dropdown .dropdown-menu').addClass('is-hidden');
        })

        if ($(window).width() > 767) {
            var height_Item = -1,
                arrayBoxWhy = $('.why-us.layout-1 .group-wrapper .row').children(),
                arrayBoxWhyCount = arrayBoxWhy.length,
                arrayBoxmedia = $('.what-we-do.layout-2 .group-list').children(),
                arrayBoxmediaCount = arrayBoxmedia.length,
                arrayOurFeature = $('.our-feature .group-list').children(),
                arrayOurFeatureCount = arrayOurFeature.length;

            for (var i = 0; i < arrayBoxWhyCount; i++) {
                height_Item = height_Item > $(arrayBoxWhy, this).height() ? height_Item : $(arrayBoxWhy, this).height();
                $(arrayBoxWhy, this).height(height_Item);
            }

            for (var i = 0; i < arrayBoxmediaCount; i++) {
                height_Item = height_Item > $(arrayBoxmedia, this).height() ? height_Item : $(arrayBoxmedia, this).height();
                $(arrayBoxmedia, this).height(height_Item);
            }

            for (var i = 0; i < arrayOurFeatureCount; i++) {
                height_Item = height_Item > $(arrayOurFeature, this).height() ? height_Item : $(arrayOurFeature, this).height();
                $(arrayOurFeature, this).height(height_Item);
            }
        }

        // Set height page banner color white
        var header_height = $('header').height();
        $('#page-banner-2').css('height', $(window).height() - header_height);

        // Set height box-media What We Do section layout 3
        var box_media_width = $('.what-we-do .box-media.layout-3').width();
        if ($(window).width() > 991) {
            $('.what-we-do .box-media.layout-3').css('height', box_media_width);
        } else if ($(window).width() > 767 && $(window).width() <= 991) {
            $('.what-we-do .box-media.layout-3').css('height', box_media_width + 60);
        }

        // Slide team member widget
        setTimeout(function() {
            $('.team-slick').slick({
                infinite: true,
                speed: 1000,
                arrows: false,
                dots: true,
                autoplay: false,
                slidesToShow: 3,
                slidesToScroll: 3,
                customPaging: function(slider, i) {
                    return '<a>' + i + '</a>';
                },
                responsive: [{
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 3
                    }
                }, {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 2
                    }
                }, {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }]
            });

            // Slide slick client
            $('.client-slick').slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                speed: 600,
                arrows: true,
                dots: true,
                appendArrows: $('.nav-slide-client'),
                appendDots: $('.nav-slide-client'),
                customPaging: function(slider, i) {
                    return '<a>' + i + '</a>';
                }
            });

            // Slide gallery widget
            $('.gallery-wrapper').slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                speed: 1000,
                arrows: false,
                dots: true,
                customPaging: function(slider, i) {
                    return '<a>' + i + '</a>';
                },
            });

            // Slide slick work widget
            $('.slider-img').slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                speed: 600,
                arrows: true,
                dots: true,
                appendArrows: $('.nav-slide'),
                appendDots: $('.nav-slide'),
                customPaging: function(slider, i) {
                    return '<a>' + i + '</a>';
                }
            });

            // Slide slick client
            $('.slide-logo-inner').slick({
                infinite: true,
                slidesToShow: 5,
                slidesToScroll: 5,
                speed: 600,
                arrows: false,
                dots: true,
                autoplay: true,
                autoplaySpeed: 5000,
                customPaging: function(slider, i) {
                    return '<a>' + i + '</a>';
                },
                responsive: [
                    {
                        breakpoint: 991,
                        settings: {
                            slidesToShow: 4,
                            slidesToScroll: 4
                        }
                    },
                    {
                        breakpoint: 479,
                        settings: {
                        slidesToShow: 3,
                        slidesToScroll: 3
                    }
                    }
                ]
            });
        }, 100);

        $('.pricing-widget .btn').on('mouseenter', function() {
            $(this).parent().addClass('active');
        });
        $('.pricing-widget .btn').on('mouseleave', function() {
            $(this).parent().removeClass('active');
            $(this).parent().find('.title-hover').addClass('slideup');
        });


        $(window).on('resize load', function() {
            if ($('.fancybox').length) {
                $(".fancybox").fancybox({
                    helpers: {
                        thumbs: {
                            width: 60,
                            height: 60
                        }
                    }
                });
            }
            if ($(".btn-play-video").length) {
                $(".btn-play-video").fancybox({
                    maxWidth: 800,
                    maxHeight: 600,
                    fitToView: false,
                    width: '70%',
                    height: '70%',
                    autoSize: false,
                    closeClick: false,
                    openEffect: 'none',
                    closeEffect: 'none'
                });
            }
            if ($('.gallery-masonry').length) {
                var $grid = $('.gallery-masonry').isotope({
                    itemSelector: '.block-item-wrapper',
                    layoutMode: 'masonry',
                    percentPosition: true,
                    masonry: {
                        columnWidth: '.grid-sizer',
                        // gutter: 5
                    }
                });

                $('.filter-button-group').on('click', 'a', function() {
                    $('.filter-button-group > a').removeClass('active');
                    $(this).addClass('active');
                    var filterValue = $(this).attr('data-filter');
                    $grid.isotope({ filter: filterValue });
                });
            }
            if ($(window).width() <= 991) {
                $('.our-latest-work.layout-1 .box-content-wrap').css('padding-bottom', $('.our-latest-work.layout-1 .box-content-wrap .box-content-left').outerHeight() + 60);
            } else {
                $('.our-latest-work.layout-1 .box-content-wrap').css('padding-bottom', '');
            }

            if ($(window).width() <= 600) {
                $('.about-us.layout-1 .box-content-wrap').css('padding-bottom', $('.about-us.layout-1 .box-content-wrap .box-content-left').height() - 30);
            } else {
                $('.about-us.layout-1 .box-content-wrap').css('padding-bottom', '');
            }
        });

        // BACK TO TOP
        if ($('.back-to-top').length) {
            var scrollTrigger = 100; // px
            var backToTop = function() {
                var scrollTop = $(window).scrollTop();
                if (scrollTop > scrollTrigger) {
                    $('.back-to-top').addClass('show');
                } else {
                    $('.back-to-top').removeClass('show');
                }
            };
            backToTop();
            $(window).on('scroll', function() {
                backToTop();
            });
            $('.back-to-top').on('click', function(e) {
                e.preventDefault();
                $('html,body').animate({
                    scrollTop: 0
                }, 700);
            });
        }
        $(window).on('scroll', function() {
            var funfactWrap = $(".fun-fact .group-wrapper .row").children(),
                funfactWrapLen = funfactWrap.length;
            for (var i = 0; i < funfactWrapLen; i++) {
                var isOnViewFunfact = isElementVisible(funfactWrap),
                    funfactItem = $(funfactWrap[i]),
                    funfactCountTo = funfactItem.find('.number');
                if (isOnViewFunfact && !funfactCountTo.hasClass('Starting')) {
                    funfactCountTo.addClass('Starting');
                    startTimer(funfactCountTo);
                }
            }

            var progressWrap = $(".group-progress-bar-list").children(),
                progressWrapLen = progressWrap.length;
            for (var i = 0; i < progressWrapLen; i++) {
                var isOnViewProgess = isElementVisible(progressWrap),
                    progressItem = $(progressWrap[i]),
                    progressBar = progressItem.find('.progress-bar'),
                    progressWidth = progressBar.data('width');
                if (isOnViewProgess && !progressBar.hasClass('Starting')) {
                    progressBar.addClass('Starting').animate({
                        'width': progressWidth
                    }, 1000);
                }
            };
        });

        function isElementVisible($elementToBeChecked) {
            var TopView = $(window).scrollTop();
            var BotView = TopView + $(window).height();
            var TopElement = $elementToBeChecked.offset().top;
            var BotElement = TopElement + $elementToBeChecked.height();
            return ((BotElement <= BotView) && (TopElement >= TopView));
        }

        function startTimer($this) {
            setTimeout(function() {
                var $count_des = $this.data('count');
                $this.countTo({
                    from: 0,
                    to: $count_des,
                    speed: 2000,
                    refreshInterval: 90
                });
            }, 300);
        }

        // Slider homepage branding - work
           
        $('.branding-slider-nav').slick({      
            slidesToShow: 3,
            slidesToScroll: 1,
            asNavFor: '.branding-slider-for',
            dots: false,
            arrows: false,
            focusOnSelect: true,
            autoplay: true,
            autoplaySpeed: 5000
        });    
        $('.branding-slider-for').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,
            fade: true,
            asNavFor: '.branding-slider-nav'
        });
    };

    /*=====  End of PAGE LOADER FUNCTION  ======*/




    /*======================================
    =            INIT FUNCTIONS            =
    ======================================*/

    $(document).ready(function() {
        SLZ.pageLoader();
        SLZ.mainLayout();
    });

    /*=====  End of INIT FUNCTIONS  ======*/


});

(function(){var a=function(a){return document.querySelector(a)},t=document.querySelectorAll(".monitorContentGroup path");a(".monitorGroup");var f=a(".monitorScreen"),g=a(".monitorLogo"),h=a(".monitorStand"),u=a(".monitorStandShadow"),c=a(".monitorBottom"),v=a(".monitorEdge"),C=document.querySelectorAll(".laptopContentGroup path"),w=a(".laptopContentGroup"),x=a(".laptopGroup"),d=a(".laptopScreen"),k=a(".laptopEdgeLeft"),l=a(".laptopEdgeRight"),m=a(".laptopTrackpad"),n=a(".laptopBase");document.querySelectorAll(".tabletContentGroup path");
var e=a(".tabletContentGroup"),b=a(".tabletGroup"),p=a(".tabletButton"),q=a(".tabletCamera"),y=a(".tabletScreen"),r=a(".phoneGroup"),z=a(".phoneButton"),A=a(".phoneCamera"),a=a(".phoneSpeaker");TweenMax.set([c],{transformOrigin:"50% 100%"});TweenMax.set([h,n,y],{transformOrigin:"50% 0%"});TweenMax.set([g,f,d,m,b,x,p,q,e,z,A,a,w,r],{transformOrigin:"50% 50%"});TweenMax.set([k,l],{transformOrigin:"0% 100%"});TweenMax.set(b,{rotation:-90});var B=new TimelineMax({repeat:-1,delay:1,yoyo:!1,paused:!1});
B.timeScale(3);B.from(c,1,{scaleY:0,ease:Power1.easeOut}).from(h,1,{y:-70,ease:Power1.easeOut},"-=1").from(u,.5,{alpha:0,ease:Power1.easeIn},"-=0.5").from(v,1,{y:330},"-=0.25").from(f,2,{y:330,ease:Power1.easeOut},"-=1").staggerFrom(t,1,{scaleX:0},.1,"-=0.51").from(g,1,{scale:0,ease:Back.easeOut.config(2)}).staggerTo(t,1,{alpha:0,delay:2},.1).to(f,1,{y:330,ease:Power1.easeIn},"-=1").to(v,1,{y:330,ease:Power1.easeIn},"-=0.75").to(c,1,{scaleX:.69,y:-23}).to(c,1,{scaleY:.45,alpha:1},"-=1").set(c,{alpha:0}).to(g,
.5,{scale:0,ease:Back.easeIn},"-=1").to(h,1,{y:-120},"-=1.5").to(u,.5,{alpha:0},"-=1.5").from(n,1,{alpha:0},"-=1").from(m,1,{scaleX:0},"-=1").from(d,1,{scale:0,ease:Back.easeOut.config(.5)}).from(k,2,{skewX:-40,scaleY:0,ease:Power3.easeOut},"-=2").from(l,2,{skewX:40,scaleY:0,ease:Power3.easeOut},"-=2").staggerFrom(C,1,{scaleX:0},.1).to(m,.3,{alpha:0,delay:2}).to(d,1,{scaleX:.67}).to(d,1,{scaleY:.8},"-=1").to(w,1,{alpha:0,scale:.5},"-=1").to(n,1,{y:-20,scaleX:0},"-=1").to(k,1,{x:40,transformOrigin:"50% 50%",
scaleY:.85},"-=1").to(l,1,{x:-40,transformOrigin:"50% 50%",scaleY:.85},"-=1").set(x,{alpha:0}).from(b,1,{scale:1.1,alpha:0},"-=1").to(b,2,{rotation:0,delay:2,ease:Anticipate.easeOut}).staggerFrom([p,q],.5,{scale:0,ease:Back.easeOut},.1,"-=1").from(e,2,{rotation:90,scaleX:1.33,scaleY:.8,ease:Power3.easeInOut},"-=0").to([p,q],.5,{scale:0,delay:2}).to(b,1,{scaleX:.45}).to(b,1,{scaleY:.7},"-=1").to(e,1,{y:-5},"-=1").to(y,.5,{scaleY:.92,y:4},"-=0.5").set(r,{alpha:1}).set([b,e],{alpha:0}).staggerFrom([z,
A,a],1,{scale:0,ease:Back.easeOut},.1).to(r,2,{y:80,delay:2,ease:Back.easeIn.config(2)});TweenMax.set("svg",{visibility:"visible"})})();
