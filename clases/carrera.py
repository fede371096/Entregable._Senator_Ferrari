from exceptions.datos_incorrectos import DatosIncorrectos
from exceptions.valores_duplicados import ValoresDuplicados

class Carrera:
    def __init__(self):
        self.__equipos  = []
        self.__abandonos = []
        self.__errores_en_pits = []
        self.__penalidades = []
        self.__pilotos = []
        self.__posiciones = []
    
    @property
    def equipos(self):
        return self.__equipos
    
    @equipos.setter
    def equipos(self, equipos):
        self.__equipos = equipos
    
    @property
    def abandonos(self):
        return self.__abandonos
    
    @abandonos.setter
    def abandonos(self, abandonos):
        self.__abandonos = abandonos
        
    @property
    def errores_en_pits(self):
        return self.__errores_en_pits
    
    @errores_en_pits.setter
    def errores_en_pits(self, errores_en_pits):
        self.__errores_en_pits = errores_en_pits
        
    @property
    def penalidades(self):
        return self.__penalidades
    
    @penalidades.setter
    def penalidades(self, penalidades):
        self.__penalidades = penalidades
        
    @property
    def pilotos(self):
        return self.__pilotos
    
    @pilotos.setter
    def pilotos(self, pilotos):
        self.__pilotos = pilotos
        
    @property
    def posiciones(self):
        return self.__posiciones
    
    @posiciones.setter
    def posiciones(self, posiciones):
        self.__posiciones = posiciones
        
    def vincular_equipo(self, lista_de_equipo):
        for equipo in lista_de_equipo:
            self.equipos.append(equipo)
        
    def ingresar_pilotos(self):
        for lista in self.equipos:
            for equipo in lista:
                for piloto in equipo.pilotos:
                    if piloto.reserva == False and piloto.lesionado == False:
                        self.pilotos.append(piloto)
          
    def ingresar_abandonos(self):
        coche = str(input("Si no existen abandonos presione Enter, de lo contrario ingrese el numero de auto del piloto que ha abandonado la carrera: "))
        if coche != str:
            raise DatosIncorrectos()
        
        for piloto in self.abandonos:
            if piloto.numero_de_auto == int(coche):
                raise ValoresDuplicados()
        
        while coche != "":
            if coche.isdigit() == True:
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == int(coche):
                        self.abandonos.append(piloto)
            else:
                raise DatosIncorrectos()
                            
    def ingresar_errores(self):
        coche = str(input("Si no existen errores presione Enter, de lo contrario ingrese el numero de auto del piloto que ha cometido algun error: "))
        if coche != str:
            raise DatosIncorrectos()
        
        while coche != "":
            if coche.isdigit() == True:
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == int(coche):
                        self.errores_en_pits.append(piloto)
            else:
                raise DatosIncorrectos()
                            
    def ingresar_penalidades(self):
        coche = str(input("Si no existen penalidades presione Enter, de lo contrario ingrese el numero de auto del piloto al cual se lo ha penalizado: "))
        if coche != str:
            raise DatosIncorrectos()
        
        while coche != "":
            if coche.isdigit() == True:
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == int(coche):
                        self.penalidades.append(piloto)
            else:
                raise DatosIncorrectos()

    def obtener_equipo(self,numero_de_auto):
        for lista in self.equipos:
            for equipo in lista:
                for piloto in equipo.pilotos:
                    if piloto.numero_de_auto == numero_de_auto:
                        return equipo
                            
    def habilidad_mecanicos(self,equipo):
        suma_de_habilidad = 0
        for mecanico in equipo.mecanicos:
            suma_de_habilidad += mecanico.habilidad
        return suma_de_habilidad
    
    def habilidad_auto(self,equipo):
        suma_de_habilidad = 0
        for temp_equipo in self.equipos:
            if equipo == temp_equipo:
                suma_de_habilidad += equipo.auto.habilidad
        return suma_de_habilidad
    
    def asignar_puntos(self):
        for posicion in self.posiciones:
            if posicion == self.posiciones[0]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 25
            elif posicion == self.posiciones[1]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 18
            elif posicion == self.posiciones[2]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 15
            elif posicion == self.posiciones[3]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 12
            elif posicion == self.posiciones[4]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 10                      
            elif posicion == self.posiciones[5]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 8
            elif posicion == self.posiciones[6]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 6
            elif posicion == self.posiciones[7]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 4
            elif posicion == self.posiciones[8]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 2
            elif posicion == self.posiciones[9]:
                auto = posicion[0]
                for piloto in self.pilotos:
                    if piloto.numero_de_auto == auto:
                        piloto.puntos += 1
    
    def puntos_totales(self):
        for piloto in self.pilotos:
            score_final = 0
            if piloto in self.abandonos:
                piloto.puntos += 0
            else:
                errores = self.errores_en_pits.count(piloto)
                penalidad = self.penalidades.count(piloto)
                equipo = self.obtener_equipo(piloto.numero_de_auto)
                score_final = self.habilidad_mecanicos(equipo) + self.habilidad_auto(equipo) + piloto.habilidad - (errores*5) - (penalidad*8)
                self.posiciones.append((piloto.numero_de_auto,score_final))    
        self.posiciones.sort(key=lambda piloto:piloto[1],reverse=True)
        self.asignar_puntos()
        
    def simular_carrera(self, lista_de_equipos):
        self.vincular_equipo(lista_de_equipos)
        self.ingresar_pilotos()
        self.ingresar_abandonos()
        self.ingresar_errores()
        self.ingresar_penalidades()
        self.puntos_totales()
        

