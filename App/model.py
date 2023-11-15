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


def req_4(data_structs,sig, gap):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    resultado = lt.newList("ARRAY_LIST")
    om_sign=data_structs["arbol_significancia"]
    om_gaps = data_structs["arbol_distancia"]
    lista = om.values(om_sign,sig,999999999999999999)
    lista2 = om.values(om_gaps, 0, gap)
    
    
    for elem in lt.iterator(lista):
        for eleme in lt.iterator(elem):
            if float(eleme["sig"])>= sig and float(eleme["gap"])<=gap:
                lt.addLast(resultado,eleme)
    quk.sort(resultado,cmp_t)
    diccionario={"eventos": lt.size(lista2)+lt.size(lista2),
                 "detalles": resultado}
    return diccionario


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs,anio,latitud,longitud,radio,numero_n):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    anio_inio= anio+"-01-01T01:01"
    anio_inio=datetime.datetime.strptime(anio_inio, "%Y-%m-%dT%H:%M")
    anio_final= anio+"-12-31T23:59"
    anio_final=datetime.datetime.strptime(anio_final, "%Y-%m-%dT%H:%M")

    eventos_anio= om.values(data_structs["mapa"],anio_inio,anio_final)

    radio_año= lt.newList()
    radio_año_ord= om.newMap("RBT",menor_o_mayor)

    for x in lt.iterator(eventos_anio):
        for y in lt.iterator(x):
            longitud1= y["long"]
            latitud1= y["lat"]
            if radio >= distancia_tierra(longitud1, latitud1, longitud, latitud):
                lt.addLast(radio_año,y)

                fecha = y['time']
 
                if om.contains(radio_año_ord, fecha):
                    lt.addLast(om.get(radio_año_ord ,fecha)["value"], y)
        
                else:
                    lista_terremotos= lt.newList("SINGLE_LINKED")
                    om.put(radio_año_ord,fecha, lista_terremotos)
                    lt.addLast(om.get(radio_año_ord,fecha)["value"], y)
        mas_sig= None
    ev_sig= 0
  
    for x in lt.iterator(radio_año):
        if int(x["sig"])> ev_sig:
            ev_sig= int(x["sig"])
            mas_sig= x


    mayores_sig= lt.newList()
    lista1=om.values(radio_año_ord,mas_sig["time"],datetime.datetime.strptime("2024-01-01T01:01", "%Y-%m-%dT%H:%M"))
    for x in lt.iterator(lista1):
        for y in lt.iterator(x):
            lt.addLast(mayores_sig,y)
    lt.removeFirst(mayores_sig)
    if lt.size(mayores_sig)> numero_n:
        mayores_sig= lt.subList(mayores_sig,1,numero_n)



    menores_sig= lt.newList()
    lista2= om.values(radio_año_ord, datetime.datetime.strptime("2000-01-01T01:01", "%Y-%m-%dT%H:%M"), mas_sig["time"])
    
    for x in lt.iterator(lista2):
        for y in lt.iterator(x):
            lt.addLast(menores_sig, y)
    final=lt.newList()
    mapa_final= om.newMap("RBT",menor_o_mayor)

    for x in lt.iterator(menores_sig):
        lt.addLast(final,x)
    for x in lt.iterator(mayores_sig):
        lt.addLast(final,x)
    
    for x in lt.iterator(final):
        fecha = x['time']
 
        if om.contains(mapa_final, fecha):
            lt.addLast(om.get(mapa_final ,fecha)["value"], x)
        
        else:
            lista_terremotos= lt.newList("SINGLE_LINKED")
            om.put(mapa_final,fecha, lista_terremotos)
            lt.addLast(om.get(mapa_final,fecha)["value"], x)

    

    
    res=om.valueSet(mapa_final)
    res_ord= lt.newList()
    for x in lt.iterator(res):
        for y in lt.iterator(x):
            lt.addLast(res_ord, y)
    eventos_en_radio= 0
    for x in lt.iterator(om.valueSet(radio_año_ord)) :
        for y in lt.iterator(x):
            Numero_eventos_en_radio+=1



    li_res=()
    return eventos_en_radio




def distancia_tierra(longitud1, latitud1, longitud2, latitud2):
    longitud1 = math.radians(float(longitud1))
    latitud1 = math.radians(float(latitud1))
    longitud2 = math.radians(float(longitud2))
    latitud2 = math.radians(float(latitud2))

    distancia = 2 * math.asin(
        math.sqrt(
            math.sin(0.5 * (longitud2 - longitud1))**2 +
            math.cos(longitud1) * math.cos(longitud2) * math.sin(0.5 * (latitud2 - latitud1))**2
        )
    ) * 6371

    return distancia


def req_7(data_structs, anio:str,titulo:str,propiedad_conteo:str,segmentos: int):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    mapa= data_structs["arbol_magnitudes"]
    sismos=lt.newList("ARRAY_LIST")
    for fecha in lt.iterator(mapa):
        la_fecha= fecha["time"]
        el_anio= la_fecha[:4]
        zona= fecha["title"]

        if el_anio==anio:
            if titulo in zona:
                lt.addLast(sismos,fecha)
    diccionario={}
    for datos in lt.iterator(sismos):
        propiedad= datos[propiedad_conteo]
        if diccionario.get(propiedad)==None:
            diccionario[propiedad]=1
        else:
            diccionario[propiedad]+=1
    return diccionario
    


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
