
import os 

from typing import List

import utilidades

from funciones_extras import \
    se_puede_editar, existe_nodo, tiene_flor,  hijos, encontrar_nodo,\
        copiar_estructura_bonsai, simetria_der, simetria_izq

class Bonsai:
    def __init__(
        self,
        identificador: str,
        costo_corte: int,
        costo_flor: int,
        estructura: list
    ) -> None:
        self.identificador = identificador
        self.costo_corte = costo_corte
        self.costo_flor = costo_flor
        self.estructura = estructura

    def cargar_bonsai_de_archivo(self, carpeta: str, archivo: str) -> None:
        #utilizamos el modulo os para que el path funcione
        ruta: str = os.path.join( "data", f"{carpeta}", f"{archivo}" )
        
        with open( ruta, "r", encoding = "utf-8") as informacion:
            
            data: List[str|bool] = informacion.readlines()
            
            for numero_de_nodo in range ( len( data ) ):
                
                data[numero_de_nodo] = data[numero_de_nodo].strip( "\n" )
                data[numero_de_nodo] = data[numero_de_nodo].split( "," )
                data[numero_de_nodo][3] = data[numero_de_nodo][3].split( ";" )
                
        #Cambiamos los F por False y los str T por True, paral luego agregarlo al atributo
        for nodo in data:
            
            if nodo[1] == "F":
                nodo[1] = False
                
                if nodo[2] == "T":
                    nodo[2] = True
                
                else:
                    nodo[2] = False
            
            else:
                nodo[1] = True
                
                if nodo[2] == "T":
                    nodo[2] = True
                
                else:
                    nodo[2] = False
            
            self.estructura.append(nodo)
            
    def visualizar_bonsai(self, orientacion: str, emojis: bool, guardar_archivo: bool) -> None:
        #si es falso, simplemente aplicamos el metodo importado
        if guardar_archivo == False:
            utilidades.visualizar_bonsai( self.estructura, orientacion, emojis, False )
        
        #en otro caso abrimos la ruta visualizaciones/dentificador.txt y escribimos
        else:
            bonsai: str = utilidades.visualizar_bonsai(self.estructura, orientacion, emojis, True)
            path: str = os.path.join( "visualizaciones", f"{self.identificador}.txt" )
            
            with open( path, "w", encoding = "utf-8" ) as visualizador:
                visualizador.write( bonsai )

class DCCortaRamas:
    def modificar_nodo(self, bonsai: Bonsai, identificador: str) -> str:
        
        for nodo in bonsai.estructura:
            
            if nodo[0] == identificador:
                
                if nodo[2] == True:
                    
                    if nodo[1] == True:
                        
                        nodo[1] = False
                        return "Realizado"
                    else:
                        nodo[1] = True
                        return "Realizado"
                else:
                    return "No permitido"
        return "No encontrado"
    
    #aclaración: la funciones creadas como "existe nodo":
    #fueron creadas luego de hacer modificar nodo
    #por si necesitaba hacer más cosas, no senti 
    #tan necesario cambiar lo que hice anteriormente
    def quitar_nodo(self, bonsai: Bonsai, identificador: str) -> str:
        
        if existe_nodo( bonsai.estructura, identificador ) == False:
            return "No encontrado"
        
        else:
            
            if se_puede_editar( bonsai.estructura, identificador ) == False:
                return "No permitido"
            
            identificadores_hijos = list( hijos( bonsai.estructura, identificador ) )
            
            for hijo in identificadores_hijos:
                if se_puede_editar( bonsai.estructura, hijo ) == False:
                    return "No permitido"
            
            for nodo in bonsai.estructura:
                
                if nodo[0] == identificador:
                    bonsai.estructura.remove( nodo )
                
                elif nodo[3][0] == identificador:
                    nodo[3][0] = "0"
                
                elif nodo[3][1] == identificador:
                    nodo[3][1] = "0"
            
            for hijo in identificadores_hijos:
                for nodo in bonsai.estructura:
                    if hijo == nodo[0]:
                        bonsai.estructura.remove( nodo )
            return "Realizado"

    
    #sacamos todos los hijos en orden tanto del lado izquierdo, como el derecho
    #y comparamos la existencia de flores y si uno es cero, el otro tambíen
    def es_simetrico(self, bonsai: Bonsai) -> bool:
        
        hijo_izq, hijo_der = encontrar_nodo(bonsai.estructura, "1")[3]
        
        if hijo_izq != "0" and hijo_der == "0":
            return False
        
        elif hijo_izq == "0" and hijo_der != "0":
            return False
        
        elif existe_nodo(bonsai.estructura, hijo_izq) != \
            existe_nodo(bonsai.estructura, hijo_der):
            return False
        
        elif hijo_izq == "0" and hijo_der == "0":
            return True
        
        if tiene_flor(bonsai.estructura, hijo_izq) != \
            tiene_flor(bonsai.estructura, hijo_der):
            return False
        
        rama_izq: List = simetria_izq(bonsai.estructura, hijo_izq)
        rama_der: List = simetria_der(bonsai.estructura, hijo_der)
        
        bools_izq = []
        bools_der = []
        
        for i in range(len(rama_izq)):
            
            if existe_nodo(bonsai.estructura, rama_izq[i]) != \
            existe_nodo(bonsai.estructura, rama_der[i]):
                return False
            
            if rama_izq[i] == "0":
                bools_izq.append("0")
        
            else:
                bools_izq.append(tiene_flor(bonsai.estructura, rama_izq[i]))
                
        for i in range(len(rama_der)):
            
            if existe_nodo(bonsai.estructura, rama_izq[i]) != \
            existe_nodo(bonsai.estructura, rama_der[i]):
                return False
            
            if rama_der[i] == "0":
                bools_der.append("0")
        
            else:
                bools_der.append(tiene_flor(bonsai.estructura, rama_der[i]))
        if bools_der == bools_izq:
            return True
        
        else:
            
            return False
    
    #comparamos cada flor de cada hijo y si un hijo existe y el otro no ( o es 0)
    #se debe quitar el nodo. Optimizado para que entregue las menores
    #instrucciones posibles
    def emparejar_bonsai(self, bonsai: Bonsai) -> list:
        
        dcc: DCCortaRamas = DCCortaRamas()
        estructura_copia: List = copiar_estructura_bonsai(bonsai.estructura)
        bonsai_nuevo: Bonsai = Bonsai("copia", 0, 0, estructura_copia)
        
        if dcc.es_simetrico(bonsai):
            return [True, []]
        
        hijo_izq, hijo_der = encontrar_nodo(bonsai.estructura, "1")[3]
        rama_izq: List = [hijo_izq] + simetria_izq(bonsai.estructura, hijo_izq)
        rama_der: List =  [hijo_der] + simetria_der(bonsai.estructura, hijo_der)
        
        if len(rama_izq) < len(rama_der):
            for i in range( len(rama_der) - len(rama_izq)):
                rama_izq.append("0")
        
        if len(rama_izq) > len(rama_der):
            for i in range( len(rama_izq) - len(rama_der)):
                rama_der.append("0")
        
        instruccion = []
        
        for i in range(len(rama_izq)):
            
            if rama_izq[i] == "0" and rama_der[i] != "0" or  \
                (existe_nodo(bonsai_nuevo.estructura, rama_der[i]) == True and \
                existe_nodo(bonsai_nuevo.estructura, rama_izq[i]) == False):
                    
                se_realizo = dcc.quitar_nodo(bonsai_nuevo, rama_der[i])
                    
                if se_realizo == "Realizado":
                    instruccion.append(["Quitar Nodo", rama_der[i]])
                        
                    if dcc.es_simetrico(bonsai_nuevo):
                        return [True, instruccion]
                        
            elif rama_der[i] == "0" and rama_izq[i] != "0" or \
                (existe_nodo(bonsai_nuevo.estructura, rama_izq[i]) == True and \
                existe_nodo(bonsai_nuevo.estructura, rama_der[i]) == False):
                    
                se_realizo = dcc.quitar_nodo(bonsai_nuevo, rama_izq[i])
                    
                if se_realizo == "Realizado":
                    instruccion.append(["Quitar Nodo", rama_izq[i]])
                        
                    if dcc.es_simetrico(bonsai_nuevo):
                        return [True, instruccion]
            
            elif tiene_flor(bonsai_nuevo.estructura, rama_izq[i]) != \
                tiene_flor(bonsai_nuevo.estructura, rama_der[i]):
                
                if existe_nodo(bonsai_nuevo.estructura, rama_izq[i]) and \
                    existe_nodo(bonsai_nuevo.estructura, rama_der[i]):
                    
                    if se_puede_editar(bonsai_nuevo.estructura, rama_izq[i]) == True and \
                        se_puede_editar(bonsai_nuevo.estructura, rama_der[i]) == False:
                            
                        se_realizo = dcc.modificar_nodo(bonsai_nuevo, rama_izq[i])
                        instruccion.append(["Modificar Flor", rama_izq[i]])
                        
                        if dcc.es_simetrico(bonsai_nuevo):
                            return [True, instruccion]
                    
                    elif se_puede_editar(bonsai_nuevo.estructura, rama_izq[i]) == False and \
                        se_puede_editar(bonsai_nuevo.estructura, rama_der[i]) == True:
                            
                        se_realizo = dcc.modificar_nodo(bonsai_nuevo, rama_der[i])
                        instruccion.append(["Modificar Flor", rama_der[i]])
                        
                        if dcc.es_simetrico(bonsai_nuevo):
                            return [True, instruccion]
                        
        return [False, []]
    
    def emparejar_bonsai_ahorro(self, bonsai: Bonsai) -> list:
        
        dcc: DCCortaRamas = DCCortaRamas()
        estructura_copia: List = copiar_estructura_bonsai(bonsai.estructura)
        bonsai_nuevo: Bonsai = Bonsai("copia", 0, 0, estructura_copia)
        costo_total: int = 0
        
        if dcc.es_simetrico(bonsai):
            return [True, 0, []]
        
        hijo_izq, hijo_der = encontrar_nodo(bonsai.estructura, "1")[3]
        rama_izq: List = [hijo_izq] + simetria_izq(bonsai.estructura, hijo_izq)
        rama_der: List =  [hijo_der] + simetria_der(bonsai.estructura, hijo_der)
        
        if len(rama_izq) < len(rama_der):
            for i in range( len(rama_der) - len(rama_izq)):
                rama_izq.append("0")
        
        if len(rama_izq) > len(rama_der):
            for i in range( len(rama_izq) - len(rama_der)):
                rama_der.append("0")
        
        instruccion = []
        for i in range(len(rama_izq)):
            
            if rama_izq[i] == "0" and rama_der[i] != "0" or  \
                (existe_nodo(bonsai_nuevo.estructura, rama_der[i]) == True and \
                existe_nodo(bonsai_nuevo.estructura, rama_izq[i]) == False):
                    
                se_realizo = dcc.quitar_nodo(bonsai_nuevo, rama_der[i])
                    
                if se_realizo == "Realizado":
                    costo_total += bonsai.costo_corte
                    instruccion.append(["Quitar Nodo", rama_der[i]])
                        
                    if dcc.es_simetrico(bonsai_nuevo):
                        return [True, costo_total, instruccion]
                        
            elif rama_der[i] == "0" and rama_izq[i] != "0" or \
                (existe_nodo(bonsai_nuevo.estructura, rama_izq[i]) == True and \
                existe_nodo(bonsai_nuevo.estructura, rama_der[i]) == False):
                    
                se_realizo = dcc.quitar_nodo(bonsai_nuevo, rama_izq[i])
                    
                if se_realizo == "Realizado":
                    costo_total += bonsai.costo_corte
                    instruccion.append(["Quitar Nodo", rama_izq[i]])
                        
                    if dcc.es_simetrico(bonsai_nuevo):
                        return [True, costo_total, instruccion]
            
            elif tiene_flor(bonsai_nuevo.estructura, rama_izq[i]) != \
                tiene_flor(bonsai_nuevo.estructura, rama_der[i]):
                
                if existe_nodo(bonsai_nuevo.estructura, rama_izq[i]) and \
                    existe_nodo(bonsai_nuevo.estructura, rama_der[i]):
                    
                    if se_puede_editar(bonsai_nuevo.estructura, rama_izq[i]) == True and \
                        se_puede_editar(bonsai_nuevo.estructura, rama_der[i]) == False:
                            
                        se_realizo = dcc.modificar_nodo(bonsai_nuevo, rama_izq[i])
                        costo_total += bonsai.costo_flor
                        instruccion.append(["Modificar Flor", rama_izq[i]])
                        
                        if dcc.es_simetrico(bonsai_nuevo):
                            return [True, costo_total, instruccion]
                    
                    elif se_puede_editar(bonsai_nuevo.estructura, rama_izq[i]) == False and \
                        se_puede_editar(bonsai_nuevo.estructura, rama_der[i]) == True:
                            
                        se_realizo = dcc.modificar_nodo(bonsai_nuevo, rama_der[i])
                        costo_total += bonsai.costo_flor
                        instruccion.append(["Modificar Flor", rama_der[i]])
                        
                        if dcc.es_simetrico(bonsai_nuevo):
                            return [True, costo_total, instruccion]
        
        return [False, []]
    
    def comprobar_solucion(self, bonsai: Bonsai, instrucciones: list) -> list:
        
        costo_corte: int = bonsai.costo_corte
        costo_flor: int = bonsai.costo_flor
        costo_total: int = 0
        identificadores: List[str] = []
        acciones: List[str] = []
        estructura_copiada: List = copiar_estructura_bonsai( bonsai.estructura )
        bonsai_copia: Bonsai = Bonsai( "copia", 0, 0, estructura_copiada )
        dcc = DCCortaRamas()
        
        if dcc.es_simetrico(bonsai_copia):
            
            return [True, 0]
        
        for instruccion in instrucciones:
            
            if ( (not existe_nodo( estructura_copiada, instruccion[1] )  \
                or instruccion[1] in identificadores) ) or \
                not se_puede_editar( estructura_copiada, instruccion[1] ):
                    
                    return [False, 0]
        
            else:
                acciones.append( instruccion[0] )
                identificadores.append( instruccion[1] )
        
        for i in range ( len(acciones) ):
            
            if acciones[i] == "Quitar Nodo":
                se_quito = dcc.quitar_nodo( bonsai_copia, identificadores[i] )
                
                if se_quito == "Realizado":
                    costo_total += costo_corte
                else:
                    return [False, 0]
            else:
                costo_total += costo_flor
                dcc.modificar_nodo( bonsai_copia, identificadores[i] ) 
        
        if dcc.es_simetrico( bonsai_copia ):
            return [True, costo_total]
        
        else:
            return [False, 0]

