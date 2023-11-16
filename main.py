from entities.carrera import Carrera
from entities.consultas_campeonato import Consultas
from exceptions.opcion_invalida import OpcionInvalida
import datetime

class Empleado:
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario):
        self.cedula = cedula 
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento 
        self.nacionalidad = nacionalidad
        self.salario = salario


class Piloto(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, puntos_campeonato=0, lesionado=False):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score
        self.numero_auto = numero_auto
        self.puntos_campeonato = puntos_campeonato
        self.lesionado = lesionado


class Mecanico(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score

class JefeEquipo(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario)

class Auto:
    def __init__(self, modelo, ano, score):
        self.modelo = modelo
        self.ano = ano
        self.score = score

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.auto = None

    def agregar_empleado(self, empleado):
        if len(self.empleados) >= 12:
            print("El equipo ya tiene todos sus empleados.")
        else:
            self.empleados.append(empleado)

    def asignar_auto(self, auto): 
        self.auto = auto

empleados = []
equipos = []
autos = []

def ingresar_cedula(): 
    cedula = input("Ingrese cedula: ")
    if len(cedula) == 8 and cedula.isdigit():
        return cedula
    else:
        print("Cédula no válida. Debe tener 8 números sin guión.") #volvia al programa principal?


def validar_fecha(date_string): #validacion
    try:
        datetime.datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False #volvia al programa principal?
    
def validar_nombre():
    nombre = input("Ingrese nombre: ")
    if nombre.isalpha() == True:
        return nombre.isalpha()
    else:
        print("Nombre no valido")

def alta_empleado():   
    
    cedula = ingresar_cedula()
    nombre = validar_nombre()

    while True:
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ") 
        if validar_fecha(fecha_nacimiento):
            break
        print("Fecha inválida, use el formato DD/MM/AAAA.")     #volvia al programa principal?
        
    while True:
        nacionalidad = input("Ingrese nacionalidad: ")
        if nacionalidad.isalpha(): #ver espacios,?
            break
        print("Nacionalidad inválida, ingrese nuevamente.") #volvia al programa principal?

    while True:
        try:
            salario = float(input("Ingrese salario: "))
            break
        except ValueError:
            print("Salario inválido, ingrese nuevamente.") #volvia al programa principal?

    
    cargo = input("Seleccione una opción: ")
    print("1. Piloto")
    print("2. Piloto de reserva")
    print("3. Mecánico")
    print("4. Jefe de equipo")
        
    if cargo in [1,2,3]:
        while True:
            try:
                score = int(input("Ingrese score: "))
                if 1 <= score <= 99:
                    break
                print("Score debe ser entre 1 y 99.")
            except ValueError:
                print("Ingrese un número válido para score.")
                
    elif cargo in [1,2]:
        while True:
            try:
                numero_auto = int(input("Ingrese número de auto: "))
                break
            except ValueError:
                print("Ingrese un número válido para número de auto.")

    if cargo == 1:
        print(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto)
        empleados.append(Piloto)
        return Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto)
    
    if cargo == 2:
        print(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, titular=False)
        empleados.append(Piloto)
        return Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, titular=False)

    elif cargo == 3:
        print(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score)
        empleados.append(Mecanico)
        return Mecanico(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score)
    
    print(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
    empleados.append(JefeEquipo)
    return JefeEquipo(cedula, nombre, fecha_nacimiento, nacionalidad, salario)



def alta_auto(modelo, ano, score):
    modelo = input("Ingrese modelo: ")
    ano = int(input("Ingrese año: "))
    
    while True:
        try:
            score = int(input("Ingrese score: "))
            if 1 <= score <= 99:
                break
            print("Score debe ser entre 1 y 99.") #volvia al programa principal?
        except ValueError:
            print("Ingrese un número válido.") #volvia al programa principal?
            
    return Auto(modelo, ano, score)

def alta_equipo(nombre, equipo, auto, empleado):
    nombre = input("Ingrese nombre del equipo: ")
    equipo = Equipo(nombre)
    
    auto = alta_auto()
    equipo.asignar_auto(auto)
    
    print("Ingrese los empleados para este equipo:")
    for _ in range(12):
        empleado = alta_empleado()
        equipo.agregar_empleado(empleado) #Verificar el orden 2 pilotos, 1 piloto reserva, 1 jefe equipo y 8 mecanicos
    
    return equipo

def simular_carrera(): #fede
    pass

def realizar_consultas(): #fede
    pass

def main():
    equipos = []
    while True:
        print("1. Alta de empleado")
        print("2. Alta de auto")
        print("3. Alta de equipo")
        print("4. Simular carrera")
        print("5. Realizar consultas")
        print("6. Finalizar programa")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                empleado = alta_empleado()
                print(f"Empleado {empleado.nombre} registrado.")
            except Exception as e:
                print(f"Error: {e}")
                
        elif opcion == "2":
            try:
                auto = alta_auto()
                print(f"Auto {auto.modelo} registrado.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            try:
                equipo = alta_equipo()
                equipos.append(equipo)
                print(f"Equipo {equipo.nombre} registrado.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "6":
            break
        else:
            print("Opción no válida.") #volvia al programa principal?

if __name__ == "__main__":
    main()

    
