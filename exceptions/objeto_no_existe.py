class ObjetoNoExiste(Exception):
    def __init__(self):
        self.__codigo = 405
        self.__mensaje = "El objetos no existe"
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def mensaje(self):
        return self.__mensaje
    
    def __str__(self):
        return f"Codigo: {self.codigo} - {self.mensaje}"