
nombres = open('userScores.txt', 'r')

numero = 0
lista = []
socore = []
nombreUsuario="ruben"
for nombrePuntaje in nombres:
    i=0

    elemento = nombrePuntaje.split(',')
    if(elemento[i]==nombreUsuario):
        print("true")
    else:
        print("ninguna")
    i=+i

    # lista=nombrePuntaje.split(',')

print(lista)
nombres.close()

for index in lista:
    print("element", index)
    print("index:", lista[1])
