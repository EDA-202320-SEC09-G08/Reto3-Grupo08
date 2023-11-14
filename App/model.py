"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
#import matplotlib.pyplot as plt

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs={"cantidad_datos": None,
                  "mapa": None}
    data_structs["cantidad_datos"]= lt.newList("ARRAY_LIST")
    data_structs["mapa"]= om.newMap(omaptype="BST", 
                                    cmpfunction=compararar_fechas)
    data_structs["arbol_magnitudes"]= om.newMap(omaptype="BST", 
                                    cmpfunction=comparar_mayor_menor)
    data_structs["arbol_profundidad"]=om.newMap(omaptype="BST", 
                                    cmpfunction=comparar_mayor_menor)
    
    return data_structs



# Funciones para agregar informacion al modelo

def add_data_mapa(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    lt.addLast(data_structs["cantidad_datos"],data)
    add_info( data_structs, data)
    add_arbol1(data_structs["arbol_magnitudes"],data)
    add_arbol2(data_structs["arbol_profundidad"],data)
    return data_structs

def add_info( data_structs, data):
    
    mapa= data_structs["mapa"]
    tiempo = data["time"]
    existe= om.contains(mapa, tiempo)
    if existe==True:
        entrada= om.get(mapa,tiempo)
        valor= me.getValue(entrada)
    else:
        valor=lt.newList()
        om.put(mapa,tiempo,valor)
    lt.addLast(valor,data)
    #return None
def add_arbol1( data_structs, data):
    mapa=data_structs
    tiempo = data["mag"]
    existe= om.contains(mapa, tiempo)
    if existe==True:
        entrada= om.get(mapa,tiempo)
        valor= me.getValue(entrada)
    else:
        valor=lt.newList()
        om.put(mapa,tiempo,valor)
    lt.addLast(valor,data)

def add_arbol2( data_structs, data):
    mapa=data_structs
    tiempo = data["depth"]
    existe= om.contains(mapa, tiempo)
    if existe==True:
        entrada= om.get(mapa,tiempo)
        valor= me.getValue(entrada)
    else:
        valor=lt.newList()
        om.put(mapa,tiempo,valor)
    lt.addLast(valor,data)  

    


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass



# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs,mag_min:float,prof_max:float):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    resultado = lt.newList("ARRAY_LIST")
    om_prof=data_structs["arbol_profundidad"]
    om_mags = data_structs["arbol_magnitudes"]
    om_prof=data_structs["arbol_profundidad"]
    lista2 = om.values(om_prof, 0, prof_max)
    lista = om.values(om_mags,mag_min,999999999999999999)
    
    for elem in lt.iterator(lista):
        for eleme in lt.iterator(elem):
            if float(eleme["depth"])<= prof_max:
                lt.addLast(resultado,eleme)
    quk.sort(resultado,cmp_t)
    diccionario={"eventos": lt.size(lista2)+lt.size(lista2),
                 "detalles": resultado}
    return diccionario


def req_4(data_structs,sig, gap):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    lista= lt.newList()
    mapa=data_structs["fechaIndex"]
    while lt.size(lista)< 15:
        mayor=om.maxKey(mapa)
        for x in om.get(mapa, mayor)["value"]:
            if int(x["sig"])> sig and int(x["gap"])< gap:
                lt.addLast(lista,x)
        mapa= om.deleteMax(mapa)
    if lt.size(lista)>15:
        merg.sort(lista, sort_fecha)
        lista= lt.subList(lista,1,15)
    merg.sort(lista, sort_fecha)
    return lista


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs, anio:str,titulo:str,propiedad_conteo:str,segmentos: int):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
def compararar_fechas(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
def comparar_mayor_menor(data1,data2):
    if float(data1)<float(data2):
        return -1
    elif float(data1)>float(data2):
        return 1
    else: 
        return 0
    
def sort_fecha(data1, data2):
    return data1["time"] >data2["time"]
def cmp_t(data1, data2):
    if (data1["time"]) > (data2["time"]):
        return True
    else:
        return False
