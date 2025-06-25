// Apply animation on initial load
window.addEventListener("pageshow", function () {
    document.body.classList.add("page-loaded");
    document.body.classList.remove("fade-exit");
});

document.addEventListener("DOMContentLoaded", function () {
    document.body.classList.add("page-loaded");
});

const links = document.querySelectorAll("a[href]");

links.forEach(link => {
    const href = link.getAttribute('href');
    const isSameSite = href && (href.startsWith("/") || href.startsWith(window.location.origin));

    if (isSameSite) {
        link.addEventListener('click', function (e) {
            if (href !== window.location.pathname) {
                e.preventDefault();
                document.body.classList.remove('page-loaded');
                document.body.classList.add('fade-exit');

                // Scroll up first and hide navbar
                document.querySelector(".navbar-container").style.opacity = "0";
                window.scrollTo({ top: 0, behavior: 'smooth' });

                setTimeout(() => {
                    window.location.href = href;
                }, 500);
            }
        });
    }
});

// Show navbar again when user scrolls down after page loads
window.addEventListener("scroll", function () {
    const navbar = document.querySelector(".navbar-container");
    if (window.scrollY > 100) {
        navbar.style.opacity = "1";
        navbar.style.transition = "opacity 0.4s ease";
    }
});