# -*- coding: utf-8 -*-

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

def restaNegConFormato(num): #funcion auxiliar nueva
    num = num * -1
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
    if len(hexatotal) == 1:
        return "0" + hexatotal
    else:
        return hexatotal
    
print(restaNegConFormato(-100))
print(bin(100))