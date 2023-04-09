class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
  
    
    def mostrar_datos(self):
        print("Nombre", self.nombre)
        print("Edad", self.edad)

    def __str__(self) -> str:
            return f"Nombre:  {self.nombre} \nEdad: {self.edad}"