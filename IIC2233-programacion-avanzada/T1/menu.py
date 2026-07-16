import dccortaramas

import os


class Loop:

    def menu_inicio() -> dccortaramas.Bonsai:
        
        running_loop_principal = True
        
        acciones = {"1","2", 1, 2}
        
        while running_loop_principal == True:
            
            print("Bienvenidos a DCortaramas!\n")
            print("*** Menú De Inicio ***\n")
            print("[1] Cargar Bonsái\n[2] Salir del programa\n")
            print("#Para retroceder: volver#\n")
            opcion = input("ingrese una opción (1, 2): ").strip(" ")
            
            if not opcion in acciones:
                
                print("\nERROR! NO EXISTE OPCIÓN, INGRESE UN OPCIÓN VALIDA")
                
            elif opcion == "2":
                
                runnin_saliendo = True
                nuevas_opciones = {"si", "no"}
                
                while runnin_saliendo:
                    
                    respuesta = input("\n¿Esta seguro de salir? (si, no): ").strip(" ").lower()
                    
                    if respuesta == "si" and respuesta in nuevas_opciones:
                        
                        print("\nSaliendo del programa!")
                        return False
                    
                    if respuesta == "no" and respuesta in nuevas_opciones:
                        
                        runnin_saliendo = False
                        break
                    
                    if not respuesta in nuevas_opciones:
                        
                        print("ERROR! POR FAVOR ESCOJA ENTRE LAS OPCIONES POSIBLES")
                
            elif opcion == "1":
                
                running_loop_principal = False
                running_carpeta = True
                
                while running_carpeta:
                    
                    carpeta = input( "\ningrese el nombre de la carpeta: ").strip(" ")
                    path_1 = os.path.join("data", carpeta)
                    
                    if os.path.isdir(path_1):
                        
                        running_carpeta = False
                        running_archivo = True
                        
                        while running_archivo:
                            
                            archivo = input("\ningrese el nombre del archivo + .txt: ").strip(" ")
                            
                            if archivo == "volver":
                                
                                running_archivo = False
                                running_carpeta = True
                                break
                            
                            if not ".txt" in archivo:
                                
                                archivo = f"{archivo}.txt"
                            
                            else:
                                
                                archivo = archivo
                            
                            path = os.path.join(path_1, archivo)
                            
                            if os.path.isfile(path):
                                
                                print("\ningresando!!")
                                
                                bonsai = dccortaramas.Bonsai(f"{archivo}", 9, 9, [])
                                
                                bonsai.cargar_bonsai_de_archivo(carpeta, archivo)
                                
                                return bonsai
                            
                            else:
                                
                                print("\n ERROR!! EL ARCHIVO NO FUE ENCONTRADO")
                
                    else:
                        
                        if carpeta == "volver":
                                
                            running_loop_principal = True
                            running_carpeta = False
                            path_1 = ""
                            break
                        
                        print("\nERROR!! LA CARPETA NO FUE ENCONTRADA")
    
    def menu_de_acciones(bonsai):
        dcc = dccortaramas.DCCortaRamas()
        
        running_loop_principal = True
        
        acciones = {"1","2", "3", "4", "5", "6"}
        
        while running_loop_principal:
            
            print("Bienvenidos a DCortaramas!\n")
            print("*** Menú De Acciones ***\n")
            print("[1] Visualizar bonsái\n[2] Modficiar Hoja")
            print("[3] Cortar Rama\n[4] Verificar Simetría")
            print("[5] Podar Bonsái\n[6] Salir del programa\n")
            print("#Para retroceder: volver#\n")
            opcion = input("\ningrese una opción (1, 2, 3, 4, 5, 6): ").strip(" ")
            
            if not opcion in acciones:
                
                print("\nERROR! NO EXISTE OPCIÓN, INGRESE UN OPCIÓN VALIDA\n")
                
            elif opcion == "6":
                
                runnin_saliendo = True
                nuevas_opciones = {"si", "no"}
                
                while runnin_saliendo:
                    
                    respuesta = input("\n¿Esta seguro de salir? (si, no): ").strip(" ").lower()
                    
                    if respuesta == "si" and respuesta in nuevas_opciones:
                        
                        print("\nSaliendo del programa!")

                        return False
                    
                    if respuesta == "no" and respuesta in nuevas_opciones:
                        
                        runnin_saliendo = False
                        break
                    
                    if not respuesta in nuevas_opciones:
                        
                        print("ERROR! POR FAVOR ESCOJA ENTRE LAS OPCIONES POSIBLES")
            
            elif opcion == "1":
                
                running_orientacion = True
                
                while running_orientacion:
                    
                    orientaciones = {"Vertical", "Horizontal"}
                    orientacion = input("\n¿Vertical U Horizontal?: ").lower()
                    orientacion = orientacion.strip(" ").capitalize()
                    
                    if orientacion == "Volver":
                        
                        running_orientacion = False
                        break
                        
                    elif not orientacion in orientaciones:
                        print("\n ERROR!! Por favor, Escoja una de las dos opciones")
                        
                    else:
                        
                        running_emojis = True
                        
                        while running_emojis:
                            
                            emojis = {"True", "False"}
                            
                            emoji = input("\nCon emojis? (True, False): ").lower()
                            
                            emoji = emoji.strip(" ").capitalize()
                            
                            if emoji == "Volver":
                                running_emojis = False
                                break
                        
                            elif not emoji in emojis:
                                print("\nERROR!! Por favor, Escoja una de las dos opciones\n")
                            
                            else:
                                
                                bonsai.visualizar_bonsai(orientacion, emoji, False)
                                running_emojis = False
                                running_orientacion = False
                                break
                
            elif opcion == "2":
                
                running_flor = True
                
                while running_flor:
                    
                    identificador = input("\ningrese un identificador: ").lower()
                    identificador = identificador.strip(" ")
                    if identificador == "volver":
                        
                        running_flor == False
                        
                        break
                    
                    elif identificador.isdigit() == "False":
                        
                        print("\nERROR!! Por favor, Escoja un digito\n")
                    
                    else:
                        
                        se_realizo = dcc.modificar_nodo(bonsai, identificador)
                        
                        tiene_flor = dccortaramas.tiene_flor(bonsai.estructura, identificador)
                        
                        if tiene_flor == False and se_realizo == "Realizado":
                            
                            print("\nSe corto la flor\n")
                            
                        elif tiene_flor == True and se_realizo == "Realizado":
                            
                            print("\nSe añadio la flor\n")
                        
                        else:
                            print("\nno fue permitida la modificación\n")
                        
                        running_flor = False
                        break
                    
            elif opcion == "3":
                
                running_nodo = True
                
                while running_nodo:
                    
                    identificador_2 = input("ingrese un identificador): ").lower()
                    identificador_2 = identificador_2.strip(" ")
                    if identificador_2 == "volver":
                        
                        running_nodo == False
                        
                        break
                    
                    elif identificador_2.isdigit() == "False":
                        
                        print("\nERROR!! Por favor, Escoja un digito\n")
                    
                    else:
                        
                        hijos = dccortaramas.hijos(bonsai.estructura, identificador_2)
                        
                        se_realizo = dcc.quitar_nodo(bonsai, identificador_2)
                        
                        if se_realizo == "Realizado":
                            
                            print(f"\nse ha eliminado {identificador_2} y sus hijos: {hijos}\n")
                            
                        else:
                            
                            print("\nno fue permitida la modificación\n")
                        
                        running_nodo = False
                        break
                        
            elif opcion == "4":
                
                simetria = dcc.es_simetrico(bonsai)
                
                if simetria == True:
                    
                    print("\nEs Simetrico\n")
                
                else:
                    
                    print("\nNo es Simetrico\n")
                    
            elif opcion == "5":
                
                running_podar = True
                
                while running_podar:
                    
                    eleccion = {"si", "no"}
                    
                    ahorros = input("consideramos ahorrar? (si, no): ") 
                    
                    ahorros = ahorros.strip(" ").lower()
                    
                    if ahorros == "volver":
                        
                        running_podar == False
                        break
                    
                    if not ahorros in eleccion:
                        
                        print("\nERROR! NO EXISTE OPCIÓN, INGRESE UN OPCIÓN VALIDA")
                    
                    else:
                        
                        if ahorros == "no":
                            
                            se_logro, pasos = dcc.emparejar_bonsai(bonsai)
                            
                            if se_logro == False:
                                
                                print("No se pudo emparejar el Bonsai")
                                
                                running_podar = False
                                break
                            
                            else:
                                
                                print("Se logro emparejar el bonsai\n")
                                print((f"PASOS REALIZADOS: {pasos}"))
                                
                                for instruccion in pasos:
                                    
                                    accion, identificadores = instruccion
                                    
                                    if accion == "Quitar Nodo":
                                        
                                        dcc.quitar_nodo(bonsai, identificadores)
                                    
                                    elif accion == "Modificar Flor":
                                        
                                        dcc.modificar_nodo(bonsai, identificadores)
                                
                                bonsai.visualizar_bonsai("Vertical", True, False)
                                
                                running_podar = False
                                break
                            
                        elif ahorros == "si":
                            
                            bonsai_ahorro = dcc.emparejar_bonsai_ahorro(bonsai)
                            se_logro = bonsai_ahorro[0]
                            
                            if se_logro == False:
                                
                                print("No se pudo emparejar el Bonsai")
                                
                                running_podar = False
                                break
                            
                            else:
                                
                                print("\nSe logro emparejar el bonsai\n")
                                print(f"\nPASOS REALIZADOS: {bonsai_ahorro[2]}")
                                print(f"\costo total: {bonsai_ahorro[1]}")
                                
                                for instruccion in bonsai_ahorro[2]:
                                    
                                    accion, identificadores = instruccion
                                    
                                    if accion == "Quitar Nodo":
                                        
                                        dcc.quitar_nodo(bonsai, identificadores)
                                    
                                    elif accion == "Modificar Flor":
                                        
                                        dcc.modificar_nodo(bonsai, identificadores)
                                
                                bonsai.visualizar_bonsai("Vertical", True, False)
                                
                                running_podar = False
                                break

