# Ejercicio Módulo 03 - Contenedores y virtualización

Este repositorio contiene la resolución del ejercicio del Módulo 03 - Contenedores y virtualización del Máster de IA, Cloud Computing y DevOps de Pontia.

## Contenido

En el repositorio se definen los siguientes archivos y carpetas:

- El directorio `api` contiene todo el código de la api. El código es simple: una api con un CRUD básico para listar, crear y eliminar perros en una base de datos. La tabla `dogs` tiene tres columnas: `id` como clave primaria, `name` con el nombre y `age` con la edad. Se utiliza Pydantic para definir los esquemas de petición y respuesta a la API, con algunas restricciones. Se devuelven los siguientes códigos de estado:
  - `200 - OK` para cualquier acción exitosa de GET o POST.
  - `203 - No content` para acciones exitosas DELETE.
  - `404 - Not found` para el caso de no encontrar el id en base de datos.
  - `422 - Unprocessable entity` para peticiones con campos erróneos.
- En `Dockerfile` se define la imagen para construir la api. Parte de `python:3.11-alpine` y simplemento copia el requirements, instala librerías, copia el codebase y lanza el servicio con `uvicorn` en el puerto 8080.
- En `docker-compose.yaml` se definen los dos servicios: api y database:
  - `api` es el servicio que construye la imagen de la API. Recibe variables de entorno necesarias para acceder correctamente a la base de datos, que estará en otro servicio funcionando simultáneamente. Como la base de datos suele tardar un poco en inicializarse, se pone como condición el `service_healthy` para la dependencia.
  - `database` es el servicio que aloja la base de datos. Se utiliza la imagen `postgres:15`. Se crea un volumen nombrado para que los datos se hagan persitentes y no se eliminen tras para el contenedor. Se le pasa tanto el user como la password como variables de entorno, definidas en un .env.

Por defecto, al lanzar `docker compose up` tomará el `.env` para inyectar variables de entorno. Dejo un ejemplo de variables definidas en `example.env`. Para usarlo, cambiarlo a `.env` o pasarlo como argumento al comando de docker compose (`docker compose up --env-file example.env`).

Ambos servicios se lanzan sobre una red común llamada `pontia`.

## Uso

Para lanzar, ejecutar el siguiente comando sobre el directorio raíz:

```shell
docker compose up --build
```
