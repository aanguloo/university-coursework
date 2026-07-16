
import parametros
import entidades.modificadores as modificadores
import entidades.arbol as arbol
class MenuPrincipal:
    
    def menu(arbol, arbol_enemigo):
        
        dinero_disponible = parametros.DINERO_INICIAL
        ronda_actual = 1
        
        
        running = True
        while running:
            
            
            print("---------------")
            print(" MENÚ PRINCIPAL ")
            print("---------------\n")
            
            print(f"Dinero disponible: ${dinero_disponible}")
            print(f"Ronda Actual: {ronda_actual}\n")
            
            print("[1] Atacar y pasar ronda")
            print("[2] Pasar ronda sin atacar")
            print("[3] Tienda")
            print("[4] Ver información del arbol")
            print("[5] Espiar al árbol enemigo")
            print("[6] Salir del juego\n")
            
            opciones = {"1", "2", "3", "4", "5", "6"}
            
            try:
                opcion = input("Indique su opción: ").strip(" ")
                
                if not opcion in opciones:
                    
                    raise ValueError("Error! Escoja una opción valida")
                
            except ValueError as error:
                print(error)
            
            if opcion == "1":
                
                pass
            
            if opcion == "2":
                
                dinero_disponible += parametros.GANANCIA_POR_RONDA
                ronda_actual += 1
                
                for ramas in arbol.ramas:
                    ramas.pasar_ronda()
                for ramas in arbol_enemigo.ramas:
                    ramas.pasar_ronda()
            
            if opcion == "3":
                
                running_tienda = True
                modificador = modificadores.obtener_modificadores_positivos()
                opciones_extras = set("0")
                
                while running_tienda:
                    
                    print("---------------")
                    print("    TIENDA     ")
                    print("---------------\n")
                    print("[0] volver al menú")
                    
                    for i in range(len(modificador)):
                        
                        print(f"[{i + 1}] {modificador[i].nombre}  precio: "
                            f"{modificador[i].precio}$")
                        opciones_extras.add(str(i + 1))
                    
                    try: 
                        eleccion = input("indique su opción: ").strip(" ")
                        if eleccion not in opciones_extras:
                            raise ValueError("ERROR: ingrese una opción valida")
                    except ValueError as error:
                        print(error)

                    else:
                        
                        if eleccion == "0":
                            
                            running_tienda = False
                        
                        else:
                            
                            
                            modificador_escogido = modificador[int(eleccion) - 1]
                            running_rama = True
                            ramas_opciones = set()
                            while running_rama:
                                
                                if modificador_escogido.precio > dinero_disponible:
                                    
                                    running_rama = False
                                    print("No tiene dinero suficiente")
                                    break
                                
                                for i in range(len(arbol.ramas)):
                                    print("ramas disponibles")
                                    print((f"[{i + 1}] {arbol.ramas[i].nombre}, identificador = " 
                                        f"{arbol.ramas[i].identificador}"))
                                    ramas_opciones.add(str(i + 1))
                    
                                try: 
                                    eleccion = input("indique su opción: ").strip(" ")
                                    if eleccion not in ramas_opciones:
                                        raise ValueError("ERROR: ingrese una opción valida")
                                    
                                except ValueError as error:
                                    print(error)
                                
                                else:
                                    
                                    dinero_disponible = dinero_disponible - \
                                        modificador_escogido.precio
                                    print("Se ha cargado con exito")
                                    arbol.cargar_modificador(arbol.ramas[int(eleccion) - 1],\
                                        modificador_escogido)
                                    running_rama = False
            
            if opcion == "4":
                
                resumir_completo = {"resumir", "completo"}
                running_opcion_4 = True
                while running_opcion_4:
                    try:
                    
                        eleccion = input(("quiere verlo completo o resumido?"
                                        "[resumir, completo]: ")).strip(" ").lower()
                        
                        if eleccion not in resumir_completo:
                            raise ValueError("ERROR, ESCOJA UNA OPCIÓN DISPONIBLE")
                        
                    except ValueError as error:
                        print(error)
                    else:
                        
                        if eleccion == "resumir":
                            print(arbol.resumir())
                            running_opcion_4 = False
                        else:
                            print(arbol)
                            running_opcion_4 = False
                            
            if opcion == "5":
                
                print(arbol_enemigo.resumir())
            
            if opcion == "6":
                
                print("Saliendo del programa")
                running = False
                