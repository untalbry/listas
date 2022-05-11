#!/bin/python3
import os
import time


def list(lista):
    op = None
    while op !=3:
        os.system('clear')
        impLista(lista)
        op = int(input("1.Añadir elementro a la lista \n2.Eliminar Un elemento\n3.-Salir\n"))
        while op != 1 and op != 2 and op != 3:
            os.system('clear')
            impLista(lista)
            print("Seleciona una de las opciones correctas [1][2][3] \n")
            op = int(input("1.Añadir elementro a la lista \n2.Eliminar Un elemento\n3.-Salir\n"))
        if op == 1:
            os.system('clear')
            impLista(lista)
            obj = input("Ingrese el objeto que quiera ingresar a la lista \n")
            add(lista, obj)
        elif op == 2:
            os.system('clear')
            impLista(lista)
            obj = input("Ingrese el objeto que quiera eliminar de la lista \n")
            remove(lista,obj)
        else:
            os.system('clear')
            impLista(lista)
            print("Gracias por usar!")


def impLista(lista):
    cont = 1
    print("Lista Actual: \n")
    for a in lista:
        print("{}.-{} \n" .format(cont, a))
        cont += 1


def validar(list, obj):
    if obj.lower() in list:
        return True
    else:
        return False


def add(list, obj):
    if not validar(list, obj):
        print("El objeto ha sido añadido")
        list.append(obj.lower())
        time.sleep(1)
    else:
        print("El objeto NO se añadira a la lista")
        time.sleep(1)
    return list


def remove(list, obj):
    if validar(list, obj):
        print("El objeto ha sido eliminado")
        list.remove(obj)
        time.sleep(1)
    else:
        print("El objeto NO se encuentra en la lista")
        time.sleep(1)


def guardar(lista):
    nom=input("Como deseas guardarlo?\n")
    nom += ".txt"
    a = open(nom, "w")
    a.write("\n".join(lista))
    a.close()


def cargarArchivo(lista):
    while True:
        file = input("Ingresa el nombre del archivo:")
        try:
            with open(file, "r") as a:
                lista = a.read().split("\n")
                list(lista)
                break
        except FileNotFoundError:
            print("Archivo no encontrado!!")
            time.sleep(1)
            if input("Deseas continuar con un nuevo archivo? [S][N]\n") == "S":
                list(lista)
                break

def main():
    lista= []
    #cargar archivo
    if input("Quieres Cargar un archivo con una lista? [S][n]\n") == "S":
       cargarArchivo(lista)
    else:
        list(lista)
    #Guardar archivo
    if input("Quieres guardar el archivo? [S][n]\n")=="S":
        guardar(lista)
    else:
        print("Gracias por usar")

if __name__ == "__main__":
    main()