class Control:

    #Método para enlazar el control remoto con TV
    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)

    
    #Métodos get y set para TV
    def getTv(self):
        return self._tv
    
    def setTv(self, nuevoTv):
        self._tv = nuevoTv

    #Métodos para controlar el encendido y el apagado desde el control remoto
    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()

    
    #Métodos para subir o bajar de canal desde el control remoto
    def canalUp(self):
        self._tv.canalUp()
    
    def canalDown(self):
        self._tv.canalDown()

    
    #Métodos para subir o bajar el volumen desde el control remoto
    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()


    #Método para elegir cualquier canal
    def setCanal(self, nuevoCanal):
        self._tv.setCanal(nuevoCanal)

    
    #Método para elegir el volumen
    def setVolumen(self, nuevoVolumen):
        self._tv.setVolumen(nuevoVolumen)