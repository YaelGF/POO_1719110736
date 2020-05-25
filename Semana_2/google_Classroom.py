class Google:
  
    def __init__(self,usuario,fecha_limite,fecha_publicado,hora_limite,calendario,clase,profesor,alumnos,actividades):
        self.usuario = usuario
        self.fecha_limite = fecha_limite
        self.fecha_publicado = fecha_publicado
        self.hora_limite = hora_limite
        self.calendario = calendario
        self.clase = clase
        self.profesor = profesor
        self.alumnos = alumnos
        self.actividades = actividades
        print("Se acaba de crear un objeto")
    def subir(self):
        print("Archivo subido")
    def bajar(self):
        print("Archivo descargado")
    def mandar_msn(self):
        print("mensaje enviado")
    def comentar(self):
        print("comentado")
    def asignar_trabajo(self):
        print("error")
    def __str__(self):
        return "el usuario {} tenia como fecha limite {} a la hora de {} para subir su actividad".format(self.usuario,self.fecha_limite,self.hora_limite)
yael = Google("yael","hoy","ahce 1 semana",12,"no","POO","SAlvador",19,"ninguna")                                                                                              
print("Metodos")
yael.subir()
yael.bajar()
yael.mandar_msn()
yael.comentar()
yael.asignar_trabajo()
print("Atributos")
print(str(yael))