# Ejemplo de herencia y polimorfismo con clases de animales

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        # Método que puede ser sobrescrito por las subclases
        return f"{self.nombre} hace un sonido."


class Perro(Animal):
    # Ejemplo de herencia: Perro hereda de Animal
    def hablar(self):
        # Ejemplo de polimorfismo: redefine el método hablar
        return f"{self.nombre} dice: ¡Guau!"


class Gato(Animal):
    # Ejemplo de herencia: Gato hereda de Animal
    def hablar(self):
        # Ejemplo de polimorfismo: redefine el método hablar
        return f"{self.nombre} dice: ¡Miau!"


# Ejemplo de uso de property (getter y setter) en una clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        # Getter para el atributo nombre
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Setter para el atributo nombre
        if isinstance(nuevo_nombre, str) and nuevo_nombre:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    @property
    def edad(self):
        # Getter para el atributo edad
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        # Setter para el atributo edad
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero no negativo.")


# Ejemplo de uso de herencia y polimorfismo
animales = [Perro("Fido"), Gato("Misu"), Animal("Criatura")]
for animal in animales:
    print(animal.hablar())

# Ejemplo de uso de property (getter y setter)
persona = Persona("Ana", 30)
print(persona.nombre)
persona.nombre = "Juan"
print(persona.nombre)



def funcion(funcion):
    def decorador(funcion):
        