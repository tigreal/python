# este archivo es parte de los ejercicios de Math and BODMAS
# este archivo llega a ser la primera parte de los ejercicios

import random  # obtenemos randint()
import os  # obtenemos remove() rename()


# definimos nuestra primera funcion
# esta funcion obtenddra puntos del usuario guardados en
# un archivo de texto
nombreUsuario = "nada"

nombreUsuario = input("Introdusca el nombre:")
res = isinstance(nombreUsuario, str) 
if(nombreUsuario.len() != 0 and res is True):
    
    try:

        score = open("userScores.txt", "r")
        
            

    except IOError():
        print("el archivo no se encuentra se procedera a crearlo")
        score = open("userScores.txt", "w")
else:
    print("introdusca un nombre")

def obtenerUsuarioPuntos(nombreUsuario):
    score=open("userScores.txt","r")
    for nombre in score:
        print(nombre.split(','))
        
    return 0
