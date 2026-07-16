# Tarea 1: DCCortaRamas 🌳✂️

## Consideraciones generales

Se añadieron todos los metodos que se debian implementar en ```dccortaramas.py``` con ayuda de funciones extras que se encuentran en ```funciones_extras.py``` y con la función  importada adecuadamente de ```utilidades.pyc```. Se implemento todo lo pedido del menu  y consola en ```menu.py``` importando el contenido necesario de ```dccortaramas.py``` para finalmente ser importado a  ```main.py``` y ser ejecutado. Si alguno de estos archivos falta, no se podra ejecutar el codigo. La estrategia que se intento utilizar es de descontuir los bonsais, muchas de las funciones son recursivas por eso mismo. En el metodo ```simetria```, se descontruyo las ramas de hijos para compararlas gracias a las dos funciones que se encuentran en ```funciones_extras```.  Hay bastantes funciones similares en ```funciones_extras``` pero muchas a pesar que "realizan lo mismo" lo hacen de diverso modo permitiendo facilitar el trabajo en diversas situaciones. Como se menciona en el enunciado, se asume que existe la carpeta ```data``` y ```visualizaciones```, donde la primera guarda las subcarpetas donde se guardan los archivos ```.txt``` con la estructura de los bonsais y la segunda para el metodo ```visualizar_bonsai``` si es que ```guardar``` es True.

### Cosas implementadas y no implementadas :white_check_mark: :x:

##### ✅ Consola

Se hizo aprueba de errores y ambos menus presentan todas las posibles opciones a escoger. Se añadio funcionalidades extras que no se pidieron, como el volver atras o a la hora de salir, preguntar si estas seguro de salir. 

##### ✅ Menú de Inicio

uso adecuado del manejo de los inputs y outputs. Se puede salir del programa y la opción de cargar bonsai funciona adecuadamente. A la hora de pedir el archivo, si el usuario incluye o no el .txt, lo reconoce adecuadamente. Se implementaron "errores" si es que el usuario no escoge una accion valida dentro de las posibilidades.

##### ✅  Menú de Acciones

Uso adecuado del manejo de los inputs y outputs. Cada vez que se realiza una acción, se vuelve al menu de acción nuevamente. Aparecen las acciones en pantalla y cuando se realiza una acción se vuelve al menu principal. Se implemento que cuando se escoja una acción, si el usuario escribe volver, retrocedera. Se puede salir del programa. Visualizar bonsai permite al usuario escoger entre vertizal u horizontal. Se implementaron "errores" si es que el usuario no escoge una accion valida dentro de las posibilidades. Todas las acciones funcionan adecuadamente.

##### 🟠 Metodos de clases DCCortaramas

Se implementaron todos los metodos de clase solicitados, la mayoria funcionan adecuadamente. pero hay dudas en el funcionamiento adecuado de emparejar_bonsai_ahorro en ciertos casos sobretodo en bonsais pequeños u donde el precio de cortar y modificar son similares.

##### ✅ Modularización

Creacion de ```menu.py``` y ```funciones_extras.py``` que contienen funciones y clases que permiten el desarrollo adecuado de las modificaciones al archivo ```DCCortaramas.py```. Ademas de uso adecuado de importacion de librerias externas como os u typing. Ningun archivo se excede de las 400 lineas. 

##### 🟠 PEP8

Uso adecuado de PEP8 pero bastante mejorable, ninguna linea supera los 100 caracteres, se ocupo snake_case and CamelCase adecuadamente. Espacios despues de las comas. Uso de variable aclarativas, explicativas.

##### ✅ .gitignore

Se implemento correctamente .gitignore, git ignora los archivos que se encuentran ahí.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además deben estar y existir los siguientes archivos para que funcione correctamente:
1. ```menu.py``` en ```la misma localización de main.py```
2. ```funciones_extras.py``` en ```la misma localización de main.py```
3. ```DCCortaramas.py``` en ```la misma localización de main.py```
4. ```utilidades.pyc``` en ```la misma localización de main.py```
5. ```data``` en ```la misma localización de main.py```
6. ```visualizaciones``` en ```la misma localización de main.py```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```Typing```: ```List```
2. ```os```: ```Path``` 


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones_extras```: Contiene diversas funciones que permitieron el desarrollo de la terea como se_puede_editar, existe_nodo, tiene_flor, encontrar_hijos, etc.
2. ```menu```: Contiene la clase loop y tiene los dos metodos de clases que permiten generar el menu de inicio y de acciones.

## consideraciones adicionales :thinking:

1. ```Menú solicita orientación y emojis a la hora de la acción visualizar Bonsai```:  Esto para que el usuario tenga mejor posibilidades a la hora de visualizar el bonsai.
2. ```escribir "volver" para volver a la acción anterior del menú```: Si se escribe volver (no en el menu de inicio) se vuelve a la acción anterior
3. ```Podar, solo visualiza en modo vertical y emojis True```: como luego se modifica el bonsai, el usuario puede accionar visualizar bonsai.
4. ```Cuando se aplica la accion de podar, el bonsai se modifica```: esto para que el usuario pueda comprobar que la simetria y la estructura cambia
5. ``` Creación de gitignore luego de los primeros commits ```: Se borraron archivos en github porque luego de haber hecho los primeros commits, se creo el gitignore.