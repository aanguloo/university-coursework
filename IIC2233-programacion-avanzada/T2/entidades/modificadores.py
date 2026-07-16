from abc import ABC
import parametros

class Modificadores(ABC):
    def __init__(self, nombre: str, ataque: int, defensa: float, vida_maxima: int, precio: int,\
        *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida_maxima = vida_maxima
        self.precio = precio
        
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return (f"{self.nombre}(ataque: {self.ataque}, defensa: {self.defensa}"
                f" vida: {self.vida_maxima}, precio: {self.precio})")

class ModificadoresPositivos(Modificadores):
    def __init__(self, nombre: str, ataque: int, defensa: float, vida_maxima: int, precio: int,\
        *args, **kwargs):
        super().__init__(nombre, ataque, defensa, vida_maxima, precio,\
            *args, **kwargs)
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
class ModificadoresNegativos(Modificadores):
    def __init__(self, nombre: str, ataque: int, defensa: float, vida_maxima: int,\
        *args, **kwargs):
        super().__init__(nombre, ataque, defensa, vida_maxima,\
            0,*args, **kwargs)
        
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return (f"ModificadoresNegativos({self.nombre}(ataque: {self.ataque}, defensa: "
                f"{self.defensa}"
                f" vida: {self.vida_maxima})")


def obtener_modificadores_negativos() -> list:
    
    with open(parametros.path_modificadores_negativos, "r", encoding = "utf-8") as archivo:
        
        data = [linea.strip("\n").split(";") for linea in archivo.readlines()]
        
        
    modificadores = []
    
    for datos in data:
        
        nombre = datos[0]
        ataque = int(datos[1])
        defensa = float(datos[2])
        vida_maxima = float(datos[3])
        
        negativo = ModificadoresNegativos(nombre, ataque, defensa, vida_maxima)
        modificadores.append(negativo)
    
    return modificadores


def obtener_modificadores_positivos() -> list:
    
    with open(parametros.path_modificadores, "r", encoding = "utf-8") as archivo:
        
        data = [linea.strip("\n").split(";") for linea in archivo.readlines()]
        
        
    modificadores = []
    
    for datos in data:
        
        nombre = datos[0]
        ataque = int(datos[1])
        defensa = float(datos[2])
        vida_maxima = float(datos[3])
        precio = int(datos[4])
        positivo = ModificadoresPositivos(nombre, ataque, defensa,\
            vida_maxima, precio )
        modificadores.append(positivo)
    
    return modificadores