import estacion
import arista
import math
import heapq
Perrache=estacion.estacion("Perrache", 156, 286, False)
AmpèreVictorHugo=estacion.estacion("Ampère Victor Hugo", 167, 311, False)
Bellecour=estacion.estacion("Bellecour", 184, 338, True)  # Transbordo A-D
Cordeliers=estacion.estacion("Cordeliers", 197, 375, False)
HôteldeVilleLouisPradel=estacion.estacion("Hôtel de Ville Louis Pradel", 196, 401, True)  # Transbordo A-C
Foch=estacion.estacion("Foch", 238, 409, False)
Masséna=estacion.estacion("Masséna", 275, 414, False)
CharpennesCharlesHernu=estacion.estacion("Charpennes Charles Hernu", 305, 417, True)  # Transbordo A-B
RépubliqueVilleurbanne=estacion.estacion("République Villeurbanne", 360, 419, False)
Gratte_Ciel=estacion.estacion("Gratte-Ciel", 387, 412, False)
Flachet=estacion.estacion("Flachet", 427, 401, False)
Cusset=estacion.estacion("Cusset", 468, 390, False)
LaurentBonnevayAstroballe=estacion.estacion("Laurent Bonnevay Astroballe", 508, 379, False)
Vaulx_en_VelinLaSoie=estacion.estacion("Vaulx-en-Velin La Soie", 572, 366, False)
Brotteaux=estacion.estacion("Brotteaux", 299, 399, False)
GarePartDieuVivierMerle=estacion.estacion("Gare Part-Dieu Vivier Merle", 288, 371, False)
PlaceGuichardBourseduTravail=estacion.estacion("Place Guichard Bourse du Travail", 250, 352, False)
SaxeGambetta=estacion.estacion("Saxe Gambetta", 244, 316, True)  # Transbordo B-D
JeanMacé=estacion.estacion("Jean Macé", 224, 266, False)
PlaceJeanJaurès=estacion.estacion("Place Jean Jaurès", 208, 229, False) 
Debourg=estacion.estacion("Debourg", 190, 177, False)
StadedeGerland=estacion.estacion("Stade de Gerland", 175, 146, False)
OullinsGare=estacion.estacion("Oullins Gare", 106, 83, False)
Cuire=estacion.estacion("Cuire", 182, 525, False)
Hénon=estacion.estacion("Hénon", 160, 469, False)
CroixRousse=estacion.estacion("Croix-Rousse", 178, 449, False)
CroixPaquet=estacion.estacion("Croix-Paquet", 194, 426, False)
GaredeVaise=estacion.estacion("Gare de Vaise", 60, 485, False)
Valmy=estacion.estacion("Valmy", 64, 447, False)
GorgedeLoup=estacion.estacion("Gorge de Loup", 66, 397, False)
VieuxLyonCathédraleStJean=estacion.estacion("Vieux Lyon Cathédrale St. Jean", 152, 356, False)
Guillotière=estacion.estacion("Guillotière", 227, 325, False)
Garibaldi=estacion.estacion("Garibaldi", 280, 299, False)
SansSouci=estacion.estacion("Sans-Souci", 324, 278, False)
MonplaisirLumière=estacion.estacion("Monplaisir - Lumière", 350, 263, False)
GrangeBlanche=estacion.estacion("Grange Blanche", 385, 247, False)
Laënnec=estacion.estacion("Laënnec", 409, 228, False)
MermozPinel=estacion.estacion("Mermoz Pinel", 418, 163, False)
Parilly=estacion.estacion("Parilly", 419, 114, False)
GaredeVénissieux=estacion.estacion("Gare de Vénissieux", 422, 23, False)
primeraest=True

#lista con todas las estaciones de la linea A
estacion_a = []

estacion_a.append(Perrache)
estacion_a.append(AmpèreVictorHugo)
estacion_a.append(Bellecour)  # Transbordo A-D
estacion_a.append(Cordeliers)
estacion_a.append(HôteldeVilleLouisPradel)  # Transbordo A-C
estacion_a.append(Foch)
estacion_a.append(Masséna)
estacion_a.append(CharpennesCharlesHernu)  # Transbordo A-B
estacion_a.append(RépubliqueVilleurbanne)
estacion_a.append(Gratte_Ciel)
estacion_a.append(Flachet)
estacion_a.append(Cusset)
estacion_a.append(LaurentBonnevayAstroballe)
estacion_a.append(Vaulx_en_VelinLaSoie)

#lista con todas las estaciones de la linea B
estacion_b = []

estacion_b.append(CharpennesCharlesHernu)  # Transbordo B-A
estacion_b.append(Brotteaux)
estacion_b.append(GarePartDieuVivierMerle)
estacion_b.append(PlaceGuichardBourseduTravail)
estacion_b.append(SaxeGambetta)  # Transbordo B-D
estacion_b.append(JeanMacé)
estacion_b.append(PlaceJeanJaurès)
estacion_b.append(Debourg)
estacion_b.append(StadedeGerland)
estacion_b.append(OullinsGare)

#lista con todas las estaciones de la linea C
estacion_c = []

estacion_c.append(Cuire)
estacion_c.append(Hénon)
estacion_c.append(CroixRousse)
estacion_c.append(CroixPaquet)
estacion_c.append(HôteldeVilleLouisPradel)  # Transbordo C-A

#lista con todas las estaciones de la linea D
estacion_d = []

estacion_d.append(GaredeVaise)
estacion_d.append(Valmy)
estacion_d.append(GorgedeLoup)
estacion_d.append(VieuxLyonCathédraleStJean)
estacion_d.append(Bellecour)  # Transbordo A-D
estacion_d.append(Guillotière)
estacion_d.append(SaxeGambetta)  # Transbordo B-D
estacion_d.append(Garibaldi)
estacion_d.append(SansSouci)
estacion_d.append(MonplaisirLumière)
estacion_d.append(GrangeBlanche)
estacion_d.append(Laënnec)
estacion_d.append(MermozPinel)
estacion_d.append(Parilly)
estacion_d.append(GaredeVénissieux)

#funcion que nos permite obtener el coste de cada arista entre cada estacion
def sacadistreal(estaciones, linea):
    i=0
    while i<(len(estaciones)-1):
        aristaact=arista.arista(estaciones[i],estaciones[i+1],math.sqrt(((estaciones[i].x)-(estaciones[i+1].x))**2+(estaciones[i].y-estaciones[i+1].y)**2), linea)  
        estaciones[i].vecinos.append(aristaact)
        estaciones[i+1].vecinos.append(aristaact)
        i=i+1

sacadistreal(estacion_a, 'A')
sacadistreal(estacion_b, 'B')
sacadistreal(estacion_c, 'C')
sacadistreal(estacion_d,  'D')


#funcion para sacar la distancia en linea recta(aerea) entre dos estaciones
def heuristica(origen, destino):
    return math.sqrt((origen.x-destino.x)**2+(origen.y-destino.y)**2)

#funcion que dado una estacion(extremo) y una arista de esa estacion, devuelve la otra estacion(extremo) de esa arista
def obtExtremo(extremo, arista):
    if arista.A==extremo:
        return arista.B
    else:
        return arista.A


def a_estrella(origen, destino):
    coste_acumulado = 0
    activos = [(coste_acumulado + heuristica(origen, destino), origen)] #Cola con prioridad para las estaciones
    consumidos = [] #Para comprobar que ya se ha pasado por una estacion
    camino = [] #Lista con el trayecto optimo que hay que devolver

    while activos:
        coste_acumulado, estacion_actual = heapq.heappop(activos)#saco de la cola la estacion mas prioritaria

        coste_acumulado = coste_acumulado - heuristica(estacion_actual ,destino) #Obtenemos el coste acumulado hasta esa estacion

        if estacion_actual.nombre == destino.nombre: # si estamos en el destino retornamos el camino
            #ver vecinos de la arista y mirar cual de todos los vecinos tiene un indice menor (esta mas bajo en la pila), y ese sera el siguiente nodo que pillaremos para el camino
            #miro el nodo que tengo, busco a ver si tengo otro vecino que este en la pila, si lo encuentro, comparo el indice y si es menor lo cambio, si no, no hago nada
            camino = [estacion_actual.nombre]
            indRes=1000000  #inicializamos para que sea un valor grande
            while estacion_actual!=origen:
                for aristas in estacion_actual.vecinos:
                    estVecino = obtExtremo(estacion_actual, aristas)
                    if estVecino in consumidos:
                        indAux = consumidos.index(estVecino)
                        if indAux < indRes:
                            indRes=indAux
                estacion_actual=consumidos[indRes]
                camino = [estacion_actual.nombre] + camino     #insertamos la estacion al principio del camino 4-3-2-1 -> 1-2-3-4

            return camino
        
        if estacion_actual in consumidos:
            continue

        consumidos.append(estacion_actual)



        #bucle para obtener los vecinos de la estacion actual, meterlos en cola si no estan y comprobar si
        #hay transbordo en la estacion actual o no
        for arista in estacion_actual.vecinos:
            otroExtremo=obtExtremo(estacion_actual,arista)
            otroExtremo.lastline=arista.linea
            if otroExtremo not in consumidos:
                global primeraest
                if primeraest==False:
                    if estacion_actual.lastline != arista.linea:
                        if arista.linea == "A": #lineaA
                            nuevo_coste = coste_acumulado + arista.distancia + 105 #Coste de transbordo a linea A
                        elif arista.linea == "B": #lineaB
                            nuevo_coste = coste_acumulado + arista.distancia + 145#Coste de transbordo a linea B
                        elif arista.linea == "C": #lineaC
                            nuevo_coste = coste_acumulado + arista.distancia + 91#Coste de transbordo a linea C
                        elif arista.linea == "D": #lineaD
                            nuevo_coste = coste_acumulado + arista.distancia + 96#Coste de transbordo a linea D
                        heapq.heappush(activos, (nuevo_coste + heuristica(otroExtremo, destino), otroExtremo))
                    elif estacion_actual.lastline == arista.linea:
                        nuevo_coste = coste_acumulado + arista.distancia
                        heapq.heappush(activos, (nuevo_coste + heuristica(otroExtremo, destino), otroExtremo))
                else:
                    primeraest=False
                    nuevo_coste = coste_acumulado + arista.distancia
                    heapq.heappush(activos, (nuevo_coste + heuristica(otroExtremo, destino), otroExtremo))
