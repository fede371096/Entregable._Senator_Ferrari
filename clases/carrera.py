class Carrera:
    def __init__(self, equipos:[]):
        self.__equipos  = equipos
        self.__pilotos = self.agregar_pilotos_carrera
        self.__abandonos = []
        self.__errores_en_pits = []
        self.__penalidades_pilotos = []
        self.__posiciones = []
    
    @property
    def equipos(self):
        return self.__equipos
    
    @equipos.setter
    def equipos(self, equipos):
        self.__equipos = equipos
    
    def agregar_pilotos_carrera(self):
        pilotos = []
        for equipo in self.equipos:
            for piloto in equipo.pilotos:
                if piloto.lesionado == False and piloto.reserva == False:
                    pilotos.append(piloto)
        return pilotos
        
    @property
    def pilotos(self):
        return self.__pilotos
    
    @pilotos.setter
    def pilotos(self, pilotos):
        self.__pilotos = pilotos
        
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
    def penalidades_pilotos(self):
        return self.__penalidades_pilotos
    
    @penalidades_pilotos.setter
    def penalidades_pilotos(self, penalidades_pilotos):
        self.__penalidades_pilotos = penalidades_pilotos
        
    @property
    def posiciones(self):
        return self.__posiciones
    
    @posiciones.setter
    def posiciones(self, posiciones):
        self.__posiciones = posiciones
        
    def piloto_abandona(self, numero_coche):
        for abandono in self.abandonos:
            if abandono.numero_coche == numero_coche:
                raise
            else:    
                for equipo in self.equipos:
                    for piloto in equipo:
                        if piloto.numero_coche == numero_coche:
                            self.abandonos.append(piloto)
                            
    def error_en_pits(self, numero_coche):
        for piloto in self.pilotos:
            if piloto.numero_coche == numero_coche:
                self.errores_en_pits.append(piloto)
                
    def penalidad(self, numero_coche):
        for piloto in self.pilotos:
            if piloto.numero_coche == numero_coche:
                self.abandonos.append(piloto)
                
    def score_equipo(self, equipo):
        score_equipo = 0
        for temp_equipo in self.equipos:
            if temp_equipo == equipo:
                for temp_mecanico in temp_equipo.mecanicos:
                    score_equipo += temp_mecanico.score
                for temp_auto in temp_equipo.auto:
                    score_equipo += temp_auto.score
                for temp_piloto in temp_equipo.pilotos:
                    if temp_piloto.lesionado == False and temp_piloto.reserva == False:
                        score_equipo += temp_piloto.score
        return score_equipo
                                    
    def score_final(self):
        score_equipo = 0
        for equipo in self.equipos:
            score_equipo = self.score_equipo(equipo)
            for piloto in equipo:
                penalidades = 0
                errores = 0
                for contador in self.penalidades_pilotos:
                    if piloto == contador:
                        penalidades +=1
                for contador in self.errores_en_pits:
                    if piloto == contador:
                        errores +=1
                if piloto in self.abandonos:
                    self.posiciones.append(piloto)
                else:
                    piloto.puntaje = score_equipo - (penalidades*5) - (errores*8)
                    self.__posiciones.append(piloto)
                
                
                
            

        
        
            
                    
              
        
    
        
    
        