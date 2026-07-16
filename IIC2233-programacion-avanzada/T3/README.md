# Tarea 3: DCC 🗣️❔❔

## Consideraciones generales :octocat:

La terea implementa adecuadamente el uso de generadores y funciones generadoras para trabajar un sistema de gestion de pedidos, productos y usuarios. Se ocupa adecuadamente diversas funciones (map, filter, etc) y generadores para trabajar de manera eficiente la información necesaria entregada en los archivos .csv. No se implemento el uso de interfaces grafícas, por ende, no existe interacción posible con el usuario.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Cargar Datos: 12 pts (9%) ✅
##### ✅ Cargar usuarios
Implementado totalmente, carga la informacion de los usuarios del archivo.csv y retorna un generador con las instancias de la namedtuple Usuarios.
##### ✅ Cargar productos
Implementado totalmente, carga la informacion de los productos del archivo.csv y retorna un generador con las instancias de la namedtuple Productos.
##### ✅ Cargar ordenes
Implementado totalmente, carga la informacion de las ordenes del archivo.csv y retorna un generador con las instancias de la namedtuple Ordenes.
##### ✅ Cargar ordenes_items
Implementado totalmente, carga la informacion de las ordenes_items del archivo.csv y retorna un generador con las instancias de la namedtuple OrdenesItems.
##### ✅ Cargar proveedores
Implementado totalmente, carga la informacion de los proveedores del archivo.csv y retorna un generador con las instancias de la namedtuple Proveedores.
##### ✅ Cargar proveedores_productos
Implementado totalmente, carga la informacion de los proveedores_productos del archivo.csv y retorna un generador con las instancias de la namedtuple ProveedoresProductos.


#### Consultas Simples: 31 pts (23%) ✅
##### ✅ productos_desde_fechas()
Implementado totalmente, retorna el generador de productos dependiendo del valor del bool en un tiempo adecuado.
##### ✅ buscar_orden_por_contenido()
Implementado totalmente, retorna el generador de id_base_datos dependiendo del producto y la cantidad indicada en un tiempo adecuado.
##### ✅ proveedores_por_estado()
Implementado totalmente, retorana el generador con los proveedores que este en el estado en un tiempo adecuado.
##### ✅ ordenes_segun_estado_orden()
Implementado totalmente, retorana el generador con las ordenes que tengan  el estado de orden indicado en un tiempo adecuado.
##### ✅ ordenes_entre_fechas()
Implementado totalmente, retorna el generador con las ordenes que esten entre las fechas indicadas en un tiempo adecuado
##### ✅ modificar_estado_orden_ordenes_previas_fecha()
Implementado totalmente, retorna el generador con las ordenes modificadas en un tiempo adecuado.

#### Consultas Complejas: 70 pts (52%)
##### ❌producto_mas_popular()
No implementado.
##### ✅ ordenes_usuario()
Implementado totalmente, retora el diccionario con la id de los usuarios como llaves y como valor el diccionario de las id de productos que ordeno como llave y la cantidad de estos como valor en un tiempo adecuado.
##### ✅ valor_orden()
Implementado totalmente, retorna el valor total de las ordenes de los generadores entregados en un tiempo adecuado.
##### ❌ proveedores_segun_precio_productos()
No implementado.
##### ✅ precio_promedio_segun_estado_orden()
Implementado totalmente, retorna el costo total promedio de las ordenes segun el estado de orden indicado en un tiempo adecuado.
##### ✅ cantidad_vendida_productos()
Implementado totalmente, retorna el diccionario con las id de productos y sus unidades totales vendidas en un tiempo adecuado.
##### ✅ ordenes_dirigidas_al_estado()
Implementado totalmente, retorna un generador con las ordenes que tengan direccion en el estado entregado en un tiempo adecuado.
##### ✅ ganancias_dadas_por_clientes()
Implementado totalmente, retorna el diccionario con las id de los usuarios y sus ganancias totales en un tiempo adecuado.
##### ✅ modificar_estados_ordenes_dirigidas_al_estado()
Implementado totalmente, retorna el generador con las instancia de Ordenes que tengan direccion en el estado indicado y que se les modifico su estado de orden en un tiempo adecuado.
##### ✅ agrupar_items_por_maximo_pedido()
Implementado totalmente, retorna el generador con instancias productos que fueron modificados o no dependiendo de la max-cantidad-ordenada en un tiempo adecuado.

#### Interfaces gráficas e interacción: 12 pts (9%) ❌
##### ❌ Ventana de entrada
No fue implementada en la tarea
##### ❌ Ventana Principal
No fue implementada en la tarea

#### PEP8 y Modularización ✅
hay un uso adecuado de PEP8. Lineas con no más de 100 caracteres, uso de snake_case y variables descriptivas y ningun archivo ocupa más de 400 lineas. Se modularizo adecuadamente.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```consultas.py``` debido a que en ```main.py``` no se implemento el uso de interfaces graficas y la union entre el backend y el frontend . Para que todo funcione correctamente, debe existir:

1. ```consultas.py``` en ```backend/```
2. ```utilidades.pyc``` en ```backend/```
3. ```backend/``` en ```T3```
4. ```parametros.py``` en ```T3```

Si se hubierai implementado las interfaces graficas, es necesario que exista.
5. ```main.py``` en ```T3```
6. ```frontend.py``` en ```frontend/```
7. ```frontend/``` en ```T3```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```date``` para trabajar con fechas de manera más sencilla.
2. ```utilidades```: ```fecha_actual(), cambio_unidad_medida(), ``` 


### Librerías propias
Por otro lado, No se crearon modulos a la hora de realizar la tarea.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El tamaño de los archivos, puede variar. Es decir, que un archivo.csv grande puede tener N elementos, pero quizas otro archivo.csv grande, puede tener N - 1 elementos. Esto permite buscar una manera eficiente de que los metodos implementados sean rapidos para cualquier archivo.




-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/2166147/namedtuple-replace-doesnt-work-as-described-in-the-documentation  saque el metodo _replace que permite cambiar los valores kwargs de las namedtuples y está implementado en el archivo <consultas.py> 
2. https://docs.python.org/es/3.9/library/datetime.html saque toda la informacion de date para poder comparar fechas y esta implementado en el archivo <consulta.py> en la mayoria de metodos que piden comparar fechas.

# Registro de cambios a la Tarea

+ Viernes 16 de mayo: Se sube la tarea al Syllabus.
+ Viernes 16 de mayo: Se agrega el archivo .pyc a la carpeta T3/.
+ Sábado 17 de mayo: Se arregló el archivo `utilidades.pyc` para calzar con la información del enunciado y se generó una copia de éste en el directorio `backend/`.
+ Lunes 19 de mayo: 
    - Se actualizó el enunciado para remover el atributo `id_producto` del `NamedTuple` `Productos` y corregir otras inconsistencias sobre las consultas, junto a otros puntos.
    - Se actualizaron los tests para estar acordes al enunciado y evitar errores en ellos por inconsistencias.
    - Se agregó el archivo `parametros.py` al directorio base. Esto con el objetivo de que puedan usar las variables definidas en él como _kwargs_ de las funciones de `consultas.py` al momento de ser llamadas por la Interfaz Gráfica. No es necesario que ignoren dicho archivo y no habrá descuento por subirlo al repositorio.
+ Jueves 22 de mayo: Se actualizan los *links* de los datos y tests publicos. Ocurren los siguientes cambios:

    * Datos:
        - Ya no existen entradas, en cualquier archivo `productos.csv`, con  `identificador_del_proveedor` repetidos, todos son unicos.
        - Ya no existen entradas, en cualquier archivo `proveedores_productos.csv`, con  `identificador_del_proveedor` repetidos, todos son unicos.
        - Ya no existen entradas, en cualquier archivo `proveedores.csv`, con  `nombre_proveedor` repetidos, todos son unicos.


    * Tests Públicos:
        - Se arregló el test `test_07_producto_mas_popular_correctitud.py` para calzar con el enunciado.
        - Se adaptó la solución `solution/test_01.py` para calzar con los nuevos datos.
        - Se adaptó la solución `solution/test_10.py` para calzar con los nuevos datos.
        - Se adaptó la solución `solution/test_16.py` para calzar con los nuevos datos.
        - Se adaptaron las descripciones de algunos tests para que calcen con lo que el test verifica.
+ Viernes 23 de mayo: Se actualizan los *links* de los datos y tests publicos. Ocurren los siguientes cambios:

    * Enunciado:
        - Se corrigió la descripción de la función `producto_mas_popular`. Ahora esta dice "Si se produce un empate en popularidad entre dos
        productos, se debe realizar un desempate según el atributo `id_base_datos`, ordenándolos de manera **descendiente**".

    * Datos:
        - Se corrigió el error de que se encuentren productos asociados en `proveedores_productos.csv` pero no se encuentren en `productos.csv`.
        - Se verificó que todos los productos que aparecen en `ordenes_items.csv` aparezcan en `productos.csv`.
        - Puede ser que aparezcan productos en `productos.csv` que posean un `identificador_del_proveedor`, pero que no aparezcan en el archivo `proveedores_productos.csv` -> Esto NO es un error. Asuman que el proveedor que vende dicho producto no está en ese dataset.
        - Puede ser que aparezcan proveedores en `proveedores.csv` que posean un `nombre_proveedor`, pero que no aparezcan en el archivo `proveedores_productos.csv` -> Esto NO es un error. Asuman que el proveedor no vende productos en dicho dataset.

    * Tests Públicos:
        - Se adaptó el test `test_03_proveedores_por_estado_carga_datos.py` para que ahora se verifique el orden en que se retornan los datos, no solo que los datos sean correctos. Sigan el orden que menciona el enunciado.
        - Se adaptó el test `test_00_cargar_datos.py` para que calze con las nuevas versiones de los archivos que se subieron.
        - Se adaptó el test `test_07_cargar_datos.py` para que calze con la modificación del enunciado.
        - Se adaptó el test `test_07_correctitud.py` para incluir un caso relacionado a la modificación del enunciado.
        - Se adaptó el test `test_15_modificar_estados_ordenes_dirigidas_al_estado_correctitud.py` para que calze con el enunciado, el cual menciona que: "Retorna un generador con instancias de `Ordenes` correspondientes a usuarios que poseen una dirección dentro del estado de Estados Unidos entregado (estado), donde los estados de orden son modificados de acuerdo a lo indicado por el diccionario de transición de estados (cambio_estados_ordenes).".
        - Se adaptó el test `test_16_agrupar_items_por_maximo_pedido_carga_datos.py` para que la fecha_actual siempre calce.
        - Se adaptó la solución `test_10.py` para que calze con las nuevas versiones de los archivos que se subieron.
        - Se adaptó la solución `test_15.py` para que calze con la nueva adaptación de su test.
        - Se adaptó la solución `test_16.py` para que calze con las nuevas versiones de los archivos que se subieron.
