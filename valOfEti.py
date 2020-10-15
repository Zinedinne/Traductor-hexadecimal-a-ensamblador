# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:32:10 2018

@author: jarob
"""

def valOfEti(a, b):#primer parametro diccionario segundo parametro eti
    if b in a:
        if len(a[b]) == 1:
            return "0" + a[b] + "00"
        if len(a[b]) == 2:
            return a[b] + "00"
        if len(a[b]) == 3:
            return a[b][1]+ a[b][2]+"0"+a[b][0]
            
        if len(a[b]) == 4:
            return a[b] 
        else:
            print ("No existe esa etiqueta en el diccionario")
#Inicia simulación de la función
#El primer parámetro es el diccionario y el segundo es la etiqueta a buscar  
#El parámetro de la etiqueta se puede enviar como una variable o directamente el string 
def main():
    punto = {'x': "AB", 'y': "B", 'z': "ABB"}
    a = 'z' #valor de la etiqueta enviado con variable
    valor = valOfEti(punto, a)
    print(type(valor))
    valor2 = valOfEti(punto, 'z') #valor de la etiqueta enviado con un string
    print(valor2)

main()
