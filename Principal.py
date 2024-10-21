# ### ---- Modulo de Python
# import ModuloTest

# print(ModuloTest.OperacionM(5,10,20))

## POO - Clase , Atributo y Metodo

class Persona:
    nombre=""
    apellidos=""
    nrotelefono=""
    nID=""
    sexo=""


    def saludar(self):
        saludo ="Hola, mi nombre es :" + self.nombre
        return saludo
    

p1 = Persona()
print(p1.saludar())

