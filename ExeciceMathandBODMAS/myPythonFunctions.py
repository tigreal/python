# este archivo es parte de los ejercicios de Math and BODMAS
# este archivo llega a ser la primera parte de los ejercicios

import random  # obtenemos randint()
import os  # obtenemos remove() rename()

#definiendo las dos listas
operandList=[0,0,0,0,0] 
operatorList=['','','','','']
operatorDict={1:'+',2:'-',3:'*',4:'**'}
print(operatorDict)
for index in  range(0,5):
    operandList[index]=random.randint(1,9)
    #print(operandList[index])
    

bandera=1    
for index in range(0,5):
    
    
    if operatorList[index]!='**':
        operatorList[index]=operatorDict[random.randint(1,4)]
        print("distinto",operatorList[index])
        
    elif operatorList[index]=='**' and bandera<2:
            operatorList[index]=operatorDict[random.randint(1,4)]
            bandera=bandera+1
            print("igual",operatorList[index])
            print("bandera",bandera)
            
    else:
        operatorList[index]=operatorDict[1]
        print("else",operatorList[index])
        
        

        
            
        
    
        
    
        
    
    
       
    
    



def obtenerUsuarioPuntos(nombreUsuario):
    
    nombres = open('userScores.txt', 'r')
#nombreUsuario="osmar"
    for nombrePuntaje in nombres:
        i=0

        elemento = nombrePuntaje.split(',')
        if(elemento[i]==nombreUsuario):
            print("El puntaje para el usuario:",elemento[i])
            print("\n es:",elemento[i+1])
            return 1
        
           
    #i=+i
    nombres.close()

def actulizarPuntosUsuario(usuarioNuevo,nombreUsuario,puntaje):
    #la funcion agregar funciona de maravilla
    #pytho mi nuevo amigo 
        if(usuarioNuevo==True):
            agregarUsuario=open('userScores.txt', 'a')
            agregarUsuario.write("\n"+nombreUsuario+","+puntaje)
            agregarUsuario.close()
        else:
            scores=open("userScores.txt",'r')
            scoresTemp=open('userScoresTemp.txt','w')
            e=0
            
    
                
            for registro in scores:
                
                res=registro.split(',')
                                
                if res[0]==nombreUsuario:
                        #print("es true",res[e])
                        scoresTemp.write(nombreUsuario+","+puntaje+"\n")
                        
                else:
                        
                  
                        scoresTemp.write(registro)
                        
                e=e+1
                print("el incremento de i",e)
                 
            
            scores.close()
            scoresTemp.close()
            os.remove('userScores.txt')
            os.rename('userScoresTemp.txt','userScores.txt')
                               
                
    


# definimos nuestra primera funcion
# esta funcion obtenddra puntos del usuario guardados en
# un archivo de texto


actulizarPuntosUsuario(False,"osmar","200")



"""
nombreUsuario = input("Introdusca el nombre:")
res = isinstance(nombreUsuario, str) 

    
try:

        score = open("userScores.txt", "r")
        score.close()
        res=obtenerUsuarioPuntos(nombreUsuario)
        if(res!=1):
            print("El nombre no existe\n")
            
        
             

except IOError:
        print("el archivo no se encuentra se procedera a crearlo")
        score = open("userScores.txt", "w")"""




    # lista=nombrePuntaje.split(',')

#print(lista)
#nombres.close()
