#from exceptions.opcion_invalida import OpcionInvalida
class Consultas:
    def __init__(self,lista_equipos):
        self.__pilotos = []
        self.__lista_equipos = lista_equipos
        
    @property
    def pilotos(self):
        return self.__pilotos
    
    @pilotos.setter
    def pilotos(self,pilotos):
        self.__pilotos = pilotos
    
    @property
    def lista_equipos(self):
        return self.__lista_equipos
    
    @lista_equipos.setter
    def lista_equipos(self, lista_equipos):
        self.__lista_equipos = lista_equipos
        
    def ingresar_pilotos(self):
        for equipo in self.lista_equipos:
            for piloto in equipo.pilotos:
                if piloto.titular == True and piloto.lesionado == False:
                    self.pilotos.append(piloto)
        
    def pilotos_con_mas_puntos(self):
        print("""
              
Pilotos con mas puntos
""")
        self.pilotos.sort(key=lambda piloto:piloto.puntos_campeonato,reverse=True)
        contador = 0
        for puntaje_piloto in self.pilotos[0:9]:
            contador +=1
            print(f"{contador}. {puntaje_piloto.nombre} - Puntos: {puntaje_piloto.puntos_campeonato}")
            
    def resumen_constructores(self):
        print("""
-----------------------
Resumen del campeonato de constructores""")
        for equipo in self.lista_equipos:
            #for equipo in lista:
            puntos_equipo = 0
            for piloto in equipo.pilotos:
                puntos_equipo += piloto.puntos_campeonato
            print(equipo.nombre + ": " + str(puntos_equipo) + " puntos")
            
    def mejores_pagos(self):
        print("""
-----------------------
Top 5 pilotos mejores pago
""")
        self.pilotos.sort(key=lambda piloto:piloto.salario,reverse=True)
        contador = 0
        for sueldo_piloto in self.pilotos[0:4]:
            contador += 1
            print(f"{contador}. {sueldo_piloto.nombre} - Sueldo: {sueldo_piloto.salario}")
            
    def habilidosos(self):
        print("""
-----------------------
Top 3 mas habilidosos
""")
        self.pilotos.sort(key=lambda piloto:piloto.score,reverse=True)
        contador = 0
        for temp_habilidad in self.pilotos[0:3]:
            contador += 1
            print(f"{contador}. {temp_habilidad.nombre} - {temp_habilidad.score}")
            
    def directores(self):
        print("""
-----------------------
Directores de equipo
""")
        for equipo in self.lista_equipos:
            print(equipo.nombre + " - Director: " + equipo.jefe_equipo.nombre)
        print(""" 
-----------------------              
              """)
            
    def prog_consultas(self):
        try:
            self.ingresar_pilotos()
            self.pilotos_con_mas_puntos()
            self.resumen_constructores()
            self.mejores_pagos()
            self.habilidosos()
            self.directores()
        except Exception as e:
            print(e)
            
#         while True:
#             print("""
# 1. Top 10 pilotos con más puntos en el campeonato
# 2. Resumen de campeonato de constructores
# 3. Top 5 de pilotos mejores pagos
# 4. Top 3 de pilotos mas habilidosos
# 5. Retornar jefes de equipo
# 6. Volver atras""")
#             opcion = int(input("Seleccione una opción: "))
        
#             if opcion == 1:
#                 try:
#                     self.pilotos_con_mas_puntos()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             elif opcion == 2:
#                 try:
#                     self.resumen_constructores()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             elif opcion == 3:
#                 try: 
#                     self.mejores_pagos()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             elif opcion == 4:
#                 try:
#                     self.habilidosos()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             elif opcion == 5:
#                 try:
#                     self.directores()
#                 except Exception as e:
#                     print(f"Error: {e}")
#             elif opcion == 6:
#                 break
#             else:
#                 raise OpcionInvalida()