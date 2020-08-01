class Estudiante:
  def __init__(self,nombre,apellido_P,apellido_M,matricula,asignatura_Fav):
    self.nombre = nombre
    self.apellido_P = apellido_P
    self.apellido_M = apellido_M
    self.matricula = matricula
    self.asignatura_Fav = asignatura_Fav
  def hacer_Tarea(self):  
    print("haciendo tarea")
  def estudiar(self):
    print("Estudiando")

class Estudiante_linea(Estudiante):
  estatura = ""
  promedio = ""
  generacion = ""
  carrera = ""
  def hacer_Tarea(self):  
    print("haciendo tarea pero mediante el polimorfismo")
  def estudiar(self):
    print("Estudiando mediante el polimorfismo")
  def trabajar(self):
    print("Trabajando")
  def comunicarse(self):
    print("comunicandose")
  def __str__(self):
        return """\
Nombre\t\t{}
Promedio\t{}""".format(self.nombre,self.promedio)


yael = Estudiante_linea("Yael","Garcia","Franco","1719110736","ninguna")
yael.estatura = 1.80
yael.promedio = 6
yael.generacion = "2019 - 2029"
yael.carrera = "Tic´s"
print("Metodos")
yael.hacer_Tarea()
yael.estudiar()
yael.trabajar()
yael.comunicarse()
print("Atributos")
print(yael)