document.addEventListener('DOMContentLoaded', () => {
    fetch('./src/config.json')
        .then(response => response.json())
        .then(config => {
            const images = document.querySelectorAll('img[data-img-key]');
            images.forEach(img => {
                const key = img.getAttribute('data-img-key');
                if (config[key]) {
                    img.src = config[key];
                }
            });
        })
        .catch(error => console.error('Error loading image config:', error));
});
