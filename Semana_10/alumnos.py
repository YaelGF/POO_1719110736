class Alumnos():
#creacion de la clase y metodo
  def get_data(self):
    #declaracion de variables
    students = [] 
    answer = "s"
    #inicio del ciclo
    while answer == "s": 
      #declaracion y asignacion de las variables
      name = input("Ingresa el nombre del alumno: ")
      year_birth = int (input("Ingresa año de nacimiento: "))
      group = input("Ingrsa el grupo del alumno: ")
      answer = input("Seguir ingresando datos(s/n) :")
      #asignacion de las variables en diccionario
      student = {"name" : name ,"year" : 2020 - year_birth}
      #asignacion de dicionarios dentro de listas
      students.append(student)
    #regreso de los valores de la lista
    return students
class Send():
  #creacion de la clase y metodo
  def shown(self,students = []):
    #inicio de ciclo para imprimir valores en lista
    for i in students:
      print(i["name"],i["year"],"\n")
#llamado de las clases
s = Alumnos()
list = s.get_data()
p = Send()
p.shown(list)