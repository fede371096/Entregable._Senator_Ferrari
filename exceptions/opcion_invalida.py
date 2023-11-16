class OpcionInvalida(Exception):
    def __init__(self):
        self.__codigo = 402
        self.__mensaje = "La opcion elegida es incorrecta"
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def mensaje(self):
        return self.__mensaje
    
    def __str__(self):
        return f"Codigo: {self.codigo} - {self.mensaje}"