
# Tarea 1: Base datos
## integrantes:
- **André Angulo** ✨  -2421003j
- **Fernanda Miranda** ✨ -24209716
- **Catalina Reyes** ✨ -24645516

## Requisitos previos
- Tener instalado `Node.js`.
- Tener instalado `PostgreSQL`.
- `npm install` no instala `Node.js` ni `PostgreSQL`; solo descarga las dependencias del proyecto dentro de la carpeta `app`.
- El servicio de `PostgreSQL` debe estar iniciado y la base de datos `tarea1` debe existir antes de ejecutar la aplicación.


## Cómo ejecutar la aplicación
1. Abrir PostgreSQL, crear la base de datos `tarea1` e importar primero `schema.sql` y luego `data.sql`.
2. En la carpeta descomprimida, entrar a la carpeta `app` y abrir una terminal.
3. Instalar dependencias con `npm install`.
4. Configurar las variables de entorno de PostgreSQL.
5. Ejecutar `npm start` y abrir `http://localhost:3000`.



## Variables de entorno necesarias
- `PGHOST`: host del servidor PostgreSQL.
- `PGPORT`: puerto de PostgreSQL.
- `PGDATABASE`: nombre de la base de datos.
- `PGUSER`: usuario de PostgreSQL.
- `PGPASSWORD`: contraseña del usuario.

Si estas variables no se definen, la aplicación usa los valores por defecto:
- host: `localhost`
- puerto: `5432`
- base de datos: `tarea1`
- usuario: `postgres`
- contraseña: `postgres`
