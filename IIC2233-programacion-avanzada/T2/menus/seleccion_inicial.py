import parametros
from random import choice
import entidades.arbol as arboles
import entidades.funciones_extras as funciones_extras


class SeleccionInicial:
    
    def facil() -> arboles.Arbol:
        
        try:
            with open(parametros.path_arboles_faciles, "r", encoding= "utf-8") as archivo:
                data = [arbol.strip("\n") for arbol in archivo]
            
            for arbol in range(len(data)):
                
                data[arbol] = data[arbol].split(":", 1)
                
            nombres_arboles = [arbol[0] for arbol in data]
            ramas_estructuradas = [arbol[1].strip(" ") for arbol in data]
            ramas_arboles = ramas_estructuradas.copy()
            largo_ramas = []
            
            for i in range(len(ramas_arboles)):
                ramas_arboles[i] = ramas_arboles[i].replace("}", "")
                ramas_arboles[i] = ramas_arboles[i].replace("{", "")
                ramas_arboles[i] = ramas_arboles[i].split(";")
            
            for i in range(len(ramas_arboles)):
                for j in range(len(ramas_arboles[i])):
                    
                    ramas_arboles[i][j] = ramas_arboles[i][j].strip(" ")
                    
                ramas_arboles[i] = [x for x in ramas_arboles[i] if x is not None and x != '']
                largo_ramas.append(len(ramas_arboles[i]))
            
            nombre_y_largo = {
                
            }
            nombre_y_ramas = {
                
            }
            for i in range(len(nombres_arboles)):
                
                nombre_y_largo[nombres_arboles[i]] = largo_ramas[i]
                nombre_y_ramas[nombres_arboles[i]] = ramas_arboles[i]
            
            running = True
            opciones = set()
            while running:
                print("----SELECCIÓN INICIAL----")
                for i in range(0, len(nombres_arboles)):
                        
                    print(f"[{i + 1}] {nombres_arboles[i]} :  "
                        f"{nombre_y_largo[nombres_arboles[i]]} Ramas")
                    opciones.add(str(i + 1))
                try:    
                    elección = input(f"ingresa una opción " 
                        f"{[i for i in range(1, len(nombres_arboles) + 1)]}: ").strip(" ")
                    if elección not in opciones:
                        raise ValueError("\nERROR, Escoge una opción valida\n")
                except ValueError as error:
                    print(error)
                
                else:
                    
                    nombre_arbol = nombres_arboles[int(elección) - 1]
                    ramas_arbol_principal = nombre_y_ramas[nombre_arbol]
                    for rama in range(len(ramas_arbol_principal)):
                        ramas_arbol_principal[rama] = \
                            funciones_extras.crear_rama(ramas_arbol_principal[rama])
                        
                    
                    rama_principal = ramas_arbol_principal[0]
                    jugador = arboles.Arbol(rama_principal, nombre_arbol)
                    jugador.ramas.extend(ramas_arbol_principal)
                    
                    nombre_arbol_enemigo = choice(nombres_arboles)
                    ramas_arbol_enemigo_principal = nombre_y_ramas[nombre_arbol_enemigo]
                    for rama in range(len(ramas_arbol_enemigo_principal)):
                        ramas_arbol_enemigo_principal[rama] = \
                            funciones_extras.crear_rama(ramas_arbol_enemigo_principal[rama])
                            
                    rama_principal_enemiga = ramas_arbol_enemigo_principal[0]
                    enemigo = arboles.Arbol(rama_principal_enemiga, nombre_arbol_enemigo)
                    enemigo.ramas.extend(ramas_arbol_enemigo_principal)
                    
                    return jugador,enemigo 
                
                
        except FileNotFoundError:
            
            print("ERROR: EL ARCHIVO NO FUE ENCONTRADO")
            
    def medios() -> arboles.Arbol:
        try:
            with open(parametros.path_arboles_medios, "r", encoding= "utf-8") as archivo:
                data = [arbol.strip("\n") for arbol in archivo]
            
            for arbol in range(len(data)):
                
                data[arbol] = data[arbol].split(":", 1)
                
            nombres_arboles = [arbol[0] for arbol in data]
            ramas_estructuradas = [arbol[1].strip(" ") for arbol in data]
            ramas_arboles = ramas_estructuradas.copy()
            largo_ramas = []
            
            for i in range(len(ramas_arboles)):
                ramas_arboles[i] = ramas_arboles[i].replace("}", "")
                ramas_arboles[i] = ramas_arboles[i].replace("{", "")
                ramas_arboles[i] = ramas_arboles[i].split(";")
            
            for i in range(len(ramas_arboles)):
                for j in range(len(ramas_arboles[i])):
                    
                    ramas_arboles[i][j] = ramas_arboles[i][j].strip(" ")
                    
                ramas_arboles[i] = [x for x in ramas_arboles[i] if x is not None and x != '']
                largo_ramas.append(len(ramas_arboles[i]))
            
            nombre_y_largo = {
                
            }
            nombre_y_ramas = {
                
            }
            for i in range(len(nombres_arboles)):
                
                nombre_y_largo[nombres_arboles[i]] = largo_ramas[i]
                nombre_y_ramas[nombres_arboles[i]] = ramas_arboles[i]
            
            running = True
            opciones = set()
            while running:
                print("----SELECCIÓN INICIAL----")
                for i in range(0, len(nombres_arboles)):
                        
                    print(f"[{i + 1}] {nombres_arboles[i]} :  "
                        f"{nombre_y_largo[nombres_arboles[i]]} Ramas")
                    opciones.add(str(i + 1))
                try:    
                    elección = input(f"ingresa una opción " 
                        f"{[i for i in range(1, len(nombres_arboles) + 1)]}: ").strip(" ")
                    if elección not in opciones:
                        raise ValueError("\nERROR, Escoge una opción valida\n")
                except ValueError as error:
                    print(error)
                
                else:
                    
                    nombre_arbol = nombres_arboles[int(elección) - 1]
                    ramas_arbol_principal = nombre_y_ramas[nombre_arbol]
                    for rama in range(len(ramas_arbol_principal)):
                        ramas_arbol_principal[rama] = \
                            funciones_extras.crear_rama(ramas_arbol_principal[rama])
                        
                    
                    rama_principal = ramas_arbol_principal[0]
                    jugador = arboles.Arbol(rama_principal, nombre_arbol)
                    jugador.ramas.extend(ramas_arbol_principal)
                    
                    nombre_arbol_enemigo = choice(nombres_arboles)
                    ramas_arbol_enemigo_principal = nombre_y_ramas[nombre_arbol_enemigo]
                    for rama in range(len(ramas_arbol_enemigo_principal)):
                        ramas_arbol_enemigo_principal[rama] = \
                            funciones_extras.crear_rama(ramas_arbol_enemigo_principal[rama])
                            
                    rama_principal_enemiga = ramas_arbol_enemigo_principal[0]
                    enemigo = arboles.Arbol(rama_principal_enemiga, nombre_arbol_enemigo)
                    enemigo.ramas.extend(ramas_arbol_enemigo_principal)
                    
                    return jugador,enemigo 
                
        except FileNotFoundError:
            
            print("ERROR: EL ARCHIVO NO FUE ENCONTRADO")
            
    def dificil() -> arboles.Arbol:
        
        try:
            with open(parametros.path_arboles_dificiles, "r", encoding= "utf-8") as archivo:
                data = [arbol.strip("\n") for arbol in archivo]
            
            for arbol in range(len(data)):
                
                data[arbol] = data[arbol].split(":", 1)
                
            nombres_arboles = [arbol[0] for arbol in data]
            ramas_estructuradas = [arbol[1].strip(" ") for arbol in data]
            ramas_arboles = ramas_estructuradas.copy()
            largo_ramas = []
            
            for i in range(len(ramas_arboles)):
                ramas_arboles[i] = ramas_arboles[i].replace("}", "")
                ramas_arboles[i] = ramas_arboles[i].replace("{", "")
                ramas_arboles[i] = ramas_arboles[i].split(";")
            
            for i in range(len(ramas_arboles)):
                for j in range(len(ramas_arboles[i])):
                    
                    ramas_arboles[i][j] = ramas_arboles[i][j].strip(" ")
                    
                ramas_arboles[i] = [x for x in ramas_arboles[i] if x is not None and x != '']
                largo_ramas.append(len(ramas_arboles[i]))
            
            nombre_y_largo = {
                
            }
            nombre_y_ramas = {
                
            }
            for i in range(len(nombres_arboles)):
                
                nombre_y_largo[nombres_arboles[i]] = largo_ramas[i]
                nombre_y_ramas[nombres_arboles[i]] = ramas_arboles[i]
            
            running = True
            opciones = set()
            while running:
                print("----SELECCIÓN INICIAL----")
                for i in range(0, len(nombres_arboles)):
                        
                    print(f"[{i + 1}] {nombres_arboles[i]} :  "
                        f"{nombre_y_largo[nombres_arboles[i]]} Ramas")
                    opciones.add(str(i + 1))
                try:    
                    elección = input(f"ingresa una opción " 
                        f"{[i for i in range(1, len(nombres_arboles) + 1)]}: ").strip(" ")
                    if elección not in opciones:
                        raise ValueError("\nERROR, Escoge una opción valida\n")
                except ValueError as error:
                    print(error)
                
                else:
                    
                    nombre_arbol = nombres_arboles[int(elección) - 1]
                    ramas_arbol_principal = nombre_y_ramas[nombre_arbol]
                    for rama in range(len(ramas_arbol_principal)):
                        ramas_arbol_principal[rama] = \
                            funciones_extras.crear_rama(ramas_arbol_principal[rama])
                        
                    
                    rama_principal = ramas_arbol_principal[0]
                    jugador = arboles.Arbol(rama_principal, nombre_arbol)
                    jugador.ramas.extend(ramas_arbol_principal)
                    
                    nombre_arbol_enemigo = choice(nombres_arboles)
                    ramas_arbol_enemigo_principal = nombre_y_ramas[nombre_arbol_enemigo]
                    for rama in range(len(ramas_arbol_enemigo_principal)):
                        ramas_arbol_enemigo_principal[rama] = \
                            funciones_extras.crear_rama(ramas_arbol_enemigo_principal[rama])
                            
                    rama_principal_enemiga = ramas_arbol_enemigo_principal[0]
                    enemigo = arboles.Arbol(rama_principal_enemiga, nombre_arbol_enemigo)
                    enemigo.ramas.extend(ramas_arbol_enemigo_principal)
                    
                    return jugador,enemigo 
                
        except FileNotFoundError:
            
            print("ERROR: EL ARCHIVO NO FUE ENCONTRADO")



