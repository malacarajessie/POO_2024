"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

METODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar valor a los atributos del objeto al crearlo, es el primer metodo que se ejecuta al crear el objeto y se manda llamar automaticamente al crearlo, es decir
este metodo puede recibir parametros al momento de crear el objeto
cuando se crea un metodo contructor se utiliza la funcion init() para que se llame automaticamente cada  vez 
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    color="rojo"
    marca="Ferrari"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2

    #Metodos o acciones o funciones que hace el objeto 
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
     self.color=color
     self.marca=marca
     self.modelo=modelo
     self.velocidad=velocidad
     self.caballaje=caballaje
     self.plazas=plazas

     #el encapsulamiento o visibilida es importante que atravez de el es posible que python sepa como vava utilizar los atributos y metodos de clase

     #atributo publico
     atributo_publico="soy un atributo publico"
     #atributo privado
     __atributo_privado="soy un atributo privado"
     #metodos o acciones
     #nota 1 para utilizar un atributo privado en necesario utilizarlo dentro de uno publico
     def MetodoPublico(self):
        return self.__atributo_privado
     
     #metodo privado
    def __metodoprivado(self):
        print("soy un metodo privado")

#nota 2 para utilizar un metodo privado es necesario usarlo dentro de un metodo publico
    def getMetodoPublico(self):
       self.__metodoprivado()
    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPlazas(self):
       return self.plazas

    def setPlazas(self,plazas):
      self.plazas=plazas 

    def getInfo(self):
       print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")  

#Fin definir clase






#clases secundarias, subclases, hijas
class camiones(Coches):
   def __init__(self, color, marca, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
      super().__init__(color, marca, modelo, velocidad, caballaje, plazas)
      self.eje=eje
      self.capacidadcarga=capacidadcarga

__tipo_carga=""
def cargar(self,tipo_carga ):
      self.tipo_carga=tipo_carga
      return self.tipo_carga

def geteje(self):
   return self.eje

def geteje(self,eje):
   self.eje=eje

def getcapacidadcarga(self):
   return self.capacidacarga

def getcapacidacarga(self,capacidadcarga):
   self.capacidacarga=capacidadcarga

def gettipo_carga(self):
   return self.tipo_carga

def gettipo_cargaa(self,tipo_carga):
   self.tipo_carga=tipo_carga


class camionetas(Coches):
   def __init__(self, color, marca, modelo, velocidad, caballaje, plazas, traccion, cerrada, transportar):
      super().__init__(color, marca, modelo, velocidad, caballaje, plazas)
      self.traccion=traccion
      self.cerrada=cerrada

__transportar=""
def transportar(self,transportar):
      self.transportar=transportar
      return self.transportar

def gettransportar(self):
   return self.transportar

def geteje(self,eje):
   self.eje=eje

def getcapacidadcarga(self):
   return self.capacidacarga

def getcapacidacarga(self,capacidadcarga):
   self.capacidacarga=capacidadcarga

def gettipo_carga(self):
   return self.tipo_carga

def gettipo_cargaa(self,tipo_carga):
   self.tipo_carga=tipo_carga




