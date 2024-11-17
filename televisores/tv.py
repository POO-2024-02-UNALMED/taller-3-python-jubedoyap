class TV:

    #atributo de clase
    _numTV = 0

    #Inicializador de los atributos de la clase TV
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    
    #Métodos get y set de marca
    def getMarca(self):
        return self._marca
    
    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca


    #Métodos get y set de canal
    def getCanal(self):
        return self._canal
    
    def setCanal(self, nuevoCanal):
        if self.getEstado() == True:
            if nuevoCanal >= 1 and nuevoCanal <=120:
                self._canal = nuevoCanal
            else:
                return
        else:
            return


    #Métodos get y set de precio
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, nuevoPrecio):
        self._precio = nuevoPrecio


    #Métodos get y set de volumen
    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, nuevoVolumen):
        if self.getEstado == True:
            if nuevoVolumen >= 0 and nuevoVolumen <=7:
                self._volumen = nuevoVolumen
            else:
                return
        else:
            return
        

    #Métodos get y set de control  
    def getControl(self):
        return self._control
    
    def setControl(self, nuevoControl):
        self._control = nuevoControl


    #método get y set de clase para numTv
    @classmethod

    def getNumTv(cls):
        return cls._numTV
    
    @classmethod

    def setNumTv(cls, nuevoNumTv):
        cls._numTV = nuevoNumTv

    
    #Métodos para encender y apagar el TV
    def turnOn(self):
        self._estado = True
    
    def turnOff(self):
        self._estado = False

    #Método para saber si el Tv está encendido o no
    def getEstado(self):
        return self._estado
    

    #Métodos para aumentar y disminuir el canal
    def canalUp(self):
        if self.getEstado() == True:
            if self.getCanal() < 120:
                self._canal += 1
            else:
                return
        else:
            return
    
    def canalDown(self):
        if self.getEstado() == True:
            if self.getCanal() > 1:
                self._canal -= 1
            else:
                return
        else:
            return
    
    #Métodos para aumentar y disminuir el volumen
    def volumenUp(self):
        if self.getEstado() == True:
            if self.getVolumen() < 7:
                self._volumen += 1
            else:
                return
        else:
            return
    
    def volumenDown(self):
        if self.getEstado == True:
            if self.getVolumen() > 0:
                self._volumen -= 1
            else:
                return
        else:
            return


    
    
    
