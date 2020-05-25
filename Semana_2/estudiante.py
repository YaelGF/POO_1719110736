class Estudiante:
  
  def __init__(self,nombre,apellido_P,apellido_M,matricula,asignatura_Fav,estatura,promedio,generacion,carrera):
    self.nombre = nombre
    self.apellido_P = apellido_P
    self.apellido_M = apellido_M
    self.matricula = matricula
    self.asignatura_Fav = asignatura_Fav
    self.estatura = estatura
    self.promedio = promedio
    self.generacion = generacion
    self.carrera = carrera
    print("Se acaba de crear un objeto")

  def hacer_Tarea(self):
    print("haciendo tarea")
  def estudiar(self):
    print("Estudiando")
  def dormir(self):
    print("Durmiendo")
  def trabajar(self):
    print("Trabajando")
  def comunicarse(self):
    print("comunicandose")

  def __str__(self):
    return "EL alumno {} de estatura {} con promedio de {} de la carrera {} de la generacion {}".format(self.nombre,
                                                                                                       self.estatura,
                                                                                                       self.promedio,
                                                                                                       self.carrera,
                                                                                                       self.generacion)

yael = Estudiante("Yael","Garcia","Franco","1719110736","ninguna","1.80","6.0","2019-2029","Programacion")
print("Metodos")
yael.hacer_Tarea()
yael.estudiar()
yael.dormir()
yael.trabajar()
yael.comunicarse()
print("Atributos")
print(str(yael))