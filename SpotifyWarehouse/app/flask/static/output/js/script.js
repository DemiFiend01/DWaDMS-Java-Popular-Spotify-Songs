let slideIndex = 1;

let slides = document.getElementsByClassName("mySlides");
if (slides.length > 0) {
    showSlides(slideIndex);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("mySlidesDot");

    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace("mySlidesDotActive", "");
    }

    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " mySlidesDotActive";
}