#Practica 3: Leer y escribir en archivos .txt

#escribir
#f = open('myFile1.txt','w')
#f.write("hello")
with open('myFile1.txt', 'w') as myFile:
	print("Hello! jeje",file=myFile)


#leer
#f = open('myFile1.txt','r') 
#f.read()
with open('myFile1.txt', 'r') as myfile:
	data = myfile.read()
	print(data)