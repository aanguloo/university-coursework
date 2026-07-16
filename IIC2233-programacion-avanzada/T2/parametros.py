from os import path

DINERO_INICIAL = 100
GANANCIA_POR_RONDA = 25
DINERO_CACTOOS = 15

path_arboles_faciles = path.join("data", "arboles_faciles.txt")
path_arboles_medios = path.join("data", "arboles_medios.txt")
path_arboles_dificiles = path.join("data", "arboles_dificiles.txt")
path_ramas = path.join("data", "ramas.txt")
path_modificadores = path.join("data", "modificadores.txt")
path_modificadores_negativos = path.join("data", "modificadores_negativos.txt")
dificultades = {"facil", "normal", "dificil"}

"""aca hay que poner todos los parametros y paths contantes
por ejemplo si hay una clase rana donde tiene una vida y defensa
la manera incorrecta de hacerlo seri definir self.vida = constante,
si no la mejor manera de hacerlo seria self.vida = modulo.variable_vida
recuerda que en el issue de path de parametros esta mejor explicado"""