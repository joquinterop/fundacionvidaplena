/*=========================NAVBAR================================*/
document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.createElement('nav');
    navbar.classList.add('navbar', 'navbar-expand-lg', 'navbar-light', 'p-3');
    navbar.id = 'menu';
  
    const container = document.createElement('div');
    container.classList.add('container');
  
    // Crear el enlace al carrito de compra
    const cartLink = document.createElement('a');
    cartLink.href = 'carrito.html'; // Enlace a la página del carrito de compra
    cartLink.classList.add('cart-button');
  
    // Agregar el botón del carrito de compra al enlace
    const cartButton = document.createElement('button');
    cartButton.innerHTML = '<i class="fas fa-shopping-cart"></i>'; // Se asume que estás usando FontAwesome para los íconos
    cartButton.classList.add('btn', 'btn-outline-dark');
  
    // Agregar el botón del carrito de compra al enlace
    cartLink.appendChild(cartButton);
  
    // Agregar la imagen del logo a la izquierda
    const logoImage = document.createElement('img');
    logoImage.src = 'fotos/logo_2.png'; // Ruta a la imagen de tu logo
    logoImage.classList.add('logo-img');
  
    const brand = document.createElement('a');
    brand.classList.add('navbar-brand');
  
    // Incluir el logo, el texto "VIAJA GO" y el botón del carrito de compra
    brand.innerHTML = `
        ${logoImage.outerHTML}
        <span class="fs-5 text-white fw-bold">VIAJA GO</span>
    `;
    brand.appendChild(cartLink);
  
    const toggleButton = document.createElement('button');
    toggleButton.classList.add('navbar-toggler');
    toggleButton.type = 'button';
    toggleButton.dataset.bsToggle = 'collapse';
    toggleButton.dataset.bsTarget = '#navbarSupportedContent';
    toggleButton.setAttribute('aria-controls', 'navbarSupportedContent');
    toggleButton.setAttribute('aria-expanded', 'false');
    toggleButton.setAttribute('aria-label', 'Toggle navigation');
    toggleButton.innerHTML = `<span class="navbar-toggler-icon"></span>`;
  
    const collapseDiv = document.createElement('div');
    collapseDiv.classList.add('collapse', 'navbar-collapse');
    collapseDiv.id = 'navbarSupportedContent';
  
    const ul = document.createElement('ul');
    ul.classList.add('navbar-nav', 'me-auto', 'mb-2', 'mb-lg-0');
  
    const menuItems = [
        { text: 'Inicio', href: 'Index.html' },
        { text: 'Paquetes de Viaje', href: '#intro' },
        { text: 'Viaja por Chile', href: '#' },
        { text: 'Latinoamérica', href: 'latinoamerica.html' },
        { text: 'Blog', href: '#' },
        { text: 'Nosotros', href: 'nosotros.html' }
    ];
  
    menuItems.forEach(item => {
        const li = document.createElement('li');
        li.classList.add('nav-item');
  
        const a = document.createElement('a');
        a.classList.add('nav-link');
        a.href = item.href;
        a.textContent = item.text;
  
        li.appendChild(a);
        ul.appendChild(li);
    });
  
    collapseDiv.appendChild(ul);
    container.appendChild(brand);
    container.appendChild(toggleButton);
    container.appendChild(collapseDiv);
    navbar.appendChild(container);
  
    document.body.prepend(navbar);
  });