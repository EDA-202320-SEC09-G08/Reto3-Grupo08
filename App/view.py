﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
import matplotlib.pyplot as plt

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control,filename,mem):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data= controller.load_data(control, filename, mem)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control,mem,fecha_i,fecha_f):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    return controller.req_1(control,mem,fecha_i,fecha_f)


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control,mem,mags_min,prof_max):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    return controller.req_3(control,mem,mags_min,prof_max)


def print_req_4(control,min_sig,max_gap):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    
    respuesta= controller.req_4(control,min_sig,max_gap)

    print (tabulate(lt.iterator(respuesta)))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control,year,lat,long,radius,n_events):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    respuesta= controller.req_4(control,year,lat,long,radius,n_events)

    print(tabulate(lt.iterator(respuesta)))


def print_req_7(control,anio,titulo,propiedad_conteo,mem):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    return controller.req_7(control,anio,titulo,propiedad_conteo,mem)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass
def tabulador(lista,header):
    lista_cabeza=[]
    
    for dato in lt.iterator(lista):
        x= dict((k,dato[k])for k in (header) if k in dato)
        lista_cabeza.append(x)
    lineas=[b.values() for b in lista_cabeza]
    print(tabulate(lineas,header,tablefmt="grid"))


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            filename = str(input("Elija el tamaño de la muestra que desea: (-5pct, -10pct, -20pct, -30pct, -50pct, -80pct, -large o -small)\n"))
            mem = input("Desea observar el uso de memoria? (True/False)\n")
            data = load_data(control,filename,mem)
            print("La cantidad de datos recolectados son: "+str(lt.size(data[0]["cantidad_datos"]))+"\n")
            print(lt.size(data[0]["cantidad_datos"])-2)
            primeros= lt.subList(data[0]["cantidad_datos"],1,5)
            ultimos= lt.subList(data[0]["cantidad_datos"], int(lt.size(data[0]["cantidad_datos"]))-4,5)
            header= ("code","time", "lat","long","mag","title", "depht", "felt", "cdi","mmi","tsunami")
            print("PRIMEROS 5 REGISTROS")
            tabulador(primeros,header)
            print("--------------------")
            print("ULTIMOS REGISTROS")
            tabulador(ultimos,header)
        elif int(inputs) == 2:
            fecha_i= input("dame la fecha inicial de intervalo en formato %Y-%m-%dT%H:%M: ")
            fecha_f= input("dame la fecha inicial de intervalo en formato %Y-%m-%dT%H:%M: ")
            rpta= print_req_1(control,mem,fecha_i,fecha_f)[0]
            primeros=lt.subList(rpta,1,3)
            ultimos= lt.subList(rpta,lt.size(rpta)-2,3)

            header= ("mag","lat","long","depth","sig","gap","nst","title","time")
            print("La cantidad de datos encontrados son: "+str(lt.size(rpta)))
            print("PRIMEROS 3 REGISTROS")
            tabulador(primeros,header)
            print("--------------------")
            print("ÚLTIMOS 3 REGISTRADOS")
            tabulador(ultimos,header)


        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            mags_min= float(input("Cual es la magnitud mínima que desea consultar: "))
            prof_max= float(input("Cuál es la profundidad máxima que desea tener como rango: "))
            print("Magnitud mínima: "+str(mags_min))
            print("Profundidad máxima: "+str(prof_max))
            data = print_req_3(control, mem, mags_min,prof_max)

            print(data[0]["eventos"])
            print(lt.size(data[0]["detalles"]))
            lista_resultado= data[0]["detalles"]
            
            la_lista=lt.subList(lista_resultado,1,10)
            header= ("code","time", "lat","long","mag","title", "depht", "cdi","mmi", "sig", "gap", "nst","magType","type")
            tabulador(la_lista, header)
            

        elif int(inputs) == 5:
            min_sig= float(input(" La significancia mínima del evento a consultar:   "))
            max_gap= float(input(" La distancia azimutal máxima del evento a consultar:   "))
            print("Significancia mínima: "+str(min_sig))
            print("Distancia azimutal máxima: "+str(max_gap))
            print_req_4(control,  min_sig,max_gap)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            year= float(input(" Ingrese el año relevante a consultar (en formato “%Y”):  "))
            lat= float(input(" Ingrese la Latitud de referencia para el área de eventos a consultar:   "))
            long=float(input("Ingrese la longitud de referencia para el área de eventos a consultar: " ))
            radius=float(input("Ingrese el radio [km] del área circundante a consultar: " ))
            n_events=float(input("Ingrese el número de los N eventos de magnitud más cercana a mostrar: " ))
            print_req_6(control,year,lat,long,radius,n_events)

        elif int(inputs) == 8:
            anio= input("Cual es su año de preferencia: ")
            titulo= input("Cual título: ")
            propiedad_conteo= input("Qué propiedad de conteo se le facilita más: ")
            segmentos= int(input("Con cuántos segmentos desea dividir el plot?: "))
            data=print_req_7(control,anio,titulo,propiedad_conteo,mem)[1]
            data2= print_req_7(control,anio,titulo,propiedad_conteo,mem)[0]
            header= ("time","lat","long","title","code","mag")
            tabulador(data2,header)
            plt.hist(data,bins=segmentos,alpha=0.5)
            plt.title("Histograma de "+str(propiedad_conteo)+" en "+str(titulo))
            plt.xlabel(propiedad_conteo)
            plt.show()

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
