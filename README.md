

# Pruebas Automatizadas para Urban Routes

---

## Descripción:

Este proyecto tiene el objetivo de testear la aplicacion web Urban Routes utilizando Selenium y Python,siguiendo el 
modelo de diseño POM (Page Object Model), con estas pruebas cubrimos el proceso de pedir un taxi con la aplicacion.
---
## Tecnologías utilizadas:

![Python](https://img.shields.io/badge/python-3.11.3-blue?logo=python)
![Pytest](https://img.shields.io/badge/pytest-8.2.0-blue?logo=pytest)
![Selenium](https://img.shields.io/badge/selenium-4.20.0-darkgreen?logo=selenium)
![Pycharm](https://img.shields.io/badge/pycharm-blue?logo=pycharm)
## Instalaciones:

1. Descarga de python 
2. Descarga de Pytest desde PyCharm 
3. Descarga de Git 
4. Descarga de paquete selenium, desde el comando pip install 
5. Descarga de paquete request, desde el comando pip install 
6. Clonar el repositorio 
7. Instalación de ChromeDriver
---

## Pasos realizados:
1. Definimos los localizadores requeridos
2. Definimos los metodos requeridos
3. Se crean las pruebas.

---
## Pruebas realizadas:
1. Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito. (Consejo: el botón 'link' (enlace) no se activa hasta que el campo CVV de la tarjeta en el modal 'Agregar una tarjeta', id="code" class="card-input", pierde el enfoque. Para cambiar el enfoque, puedes simular que el usuario o usuaria presiona TAB o hace clic en otro lugar de la pantalla).
El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación requerido para agregar una tarjeta.
5. Escribir un mensaje para el controlador.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.
9. Esperar a que aparezca la información del conductor en el modal (opcional). Además de los pasos anteriores, hay un paso opcional que puedes comprobar; este es un poco más complicado que los demás, pero es una buena práctica, ya que es probable que en tu trayectoria profesional encuentres tareas más difíciles.

---
# Ejecucion del proyecto

 Asegurate de tener instaladas las tecnologias antes mencionadas 
 y luego esperar a que se ejecuten las 9 pruebas. La ejecución finaliza cuando se cierra el navegador  exitosamente.
