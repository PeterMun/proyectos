# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:21:25 2017

@author: 22B
"""

def rectangulo():
    x = int(input("ingrese x: "))
    y = int(input("ingrese el altura: "))
    z = int(input("ingrese el z: "))
    
    ##x, y, z
    volrec = x*y*z
    print (volrec)
    def creartxt():
        archi = open("historial.log", "w")
        archi.close()
        creartxt()
    def grabartxt():
        archi = open("historial.log", "a")
        archi.write(str(x))
        archi.write(str(y ))
        archi.write(str(z))
        archi.write(str(volrec))
        archi.close()
        grabartxt()
    
def circulo():
    r = int(input("ingrese el radio: "))
    h = int(input("ingrese el altura: "))
    
    volcir = 3.1415*(r**2)*h
    print (volcir)       
    
    def grabartxt():
        archi = open("historial.log", "a")
        archi.write(str(r))
        archi.write(str(h))
        archi.write(str(volcir))
        archi.close()
                    
                    
    
def cuadrado():
    x = int(input("ingrese x: "))
   
    volcuad = x**3
    print (volcuad)
    def grabartxt():
       archi = open("historial.log", "a")
       archi.write(str(x))
       archi.write(str(volcuad))
       
       archi.close()

    

    

    
print("BIENVENIDO A LA CALCULADORA GEOMETRICA")
figura = int(input("Ingrese el tipo de piscina: "))
print("1.- piscina rectangular")
print("2.- piscina circular")
print("3.- piscina cuadrada")

##rectangulo = 1
##circulo = 2
##cuadrado = 3


if(figura == 1):
    rectangulo()
    
   
    
if(figura == 2):
    circulo()
    
    
if(figura == 3):
    
    cuadrado()




