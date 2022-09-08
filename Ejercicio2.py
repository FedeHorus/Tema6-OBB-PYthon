class Alumno:
    
    def datos(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        
        
    def imprimir(self):
        
        print("nota:", self.nota)
        print("Almuno: ", self.nombre)
        
        
    def resultado(self):
        
        if self.nota < 6:
            print("El alumno no aprobo")  
            
        else:
            print("El alumno aprobo!")  
            
            
alumno = Alumno()

alumno.datos(input("Ingrese nombre:"), int(input("Ingrese nota:")))      

alumno.imprimir()
alumno.resultado()    