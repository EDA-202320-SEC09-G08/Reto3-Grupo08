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
from matplotlib import pyplot as plt
import math
import datetime

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
    data_structs["arbol_significancia"]=om.newMap(omaptype="BST", 
                                    cmpfunction=comparar_mayor_menor)
    data_structs["arbol_distancia"]=om.newMap(omaptype="BST", 
                                    cmpfunction=comparar_mayor_menor)
    data_structs["requerimiento_7"]= mp.newMap(20,maptype="PROBING",
                                               loadfactor= 0.5)
    
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
    add_arbol3(data_structs["arbol_significancia"],data)
    add_arbol4(data_structs["arbol_distancia"],data)
    add_mapa(data_structs,data)
    return data_structs

def add_mapa(data_structs, data):
    datastructs=data_structs["requerimiento_7"]
    titulo= data["title"]
    contiene= mp.contains(datastructs,titulo)
    if contiene:
        title= me.getValue(mp.get(datastructs,titulo))
    else:
        title= lt.newList("ARRAY_LIST")
        mp.put(datastructs,titulo,title)
    lt.addLast(title,data)
    
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

def add_arbol3( data_structs, data):
    mapa=data_structs
    tiempo = data["sig"]
    existe= om.contains(mapa, tiempo)
    if existe==True:
        entrada= om.get(mapa,tiempo)
        valor= me.getValue(entrada)
    else:
        valor=lt.newList()
        om.put(mapa,tiempo,valor)
    lt.addLast(valor,data)  

def add_arbol4( data_structs, data):
    mapa=data_structs
    tiempo = data["gap"]
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


def req_4(data_structs,min_sig,max_gap):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4

    tree_by_sig = data_structs["albol_significancia"]

    max_sig = om.maxKey(tree_by_sig)

    keys = om.keys(tree_by_sig,min_sig,max_sig)

    lista_filtrados = lt.newList("ARRAY_LIST")

    for sig in lt.iterator(keys):

        list_value_sig = me.getValue(om.get(tree_by_sig,sig))

        for terremoto in lt.iterator(list_value_sig):

            if terremoto["gap"] <= max_gap:

                lt.addLast(lista_filtrados,terremoto)


    ordenamiento_por_fechas = merg.sort(lista_filtrados,cmp_by_time)

    if lt.size(ordenamiento_por_fechas) > 15:

        lista_return = lt.subList(ordenamiento_por_fechas,1,15)

    else:

        lista_return = ordenamiento_por_fechas


    return lista_return


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs,year,lat,long,radius,n_events):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    map_by_years = data_structs["map_by_years"]

    entry_map_year = mp.get(map_by_years,year)

    lista_filtrados = lt.newList("ARRAY_LIST")

    if entry_map_year:

        value_tree_year = me.getValue(entry_map_year)

        min_key_tree = om.minKey(value_tree_year)

        min_key_tree = om.maxKey(value_tree_year)

        list_values_tree = om.values(value_tree_year,min_key_tree,min_key_tree)

        for terremoto in lt.iterator(list_values_tree):

            haversine_function = haversine(lat,long,terremoto["lat"],terremoto["long"])

            if haversine_function <= radius:

                terremoto["distance"] = haversine_function

                lt.addLast(lista_filtrados,terremoto)

    order_by_sig = merg.sort(lista_filtrados,cmp_by_sig)

    max_sig_element = lt.getElement(order_by_sig,1)


    date_x = datetime.strptime(max_sig_element["time"], "%Y-%m-%dT%H:%M")

    near_events = lt.newList("ARRAY_LIST")
    for event in lt.iterator(order_by_sig):
        date_event = datetime.strptime(event["time"], "%Y-%m-%dT%H:%M")
        time_diference = abs(date_event - date_x)
        event["diference"] = time_diference
        lt.addLast(near_events,event)


    sorted_by_time_diference = merg.sort(near_events,cmp_by_time_diferrence)

    if lt.size(sorted_by_time_diference) > n_events:

        return_list = lt.subList(sorted_by_time_diference,1,n_events+2)

    else:

        return_list = sorted_by_time_diference

    return return_list


def req_7(data_structs, anio:str,titulo:str,propiedad_conteo:str):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    lista= data_structs["cantidad_datos"]
    sismos=lt.newList("ARRAY_LIST")
    for fecha in lt.iterator(lista):
        la_fecha= fecha["time"]
        el_anio= la_fecha[:4]
        zona= fecha["title"]

        if el_anio==anio:
            if titulo in zona:
                lt.addLast(sismos,fecha)
    lista= []
    for datos in lt.iterator(sismos):
        propiedad= datos[propiedad_conteo]
        lista.append(propiedad)
    return sismos,lista
    


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
def menor_o_mayor(mag1, mag2):
    
    if (mag1 == mag2):
        return 0
    elif (mag1 > mag2):
        return 1
    else:
        return -1
    
def sort_fecha(data1, data2):
    return data1["time"] >data2["time"]

def add_data_tree_by_sig_2(data_structs,terremoto):

    arbol_by_sig = data_structs["tree_by_sig"]

    sig = terremoto["sig"]

    entry_tree = om.get(arbol_by_sig,sig)

    if entry_tree:

        value_list_sig = me.getValue(entry_tree)

        lt.addLast(value_list_sig,terremoto)

    else:

        new_value_list_sig = lt.newList("ARRAY_LIST")

        lt.addLast(new_value_list_sig,terremoto)

        om.put(arbol_by_sig,sig,new_value_list_sig)


    return data_structs

def cmp_by_time (data_1,data_2):
    
    if data_1["time"]>data_2["time"]:
        return True
    else:
        return False
    
def compare_dates(data_1,data_2):
    if data_1==data_2:
        return 0
    elif data_1>data_2:
        return 1
    else:
        return -1
    
def add_data_map_by_years_2(data_structs,terremoto):

    map_by_years = data_structs["map_by_years"]

    year = terremoto["time"][0:4]

    entry_map_years = mp.get(map_by_years,year)

    if entry_map_years:

        value_tree_year = me.getValue(entry_map_years)

        om.put(value_tree_year,terremoto)

    else:

        new_value_tree_year = om.newMap(omaptype="RBT",cmpfunction=compare_dates)

        om.put(new_value_tree_year,terremoto)

        mp.put(map_by_years,year,new_value_tree_year)

    return data_structs

def haversine(lat1, lon1, lat2, lon2):

    R = 6371.0

    # Convertir las latitudes y longitudes de grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Diferencias de latitud y longitud
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Fórmula de Haversine
    #a = math.sin(dlat / 2)2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distancia en kilómetros
    distance = R * c

    return distance

def cmp_by_time_diferrence(data_1,data_2):

    if data_1["diference"] < data_2["diference"]:
        return True
    else:
        return False