from sys import argv
import parametros
import menus.seleccion_inicial as inicio_programa
import menus.menu_y_tienda as menu


if __name__ == "__main__":
    
    
    try:
        
        if len(argv) != 2:
            
            raise ValueError("Cantidad de argumentos entregados invalidos")
        
        dificultad_escogida = argv[1].strip(" ").lower()
        
        if dificultad_escogida not in parametros.dificultades:
            
            raise ValueError("Escoja una dificultad valida")
        
    except ValueError as error:
        
        print(error)
    
    else:
        if dificultad_escogida == "facil":
            
            jugador, enemigo = inicio_programa.SeleccionInicial.facil()
            print(f"\n JUGADOR: {jugador.resumir()}")
            print(f"\n ENEMIGO: {enemigo.resumir()}")
            print(f"BIENVENIDO AL JUEGO")
            
        elif dificultad_escogida == "normal":
            
            jugador, enemigo = inicio_programa.SeleccionInicial.medios()
            print(f"\n JUGADOR: {jugador.resumir()}")
            print(f"\n ENEMIGO: {enemigo.resumir()}")
            print(f"BIENVENIDO AL JUEGO")
        elif dificultad_escogida == "dificil":
            
            jugador, enemigo = inicio_programa.SeleccionInicial.dificil()
            print(f"\n JUGADOR: {jugador.resumir()}")
            print(f"\n ENEMIGO: {enemigo.resumir()}")
            print(f"BIENVENIDO AL JUEGO")

menu.MenuPrincipal.menu(jugador, enemigo)