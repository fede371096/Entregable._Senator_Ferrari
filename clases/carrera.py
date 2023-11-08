class Carrera:
    def __init__(self):
        self.__equipos  = []
        self.__abandonos = []
        self.__errores_en_pits = []
        self.__penalidades = []
        self.__pilotos = []
    
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
        
    def vincular_equipo(self, *equipo):
        self.equipos.append(equipo)
        
    def ingresar_pilotos(self):
        for lista in self.equipos:
            for equipo in lista:
                for piloto in equipo.pilotos:
                    if piloto.reserva == False and piloto.lesionado == False:
                        self.pilotos.append(piloto)
          
    def ingresar_abandonos(self, *numero_de_auto):
        for numero in numero_de_auto:
            for lista in self.equipos:
                for equipo in lista:
                    for piloto in equipo.pilotos:
                        if piloto.numero_de_auto == numero:
                            self.abandonos.append(piloto)
                            
    def ingresar_errores(self, *numero_de_auto):
        for numero in numero_de_auto:
            for lista in self.equipos:
                for equipo in lista:
                    for piloto in equipo.pilotos:
                        if piloto.numero_de_auto == numero:
                            self.errores_en_pits.append(numero)
                            
    def ingresar_penalidades(self, *numero_de_auto):
        for numero in numero_de_auto:
            for lista in self.equipos:
                for equipo in lista:
                    for piloto in equipo.pilotos:
                        if piloto.numero_de_auto == numero:
                            self.penalidades.append(numero)

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
        for piloto in self.pilotos:
            if piloto == self.pilotos[0]:
                piloto.puntos += 25
            elif piloto == self.pilotos[1]:
                piloto.puntos += 18
            elif piloto == self.pilotos[2]:
                piloto.puntos += 15
            elif piloto == self.pilotos[3]:
                piloto.puntos += 12
            elif piloto == self.pilotos[4]:
                piloto.puntos += 10
            elif piloto == self.pilotos[5]:
                piloto.puntos += 8
            elif piloto == self.pilotos[6]:
                piloto.puntos += 6
            elif piloto == self.pilotos[7]:
                piloto.puntos += 4
            elif piloto == self.pilotos[8]:
                piloto.puntos += 2
            elif piloto == self.pilotos[9]:
                piloto.puntos += 1
    
    def puntos_totales(self):
        for piloto in self.pilotos:
            piloto.habilidad_total = 0
            if piloto in self.abandonos:
                piloto.puntos += 0
            else:
                errores = self.errores_en_pits.count(piloto)
                penalidad = self.penalidades.count(piloto)
                equipo = self.obtener_equipo(piloto.numero)
                piloto.habilidad_total = self.habilidad_mecanicos(equipo) + self.habilidad_auto(equipo) + piloto.habilidad - (errores*5) - (penalidad*8)
            self.pilotos.sort(key=lambda piloto:piloto[-1])
        self.asignar_puntos()
        

