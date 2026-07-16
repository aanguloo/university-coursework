## integrantes:
# Version POSTGRESQL

Se utilizo la versión 18.3 de PostgreSQL para el desarrollo de esta tarea. Es importante asegurarse de tener esta versión o una compatible para evitar problemas de compatibilidad con las funciones y características utilizadas en los scripts SQL proporcionados.

# Como ejecutar la tarea

Como el orden de los pasos es inverso, se debe seguir las siguientes instrucciones: 

1. Crear la base de datos `bookstore_g3` en PostgreSQL.
2. Importar el archivo `schema.sql` para crear las tablas necesarias.(`psql -d bookstore_g3 -f schema.sql`)
3. Importar el archivo `data.sql` para llenar las tablas con datos de ejemplo. (`psql -d bookstore_g3 -f data.sql`)
4. Aplicar el script de `matview.sql` para crear las vistas necesarias. (`psql -d bookstore_g3 -f matview.sql`)
5. Aplicar el script de `indexes.sql` para crear los índices necesarios. (`psql -d bookstore_g3 -f indexes.sql`)
6. Correr el `workload_after.sql` para ejecutar las consultas y medir su rendimiento. (`python3 run_workload.py --db bookstore_g3 \--workload workload_after.sql \--csv times_after.csv`)

# Bonus: Explain 

Se añadieron dos archivos donde se ejecutan las consultas con `EXPLAIN ANALYZE` para mostrar el plan de ejecución de cada consulta antes y después de la optimización. Estos archivos son `explain_before.sql` y `explain_after.sql`. Para explain after se recomienda crear otra base de datos llamada `bookstore_g3_copy` y aplicar los scripts de optimización antes de ejecutar el explain.
