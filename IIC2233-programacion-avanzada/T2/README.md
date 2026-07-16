# Tarea 2: DCConquista de Yggdrasil 🌳

## Consideraciones generales :octocat:

La tarea modela el comportamiento de las clases ramas y arbol de forma adecuadamente ocupando poo avanzado. Sin embargo no es capaz de simular todo el juego en si y solo se puede ver algunas interacciones con el menu de inicio. Presenta algunos errores al escoger al azar el arbol generando NoneType el arbol enemigo. El juego no se puede jugar, pero si se puede acceder a los menus y ocurren los funcionamientos de cada parte pedida. Se implemento cada metodo pedido y cada atributo de clase y cada una. Ademas no se logro implementar algun metodo que permita que cada rama tenga sus ramas hijas. pero se dejo representado como deberia funcionar el programa.

### Cosas implementadas y no implementadas :white_check_mark: :x:

##### ✅ Programación Orientada a Objetos (16 pts)
Se incluye herencia, polimorfismo, clases abstractas y propertys (decoradores) de manera adecuada. Principalmente, se puede observar todo esto en la clase  ```Ramas```

##### ✅ Preparación programa (15 pts)
El programa recibe la dificultad por consola y muestra la selección inicial de forma adecuada segun el argumento entregado. El jugador luego de seleccionar un arbol, comienza con este arbol y el arbol enemigo es escogido de manera aleatoria entre los posibles arboles. y se muestra el cuadro de resumen.

##### 🟠 Entidades (55 pts)
La clase ramas y todos sus atributos son implementados. (Falta hybried). La clase arbol falta ataque solamente.

##### 🟠 Flujo del programa (31 pts)
El menu principal contiene todas las opciones pedidas. La tienda tiene todos los modificadores con sus respectivos precios y toda la informacion pedida. La opcion de volver al menu de inicio funciona correctamente. Se pone en la rama pedida el modificador correspondiente. Pasar ronda sin atacar funciona, pero pasar ronda y atacar no esta implementado. No hay fin del juego tampoco.

##### ❌ Combate (25 pts)
No se realizado

##### ✅ Archivos (15 pts)
Se trabaja adecuadamente con todos los archivos del enunciado,ademas parametro.py contiene todos los valores constantes dados por el enunciado y los que fueron añadidos al programa.

##### ❌ Bonus (5 décimas)
no se realizo.


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además deben exitir los siguientes archivos y directorios adicionales:
1. directorio ```menus``` en ```T2```
2. directorio ```entidades``` en ```T2```
3. ```arbol.py``` en ```entidades```
4. ```funciones_extras.py``` en ```entidades```
5. ```ramas.py``` en ```entidades```
6. ```modificadores``` en ```entidades```
3. ```menu_y_tienda.py``` en ```menus```
4. ```seleccion_inicial``` en ```menus```
5. ```main.py``` en ```T2```
6. ```parametros.py``` en ```T2```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```Collections```: ```Deque```
2. ```abc```: ```ABC``` 
3. ```Random```: ```Choice y Random```
4. ```sys```: ```argv```
4. ```math```: ```floor```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```arbol.py```: Contiene a la clase ```Arbol`` y todos sus metodos y atributos.

2. ```ramas.py```: Contiene a ```Ramas``` clase abstracta que contiene todos los metodos pedidos, además de contener todas las subclases que heredan los metodos y modifican algunos, estas son ```Ficus```, ```Celery```, ```Hyedrid```, ```Paalm```, ```Alovelis```, ```Pine```, ```Cactoos```

3. ```modificadores.py```: Contiene la clase abstracta ```Modificadores``` que contiene los atributos pedidos, además contiene dos subclases que heredan los atributos. ```ModificadoresPositivos```, ```ModificadoresNegativos```  

4. ```funciones_extras.py```: Contiene las funciones ```crear_rama```, ```obtener_modificadores_positivos``` y ```obtener_modificadores_negativos```

5. ```menu_y_tienda.py```: Contiene a la clase ```MenuPrincipal``` que tiene el metodo ```Menu``` que sigue toda la logica de este apartado

6. ```seleccion_inicial.py```: Contiene a la clase ```SelecciónInicial`` que contiene los metodos ```facil```, 
```medio```, ```dificil``` , metodos que permiten el flujo dependiendo el programa.

7. ```parametros.py```: Contiene todos los valores constantes y paths utilizados durante la tarea.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. ```Floats redondeado a tres decimales```: debido al problema que tiene los floats como 0.3 o 0.5 a la hora de sumarlos y restarlos, se decide trabajar atributos como defensa o resistencia una precisión de 3 decimales.
2. ```Profundidad parte desde cero```: la rama principal tiene profundidad cero.

