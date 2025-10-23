class estacion:
    def __init__(self, nombre, x, y, transbordos):
        self.nombre = nombre # String
        self.transbordos = transbordos #Boolean
        self.x=x #Coordenadas de la estacion
        self.y=y #en el mapa
        self.vecinos = []  #Lista con las aristas de esta estacion
        self.lastline= 'N' #Ultima linea por la que hemos llegado a la estacion, se inicializa a N