class Banco:
  
  def __init__(self,nombre,tasa_interes,cobertura,sucursales,empleados,seguridad,conexion_internacional,agilidad,rapidez,clientes):
    self.nombre = nombre
    self.tasa_interes = tasa_interes
    self.cobertura = cobertura
    self.sucursales = sucursales
    self.empleados = empleados
    self.seguridad =seguridad
    self.conexion_internacional = conexion_internacional
    self.agilidad = agilidad
    self.rapidez = rapidez
    self.clientes = clientes
    
    print("Se acaba de crear un objeto")

  def retirar_Efectivo(self):
    print("Se a retirado el efectivo")
  def deposito(self):
    print("Se a Depositado")
  def transferencia(self):
    print("Se a transferido")
  def pago_Servicio(self):
    print("Pago Realizado")
  def inversion(self):
    print("Se a retirado la inversion")
  def __str__(self):
    return "EL banco {} tiene una tasa de interes de {} tiene una rapidez en sus operaciones {}".format(self.nombre,self.tasa_interes
                                                                                                          , self.rapidez)


bbva = Banco("bbva","16.01","si",120,15000,"mucha","si",",muy eficaz","como el rayo mcqueen", 25000)
str(bbva)
print("Metodos")
bbva.retirar_Efectivo()
bbva.deposito()
bbva.transferencia()
bbva.pago_Servicio()
bbva.inversion()
print("Atributos")
print(str(bbva))
