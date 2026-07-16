from abc import ABC
import parametros
import entidades.modificadores as modificadores
from collections import deque
from random import random, choice
class Rama(ABC):
    identificador = 0
    def __init__(self, nombre: str, daño_base: int, defensa: float,\
        vitalidad_maxima: int, resistencia_plagas: float,\
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self._vitalidad_maxima = vitalidad_maxima
        self._daño_base = daño_base
        self._defensa = round(defensa, 3)
        self._resistencia_plagas = round(resistencia_plagas, 3)
        self._vida = self.vitalidad_maxima
        self.modificador = None
        self.ramas_hijas =  []
        self.rama_padre = None
        self.efecto = None
        self.viva = True
        Rama.identificador += 1
        self.identificador = Rama.identificador
        
    @property
    def daño_base(self):
        return self._daño_base
    
    @daño_base.setter
    def daño_base(self, valor):
        
        if valor <= 0:
            self._daño_base = 0
        else:
            self._daño_base = valor
            
    @property
    def vitalidad_maxima(self):
        return self._vitalidad_maxima
    
    @vitalidad_maxima.setter
    def vitalidad_maxima(self, valor):
        if not isinstance(valor, int):
            valor = int(valor)
        if valor <= 0:
            self._vitalidad_maxima = 0
        else:
            self._vitalidad_maxima = valor
            
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, valor: int):
        if not isinstance(valor, int):
            valor = int(valor)
            
        if valor > self.vitalidad_maxima:
            self._vida = self.vitalidad_maxima
        elif valor <= 0:
            self._vida = 0
        else:
            self._vida = valor
            
    @property
    def defensa(self):
        return self._defensa
    
    @defensa.setter
    def defensa(self, valor: float):
        if not isinstance(valor, float):
                valor = float(valor)
        valor = round(valor, 3)
        if valor >= 0.5:
            self._defensa= 0.5
        elif valor <= - 0.5:
            self._defensa = - 0.5
        else:
            self._defensa = valor
            
    @property
    def resistencia_plagas(self):
        return self._resistencia_plagas
    
    @resistencia_plagas.setter
    def resistencia_plagas(self, valor):
        
        if not isinstance(valor, float):
                valor = float(valor)
        valor = round(valor, 3)
        if valor <= 0.0:
            self._resistencia_plagas= 0.0
        elif valor >= 1.0:
            self._resistencia_plagas = 1.0
        else:
            self._resistencia_plagas = valor
    
    def muerte(self):
        self.vida = 0
        self.viva = False
        
        if len(self.ramas_hijas) > 0:
            for hija in self.ramas_hijas:
                hija.muerte()
                
        return None
    def cargar_modificador(self, modificador: modificadores.Modificadores) -> None:
        
        if self.modificador == None:
            self.modificador = modificador
            self.vitalidad_maxima = self.vitalidad_maxima + self.modificador.vida_maxima
            self.vida = self.vida + self.modificador.vida_maxima
            self.defensa_pasada = self.defensa
            self.defensa = self.defensa + self.modificador.defensa
            
        
        else:
            self.vitalidad_maxima = self.vitalidad_maxima - self.modificador.vida_maxima
            self.vida = self.vida - self.modificador.vida_maxima
            self.defensa = self.defensa - self.modificador.defensa
            
            if self.vida == 0:
                self.muerte()
                return None
            
            self.vitalidad_maxima = self.vitalidad_maxima + modificador.vida_maxima
            self.vida = self.vida + modificador.vida_maxima
            self.defensa = self.defensa + modificador.defensa
            self.modificador = modificador
            
        if self.vida == 0:
                self.muerte()
                return None

    def pasar_ronda(self):
        
        probabilidad_no_obtener = self.resistencia_plagas
        probabilidad_obtenida = random()
        
        if probabilidad_obtenida > probabilidad_no_obtener:
            
            modi_negativo = choice(modificadores.obtener_modificadores_negativos())
            self.cargar_modificador(modi_negativo)
        
        #actualizar el efecto depende de cada rama
    
    def atacar(self):
        
        if self.modificador != None:
            
            daño_base = self.daño_base
            daño_modificador = self.modificador.ataque
            return daño_base + daño_modificador
        else:
            return self.daño_base
        
    def recibir_daño(self, daño_entrante: int):
        
        daño_verdadero = round(daño_entrante *(1 - self._defensa))
        daño_sobrante = self.vida - daño_verdadero
        self.vida = self.vida - daño_verdadero
        
        if self.vida == 0:
            self.muerte()
            
        if daño_sobrante < 0:
            return abs(daño_sobrante)
        
        return 0
        
    def __str__(self):
        return (f"{self.nombre}: Vida: {self.vida}/{self.vitalidad_maxima}, " 
                f"defensa: {self.defensa * 100}%, Daño base: {self.daño_base}, "
                f"Resistencia a plagas: {self.resistencia_plagas * 100}%, "
                f"Modificador: {self.modificador}, "
                f"Número de ramas hijas: {len(self.ramas_hijas)}")
        
    def __repr__(self):
        return (f"Rama(nombre: {self.nombre}, Vida: {self.vida}/{self.vitalidad_maxima}," 
                f"defensa: {self.defensa * 100}%, Daño base: {self.daño_base}, "
                f"Resistencia a plagas: {self.resistencia_plagas * 100}%, "
                f"Modificador: {self.modificador}, " 
                f"Número de ramas hijas: {len(self.ramas_hijas)})")

class Ficus(Rama):
    
    def __init__(self, nombre: str, daño_base: int, defensa: float,\
        vitalidad_maxima: int, resistencia_plagas: float,\
            *args, **kwargs):
        super().__init__(nombre, daño_base, defensa,\
        vitalidad_maxima, resistencia_plagas, *args, **kwargs)
        
        self.vida = self.vitalidad_maxima
        self.modificador = None
        self.ramas_hijas =  []
        self.efecto = ("Cada vez que transcurre una ronda, " 
        "esta rama y sus hijas recuperan 4% ""de su salud faltante")
        
    def pasar_ronda(self):
        if self.vida == 0:
            self.muerte()
            return None
        
        salud_restante = self.vitalidad_maxima - self.vida
        self.vida = self.vida + salud_restante * 0.04
        
        if len(self.ramas_hijas) > 0:
            
            for hijas in self.ramas_hijas:
                hijas.pasar_ronda()
            
        super().pasar_ronda()
            

class Celery(Rama):
    
    def __init__(self, nombre: str, daño_base: int, defensa: float,\
        vitalidad_maxima: int, resistencia_plagas: float,\
            *args, **kwargs):
        
        super().__init__(nombre, daño_base, defensa,\
        vitalidad_maxima, resistencia_plagas, *args, **kwargs)
        
        self.vida = self.vitalidad_maxima
        self.modificador = None
        self.ramas_hijas =  []
        self.efecto = ("Por cada ronda que esta rama "
                    "no ataque ni forme parte de un ataque, su daño base aumenta un 1%")
        self.ataque = False
        
    def atacar(self):
        self.ataque = True
        return super().atacar()
    
    def pasar_ronda(self):
        if self.ataque == False:
            self.daño_base = self.daño_base + self.daño_base * 0.01
            
            if len(self.ramas_hijas) > 0:
            
                for hijas in self.ramas_hijas:
                    hijas.pasar_ronda()
        else:
            self.ataque = False
            
            if len(self.ramas_hijas) > 0:
            
                for hijas in self.ramas_hijas:
                    hijas.pasar_ronda()
                    
        super().pasar_ronda()
            
class Hyedrid(Rama):
    
    def __init__(self, nombre: str, daño_base: int, defensa: float,\
        vitalidad_maxima: int, resistencia_plagas: float,\
            *args, **kwargs):
        
        super().__init__(nombre, daño_base, defensa,\
        vitalidad_maxima, resistencia_plagas, *args, **kwargs)
        
        self.vida = self.vitalidad_maxima
        self.modificador = None
        self.ramas_hijas =  []
        self.efecto = ("Esta rama se puede equipar dos objetos Modificador en lugar" 
                    "de uno. Para la mecánica de reemplazo," 
                    "se debe considerar el órden en que ingresan los objetos)")

class Paalm(Rama):
    
    def __init__(self, nombre: str, daño_base: int, defensa: float,\
        vitalidad_maxima: int, resistencia_plagas: float,\
            *args, **kwargs):
        
        super().__init__(nombre, daño_base, defensa,\
        vitalidad_maxima, resistencia_plagas, *args, **kwargs)
        
        self.vida = self.vitalidad_maxima
        self.modificador = None
        self.ramas_hijas =  []
        self.efecto = ("Cada vez que esta rama recibe daño y" 
                    "no muere, su defensa aumenta en 0.02.")
        
    def recibir_daño(self, daño_entrante):
        
        daño_verdadero = round(daño_entrante *(1 - self._defensa))
        daño_sobrante = self.vida - daño_verdadero
        self.vida = self.vida - daño_verdadero
        
        if self.vida == 0:
            self.muerte()
            
        if daño_sobrante < 0:
            return abs(daño_sobrante)
        
        else:
            self.defensa = self.defensa + 0.02
        
class Alovelis(Rama):
    
    def __init__(self, nombre: str, daño_base: int, defensa: float,\
        vitalidad_maxima: int, resistencia_plagas: float,\
            *args, **kwargs):
        
        super().__init__(nombre, daño_base, defensa,\
        vitalidad_maxima, resistencia_plagas, *args, **kwargs)
        
        self.vida = self.vitalidad_maxima
        self.modificador = None
        self.ramas_hijas =  []
        self.efecto = ("Sin efectos adicionales")

class Pine(Rama):
    
    def __init__(self, nombre: str, daño_base: int, defensa: float,\
        vitalidad_maxima: int, resistencia_plagas: float,\
            *args, **kwargs):
        
        super().__init__(nombre, daño_base, defensa,\
        vitalidad_maxima, resistencia_plagas, *args, **kwargs)
        
        self.vida = self.vitalidad_maxima
        self.modificador = None
        self.ramas_hijas =  []
        self.efecto = ("Si esta rama muere, anula el daño de penetración hacia su padre")
        
    def recibir_daño(self, daño_entrante):
        
        daño_verdadero = round(daño_entrante *(1 - self._defensa))
        self.vida = self.vida - daño_verdadero
        
        if self.vida == 0:
            self.muerte()
        
        return 0

class Cactoos(Rama):
    
    def __init__(self, nombre: str, daño_base: int, defensa: float,\
        vitalidad_maxima: int, resistencia_plagas: float,\
            *args, **kwargs):
        
        super().__init__(nombre, daño_base, defensa,\
        vitalidad_maxima, resistencia_plagas, *args, **kwargs)
        
        self.vida = self.vitalidad_maxima
        self.modificador = None
        self.ramas_hijas =  []
        self.efecto = ("Si no ataca ni recibe daño por una ronda"
                    f", genera {parametros.DINERO_CACTOOS} de dinero "
                    "por cada rama hija")
        self.ataco = False
        self.recibio_daño = False
        self.dinero_generado = 0
        
    def atacar(self):
        self.ataco = True
        return super().atacar()
    
    def recibir_daño(self, daño_entrante):
        self.recibio_daño = True
        return super().recibir_daño(daño_entrante)
    
    def pasar_ronda(self):
        if not self.recibio_daño and not self.ataco:
            self.dinero_generado = len(self.ramas_hijas) * parametros.DINERO_CACTOOS
        self.recibio_daño = False
        self.ataco = False
        super().pasar_ronda()

