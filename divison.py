divi = 0
try:
    a = int(input("Ingrese el Diviendo: "))
    b = int(input("Ingrese el Divisor: "))
    
    divi = a / b
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as error:
    print("Ha ocurrido error no previsto", type(error).__name__)
except ValueError:
    print("Ingrese solo numeros enteros")
print ("La divison es: ", divi)