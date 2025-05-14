document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.getElementById('overlay');
    const popup = document.getElementById('popup');
    const closeBtn = document.getElementById('popup-close');
    const titleBox = document.getElementById('popup-title');
    const bodyBox = document.getElementById('popup-body');


    function openPopup(title, body) {
        titleBox.textContent = title;
        bodyBox.textContent = body;
        overlay.style.display = 'block';
        popup.style.display = 'block';
    }

    function closePopup() {
        overlay.style.display = 'none';
        popup.style.display = 'none';
    }

    document.querySelectorAll('.footer-link').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const title = link.getAttribute('data-title');
            const body = link.getAttribute('data-body');
            openPopup(title, body)
        });
    });

    overlay.addEventListener('click', closePopup)
    closeBtn.addEventListener('click', closePopup)

});




document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const mobileMenu = document.querySelector(".mobile-menu");

    menuToggle.addEventListener("click", function () {
        mobileMenu.classList.toggle("show");
    });
});

