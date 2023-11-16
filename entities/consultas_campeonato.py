from exceptions.opcion_invalida import OpcionInvalida
class Consultas:
    def __init__(self,lista_de_equipos):
        self.__pilotos = []
        self.__lista_de_equipos = lista_de_equipos
        
    @property
    def pilotos(self):
        return self.__pilotos
    
    @pilotos.setter
    def pilotos(self,pilotos):
        self.__pilotos = pilotos
    
    @property
    def lista_de_equipos(self):
        return self.__lista_de_equipos
    
    @lista_de_equipos.setter
    def lista_de_equipos(self, lista_de_equipos):
        self.__lista_de_equipos = lista_de_equipos
        
    def ingresar_pilotos(self):
        for equipo in self.lista_de_equipos:
            for piloto in equipo.pilotos:
                if piloto.reserva == False and piloto.lesionado == False:
                    self.pilotos.append(piloto)
        
    def pilotos_con_mas_puntos(self):
        self.pilotos.sort(key=lambda piloto:piloto.puntos,reverse=True)
        for puntaje_piloto in self.pilotos[0:9]:
            print(puntaje_piloto)
            
    def resumen_constructores(self):
        print("Resumen del campeonato de constructores:")
        for equipo in self.lista_de_equipos:
            #for equipo in lista:
            puntos_equipo = 0
            for piloto in equipo.pilotos:
                puntos_equipo += piloto.puntos
            print(equipo.nombre + ": " + str(puntos_equipo) + " puntos")
            
    def mejores_pagos(self):
        self.pilotos.sort(key=lambda piloto:piloto.salario,reverse=True)
        for sueldo_piloto in self.pilotos[0:2]:
            print(sueldo_piloto)
            
    def habilidosos(self):
        self.pilotos.sort(key=lambda piloto:piloto.habilidad,reverse=True)
        for temp_habilidad in self.pilotos[0:3]:
            print(temp_habilidad)
            
    def directores(self):
        print("Directores de equipo:")
        for equipo in self.lista_de_equipos:
            print(equipo.nombre + " - Director: " + equipo.director.nombre)
            
    def prog_consultas(self):
        while True:
            print("""
1. Top 10 pilotos con más puntos en el campeonato
2. Resumen de campeonato de constructores
3. Top 5 de pilotos mejores pagos
4. Top 3 de pilotos mas habilidosos
5. Retornar jefes de equipo
6. Volver atras""")
            opcion = int(input("Seleccione una opción: "))
        
            if opcion == 1:
                try:
                    self.pilotos_con_mas_puntos()
                except Exception as e:
                    print(f"Error: {e}")
            elif opcion == 2:
                try:
                    self.resumen_constructores()
                except Exception as e:
                    print(f"Error: {e}")
            elif opcion == 3:
                try: 
                    self.mejores_pagos()
                except Exception as e:
                    print(f"Error: {e}")
            elif opcion == 4:
                try:
                    self.habilidosos()
                except Exception as e:
                    print(f"Error: {e}")
            elif opcion == 5:
                try:
                    self.directores()
                except Exception as e:
                    print(f"Error: {e}")
            elif opcion == 6:
                break
            else:
                raise OpcionInvalida()