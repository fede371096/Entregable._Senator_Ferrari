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
        for temp_equipo in equipo:
            self.equipos.append(temp_equipo)
        
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
        for lista in numero_de_auto:
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
        for auto in equipo.auto:
            suma_de_habilidad += auto.habilidad
        return suma_de_habilidad
    
    def puntos_totales(self):
        for piloto in self.pilotos:
            piloto.puntos = 0
            if piloto in self.abandonos:
                piloto.puntos = 0
            else:
                errores = self.errores_en_pits.count(piloto)
                penalidad = self.penalidades.count(piloto)
                equipo = self.obtener_equipo(piloto.numero)
                piloto.habilidad_total = self.habilidad_mecanicos(equipo) + self.habilidad_auto(equipo) + piloto.habilidad - (errores*5) - (penalidad*8)
        self.pilotos.sort(key=lambda piloto:piloto[-1])
        

