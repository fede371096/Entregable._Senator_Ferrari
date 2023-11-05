class Carrera:
    def __init__(self, equipos:[]):
        self.__equipos  = equipos
        self.__pilotos = self.agregar_pilotos_carrera
        self.__abandonos = []
        self.__errores_en_pits = []
        self.__penalidades_pilotos = []
    
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

#Se obtiene la habilidad del auto y de los mecanicos del equipo ingresado en el parametro              
    def habilidad_equipo(self, equipo):
        habilidad_equipo = 0
        for temp_equipo in self.equipos:
            if temp_equipo == equipo:
                for temp_mecanico in temp_equipo.mecanicos:
                    habilidad_equipo += temp_mecanico.habilidad
                for temp_auto in temp_equipo.auto:
                    habilidad_equipo += temp_auto.habilidad
        return habilidad_equipo
                 
#Se obtiene la habilidad final del piloto en la carrera teniendo en cuenta abandonos, penalizaciones y errores en pits                   
    def habilidad_carrera(self):
        for piloto in self.pilotos:
            if piloto not in self.abandonos:
                for equipo in self.equipos:
                    if piloto in equipo.pilotos:
                        piloto.habilidad_carrera = 0
                        penalidades = 0
                        errores = 0
                        for piloto_penalidad in self.penalidades_pilotos:
                            if piloto_penalidad == piloto:
                                penalidades +=1
                        for piloto_error in self.errores_en_pits:
                            if piloto_error == piloto:
                                errores +=1
                        piloto.habilidad_carrera = self.habilidad_equipo(equipo) + piloto.habilidad - (penalidades*5) - (errores*8)
            else:
                piloto.habilidad_carrera = 0

#Se asignan los puntos de la carrera al piloto          
    def puntaje_piloto(self):
        posiciones = sorted(self.pilotos, key=habilidad_carrera)
        for piloto in posiciones:
            if piloto == posiciones[0]:
                piloto.puntaje += 25
            elif piloto == posiciones[1]:
                piloto.puntaje += 18
            elif piloto == posiciones[2]:
                piloto.puntaje += 15
            elif piloto == posiciones[1]:
                piloto.puntaje += 12
            elif piloto == posiciones[1]:
                piloto.puntaje += 10
            elif piloto == posiciones[1]:
                piloto.puntaje += 8
            elif piloto == posiciones[1]:
                piloto.puntaje += 6
            elif piloto == posiciones[1]:
                piloto.puntaje += 4
            elif piloto == posiciones[1]:
                piloto.puntaje += 2
            elif piloto == posiciones[1]:
                piloto.puntaje += 1
            else:
                piloto.puntaje += 0
        posiciones.sort(key=puntaje)
        

