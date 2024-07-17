// js de formulario
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
  
    form.addEventListener('submit', function(event) {
      event.preventDefault();
  
      const nameInput = document.getElementById('name');
      const emailInput = document.getElementById('email');
      const phoneInput = document.getElementById('phone');
      const subjectInput = document.getElementById('subject');
      const messageInput = document.getElementById('message');
  
      // Validar campos
      if (nameInput.value.trim() === '') {
        alert('Por favor, ingresa tu nombre.');
        return;
      }
  
      if (emailInput.value.trim() === '') {
        alert('Por favor, ingresa tu correo electrónico.');
        return;
      }

      if (phoneInput.value.trim() === '') {
        alert('Por favor, ingresa tu teléfono.');
        return;
      }

      // Validar formato de teléfono en Chile con +56
      const phoneRegex = /^\+56\s?[2-9]\d{1}\s?\d{7}$/;
      if (!phoneRegex.test(phoneInput.value.trim())) {
        alert('Por favor, ingresa un número de teléfono válido de Chile con el formato +56 9XXXXXXXX.');
        return;
      }

      if (subjectInput.value.trim() === '') {
        alert('Por favor, ingresa el asunto.');
        return;
      }
  
      if (messageInput.value.trim() === '') {
        alert('Por favor, ingresa tu mensaje.');
        return;
      }
  
      // Enviar formulario (aquí iría la lógica para enviar el formulario)
      alert('¡Formulario enviado exitosamente!');
      form.reset();
    });
});
