class SinCupos(Exception):
    def __init__(self):
        self.__codigo = 406
        self.__mensaje = "No quedan cupos disponibles para ingresar"
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def mensaje(self):
        return self.__mensaje
    
    def __str__(self):
        return f"Codigo: {self.codigo} - {self.mensaje}"