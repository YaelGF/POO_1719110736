class Banco:
  
    def __init__(self,nombre,tasa_interes,cobertura,sucursales,empleados):
        self.nombre = nombre
        self.tasa_interes = tasa_interes
        self.cobertura = cobertura
        self.sucursales = sucursales
        self.empleados = empleados
        
    def retirar_Efectivo(self):
        print("Se a retirado el efectivo")
    def deposito(self):
        print("Se a Depositado")
    def transferencia(self):
        print("Se a transferido")
class Banco_Digital(Banco):
    seguridad = ""
    rapidez = ""
    agilidad = ""
    conexion_internacional = ""                          
    clientes = ""  
    
    def pago_Servicio(self):
        print("Pago Realizado")
    def inversion(self):
        print("Se a retirado la inversion")
    def __str__(self):
        return """\
Nombre\t\t{}
Clientes\t{}
        """.format(self.nombre,self.clientes)
    
bbva = Banco_Digital("bbva","16.01","si",120,15000) 
bbva.seguridad = "mucha"
bbva.rapidez =  "casi le llega al mcqueen"
bbva.agilidad = "muy agil"
bbva.conexion_internacional = "si" 
print("Metodos")
bbva.clientes =  250000
bbva.retirar_Efectivo()
bbva.deposito()
bbva.transferencia()
bbva.pago_Servicio()
bbva.inversion()
print("Atributos")
print(bbva)