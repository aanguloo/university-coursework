from typing import List

#funcion que retorna True or False si es que se puede editar
#el nodo
def se_puede_editar(bonsai_estructura: List[List[bool|str]], identificador: str) -> bool:
    
    for nodo in bonsai_estructura:
        
        if nodo[0] == identificador:
            
            if nodo[2] == True:
                
                return True
            
            else:
                
                return False

#funcion que permite identificar si un nodo exite o no. Devuelve True or False
def existe_nodo(bonsai_estructura: List[List[bool|str]], identificador: str)-> bool:
    
    for nodo in bonsai_estructura:
        
        if nodo[0] == identificador:
            
            return True
    return False


#funcion que permite ver si un nodo contiene una flor o no. Devuelve True or False
def tiene_flor(bonsai_estructura: List[List[bool|str]], identificador: str) -> bool:
    
    for nodo in bonsai_estructura:
        
        if nodo[0] == identificador:
            
            if nodo[1] == True:
                
                return True
            
            else:
                
                return False

#Permite obtener los identificadores hijos de un nodo en especifico
def encontrar_nodo(bonsai_estructura: List[List[bool|str]], identificador: str) -> List:
    
    for nodo in bonsai_estructura:
        
        if nodo[0] == identificador:
            
            return nodo
#funcion recursiva que guarda en una lista todos los hijos izquierdos del nodo principal
#llega hasta el ultimo hijo que su identificador no sea cero
def hijos_izquierdos(bonsai_estructura: List[List[bool|str]], identificador: str) -> List:
            
            for nodo in bonsai_estructura:
                
                if nodo[0] == identificador:
                    
                    if nodo[3][0] == "0":
                        return []
                    
                    return [nodo[3][0]] + hijos_izquierdos(bonsai_estructura, nodo[3][0])


#funcion recursiva que guarda en una lista todos los hijos derechos del nodo principal
#llega hasta el ultimo hijo que su identificador no sea cero
def hijos_derechos(bonsai_estructura: List[List[bool|str]], identificador: str) -> List:
            
            for nodo in bonsai_estructura:
                
                if nodo[0] == identificador:
                    
                    if nodo[3][1] == "0":
                        
                        return []
                    
                    return [nodo[3][1]] + hijos_derechos(bonsai_estructura, nodo[3][1])

#hijos izquierdos estan todos, hacemos una lista donde esten los identificadores de la izquierda y vamos poniendo identificadores


#Metodo que permite conocer toda la familia del nodo, los hijos de los hijos, etc. Se crea 
#una lista con todos los identificadores de los hijos. Ignorando los identificadores cero
def hijos(bonsai_estructura: List[List[bool|str]], identificador: str)-> List:
    
    identificadores_izquierdos = hijos_izquierdos(bonsai_estructura, identificador)
    
    identificadores_derechos = hijos_derechos(bonsai_estructura, identificador)
    
    for identifi in identificadores_izquierdos:
        
        for nodo in bonsai_estructura:
            
            if identifi == nodo[0] and nodo[3] != ["0","0"]:
                
                for hijo in nodo[3]:
                    
                    if hijo != "0" and hijo not in identificadores_izquierdos:
                        identificadores_izquierdos.append(hijo)
    
    for identifi in identificadores_derechos:
        
        for nodo in bonsai_estructura:
            
            if identifi == nodo[0] and nodo[3] != ["0","0"]:
                
                for hijo in nodo[3]:
                    
                    if hijo != "0" and hijo not in identificadores_derechos:
                        identificadores_derechos.append( hijo )
                
    identificadores_hijos = identificadores_izquierdos + identificadores_derechos
    
    return identificadores_hijos

#Funcion que permite hacer copia exacta de la extructura de un bonsai
def copiar_estructura_bonsai(bonsai_estructura: List[List[bool|str]]) -> List:
    
    estructura_copiada = []
    
    for nodo in bonsai_estructura:
            
            elementos = [nodo[0], nodo[1], nodo[2]]
            subnodos = []
            
            for hijos in nodo[3]:
                
                subnodos.append(hijos)
                
            elementos.append(subnodos)
            
            estructura_copiada.append(elementos)
        
    return estructura_copiada


#A diferencia de funciones anteriores, estas dos funciones nos permite
#obtener los hijos y el orden correto a partir de los dos hijos 
#principales del nodo raiz, permitiendo la comparación correcta
#para ver si tienen o no flores o si exite o no el nodo.
def simetria_izq(bonsai: List[List[bool|str]], identificador: str)-> List:
    
    if identificador == "0":
        
        return ["0"]
    
    rama_izq, rama_der = encontrar_nodo(bonsai, identificador)[3]
    return [rama_izq, rama_der] + simetria_izq(bonsai, rama_izq)  + simetria_izq(bonsai, rama_der)


def simetria_der(bonsai: List[List[bool|str]], identificador: str)-> List:
    
    if identificador == "0":
        
        return ["0"]
    
    rama_izq, rama_der = encontrar_nodo(bonsai, identificador)[3]
    return  [rama_der, rama_izq] + simetria_der(bonsai, rama_der) + simetria_der(bonsai, rama_izq)





