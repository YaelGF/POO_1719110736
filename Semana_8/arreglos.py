class Temperaturas():
  def calcular (self):
    #declaracion variables
    temperature_C = []
    temperature_F = []
    es = Txts()
    answer = "s"
    while (answer == "s"):
      #asignacion de valores
      temp_C = float(input("Ingrese temperatura en Grados Centigrados: "))
      temperature_C.append(temp_C)
      es.escribir(str(temp_C)+", ")
      temp_F = float(temp_C * 1.8 + 32)
      temperature_F.append(temp_F)
      es.escribir(str(temp_F)+", ")
      answer = input("¿Quiere seguir ingresando datos?(s/n) ")
    #declaracion y asignacion de valores
    sus = 0
    sus2 = 0
    #sacar promedio de las temperaturas ingresadas
    for i in temperature_C:
      sus = sus + i
    for j in temperature_F:
      sus2 = sus2 + j
    promedio_C = sus/len(temperature_C)
    promedio_F = sus2/len(temperature_F)
    #guardar en el TXT
    es.escribir("\n"+str(promedio_C)+", ")
    es.escribir(str(promedio_F)+", ")
    #imprimir los promedios
    print("Promedios:")
    print ("C"+"\t\t","F")
    print(promedio_C,"\t",promedio_F)
#edicion del archivo TXT
class Txts():
  def escribir (self,texto):
    file = open ("temperaturas.txt","a")
    file.write(texto)
    file.close()
#Lectura del archivo TXT
file = open ("temperaturas.txt","w")
file.write("Temperaturas: \n")
file.close()
#Llamado de la clase a usar
a = Temperaturas()
a.calcular()