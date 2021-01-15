
#este hace que leas binari files como ser fotos o algun 
#otro archivo este abre una foto y la duplica en si podria
#duplicar cualquier archivo

inputFile = open('myimage.jpg','rb');
outputFile = open('myoutputimage.jpg','wb');
msg = inputFile.read(10);
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close();
outputFile.close();


    

