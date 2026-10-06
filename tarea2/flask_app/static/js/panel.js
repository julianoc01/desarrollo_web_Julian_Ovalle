
const formulario = document.getElementById("formAvistamiento");
const listaAvistamientos = document.getElementById("listaAvistamientos");

formulario.addEventListener("submit", function(event) {
    // Evita que la página se recargue
    event.preventDefault();

    // Obtener los datos del formulario
    const ave = document.getElementById("ave").value;
    const fecha = document.getElementById("fecha").value;
    const lugar = document.getElementById("lugar").value;
    const comentario = document.getElementById("comentario").value;
    const foto = document.getElementById("foto").files[0];

    // Crear un elemento para el nuevo avistamiento
    const avistamiento = document.createElement("div");

    // Añadir los datos
    avistamiento.innerHTML = `
<h3>${ave}</h3>
<p><strong>Fecha:</strong> ${fecha}</p>
<p><strong>Lugar:</strong> ${lugar}</p>
<p><strong>Comentario:</strong> ${comentario}</p>
    `;

    // Si se ha seleccionado una foto o video
    if (foto) {
        const imagen = document.createElement("img");

        imagen.src = URL.createObjectURL(foto);
        imagen.alt = "Foto del avistamiento";

        imagen.style.width = "150px";
        imagen.style.height = "150px";
        imagen.style.objectFit = "cover";

        avistamiento.appendChild(imagen);
    }

    // Añadir el avistamiento a la lista
    listaAvistamientos.appendChild(avistamiento);

    // Limpiar el formulario
    formulario.reset();
});

