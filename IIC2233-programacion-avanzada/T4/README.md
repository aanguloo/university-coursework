# Tarea 4: DCCaída de palabras

## Consideraciones generales :octocat:

La tarea es capaz de simular y trabajar en networking con codificación y decodificación de mensajes enviados y recibidos. Se puede ver una ventana de inicio que simula el inicio del juego. La tarea no es capaz de simular el juego, pero maneja bien el flujo entre interacción del cliente y servidor.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### 🟠 Cliente (63 pts)
##### Ventana de Inicio	🟠
Se visualiza correctamente la ventana. Se muestran todos los elementos mínimos solicitados en el enunciado. Pero no se implementa las notificaciones ni el flujo hacia otras ventanas. Y si un cliente no logra conectarse, aparece en la consola del cliente que no se establecio conexion.

##### Ventana principal	❌
No se implementa

##### Ventana de Juego	❌
No se implementa

#### ✅ Networking (46 pts)
##### ✅ Networking General	
correcto uso TCP/IP, si algun cliente se desconecta el servidor sigue funcionando. Se intancian y conectan los sockets y no se bloquean al escuchar un socket.

##### ✅Codificación y decodificación			
Se envia el largo del contenigo (correcto) y luego el contenido. Se desordenan los paquetes de manera correcta. Cada paquete tiene su número correspondiente y la cantidad de bytes correcta. Se rellenan con bytes ceros correctamente si no es un divisor de 124. Se aplica XOR al paquete antes de enviarlo. Se obtiene el objeto correctamente y solo se envia un mensaje completo a la vez.

#### 🟠 Servidor (108 pts)
##### 🟠 General
si algun cliente se desconecta, se muestra en el servidor el mensaje de desconexion en consola.

##### ❌ Creación de partidas		
No fue implementado nada de este apartado.

##### ❌ Durante la partida			
No fue implementado nada de este apartado.														
##### ❌ WebServices	
No fue implementado nada de este apartado.	

#### ❌ WebServices (40 pts)
No fue implementado
#### 🟠 Archivos (18 pts)
Se respeta la organización minima pedida en el directorio, se trabaja correctamente con conexion.json y se implementan el archivo de parametros y se trabaja con estos como se dice en el enunciado. No se trabaja con dcconjuntos.
#### ❌ Bonus (4 décimas)
No implementado

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` en la carpeta servidor y ```main.py``` en la carpeta cliente (si se quiere visualizar la ventana de inicio se debe ejectuar ```ventanas.y```). Además se debe crear los siguientes archivos y directorios adicionales:

1. directorio ```servidor``` en ```T4```
2. directorio ```cliente``` en ```T4```
3. directorio ```backend``` en ```cliente```
4. directorio ```frontend``` en ```cliente```
5. directorio ```sprites``` en ```frontend```
6. directorio ```dcconjuntos``` en ```servidor```
7. ```conexion.json``` en ```servidor```
8. ```conexion.json``` en ```backend```
9. ```parametros.py``` en ```servidor```
10. ```parametros.py``` en ```cliente```
11. ```main.py``` en ```cliente```
12. ```main.py``` en ```servidor```
13. ```server.py``` en ```servidor```
14. ```networking.py``` en ```backend```
15. ```ventanas.py``` en ```frontend```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```shuffle``` para desordenar los paquetes
2. ```json```: ```load, loads, dumps``` para la serialización
3. ```socket```: para  trabajar el networking
4. ```sys```: ```exit```: para salir de los widgets
5. ```threading```: para trabajr con threads el manejo del server y el usuario
6. ```PYQT5``` (se instala): ```PyQt5.QtGui, PyQt5.QtCore, PyQt5.QtWidgets```  para trabajar en las interfaces gracias.
7. ```os```: ```path``` para manejar correctamente el uso de paths. 


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```propiedades.py```: contiene todos los valores constantes
2. ```server.py```: Contiene la clase servidor que maneja el flujo de este y las apis (no implementadas)
3. ```networking.py```: Contiene la clase cliente que maneja el flujo de los usuarios

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Se escogio que la ip sea localhost
2. Tanto server y cliente se trabaja con la ip y port de conexion.json dentro del init de estos.


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://stackoverflow.com/questions/20243637/pyqt4-center-window-on-active-screen>: este centra automaticamente la interfaz grafica al medio de la pantalla y está implementado en el archivo <ventanas.py> en las líneas 62-68
2. \<https://doc.qt.io/qt-6/stylesheet-examples.html>: documentación sobre estilos para personalizar las interfaces en pyqt5, esta en <ventanas.py> en las lineas 17-59
3. \<https://www.youtube.com/watch?v=735dNm-ar_0>: guia sobre estilos para personalizar widgets las interfaces en pyqt5, esta en <ventanas.py> en las lineas 17-59
4. \<https://github.com/IIC2233/contenidos/blob/main/semana-13-networking-y-webservices/1-Networking-ejemplos.ipynb>: ocupado como base para crear los usuarios y el servidor, esta en <networking.py> y <servidor.py>, su estructura fue la base para crear las clases pero fue modificada.
5. \<https://github.com/IIC2233/Syllabus/tree/main/Experiencias/EX02/solucion>: ocupado como base para crear los usuarios y el servidor, esta en <networking.py> y <servidor.py>, su estructura fue la base para crear las clases pero fue modificada.

# Registro de cambios a la Tarea

+ Lunes 9 de junio: Se sube la tarea al Syllabus
