# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:34:27 2017

@author: 22B
"""

"huevos y pan"
print("huevos y pan")
'huevos y pan'
nombre = "peter"
print (nombre)
nombres = "Pedro Anibal"
apellidos = " Muñoz Burgos"
print(nombres + apellidos)
palabra = "python"
print(palabra[1])
print(palabra[2])
print(palabra[3])
print(palabra[4])
print(palabra[5])
print(palabra[0])
print(palabra[-1])
print(palabra[:2])
print(palabra[4:])
print(palabra[-2:])
print(palabra[2:4])
print(palabra[-2:4])
##print(palabra[0] = "j")
print(len (palabra))
print(palabra.find("t"))
cadena = "hola amigos"
print(cadena.replace("hola", "bye"))

cadena1 = "esta cadena tiene espacaios a los lados"
print(cadena1.strip())
frase = "yo soy peter"
a = "."
h = "-"
o = "*"
l = "i"
r = "4"
i = "5"
c = "2"
a = "9"
d = "/"

frase = "hola ricardo"
##print (frase.replace("h","_")+frase.replace("o","*")+ + + + frase.replace("c","2")+ frase.replace("a","."))
frase = frase.replace("h","_")
frase = frase.replace("o","*")
frase = frase.replace("l","i")
frase = frase.replace("r","4")
frase = frase.replace("a",".")
frase = frase.replace("i","5")
frase = frase.replace("c","2")
frase = frase.replace("d","/")
print (frase)

cadena = "codejobs"
print (cadena.upper())
print(cadena.lower())

nombres = "carlos|cristina|rodrigo|hugo"
print(nombres.split("|"))
var = nombres.split("|")
print (len(var))

caracter = "|"
nombres = [ "carlos", "cristina", "rodrigo","hugo"]
print (caracter.join(nombres))

cuadrados = [1, 2, 9, 16, 25]
print(cuadrados[0])
print(cuadrados[-1])
print(cuadrados[-3:])

sublista1 = [1, 2, 3, 4, 5]
sublista2 = [6, 7, 8, 9, 10]
sublista3 = [11, 12, 13, 14, 15]
print(cuadrados[2:])
print(cuadrados[-5:])
print(cuadrados[7:])


cubos = [1, 8, 27, 65, 125]
##print (cubos.append)

cuadrados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (cuadrados.append(216))
print(cuadrados.append(7 ** 3))
print (cuadrados)



o = [[25,36,89],[14,10,20],[12,6,89]]
p = [[10,3,5],[65,20,36],[30,20,10]]

r = [[o[0][0]+p[0][0]],
     [o[0][1]+p[0][1]],
     [o[0][2]+p[0][2]],
     [o[1][0]+p[1][0]],
     [o[1][1]+p[1][1]],
     [o[1][2]+p[1][2]],
     [o[2][0]+p[2][0]],
     [o[2][1]+p[2][1]],
     [o[2][2]+p[2][2]]]

print(r)












