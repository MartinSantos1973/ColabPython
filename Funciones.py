# def saludar():
#     pass

# def saludar():
#     print("Hola Mundo")

# saludar()

# def saludaramigo(nombre, apellido):
#     print("Hola ", nombre + " " + apellido)

# nombrepersona = "Martin"
# apellidopersona = "Santos"
# saludaramigo(nombrepersona, apellidopersona)

# Funciones con valor de retorno
# def operacion(num1, num2):
#     resultado = num1 + num2
#     return resultado

# resultadofinal = (operacion(15,12))+50
# print  (resultadofinal)

# Funciones con Parámetros por DEFECTO
def operacion (num1=1, num2=1) :
    resultado = num1 * num2
    return resultado

print(operacion(5,3)) #Falta un parametro