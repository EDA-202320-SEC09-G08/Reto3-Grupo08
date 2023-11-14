"""
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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


from controller import new_controller, load_data

def main():
    """
    Punto de entrada principal para cargar datos y mostrar información
    """
    control = new_controller()
    filename = 'datos_temblores-large.csv'  # Nombre del archivo a cargar
    data_loaded = load_data(control, filename)
    if data_loaded > 0:
        print("Datos cargados exitosamente.")
        # Aquí puedes agregar la lógica para mostrar o trabajar con los datos cargados
        print_first_and_last_events(control)
    else:
        print("No se cargaron datos o hubo un error en la carga.")

def print_first_and_last_events(control):
    """
    Imprime los primeros y últimos eventos cargados
    """
    print("Primeros 5 eventos:")
    print("------------------------------------------------------------------------------------")
    print_header()
    for event in control['events'][:5]:
        print_data(event)
    print("...")  # Se omite la impresión de los datos intermedios
    print("Últimos 5 eventos:")
    print("------------------------------------------------------------------------------------")
    print_header()
    for event in control['events'][-5:]:
        print_data(event)

def print_header():
    """
    Imprime los encabezados de los datos
    """
    headers = ['time', 'lat', 'long', 'depth', 'mag', 'sig', 'nst', 'gap', 'title', 'felt', 'cdi', 'mmi', 'tsunami']
    print(tabulate([headers], tablefmt="pretty"))

def print_data(event):
    """
    Imprime los detalles de un evento sísmico
    """
  
    event_values = [
        event['time'],
        round(event['lat'], 3),
        round(event['long'], 3),
        round(event['depth'], 3),
        round(event['mag'], 3),
        event['sig'],
        event['nst'],
        event['gap'],
        event['title'],
        event['felt'],
        event['cdi'],
        event['mmi'],
        event['tsunami']
    ]
    print(tabulate([event_values], tablefmt="pretty"))


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


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
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
