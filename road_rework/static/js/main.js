new Swiper('.image-slider',{
    navigation:{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    pagination:{
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullets: true,
    },

    scrollbar: {
        el: '.swiper-scrollbar',
        draggable: true
    },

    keyboard:{
        enabled:true,
        onlyInViewport:true,
    },
});
