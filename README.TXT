Game Service API

Este proyecto contiene una API para gestionar información relacionada con juegos. Proporciona operaciones básicas para crear, leer, actualizar y eliminar (CRUD) juegos en una base de datos.

equisitos Previos

Asegúrate de tener instalado Python y las dependencias necesarias. Puedes instalar las dependencias utilizando el siguiente comando:

pip install -r requirements.txt


Configuración

1. Configuración de la Base de Datos:**
   - El proyecto utiliza una base de datos para almacenar la información de los juegos. Asegúrate de tener una base de datos configurada y actualiza la configuración en el archivo `config/database.py`.

2. Ejecución de la Aplicación:**
   - Ejecuta la aplicación con el siguiente comando:

     uvicorn main:app --port 5000 --reload

   - La aplicación estará disponible en el navegador web ubicando localhost:5000

Uso de la API

La API proporciona varios endpoints para interactuar con la información de los juegos. Puedes explorar la documentación interactiva de la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para obtener detalles sobre los endpoints disponibles y cómo utilizarlos.

Ejemplos de Operaciones:

- Obtener Todos los Juegos:**
  - Método: GET
  - Ruta: `/games`

- Obtener un Juego por ID:**
  - Método: GET
  - Ruta: `/games/{id}`

- Crear un Nuevo Juego:**
  - Método: POST
  - Ruta: `/games`
  - Cuerpo de la Solicitud (JSON):

    ```json
    {
      "nombre": "Nuevo Juego",
      "categoria": "Aventura",
      "calificacion": 9.5
    }
    ```

- Actualizar un Juego Existente:**
  - Método: PUT
  - Ruta: `/games/{id}`
  - Cuerpo de la Solicitud (JSON):

    ```json
    {
      "nombre": "Juego Actualizado",
      "categoria": "Estrategia",
      "calificacion": 8.7
    }
    ```

- **Eliminar un Juego por ID:**
  - Método: DELETE
  - Ruta: `/games/{id}`