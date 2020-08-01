class Cajero:
  def __init__(self,referencia,monto,interes,destinatario,fecha):
    self.referencia = referencia
    self.monto = monto
    self.interes = interes
    self.destinatario = destinatario
    self.fecha = fecha
  def retirar(self):
    print("retirando")
  def depositar(self):
    print("depositando")
class Banco (Cajero):
  horario  = ""
  iva = ""
  unidad_Monetaria = ""
  sucursal = ""
  def retirar(self):
    print("retirando mediante el polimorfismo")
  def depositar(self):
    print("depositando mediante el polimorfismo")
  def pagar_servicio(self):
    print("pagando")
  def transferencia(self):
    print("transfiriendo")
  def __str__(self):
        return """\
Referencia\t{}
IVA\t\t\t{}
        """.format(self.referencia,self.iva)
cA = Banco("151515151",1500,.16,"yael","hoy")
cA.horario = "1:25"
cA.iva = .16
cA.unidad_Monetaria = "MXN"
cA.sucursal = "Banorte"
print("Metodos")
cA.retirar()
cA.depositar()
cA.pagar_servicio()
cA.transferencia()
print("Atributos")
print(cA)