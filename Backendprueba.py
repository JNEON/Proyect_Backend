palabras = [] 
cuenta = ''
dato={}
texto = input("\n" + 'ingrese texto : ')
cadena = ''.join([i for i in texto if not i.isdigit()]) #elimina numeros de la cadena
#cadena = '6 barco casa barco perro  lote lote'
lista = cadena.split()
for i in lista:
    if i in dato:
        dato[i] +=1
    else:
        dato[i] =1
    cuenta=len(dato)
datos = dato.values()
datos = list(datos)
data="".join(map(str, datos))

##print(cadena +"\n") cadena ingresada por el usuario
##print(str(lista) + "\n"+ "\n") cadena en lista
print("\n" + str(cuenta) + "\n")
print(data + "\n")
#print(str(dato) + "\n") diccionario con la informacion de las palabras
#print(str(datos) + "\n") diccionario  pasa a lista
##print(str(palabras) + "\n") total palabras en lista
