class figuras:
    def cal_area(self):
        return 0

class rectangulo(figuras):
    def _init_(self,largo,ancho):
        self.__largo = largo
        self.__ancho = ancho

    def getLargo(self):
        return self.__largo

    def setLargo(self, largo):
        self.__largo = largo

    def getAncho(self):
        return self.__ancho

    def setAncho(self, ancho):
        self.__ancho = ancho

    def cal_area(self):
        return self._largo * self._ancho

    def getInfo(self):
        print(f"largo {self._largo} \n ancho {self._ancho}, \n area: {self.cal_area()}")

class circulo(figuras):
    def _init_(self, radio):
        self.__radio = radio

    def getradio(self):
        return self.__radio

    def setRadio(self, radio):
        self.__radio = radio

    def cal_area(self):
        return 3.14 * self.__radio ** 2

    def getInfo(self):
        print(f"radio {self._radio}, \n area: {self.cal_area()}")

class triangulo(figuras):
    def _init_(self, altura, base):
        self.__altura = altura
        self.__base = base

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def cal_area(self):
        return (self._altura * self._base) / 2

    def getInfo(self):
        print(f"altura {self._altura} \n base {self._base}, \n area: {self.cal_area()}")