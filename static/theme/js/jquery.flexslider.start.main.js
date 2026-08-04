jQuery(window).load(function() {
/*global jQuery:false */
"use strict";

  // КАСТОМ: переносим блок стрелок (.flex-direction-nav) внутрь .flexinside
  // активного слайда, чтобы стрелки «примагничивались» к текстовому блоку
  // (левый нижний угол) на любом слайде независимо от его высоты.
  function navToCaption(slider, index) {
    var nav = slider.find('.flex-direction-nav').first();
    var caption = slider.slides.eq(index).find('.flexinside').first();
    if (nav.length && caption.length) {
      caption.append(nav);
    }
  }

  jQuery('.mainflex').flexslider({
    animation: "fade",
    slideshow: true,                //Boolean: Animate slider automatically
    slideshowSpeed: 11000,           //Integer: Set the speed of the slideshow cycling, in milliseconds
    animationDuration: 600,
    smoothHeight: true,
    useCSS: false,
    prevText: "",
    nextText: "",
    start: function(slider) {
      slider.removeClass('loading');
      navToCaption(slider, slider.currentSlide);          // на старте — в активный блок
    },
    before: function(slider) {
      navToCaption(slider, slider.animatingTo);           // перед переключением — в следующий блок
    }
  });

});