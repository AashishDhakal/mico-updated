// $(".slidebanner").owlCarousel({
//   loop: true,
//   margin: 10,
//   dots: true,
//   nav: false,
//   center: true,
//   autoWidth: true,
//   // autoplay: true,
//   autoplayTimeout: 5000,
//   animateIn: "fadeIn",
//   animateOut: "fadeOut",
//   responsive: {
//     0: {
//       items: 1,
//     },
//     425: {
//       items: 1,
//     },
//     600: {
//       items: 1,
//     },
//     1000: {
//       items: 1,
//     },
//   },
// });

$(".newsslide").owlCarousel({
  loop: false,
  margin: 10,
  dots: false,
  nav: true,
  autoplay: true,
  autoplayTimeout: 2000,
  animateIn: "fadeIn",
  animateOut: "fadeOut",
  responsive: {
    0: {
      items: 1,
    },
    425: {
      items: 1,
    },
    600: {
      items: 2,
    },
    1000: {
      items: 3,
    },
    1400: {
      items: 4,
    },
  },
});

$(".newssingle-gallery").owlCarousel({
  loop: true,
  margin: 10,
  dots: true,
  nav: false,
  // autoplay: true,
  autoplayTimeout: 5000,
  animateIn: "fadeIn",
  animateOut: "fadeOut",
  responsive: {
    0: {
      items: 2,
    },
    425: {
      items: 2,
    },
    600: {
      items: 3,
    },
    1000: {
      items: 4,
    },
  },
});

$(".donatelist").owlCarousel({
  loop: false,
  margin: 10,
  dots: true,
  nav: true,
  // autoplay: true,
  autoplayTimeout: 5000,
  animateIn: "fadeIn",
  animateOut: "fadeOut",
  responsive: {
    0: {
      items: 1,
    },
    425: {
      items: 1,
    },
    600: {
      items: 2,
    },
    1000: {
      items: 3,
    },
  },
});

$(".slider").slick({
  centerMode: true,
  centerPadding: "60px",
  slidesToShow: 3,
  variableWidth: true,

  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: "40px",
        slidesToShow: 3,
      },
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: "40px",
        slidesToShow: 1,
      },
    },
  ],
});
