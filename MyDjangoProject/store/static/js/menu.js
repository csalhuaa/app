document.addEventListener("DOMContentLoaded", function() {
    // Código JavaScript
    const menuBtn = document.getElementById('menuBtn');
    const leftLinks = document.querySelector('.left-links');
    // const rightLinks = document.querySelector('.right-links');
    const personalLinks = document.querySelector('.personal-space');
    const userLinks = document.querySelector('.user-links');

    console.log(menuBtn); // Verifica si el elemento con el ID 'menuBtn' se ha seleccionado correctamente

    menuBtn.addEventListener('click', () => {
        leftLinks.classList.toggle('active');
        // rightLinks.classList.toggle('active');
        personalLinks.classList.toggle('active');
        userLinks.classList.toggle('active');
    });
});
