#clase Catalogo
class Catalogue:

 #metodo get_information
  def get_information():

    #declaracion de lista y diccionario
    movies = []
    movie = {}

    #Ciclo para parar hasta que el usuario quiera
    answer = "s"
    while answer == "s" :

      #obtenicon de datos
      title = input("Ingrese Titulo de la pelicula: ")
      genre = input("Ingrese Genero de la pelicula: ")
      release_year = input("Ingrese El año de lanzamiento de la pelicula: ")

      #asignacion de valores al dicionario
      movie = {"title" : title, "genre" : genre, "release_year" : release_year }

      #asignacion de valor a la lista
      movies.append(movie)

      #respuesta del usuario
      answer = input("\nleer otra pelicula s/n: ")
      
    #imprimir estructura
    print("\n\t\tCatalogo Peliculas \n")
    print("\tTitulo","\tGenero","\tAño de Lanzamiento ")

    #imprimir los valores de la lista y del diccionario
    for movie in movies:
      print("\t",movie["title"], movie["genre"], movie["release_year"])

    #filtro del usuario
    index = input("\n\t¿Que genero busca? ")

    #impresion de la estructura
    print("\tTitulo","\tGenero","\tAño de Lanzamiento ")

    #imprimir las diversas peliulas del genero antes ingresado
    for movie in movies:
      if index == movie["genre"]:
        print("\t",movie["title"], movie["genre"], movie["release_year"])


#Declaracion de la clase
c = Catalogue
c.get_information()