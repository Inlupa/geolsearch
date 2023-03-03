new Swiper('.image-slider',{
    navigation:{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    //возможность скроллить стрелочками клавиатуры
    keyboard:{
        enabled:true,
        onlyInViewport:true,
    },
    // возможномть скроллить колесом мыши
    mousewheel: {
        sensitivity: 1,
        eventsTarget: ".image-slider"
    },
    // автовысота слайда и бесконечная прокрутка
    loop: true,
    //автопрокрутка
    autoplay: {
        delay:5000,
    },
    //скорость изменения картинки
    speed:1000,
});
