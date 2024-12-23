document.addEventListener("DOMContentLoaded", function () {
    // Dropdown change event for "admin"
    document.getElementById("admin").addEventListener("change", function () {// 2l drop down law dost 3la function mnhom ywadeeny leeha
        const val = this.value;
        if (val) {
            window.location.href = `/${val}`;
        }
    });

    // 2l buttons 2ll bt2lb beeb 2lswar
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const carouselImages = document.querySelector('.carousel-images');
    let index = 0;

    const totalImages = carouselImages.children.length;

    prevButton.addEventListener("click", function () {
        index = (index === 0) ? totalImages - 1 : index - 1;// law 2na 2sln 3la 2wl sora hyawdeeny l25r sora law l2 hyrag3ny sora wra
        updateCarousel();
    });

    nextButton.addEventListener("click", function () {
        index = (index === totalImages - 1) ? 0 : index + 1; // 3ks 2llfo2 law 2na 25r wa7da yrag3ny 3la 2wl wa7da  law l2 ywadeeney sora llymeen
        updateCarousel();
    });

    function updateCarousel() {
        const offset = -index * 100;
        carouselImages.style.transform = `translateX(${offset}%)`;// 34an yt7rk
    }

   
    

    const exploreButtons = document.querySelectorAll(".explore");// hageeb 2l buttons 2ll no3ha explore

    exploreButtons.forEach(button => { // lkl button mnhom 
        button.addEventListener("click", function () {// law dost 3aleeh
            const category = this.closest(".card").dataset.category;
    
            if (category) {
                // Redirect to the products page with the category as a query parameter
                window.location.href = `/products?type=${category}`;//wadeeny ll products page wdh 2l prameter bta3ha (menas part)
            }
        });
    });
});

