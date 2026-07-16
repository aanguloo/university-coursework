import entidades.ramas as ramas
import parametros

def crear_rama(nombre_rama) -> ramas.Rama:
    
    with open(parametros.path_ramas, "r", encoding= "utf-8") as archivo:
        
        data = [linea.strip("\n").split(";") for linea in archivo.readlines()]
        
    
    for rama in data:
        nombre = rama[0]
        vida = int(rama[1]) 
        defensa = float(rama[2])
        daño_base = int(rama[3])
        resistencia = float(rama[4])
        
        args = (nombre, vida, defensa, daño_base, resistencia)
        
        if nombre == nombre_rama and nombre_rama == "Ficus":
            
            return ramas.Ficus(*args)
        
        if nombre == nombre_rama and nombre_rama == "Celery":
            
            return ramas.Celery(*args)
        
        if nombre == nombre_rama and nombre_rama == "Hyedrid":
            
            return ramas.Hyedrid(*args)
        
        if nombre == nombre_rama and nombre_rama == "Paalm":
            
            return ramas.Paalm(*args)
        
        if nombre == nombre_rama and nombre_rama == "Alovelis":
            
            return ramas.Alovelis(*args)
        
        if nombre == nombre_rama and nombre_rama == "Pine":
            
            return ramas.Pine(*args)
        
        if rama[0] == nombre_rama and nombre_rama == "Cactoos":
            
            return ramas.Cactoos(*args)




#lista de listas que contiene las ramas con mayor profundidad
def mayor_profundidad(rama_principal, profundidad_actual = 0):
    
    lista_profundidad = []
    
    if rama_principal.ramas_hijas == []:
        return [[rama_principal, profundidad_actual]]
    
    else:
        
        for rama in rama_principal.ramas_hijas:
            
            lista_profundidad.extend(mayor_profundidad(rama, profundidad_actual + 1))
    
    def ordenar_produndidad(lista):
        
        return lista[1]
    
    return sorted(lista_profundidad, key=ordenar_produndidad, reverse= True)