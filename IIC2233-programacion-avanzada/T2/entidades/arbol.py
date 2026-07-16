
import entidades.ramas as ramas
import math
import entidades.funciones_extras

class Arbol:
    
    def __init__(self, rama_principal, nombre: str):
        self.rama_principal = rama_principal
        self.nombre = nombre
        self.ramas = []
        self.profundidad = 0
        
    def cargar_modificador(self, rama: ramas.Rama, modificador):
        for rama_encontrar in self.ramas:
            if rama_encontrar == rama:
                
                rama_encontrar.cargar_modificador(modificador)
                return True
        return False
    
    def atacar(self, rama: ramas.Rama):
        pass
    
    def resumir(self):
        vitalidad_total = 0
        ataque = 0
        for rama in self.ramas:
            vitalidad_total += rama.vitalidad_maxima
            ataque += rama.atacar()
        
        ataque = math.floor(ataque/(len(self.ramas)))
        profundida = entidades.funciones_extras.mayor_profundidad(self.rama_principal, 0)[0][1]
        
        return (f"vida: {vitalidad_total}, ataque promedio: {ataque}, profundidad: {profundida} "
                f"largo: {len(self.ramas)}")
        
    def __str__(self):
        
        def estructura_completa(rama_principal, profundidad = 0):
            
            resultado =  rama_principal.__str__()
        

            for hija in rama_principal.ramas_hijas:
                resultado += "\n" + "  " * profundidad + "\ \n" + "  " * profundidad + \
                    estructura_completa(hija, profundidad + 1)
            
            return resultado
                

        
        return estructura_completa(self.rama_principal)
        
        
    
    def __repr__(self):
        
        def estructura_completa(rama_principal, profundidad = 0):
            
            resultado =  rama_principal.__repr__()
        

            for hija in rama_principal.ramas_hijas:
                resultado += "\n" + "  " * profundidad + "\ \n" + "  " * profundidad + \
                    estructura_completa(hija, profundidad + 1)
            
            return resultado
                

        
        return estructura_completa(self.rama_principal)




