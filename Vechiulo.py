class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        color = self.color
        ruedas = self.ruedas
        puertas = self.puertas
    def __str__(self) -> str:
        return f"Color {self.color}, {self.ruedas} ruedas, {self.puertas}puertas"
        

class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad= velocidad
        self.cilindrada = cilindrada
    def __str__(self) -> str:
        return f"color {self.color}, {self.velocidad} km/h, {self.cilindrada}cc,{self.puertas} puertas, {self.ruedas} ruedas" 
      
coche = Coche("verde", 4,5,120,1600,)
print(coche)


