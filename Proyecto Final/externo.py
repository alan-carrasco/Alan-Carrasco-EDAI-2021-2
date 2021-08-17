#externo
#Proyecto final
import os
os.system("cls") #Sirve para limpiar pantalla cada que iniciemos el programa en la terminal
a=int(0) #Variable que almacena la edad de los archivos
b=float(0.0)#variable de tipo flotante para almacenar los valores del archivo del indicador
co=int(0) 	#Variable de personas que si tienen covid
acum=int(0)	#Variable de la edad de las personas positivas
datos=[]	#Lista vacía
sc=int(0)	#Variable para las personas sin covid
pila=[]		#variable de pilas con listas
cola=[]		#Variable de colas con listas
with open("copia.csv",'r') as archivo:
	lineas=archivo.read().splitlines() 
	lineas.pop(0)   #Sirve para eliminar la primera fila que tiene texto para que no afecte y tener datos del mismo tipo
	for l in lineas:  #Corre el ciclo hasta el último dato del archivo
		linea=l.split('\t') #Nos separa la liena y rempaza cada que encuentra \t para poder manejarlo como lista
		print (linea)   #Imprime el valor de la variale linea
		datos.append([[int(linea[0]),float(linea[1])]]) #Saca los datos del archivo y los transforma
		a=int(linea[0]) #Variable que almacena los datos de edad del archivo csv
		if(a<18):	#If que analiza la variable a que contiene la edad si es menor a 18 indica que es niño
			print("Niño")
			pila.append(a)
		else:
			cola.append(a)
			print("Persona mayor de edad")
		b=float(linea[1]) #Varibale que almacena el indicador de la lista convertido en float
		if(b<.8):   #Si el indicador es menor que .8 no tiene covid
			print("No tiene covid\n")
			sc=sc+a
		else:     #Si el indicador es mayor o igual a .8 tendra covid
			print("Tiene covid\n")
			co=co+1  #Varibale que lleva las cuentas de las personas con covid
			acum=acum+a  #Varable qeu almacena la edad de las personas con covid
		
		
print("Las personas con covid son: "+str(co))
if(co<0):		#Todo el if va a analizar a la variable co de covid para saber el número de personas
	print("\nEstamos en semaforo verde")
elif(co<30):
	print("\nEstamos en semaforo Amarillo")
elif(co<70):
	print("\nEstamos en semaforo Naranja")
elif(co<100):
	print("\nEstamos en semaforo Rojo")
else:
	print("Opcion no valida")	

prom=acum/co
roundnumber=round(prom,2)	#Sirve para redondear a solo dos decimales y no salgan muchos
print("\nEl promedio de las personas con covid es: \n"+str(roundnumber))#Imrpime la variable prom que es el promedio de las personas con covid

prn=100-co
proms=sc/prn
roundproms=round(proms,2)
print("\nEl promedio de las personas sin covid es: \n"+str(roundproms))
porc=100-co
print("\nEl porcentaje de las personas sin covid es el \n"+str(porc)+"%")

i=int(0) #Contador
mn=int(100)		#Variable de persona menor que asistio a las pruebas
print("\nLas edades de los niños que les hicieron las pruebas son: ")
while(i<21):   
	p=pila.pop()#Vacia el contenido de los datos dentro de la pila
	print("\n"+str(p))
	i=i+1	#incrementa a i cada que se repite el ciclo
	if(mn>p):
		mn=p

mm=int(0)	#Variable de persona mayor que asistio a las pruebas
j=int(0) #Contador
print("\nLas edades de las personas mayores que asistieron a ahcerse las pruebas son: ")
while(j<79):
	c=cola.pop(int(0)) #Vacia el contenido de los datos dentro de la cola
	print("\n"+str(c))
	j=j+1	#incrementa a j cada que se repite el ciclo
	if(mm<c):
		mm=c

print("La persona de menor edad que acudió a la prueba fue de :"+str(mn))
print("La persona de mayor edad que acudió a la prueba fue de :"+str(mm))
