from io import open
import random
from os import path

sujetos = ["él", "ella", "ellos", "ellas"]
verbos = ["corren", "saltan", "cantan", "bailan"]
objetos = ["en el parque", "en la calle", "en la playa", "en el jardín"]

oracion = random.choice(sujetos) + " " + random.choice(verbos) + " " + random.choice(objetos) + "."

#def escribir_archivo():
    #archivo = open("Texto.txt", "w")
    #archivo.write("Hola Mundo de Python\n"+ oracion)
    #archivo.close()

#def leer_archivo():
    #if path.isfile("Texto.txt"):
        #archivo = open ("Texto.txt", "r")
        #textos = archivo.read()
        #archivo.close()
        #print(textos)
    #else:
        #print("No existe el archivo")
def modificar_datos():
    if path.isfile("Texto.txt"):
        archivo = open("Texto.txt", "r+")
        texto = archivo.readlines()
        print(texto)
        texto[1] = "Hola efrain"
        #archivo.write("\nHola Andres" + oracion)
        print(texto)
        archivo.seek(0)
        archivo.writelines(oracion)
        archivo.close()
        print(texto)
        
    else:
        print("No existe el archivo")
    
#escribir_archivo()
#leer_archivo()
modificar_datos()
