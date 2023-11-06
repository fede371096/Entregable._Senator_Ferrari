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
