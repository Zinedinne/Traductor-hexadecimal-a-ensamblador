# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:13:28 2018

@author: jarob
"""
#Estas funciones las estoy reutilizando
def complementoADos(binar):
    binary=""
  #print(hex(int(binar,2)).replace("0x","").upper())
    for i in range(len(binar)):  
        if(binar[i]=="1"):
            binary=binary+"0"
        else:
            binary=binary+"1"
    return binary
  
def valOfEti(a, b):
    if b in a:
        return str((a[b]))
    else:
        print ("No existe esa etiqueta en el diccionario")
        
def CambiarDigitos(digitos):
    decimales = [10, 11, 12, 13, 14, 15]
    hexadecimales = ["A", "B", "C", "D", "E", "F"]
    for c  in range(7):
        if digitos == decimales[c-1]:
            digitos = hexadecimales[c-1]
    return digitos

def DecimalAHexa(num):
    hexadecimal = ""
    while num != 0:
        rem = CambiarDigitos(int(num) % 16)
        hexadecimal = str(rem) + hexadecimal
        num = int(int(num)/16)
    return hexadecimal

def comADos(binar):
    co=len(binar)
    flag=0
    binary=""
  #print(hex(int(binar,2)).replace("0x","").upper()) 
    for i in range (len(binar)):
        co=co-1
        if(flag==1):
            flag=co+1
            break
        else:
          if(co!=0):  
              if(binar[co]=="1"):
                flag=1
    for i in range(flag):   
        if(binar[i]=="1"):
          binary=binary+"0"
        else:
          binary=binary+"1"
  #print(binary)
    for i in range(len(binar)-flag):
        binary=binary+binar[flag]
        flag=flag+1
    return binary

#Aquí empieza la función nueva:
    
def getDecDigit(digit): #Función auxiliar nueva
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for x in range (len(digits)):
        if digit == digits[x]:
            return x

def hexToDec(hexNum): #Funcion auxiliar nueva
    decNum = 0
    power = 0
    for digit in range (len(hexNum), 0, -1):
        decNum = decNum + 16 ** power * getDecDigit(hexNum[digit-1])
        power += 1
    return (str(decNum))
  
def restaNeg(num): #funcion auxiliar nueva
    a = (bin(num).replace("0b", ""))
    if len(a) == 1:
        arreglo = "0000000" + a
    if len(a) == 2:
        arreglo = "000000" + a
    if len(a) == 3:
        arreglo = "00000" + a
    if len(a) == 4:
        arreglo = "0000" + a
    if len(a) == 5:
        arreglo = "000" + a
    if len(a) == 6:
        arreglo = "00" + a
    if len(a) == 7:
        arreglo = "0" + a
    if len(a) == 8:
        arreglo = a
    res = comADos(arreglo)
    parte1 = res[0:4]
    parte2 = res[4:8]
    hexa1 = hex(int(parte1,2)).replace("0x","").upper()
    hexa2 = hex(int(parte2,2)).replace("0x","").upper()
    hexatotal = hexa1 + hexa2
    return hexatotal

def resEtiArr(a, b, c): #El primer parámetro es el diccionaio, el segundo es la etiqueta y el último el arreglo
    numDecDicc = hexToDec(valOfEti(a, b))
    numDecArr = hexToDec(c[0])
    valor = int(numDecDicc) - int(numDecArr)
    if valor > 0:
        valhex = DecimalAHexa(valor)
        if len(valhex) == 1:
            return "0" + valhex
        else:
            return valhex
    else:
        valor = valor * -1
        valneg = restaNeg(valor)
        if len(valneg) == 1:
            return "0" + valneg
        else:
            return valneg

        
        

def main():
   punto = {'x': "A", 'y': 1, 'z': 4}
   c = ["B","B"]
   d = "x"
   a = resEtiArr(punto, d , c)
   print(a)
main()
    
        
    