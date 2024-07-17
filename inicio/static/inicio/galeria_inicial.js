async function loadImages() {
    const accessKey = 'xlbHD712R2Vu7yyRLIOhrW99RXvi2Loa3xFEK37XZmk'; 
    const queries = ['ancianos'];
    const imagePromises = queries.map(query => fetch(`https://api.unsplash.com/photos/random?query=${query}&count=3&client_id=${accessKey}`));

    try {
        const responses = await Promise.all(imagePromises);
        const data = await Promise.all(responses.map(response => response.json()));
        const images = data.flat();
        displayImages(images);
    } catch (error) {
        console.error('Error fetching images from Unsplash:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const showImagesBtn = document.getElementById('showImagesBtn');
    const hideImagesBtn = document.getElementById('hideImagesBtn');

    showImagesBtn.addEventListener('click', () => {
        loadImages();
    });

    hideImagesBtn.addEventListener('click', () => {
        const gallery = document.getElementById('gallery');
        gallery.innerHTML = '';
        hideImagesBtn.style.display = 'none';
        showImagesBtn.style.display = 'inline-block';
    });
});

function displayImages(images) {
    const gallery = document.getElementById('gallery');
    gallery.innerHTML = '';

    images.forEach(image => {
        const imgElement = document.createElement('img');
        imgElement.src = image.urls.small;
        imgElement.alt = image.alt_description || 'Unsplash Image';
        imgElement.classList.add('gallery-img');
        gallery.appendChild(imgElement);
    });

    // Mostrar el botón "Ocultar imágenes" y ocultar el botón "Ver más imágenes"
    document.getElementById('showImagesBtn').style.display = 'none';
    document.getElementById('hideImagesBtn').style.display = 'inline-block';
}