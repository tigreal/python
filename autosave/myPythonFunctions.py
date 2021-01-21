#este archivo es parte de los ejercicios de Math and BODMAS
#este archivo llega a ser la primera parte de los ejercicios

import random; #obtenemos randint()
import os; #obtenemos remove() rename()


#definimos nuestra primera funcion 
#esta funcion obtenddra puntos del usuario guardados en
#un archivo de texto

getUserPoint("o");



def getUserPoint(nombreUsuario):
    try:
        puntajeUsuario=open("userScore.txt",'r');
        for i in puntajeUsuario:
            
            print(i.split(','));
            
        puntajeUsuario.close();
    except IOError:
        puntajeUsuario=open("userScore.txt",'r');
        print("El archivo fue creado");
    return 0

