var emblaNode = document.querySelector('.embla')
var options = { loop: true }

var embla = EmblaCarousel(emblaNode, options)

const navigationsButtons = document.querySelectorAll(".destination__navigation");

navigationsButtons.forEach(button => {
    button.addEventListener('click', function () {
        const navigateTo = this.getAttribute('data-target');
        if (navigateTo == 'prev') {
            embla.scrollPrev();
        }
        else {
            embla.scrollNext();
        }
    })
})