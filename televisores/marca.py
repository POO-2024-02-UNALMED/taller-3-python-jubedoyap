class Marca:

    #Inicializador del atributo de la clase marca
    def __init__(self, nombre):
        self._nombre = nombre
    

    #métodos get y set de nombre
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre