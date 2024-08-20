let currentIndex = 0;

function moveSlide(direction) {
    const slides = document.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;

    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = totalSlides - 1;
    } else if (currentIndex >= totalSlides) {
        currentIndex = 0;
    }

    const offset = -currentIndex * 100; // Mueve el carrusel
    document.querySelector('.carousel-inner').style.transform = `translateX(${offset}%)`;
}

function redirectToCourse() {
    window.location.href = 'course-page.html';
}

let contador = 0;

// Obtiene el elemento del contador y el botón
const contadorElement = document.getElementById('contador');
const inscribirseBtn = document.getElementById('inscribirseBtn');

// Añade un evento de clic al botón
inscribirseBtn.addEventListener('click', function() {
  // Incrementa el contador
  contador++;
  // Actualiza el contenido del elemento del contador
  contadorElement.textContent = contador;
});

