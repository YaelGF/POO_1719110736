class Errors():
  def numeros(self):
  #declaracion de la clase y metodo
    list = []
    #declaracion de lista
    while (True):
    #ciclo
      try:
      #atrapar errores 
        parametro = int(input("¿Cuantós números quiere ingresar?: "))
        #asignacion de valores

        for i in range(parametro):
          numbers = int(input("Ingrese el número {n}:  ".format(n = i+1 )))
        #asignacion de valores
          if ( numbers > 0) :
            list.append(numbers)
            #asignacion de valores a la lista
          else:
            #si ingresan numeros negativos
            print("Ingrese números enteros")
            break
      except ValueError:
      #errores por el tipo de dato
        print("ingrese un valor")
      except Exception as e:
      #por si se genera otro tipo de error
        print(type(e).__name__)
      else:
        break
    answer = "s"
    while (answer == "s"):
      try: 
        index = int(input("ingrese el indice del numero al cual le quiera reaalizar las operaciones: "))
        #asignacion de valores
      except ValueError:
      #errores por el tipo de dato
          print("ingrese un valor")
      else:
      #si no se genera ningun error
        number = list[index]
        if number % 2 == 0:
          print("Es par")
        else:
          print("Es impar")
        print (number)
        #calcular si es par o impar
        square = number * number
        cube = number * number * number
        #calcular cuadrado y cubo respectivamente
        print("al cuadrado: ",square)
        print("al cubo: ", cube)
        #imprimir resultados
        answer = input("desea realizar otro cálculo?(s/n): ")
        #preguntar si quiere hacer otro calculo

ex = Errors()
ex.numeros()
#llamada de la clase y metodo