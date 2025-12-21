document.addEventListener('DOMContentLoaded', function() {
    const lightbox = document.createElement('div');
    lightbox.id = 'image-lightbox';
    lightbox.classList.add('lightbox');

    const lightboxContent = document.createElement('img');
    lightboxContent.classList.add('lightbox-content');

    const closeButton = document.createElement('span');
    closeButton.classList.add('close');
    closeButton.innerHTML = '&times;';

    const prevButton = document.createElement('a');
    prevButton.classList.add('prev');
    prevButton.innerHTML = '&#10094;';

    const nextButton = document.createElement('a');
    nextButton.classList.add('next');
    nextButton.innerHTML = '&#10095;';

    lightbox.appendChild(closeButton);
    lightbox.appendChild(prevButton);
    lightbox.appendChild(nextButton);
    lightbox.appendChild(lightboxContent);
    document.body.appendChild(lightbox);

    const imageLinks = Array.from(document.querySelectorAll('.lightbox-trigger'));
    let currentIndex = 0;

    function showImage(index) {
        if (index >= imageLinks.length) {
            index = 0;
        } else if (index < 0) {
            index = imageLinks.length - 1;
        }
        lightboxContent.src = imageLinks[index].href;
        currentIndex = index;
    }

    imageLinks.forEach((link, index) => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            lightbox.style.display = 'flex';
            showImage(index);
        });
    });

    function closeLightbox() {
        lightbox.style.display = 'none';
        lightboxContent.src = '';
    }

    function showNextImage() {
        showImage(currentIndex + 1);
    }

    function showPrevImage() {
        showImage(currentIndex - 1);
    }

    closeButton.addEventListener('click', closeLightbox);
    nextButton.addEventListener('click', showNextImage);
    prevButton.addEventListener('click', showPrevImage);

    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    document.addEventListener('keydown', function(e) {
        if (lightbox.style.display === 'flex') {
            if (e.key === 'Escape') {
                closeLightbox();
            } else if (e.key === 'ArrowRight') {
                showNextImage();
            } else if (e.key === 'ArrowLeft') {
                showPrevImage();
            }
        }
    });
});
