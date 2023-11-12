class DatosIncorrectos(Exception):
    def __init__(self):
        self.__codigo = 400
        self.__mensaje = "Los datos ingresados son incorrectos"
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def mensaje(self):
        return self.__mensaje
    
    def __str__(self):
        return f"Codigo: {self.codigo} - {self.mensaje}"