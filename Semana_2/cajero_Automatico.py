class Cajero:
  
    def __init__(self,referencia,monto,interes,destinatario,fecha,horario,iva,unidad_monetaria,sucursal):
        self.referencia = referencia
        self.monto = monto
        self.interes = interes
        self.destinatario = destinatario
        self.fecha = fecha
        self.horario = horario
        self.iva = iva
        self.unidad_monetaria =unidad_monetaria
        self.sucursal = sucursal
        print("Se acaba de crear un objeto")
    def retirar(self):
        print("retirando")
    def depositar(self):
        print("depositando")
    def pagar_servicio(self):
        print("pagando")
    def transferencia(self):
        print("transfiriendo")
    def cobrar(self):
        print("cobrando")
    def __str__(self):
        return "la sucursal {} usa la unidad de moneda {} ".format(self.sucursal,self.unidad_monetaria)
retiro = Cajero("151515151",1500,.16,"yael","hoy","1:25 am",.16,"MXN","Banorte")
print("Metodos")
retiro.retirar()
retiro.depositar()
retiro.pagar_servicio()
retiro.transferencia()
retiro.cobrar()
print("Atributos")
print(str(retiro))