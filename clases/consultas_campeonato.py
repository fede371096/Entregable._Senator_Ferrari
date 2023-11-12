#Asignar la lista de pilotos y de equipos del main del programa a este modulo para que los agregue automaticamente
from carrera import Carrera.pilotos
from carrera import Carrera.equipos

class Consultas:
    def __init__(self,):
        self.__pilotos = [pilotos]
    
    def ingresar_pilotos(self, pilotos):
        for piloto in lista_pilotos:
            self.pilotos.append(piloto)

    @property
    def pilotos(self):
        return self.__pilotos
    
    @pilotos.setter
    def pilotos(self,pilotos):
        self.__pilotos = pilotos
        
    def pilotos_con_mas_puntos(self):
        self.pilotos.sort(key=lambda piloto:piloto.puntos,reverse=True)
        for puntaje_piloto in self.pilotos[0:9]:
            print(puntaje_piloto)
    
    #Vincular la lista de equipo a la lista del main        
    def resumen_constructores(self):
        print("Resumen del campeonato de constructores:")
        for lista in equipos:
            for equipo in lista:
                puntos_equipo = 0
                for piloto in equipo.pilotos:
                    puntos_equipo += piloto.puntos
            print(equipo.nombre + ": " + str(puntos_equipo) + " puntos")
            
    def mejores_pagos(self):
        self.pilotos.sort(key=lambda piloto:piloto.salario,reverse=True)
        for sueldo_piloto in self.pilotos[0:2]:
            print(sueldo_piloto)
    
    #Vincular la lista de equipos a la lista del main 
    def directores(self):
        for lista in equipos:
            for equipo in lista:
                print(equipo.nombre + " - Director: " + equipo.director.nombre)