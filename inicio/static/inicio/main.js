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

  document.addEventListener("DOMContentLoaded", function () {
    const footer = document.querySelector('.footer');
    if (!footer) return;

    // Crear el contenedor principal del footer
    const footerContent = document.createElement('div');
    footerContent.className = 'footer-content';

    // Crear el contenedor para los iconos sociales
    const socialIcons = document.createElement('div');
    socialIcons.className = 'social-icons';

    // Definir las redes sociales
    const socialNetworks = [
        { name: 'Facebook', icon: 'fab fa-facebook-f', url: 'https://www.facebook.com/login/' },
        { name: 'Twitter', icon: 'fab fa-x', url: 'https://x.com/' },
        { name: 'Instagram', icon: 'fab fa-instagram', url: 'https://www.instagram.com/' }
    ];

    // Crear los iconos de redes sociales
    socialNetworks.forEach(network => {
        const link = document.createElement('a');
        link.href = network.url;
        link.className = 'social-icon';
        link.setAttribute('aria-label', network.name);

        const icon = document.createElement('i');
        icon.className = network.icon;

        link.appendChild(icon);
        socialIcons.appendChild(link);
    });

    // Crear el texto de copyright
    const copyright = document.createElement('p');
    copyright.className = 'copyright';
    copyright.textContent = '© 2024 VidaPlena. Todos los derechos reservados.';

    // Agregar todo al footer
    footerContent.appendChild(socialIcons);
    footerContent.appendChild(copyright);
    footer.appendChild(footerContent);

    // Estilos inline (considera mover esto a un archivo CSS separado)
    footer.style.backgroundColor = '#f8f9fa';
    footer.style.padding = '20px 0';
    footer.style.textAlign = 'center';

    footerContent.style.maxWidth = '1200px';
    footerContent.style.margin = '0 auto';

    socialIcons.style.marginBottom = '15px';

    const icons = footer.querySelectorAll('.social-icon');
    icons.forEach(icon => {
        icon.style.color = '#333';
        icon.style.fontSize = '24px';
        icon.style.margin = '0 10px';
        icon.style.textDecoration = 'none';
    });

    copyright.style.color = '#666';
    copyright.style.fontSize = '14px';
});