// Definimos la URL de la API que nos conecta con el servidor Flask
const apiUrl = "http://127.0.0.1:5000/tareas";

/**
 * Función para añadir una tarea al servidor
 * - Obtiene el valor del input de texto y lo envía al servidor como JSON mediante una solicitud POST.
 */
function addTask() {
  // Obtener el valor del input donde el usuario escribe la tarea
  const task = document.getElementById("taskInput").value;

  // Si el campo de la tarea está vacío, no hacer nada
  if (task === "") return;

  // Realizar una solicitud POST al servidor para añadir la tarea
  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json", // Indicamos que estamos enviando JSON
    },
    body: JSON.stringify({ tarea: task }), // Convertimos la tarea a formato JSON
  })
    .then((response) => response.json()) // Convertimos la respuesta a JSON
    .then((data) => alert("Tarea añadida con éxito")) // Mostramos un mensaje de éxito
    .catch((error) => console.error("Error:", error)); // Capturamos y mostramos errores

  // Limpiar el campo de entrada de texto después de enviar la tarea
  document.getElementById("taskInput").value = "";
}

/**
 * Función para obtener la lista de tareas desde el servidor
 * - Hace una solicitud GET al servidor y muestra la lista de tareas en la página.
 */
function getTasks() {
  // Realizar una solicitud GET al servidor para obtener las tareas
  fetch(apiUrl)
    .then((response) => response.json()) // Convertimos la respuesta a JSON
    .then((data) => {
      // Limpiamos la lista de tareas existente
      const taskList = document.getElementById("taskList");
      taskList.innerHTML = "";

      // Recorremos cada tarea y la añadimos a la lista en HTML
      data.forEach((task) => {
        const li = document.createElement("li"); // Creamos un elemento <li>
        li.textContent = task; // Asignamos la tarea como texto del <li>
        taskList.appendChild(li); // Añadimos el <li> a la lista <ul>
      });
    })
    .catch((error) => console.error("Error:", error)); // Capturamos y mostramos errores
}

function deleteTasks() {
  console.log("ENTRO A ELIMINAR");

  fetch(apiUrl, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: null,
  })
    .then((response) => response.json())
    .then((data) => alert("Se eliminaron las tareas")) // Mostramos un mensaje de éxito
    .catch((error) => console.error("Error:", error)); // Capturamos y mostramos errores
}
