/*===============NAVBAR================*/
document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.createElement('nav');
    navbar.classList.add('navbar', 'navbar-expand-lg', 'navbar-light', 'p-3');
    navbar.id = 'menu';

    const container = document.createElement('div');
    container.classList.add('container');

    // Agregar la imagen del logo a la izquierda
    const logoImage = document.createElement('img');
    logoImage.src = '/static/inicio/images/logo_blanco.png'; // Asegúrate de que la ruta sea correcta
    logoImage.classList.add('logo-img');

    const brand = document.createElement('a');
    brand.classList.add('navbar-brand');

    // Incluir el logo y el texto "VIDA PLENA"
    brand.innerHTML = `
        ${logoImage.outerHTML}
        <span class="fs-5 text-white fw-bold">Vida Plena</span>
    `;

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
        { text: 'Inicio', href: urls.inicio },
        { text: 'Ubicación', href: urls.ubicacion },
        { text: 'Servicios', href: urls.servicios },
        { text: 'Preguntas Frecuentes', href: urls.preguntas_frecuentes },
        { text: 'Contacto', href: urls.contacto },
        { text: 'Blog', href: urls.blog },
        { text: 'Donaciones', href: urls.donaciones }
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


/*===============TYPEWRITER================*/

let app = document.getElementById('typewriter');

let typewriter = new Typewriter(app, {
  loop: true,
  delay: 75,
});

typewriter
  .pauseFor(2500)
  .typeString('¡TU HOGAR EN PLENO CORAZON DE SANTIAGO!')
  .pauseFor(200)
  .deleteChars(10)
  .start();

  /*===========================FOOTER==================================*/

  const footer = document.querySelector('.footer');

  const footerContainer = document.createElement('div');
  footerContainer.classList.add('footer-container');
  
  const column1 = document.createElement('div');
  column1.classList.add('column');
  column1.innerHTML = `
    <h3>Información de contacto:</h3>
    <p>Teléfono: +56 9 1234 5678</p>
    <p>Correo electrónico: info@vidaplena.com</p>
  `;
  
  const column2 = document.createElement('div');
  column2.classList.add('column');
  column2.innerHTML = `
    <h3>Información Importante:</h3>
    <ul>
      <li><a href="formulario.html">Contacto</a></li>
      <li><a href="#">Preguntas frecuentes</a></li>
      <li><a href="#">Términos y condiciones</a></li>
    </ul>
  `;
  
  const column3 = document.createElement('div');
  column3.classList.add('column');
  column3.innerHTML = `
    <h3>¡Suscríbete a nuestro boletín!</h3>
    <p>Mantente informado sobre nuestras actividades, eventos y consejos para una vida plena y saludable.</p>
    <form>
      <input type="email" placeholder="Correo electrónico" required>
      <button type="submit">Suscribirse</button>
    </form>
  `;
  
  footerContainer.appendChild(column1);
  footerContainer.appendChild(column2);
  footerContainer.appendChild(column3);
  footer.appendChild(footerContainer);
  