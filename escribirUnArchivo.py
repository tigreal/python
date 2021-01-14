
#cuando queremos abrir un archivo y no queremos que 
#consuma mucha memoria usamos la funcion read()
#donde espesificas el buffer zise que queremos

inputFile = open('myfile.txt','r');
outputFile = open('myoutputfile.txt','w');
msg = inputFile.read(10);
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close();
outputFile.close();


    

