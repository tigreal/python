nombres = open('userScores.txt', 'r')

numero = 0
lista = []
socore = []
nombreUsuario="osmar"
for nombrePuntaje in nombres:
    i=0

    elemento = nombrePuntaje.split(',')
    if(elemento[i]==nombreUsuario):
        print(elemento)
    else:
        print("false:",elemento)
    i=+i

    # lista=nombrePuntaje.split(',')

print(lista)
nombres.close()


print("el segundo bucle")
index= open('userScores.txt', 'r')

for i in index:
    j=0;
    elemento = i.split(',')
    print(elemento)
    print(elemento[j+1])
    j+=j
    
nombres.close()
    
