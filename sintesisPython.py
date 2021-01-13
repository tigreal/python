# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
entero=123;
message = "hola mundo"
print(entero);

decimalFlotante=1.23;
print("decimal de puto flotante: ",decimalFlotante);


print("como concatenar cadenas \n");
print("osmar "+"Alvarez "+"Paredes".upper());

brand = 'Apple';
exchangerRate=1.235235245;
message = 'The price of this %s Laptop is %d USD \
    and the \
 exchage rates is %4.2f USD to 1 EUR' %(brand,1299,exchangerRate)
print(message);

#el el marcador %d que se utiliza para enteros se puede colocar 
#un numero entre %5d quiere decir que se mosmtrara 5 caracteres 
#ejemplo si es 123, se antepondra 2 espacios mas los
#tres nuemors "  123" este sera el resultado.
#% 4.2f donde 4 se refiere a la longitud total y 2 se 
#refiere a 2 lugares decimales. Si queremos agregar
#si el numero es 1.3 agregara un espacio al principio para que en total sean 4

#utilizando el parametro .format

message = 'The price of this {0:s} Laptop is {1:d} USD \
    and the \
 exchage rates is {2:4.2f} USD to 1 EUR'.format(brand,1299,exchangerRate);
print(message);

#si no queremos dar formato a la cadena se puede anortar asi
#usando metodo .format 
message = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
print(message);

# casting o conversores 
#int(), float(), str(),

#lista de datos y se puede declarar vacia pero 
# tienen que agragar items con el metodo append()

ListaDeAnos=[21,22,23,24,25];
ListaDeAnosVacia=[];
print("este es el primer item",ListaDeAnos[0]);

print("este es el ultimo item",ListaDeAnos[-1]);

ListaDeAnosNueva = ListaDeAnos;
print("se paso la listaDeAnos a la ListaDeAnosNueva",ListaDeAnosNueva);

ListaDeAnosOtra=ListaDeAnos[2:4];
print("se esta cortando la cadena\
       donde estamos pasando \
 el elemento 3ro ya que empieza con el index 0\
 y el elemento 4 la segunda variable desdepues de los\
   : empieza de 1   [2:4]= 23,24\n\n",ListaDeAnosOtra);
   
#agragar elementos con el metodo append()
listaItems=[];
print(listaItems);
listaItems.append(44);
listaItems.append(66);
print(listaItems);

#borrar elementos de la lista con metodo .del
ListaParaBorrar = [1,2,3,4];
print("lista para borrar completa:\n",ListaParaBorrar);
del ListaParaBorrar[2];
print("se borro el index 2 que seria el tercer elemento:\n",ListaParaBorrar);
# Ejemplo de asigancion o slide lista o cortar 
#la lista o dividir la lista

miLista=[1,2,3,4,5,"Hola mundo"];
print("Mi lista completa:\n",miLista);
print("el elemento de indice 3",miLista[4]);
print("el ultimo elemento",miLista[-1]);
print("aqui vamos hacer un slice/corte de lista");
miListaSlice=miLista[2:5];
print("los elementos a mostrar deberian ser el 2 y 5 \n");
print(miListaSlice);
miLista[1]=20;
print("se modifico el elemento 2 que seria ahora:\n",miLista);
miLista.append("how are you");
print("se agrego un ultimo elemento como estas en igles\n");
print(miLista);
del miLista[5];
print("se elimino el index 5",miLista);
    
#tuple o tuplas son como las listas pero su valor
#no se puede cambiar

monthsOfYear = ("enero","febrero","marzo","abril\
","mayo","junio","julio","agosto","septiembre\
","octubre","nobiembre","diciembre");
print("para acceder a los elementos se utiliza los\
      index como en las listas");
print(monthsOfYear[0]);
print(monthsOfYear[-1]);

#Dictionaty o diccionarios en ingles
#tiene una palabra key que tiene que ser unica
#y un valor
miDiccionario = {"Osmar:25","Jorge:26","Samadi:25\
"};
print("imprimiendo el diccionario\n",miDiccionario);
#tambien se puede crear haciendo el uso del metodo 
#dict()

miDiccionario2=dict(Osmar = 38,Jorge = 51,Samadi=15);
print("el diccionario creado con el metodo dict\n");
print(miDiccionario2);
print("para obtener el valor de un item del diccionario\
tienes que colocar el key y te devuelve el valor que\
que esta enlasado a ese key");
print("\n el valor de Osmar seria:", miDiccionario2["Osmar"]);
#modificar un dato del diccionario se tiene
#que espesificar el su valor kay y realizar el cambio 
miDiccionario2["Osmar"]=15;
print("el nuevo valor:\n", miDiccionario2["Osmar"]);

miDiccionarioVacio={};
miDiccionarioVacio["Pepe"]=10;
miDiccionarioVacio["Lorenzo"]=30;
miDiccionarioVacio["David"]=40;
print("el diccionario ahora tiene estos \
      datos\n",miDiccionarioVacio);

del miDiccionarioVacio["David"];
print("se borro a david de \
los elemnetos del diccionario \n",miDiccionarioVacio);
#el diccionario puede tener varios tipos de datos
miDiccionarioVariado={"one":1.35,2.5:"two point five\
                      ",3:"+",7.9:2};
print("imprimimos nuestro diccionario variado con\
      multiples valores de todo tipo\n",miDiccionarioVariado);
#aumentaremos un nuevo item
miDiccionarioVariado["nuevo item"]="soy un nuevo item";
print("un nuevo valor agreagado\n",miDiccionarioVariado);
#removiendo un item del diccionario 
del miDiccionarioVariado["one"];
print("se borro del diccionario\
      el item: one\n",miDiccionarioVariado);      
                      




