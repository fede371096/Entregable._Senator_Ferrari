from entities.carrera import Carrera
from entities.consultas_campeonato import Consultas
from exceptions.opcion_invalida import OpcionInvalida
from exceptions.datos_incorrectos import DatosIncorrectos
from exceptions.formato_incorrecto import FormatoIncorrecto
from exceptions.objeto_no_existe import ObjetoNoExiste
from exceptions.valores_duplicados import ValoresDuplicados
from exceptions.sin_cupos import SinCupos
import datetime

class Empleado:
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario):
        self.cedula = cedula 
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento 
        self.nacionalidad = nacionalidad
        self.salario = salario


class Piloto(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, puntos_campeonato=0, lesionado=False, titular=False):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score
        self.numero_auto = numero_auto
        self.puntos_campeonato = puntos_campeonato
        self.lesionado = lesionado
        self.titular = titular
    
    def __str__(self):
        return f"Cedula: {self.cedula} - Nombre: {self.nombre} - Fecha de nacimiento: {self.fecha_nacimiento} - Nacionalidad: {self.nacionalidad} - Salario: {self.salario} - Score: {self.score} - Numero de auto: {self.numero_auto} - Puntos del campeonato: {self.puntos_campeonato} - Lesionado: {self.lesionado} - Piloto titular: {self.titular}"


class Mecanico(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score
    
    def __str__(self):
        return f"Cedula: {self.cedula} - Nombre: {self.nombre} - Fecha de nacimiento: {self.fecha_nacimiento} - Nacionalidad: {self.nacionalidad} - Salario: {self.salario} - Score: {self.score}"

class JefeEquipo(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
    
    def __str__(self):
        return f"Cedula: {self.cedula} - Nombre: {self.nombre} - Fecha de nacimiento: {self.fecha_nacimiento} - Nacionalidad: {self.nacionalidad} - Salario: {self.salario}"

class Auto:
    def __init__(self, modelo, anio, score):
        self.modelo = modelo
        self.anio = anio
        self.score = score

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pilotos = []
        self.auto = None
        self.mecanicos = []
        self.jefe_equipo = []
        
    def agregar_empleado(self, lista_empleados):
        pilotos_titulares = 0
        piloto_reserva = 0
        cant_mecanicos = 0
        #while True:
        documento = ingresar_cedula()
        empleado_existente = buscar_empleado(documento, lista_empleados)
        if len(self.pilotos) < 3 and len(self.mecanicos) < 2 and self.jefe_equipo != None:    
            if empleado_existente in self.pilotos:
                raise ValoresDuplicados()
            elif empleado_existente in self.mecanicos:
                raise ValoresDuplicados()
            elif empleado_existente in self.jefe_equipo:
                raise ValoresDuplicados()
            for piloto in self.pilotos:
                tipo = type(piloto)
                if tipo == Piloto:
                    if piloto.titular == True:
                        pilotos_titulares += 1
                    else:
                        piloto_reserva += 1
                for mecanico in self.mecanicos:
                    tipo = type(mecanico)
                    if tipo == Mecanico:
                        cant_mecanicos += 1
                
            if type(empleado_existente) == Piloto:
                if empleado_existente.titular == True and pilotos_titulares <2:
                    self.pilotos.append(empleado_existente)
                    print(f"Empleado {empleado_existente.nombre} registrado")
                elif empleado_existente.titular == False and piloto_reserva == 0:
                    self.pilotos.append(empleado_existente)
                    print(f"Empleado {empleado_existente.nombre} registrado")
                else:
                    raise SinCupos()
            elif type(empleado_existente) == Mecanico:
                if cant_mecanicos < 8:
                    self.mecanicos.append(empleado_existente)
                    print(f"Empleado {empleado_existente.nombre} registrado")
                else:
                    raise SinCupos()
            elif tipo == JefeEquipo:
                if self.jefe_equipo != None:
                    self.jefe_equipo = empleado_existente
                    print(f"Empleado {empleado_existente.nombre} registrado")
                else:
                    raise SinCupos()
        else:
            print("EL equipo se encuentra completo")
            
        

def ingresar_cedula(): 
    cedula = input("Ingrese cedula: ")
    if len(cedula) != 8 or cedula.isdigit() == False:
        raise DatosIncorrectos()
    else:
        cedula = int(cedula)
        return cedula

def ingresar_nombre():
    nombre = input("Ingrese nombre: ")
    if nombre.isalpha() == True:
        return nombre
    else:
        raise DatosIncorrectos()
    
def validar_fecha(): #validacion
    fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
    validacion = False
    try:
        datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
        validacion = True
    except ValueError:
        validacion = False
    if validacion == True:
        return fecha_nacimiento
    else:
        raise FormatoIncorrecto()
    
def ingresar_nacionalidad():
    nacionalidad = input("Ingrese nacionalidad: ")
    if nacionalidad.isalpha() == True:
        return nacionalidad
    else:
        raise DatosIncorrectos()

def ingresar_salario():
    salario = input("Ingrese salario: ")
    if salario.isdigit() == False:
        raise DatosIncorrectos()
    else:
        salario = int(salario)
        return salario
    
def ingresar_score():
    valicacion = False
    try:
        score = int(input("Ingrese el score: "))
        if 1 < score < 99:
            valicacion = True
    except DatosIncorrectos:
        valicacion = False
    if valicacion == True:
        return score
    else:
        raise DatosIncorrectos()
    
def ingresar_numero_auto():
    numero_del_auto = input("Ingrese numero del auto del piloto: ")
    if numero_del_auto.isdigit() == False:
        raise DatosIncorrectos()
    else:
        numero_del_auto = int(numero_del_auto)
        return numero_del_auto
    
def ingresar_modelo():
    try:
        modelo = input("Ingrese modelo del auto: ")
    except DatosIncorrectos as e:
        print(e)
    return modelo
        
def ingresar_anio():
    try:
        anio = int(input("Ingrese el año del modelo: "))
        if 1900 < anio < 2024:
            validacion = True
    except DatosIncorrectos:
        validacion = False
    if validacion == True:
        return anio
    else:
        raise DatosIncorrectos()
    
def buscar_auto(modelo,lista_autos):
    for auto in lista_autos:
        if auto.modelo == modelo:
            return auto
        else:
            raise ObjetoNoExiste()

def buscar_empleado(documento, lista_empleados):
    for empleado in lista_empleados:
        if empleado.cedula == documento:
            return empleado
        else:
            raise ObjetoNoExiste()
    
def alta_empleado():   

    cedula = ingresar_cedula()
    nombre = ingresar_nombre()
    fecha_nacimiento = validar_fecha()
    nacionalidad = ingresar_nacionalidad()
    salario = ingresar_salario()
    try:
        cargo = int(input("""
Seleccione el cargo del empleado ingresando el número de la opción
1. Piloto
2. Piloto de reserva
3. Mecánico
4. Jefe de equipo
Opcion: """))
    except OpcionInvalida as e:
        print(e)
            
    if cargo == 1:
        try:
            score = ingresar_score()
            numero_auto = ingresar_numero_auto()
            return Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, puntos_campeonato=0, lesionado=False, titular=True)
        except DatosIncorrectos as e:
            print(e)
    elif cargo == 2:
        try:
            score = ingresar_score()
            numero_auto = ingresar_numero_auto()
            return Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, puntos_campeonato=0, lesionado=False, titular=False)
        except DatosIncorrectos as e:
            print(e)
    elif cargo == 3:
        try:
            score = ingresar_score()
            return Mecanico(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score,)
        except DatosIncorrectos as e:
            print(e)
    elif cargo == 4:
        try:
            return JefeEquipo(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
        except DatosIncorrectos as e:
            print({e}) 
    else:
        raise OpcionInvalida()

def alta_auto():
    modelo = ingresar_modelo()
    anio = ingresar_anio()
    score = ingresar_score()
    return Auto(modelo,anio,score)

def alta_equipo(lista_autos, lista_empleados):
    nombre = ingresar_nombre()
    equipo = Equipo(nombre)
    try:
        modelo= ingresar_modelo()
        auto = buscar_auto(modelo,lista_autos)
        equipo.auto = auto
    except DatosIncorrectos as e:
        print(e)
    
    for i in range(12):
        try:
            equipo.agregar_empleado(lista_empleados)
        except Exception as e:
            print(e)
    return equipo
        
def main():
    lista_equipos = []
    lista_empleados = []
    lista_autos = []
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
                lista_empleados.append(empleado)
                print(f"El empleado {empleado.nombre} fue registrado.")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "2":
            try:
                auto = alta_auto()
                lista_autos.append(auto)
                print(f"Auto {auto.modelo} fue resgistrado.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            try:
                equipo = alta_equipo(lista_autos, lista_empleados)
                lista_equipos.append(equipo)
                print(f"Equipo {equipo.nombre} registrado.")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "4":
            try:
                carrera = Carrera()
                carrera.simular_carrera(lista_equipos)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "5":
            try:
                consultas = Consultas(lista_equipos)
                consultas.prog_consultas()
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "6":
            break
        else:
            print("Opción no válida.") #volvia al programa principal?

if __name__ == "__main__":
    main()

    
