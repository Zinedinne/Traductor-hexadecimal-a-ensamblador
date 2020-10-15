'''
Created on 18/11/2018

@author: Ríos Reynoso Mauricio Ismael
@author: Gutíerrez Aburto Julio Rafael
@author: Bautista Jaime
@author: Guzmán Miguel Zinedinne
'''

import openpyxl
import re
from buscarCLTODAS import buscarCLTODAS
from buscarCOTODAS import buscarCOTODAS
from manejoEtis import manejoEtis
from ArrofArr import arrOfArrToText
from valOfEti import valOfEti
from DectoHexa import CambiarDigitos
from restaEtiArr import resEtiArr
from DectoHexa import DecimalAHexa
from SumaHexa import sumaHexa
from FormatoHexaSinCambiar import formatoHexaSinCambiar
from resta import resta
import checksum
from dochex import dochex
from juntarCO import juntarCO

doc=openpyxl.load_workbook('instrucciones.xlsx')
asm=open("ej.asm","r")

CL="0000"
tS={} #Tabla de símbolos

#Todo lo que se hace en CL es en hexa
arreglo=["0","0","0"]

lineas=asm.readlines()

#Inicializa la matriz
matriz=[]
for i in range(len(lineas)):
    matriz.append([])
    for j in range(3):
        matriz[i].append("0")
        

cont=0
for i in lineas:
    lineas[cont]=i.replace("\n","")
    cont=cont+1
    
trans="0000" #Es para pruebas
print(lineas)
cont=0

if lineas[0]=="LD A,A":
    print("Son iguales")

for p in range(1,3): 

    i=0
    
    for cont in range(len(lineas)):
        
        print("La linea que esta leyendo",lineas[cont])
        c=0

        if re.match("eti[0-9]{1,3}:", lineas[cont]):
            print("Es igual a una etiqueta")
            if (p==1):
                lineas[cont],eti,dDot,tS=manejoEtis(p,lineas[cont],tS,CL)
                print(tS)
                print(lineas[cont])
                
                
            if (p==2):
                lineas[cont]=manejoEtis(p,lineas[cont],tS,CL)


        if  re.search("LD .*", lineas[cont]):
            c=1
            print("La pasada en la que esta ",p)


            if re.search("(LD \(?[A-Z]{1,2}\)?, \(?[A-Z]{1,2}\)?)$", lineas[cont]):# Y no hay un +
                print("Es igual a Registro,registro")#Esta clasificación se busca asi normal en la lista sin modificar
                if (p==1):
                    print("Entra pasada 1")
                    g=buscarCLTODAS(lineas[cont])
                    g=str(g)
                    print(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL,g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
    
                if (p==2):
                    print("Entra pasada 2")
                    h=buscarCOTODAS(lineas[cont])
                    j=matriz[i]
                    l=h
                    j[1]=l 
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])


            if re.search("(LD \(?[A-Z]{1,2}\)?, [0-9]{0,19})$", lineas[cont]):
                print("Es igual a Registro,numero")
                print(lineas[cont])
                if (p==1):
                    temp=lineas[cont].split(",")
                    b=lineas[cont].replace(temp[1]," n")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
    
                if (p==2):
                    print("Entra pasada 2")
                    temp=lineas[cont].split(",")
                    b=lineas[cont].replace(temp[1]," n")
                    m=re.search("[0-9]{1,5}",lineas[cont])
                    h=buscarCOTODAS(b)
                    j=matriz[i]
                    trans=DecimalAHexa(m[0])
                    l=h+trans
                    j[1]=l 
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])
    
    
            if re.search("(LD \(?[A-Z]{1,2}\)?, #.*)$", lineas[cont]):
                print("Es igual a Registro,EQU")
                if (p==1):
                   
                    temp=lineas[cont].split(",")
                    b=lineas[cont].replace(temp[1]," n")
                    print(b)
    
                    print("Entra pasada 1")
                    
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL,g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:5])
                    
    
                if (p==2):
                    print(tS)
                    print("Entra pasada 2")
                    temp=lineas[cont].split(",")
                    b=lineas[cont].replace(temp[1]," n")
                    m=re.search("#.*",lineas[cont])
                    h=str(buscarCOTODAS(b))
                    j=matriz[i]
                    res=tS[m[0]]
                    l=h+res
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:5])
    
    
            if re.search("LD \(?[A-Z]{1,2}\)?, \(?[A-Z]{1,3}(\+)[0-9]{1,9}\)?", lineas[cont]):
                print("Es igual a Registro,numero+")
                if (p==1):
                    temp=lineas[cont].split("+")
                    b=lineas[cont].replace(temp[1],"d)")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL,g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:5])
                    
    
                if (p==2):
                    print("Entra pasada 2")
                    temp=lineas[cont].split("+")
                    b=lineas[cont].replace(temp[1],"d)")
                    m=re.search("[0-9]{1,5}",lineas[cont])
                    h=str(buscarCOTODAS(b))
                    trans=DecimalAHexa(m[0])
                    j=matriz[i]
                    l=h+trans
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:5])
    
    
            if re.search("LD \([A-Z]{1,2}(\+)[0-9]{1,9}\), \(?[A-Z]{1,2}\)?", lineas[cont]):
                print("Es igual a numero+,Regsitro")
                if (p==1):
                    
                    temp=lineas[cont].split("+")
                    temp2=temp[1].split(",")
                    b=lineas[cont].replace(temp2[0],"d)")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL,g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:5])
                    
    
                if (p==2):
                    print("Entra pasada 2")
                    temp=lineas[cont].split("+")
                    temp2=temp[1].split(",")
                    b=lineas[cont].replace(temp2[0],"d)")
                    print(b)
                    m=re.search("[0-9]{1,5}",lineas[cont])
                    h=str(buscarCOTODAS(b))
                    trans=DecimalAHexa(m[0])
                    j=matriz[i]
                    l=h+trans
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:5])
 
    
            if re.search("LD \([A-Z]{1,2}(\+)[0-9]{1,9}\), [0-9]{1,19}", lineas[cont]):
                print("Es igual a numero+,numero")
    
                if (p==1):
                    m=re.sub("\+[0-9]{1,3}","+d", lineas[cont])
                    n=re.sub("[0-9]{1,3}","n", m)
                    print("Entra pasada 1")
                    g=buscarCLTODAS(n)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL,g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:20])
                   
    
                if (p==2):
                    print("Entra pasada 2")
                    b=re.search("[0-9]{1,3}", lineas[cont])
                    m=re.sub("\+[0-9]{1,3}","+d", lineas[cont])
                    n=re.sub("[0-9]{1,3}","n", m)
                    c=re.search("[0-9]{1,3}", m)
                    b=DecimalAHexa(b[0])
                    c=DecimalAHexa(c[0])
                    h=str(buscarCOTODAS(n))
                    j=matriz[i]
                    l=h+b+c
                    j[1]=l 
                    matriz[i]=j
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:20])
    
    
            if re.search("LD \([A-Z]{1,2}(\+)[0-9]{1,9}\), #.*", lineas[cont]):
                print("Es igual a numero+,EQU")
                if (p==1):
                    m=re.sub("\+[0-9]{1,3}","+d", lineas[cont])
                    n=re.sub("#.*","n", m)
                    
                    print("Entra pasada 1")
                    g=buscarCLTODAS(n)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL,g)
                    i=i+1
                    print("CL ", CL)
                    
    
                if (p==2):
                    print("Entra pasada 2")
                    m=re.sub("\+[0-9]{1,3}","+d", lineas[cont])
                    n=re.sub("#.*","n", m)
                    b=re.search("[0-9]{1,3}", lineas[cont])
                    c=re.search("#.*", m)
                    c=tS[c[0]]
                    b=DecimalAHexa(b[0])
                    h=str(buscarCOTODAS(n))
                    j=matriz[i]
                    l=h+b+c
                    j[1]=l 
                    matriz[i]=j
                    i=i+1
    
    
            if re.search("LD \(?[A-Z]{1,2}\)?, \(?[0-9]{1,30}h\)?", lineas[cont]):#Si es nn debe tener una h
                print("Es igual a Registro,numero (nn)")
                if (p==1):
                    print("Entra pasada 1")
                    
                    m=re.sub("[0-9]{1,5}h","nn", lineas[cont])
                    g=buscarCLTODAS(m)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    
                    CL=sumaHexa(CL,g)
    
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:6])
                    
    
                if (p==2):
                    print("Entra pasada 2")
                    m=re.sub("[0-9]{1,5}h","nn", lineas[cont])
                    print(m)
                    b=re.search("[0-9]{1,5}h",lineas[cont])
                    b=DecimalAHexa(b[0])
                    h=str(buscarCOTODAS(m))
                    j=matriz[i]
                    l=h+b
                    j[1]=l 
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:6])


    
    
            if re.search("LD \(?[A-Z]{1,2}\)?, \(?eti.*\)?", lineas[cont]):#Si es nn debe tener una h
                print("Es igual a Registro,etiqueta (eti)")#Escribir xx en la parte del numero para leer la nstruccion
                
                if (p==1):
                    temp=lineas[cont].split(",")
                    if temp[1].find("(")!=-1:
                        b=lineas[cont].replace(temp[1]," (nn)")
                    else:
                        b=lineas[cont].replace(temp[1]," nn")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
    
                if (p==2):
                    print("Entra pasada 2")
                    temp=lineas[cont].split(",")
                    if temp[1].find("(")!=-1:
                        b=lineas[cont].replace(temp[1]," (nn)")
                    else:
                        b=lineas[cont].replace(temp[1]," nn")

                    m=re.search("eti[0-9]{1,5}",lineas[cont])
                    m=valOfEti(tS,m[0])
                    h=buscarCOTODAS(b)
                    j=matriz[i]
                    l=h+m
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])
    
    

            if re.search("LD \([0-9]{0,30}h\), [A-Z]{1,2}", lineas[cont]):
                print("Es igual a numero nn,Registro")#Escribir xx en la parte del numero para leer la nstruccion
                if (p==1):
                    print("Entra pasada 1")
                    m=re.sub("[0-9]{1,5}h","nn", lineas[cont])
                    print(m)
                    g=buscarCLTODAS(m)
                    g=str(g)
    
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    
                    CL=sumaHexa(CL,g)
    
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:6])
    
                if (p==2):
                    print("Entra pasada 2")
                    m=re.sub("[0-9]{1,5}h","nn", lineas[cont])
                    b=re.search("[0-9]{1,5}h",lineas[cont])
                    b=DecimalAHexa(b[0])
                    h=str(buscarCOTODAS(m))
                    j=matriz[i]
                    l=h+b
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:6])
    
    
            if re.search("LD \(?eti.*\)?, [A-Z]{1,2}", lineas[cont]):
                print("Es igual a etiqueta,Registro")#Escribir xx en la parte del numero para leer la nstruccion
                if (p==1):
                    temp=lineas[cont].split(",")
                    if temp[0].find("("):
                        b=lineas[cont].replace(temp[0],"LD (nn)")
                    else:
                        b=lineas[cont].replace(temp[0],"LD nn")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
    
                if (p==2):
                    print("Entra pasada 2")
                    temp=lineas[cont].split(",")
                    if temp[0].find("("):
                        b=lineas[cont].replace(temp[0],"LD (nn)")
                    else:
                        b=lineas[cont].replace(temp[0],"LD nn")
                    m=re.search("eti[0-9]{1,5}",lineas[cont])
                    m=valOfEti(tS,m[0])
                    h=buscarCOTODAS(b)
                    j=matriz[i]
                    l=h+m
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])


                #Continuando con otras tablas
                #Los de LD van a estar dentro de un if que vea que son LD\s
                #Poner un contador que diga si ya entro a los LD 

                #if re.search("([A-Z]{1,4})$" ,a):
                #print("Es igual a AAAA")


                #Poner un if para los JP y JR


        #############################
        #############################
        #############################
        #############################
        #############################
                
        if re.search("(JP|JR|CALL) .*", lineas[cont]) and c==0:
            c=1

            if re.search("JP (\([A-Z]{1,5}\))$" ,lineas[cont]):
                print("Es igual a JP de solo codigo")
                if (p==1):
                    print("Entra pasada 1")
                    g=buscarCLTODAS(lineas[cont])
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
                    
                if (p==2):
                    print("Entra pasada 2")
                    h=buscarCOTODAS(lineas[cont])
                    j=matriz[i]
                    j[1]=h
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])
    
    
            if re.search("JP .*([0-9]{1,5})h" ,lineas[cont]):
    
    
                print("Es igual a JP numero")   
                if (p==1):
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
    
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
                    
    
                if (p==2):
                    print("Entra pasada 2")
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                    print(b)
                    m=re.search("[0-9]{1,5}h",lineas[cont])
                    h=buscarCOTODAS(b)
                    j=matriz[i]
                    trans=DecimalAHexa(m[0])
                    l=h+trans
                    j[1]=l 
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])
    
    
            if re.search("JP .*\(?eti.*\)?" ,lineas[cont]):
                print("Es igual a JP etiqueta") #Los numeros siempre son nn   
                if (p==1):
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
                    
                if (p==2):
                    print("Entra pasada 2")
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                    r=re.search("eti[0-9]{1,5}",lineas[cont])
                    print(tS)
                    m=valOfEti(tS,r[0])
                    print(temp[1])
                    h=buscarCOTODAS(b)
                    j=matriz[i]
                    l=h+m
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])
    
    
            if re.search("(CALL .*([0-9]{1,5})h)$" ,lineas[cont]):
                print("Es igual a CALL numero") #Los numeros siempre son nn   
                if (p==1):
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")            
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])

                    
                if (p==2):
                    print("Entra pasada 2")
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                    m=re.search("[0-9]{1,5}h",lineas[cont])
                    h=buscarCOTODAS(b)
                    j=matriz[i]
                    trans=DecimalAHexa(m[0])
                    l=h+trans
                    j[1]=l 
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])
    
    
            if re.search("CALL .*(\(?eti.*\)?)$" ,lineas[cont]):
                print("Es igual a CALL etiqueta") #Los numeros siempre son nn   
                if (p==1):
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
                    
    
                if (p==2):
                    print("Entra pasada 2")
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                    r=re.search("eti[0-9]{1,5}",lineas[cont])
                    m=valOfEti(tS,r[0])
                    h=buscarCOTODAS(b)
                    j=matriz[i]
                    l=h+m
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])
                    
    
    
            if re.search("(JR .*h)$" ,lineas[cont]):
                print("Es igual a JR numero") 
                if (p==1):
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                        print(b)
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
                    
                    
    
                if (p==2):
                    print("Entra pasada 2")
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                        
                    m=re.search("[0-9]{1,5}",lineas[cont])
                    h=buscarCOTODAS(b)
                    trans=formatoHexaSinCambiar(m[0])
                    print("##################", trans)
                    res=resta(trans, matriz[i+1])
                    j=matriz[i]
                    l=h+res
                    
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:7])
    
    
            if re.search("JR .*(\(?eti.*\)?)$" ,lineas[cont]):
                print("Es igual a JR etiqueta")  
                if (p==1):
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL,g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
                    
                if (p==2):
                    print("Entra pasada 2")
                    
                    if re.search(",",lineas[cont]):
                        temp=lineas[cont].split(",")
                        b=lineas[cont].replace(temp[1]," nn")
                    else:
                        temp=lineas[cont].split(" ")
                        b=lineas[cont].replace(temp[1],"nn")
                        
                    m=re.search("eti[0-9]{1,8}",lineas[cont])
                    h=buscarCOTODAS(b)
                    trans=valOfEti(tS,m[0])
                    trans=trans[2]+trans[3]+trans[0]+trans[1]
                    res=resta(trans, matriz[i+1])
                    j=matriz[i]
                    l=h+res
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:7])


        ###########################
        ##########################
        ############################
        ############################
        ###########################


        if re.search("(BIT|SET|RES) [0-7], \(I(X|Y)\+[0-9]{1,3}\)", lineas[cont]) and c==0:
            print("Caso especial de bit")
            c=1




        ##########################
        #############################
        ###############################
        ################################

        #Pseudoinstrucciones

        if re.search("#.*:EQU [0-9]{1,4}" ,lineas[cont]) and c==0:
            if p==1:
                m=re.match("#[A-Z]{1,10}.", lineas[cont])
                m=re.sub(":","", m[0])
                n=re.search("[0-9]{1,4}",lineas[cont])
                trans=DecimalAHexa(n[0])
                
                tS.update({m:trans})
                print(tS)
            
                c=1
            if p==2:
                c=1
       
        if re.search("ORG [0-9]{1,5}h" ,lineas[cont]) and c==0:
            if p==1:
                m=re.search("[0-9]{1,5}",lineas[cont])
                trans=formatoHexaSinCambiar(m[0])
                CL=trans
                print(CL)
                c=1
            if p==2:
                c=1

        if re.match("(END)$" ,lineas[cont]) and c==0:
            c=1
            p=p+1
            break











        ###############################
        ################################
        ##################################
        ##################################



        if re.search("(.*[0-9]{1,5})$",lineas[cont]) and c==0:

                print("Es igual a cuaquier cosa   numero")
        

                #Hacer lo de registro y numero
                    
                print(lineas[cont])
                if (p==1):
                    temp=lineas[cont].split(",")
                    b=lineas[cont].replace(temp[1]," n")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=sumaHexa(CL, g)
                    i=i+1
                    print("CL ", CL)
                    print(matriz[0:7])
                    c=1

                if (p==2):
                    print("Entra pasada 2")
                    temp=lineas[cont].split(",")
                    b=lineas[cont].replace(temp[1]," n")
                    m=re.search("[0-9]{1,5}",lineas[cont])
                    h=buscarCOTODAS(b)
                    j=matriz[i]
                    trans=DecimalAHexa(m[0])
                    l=h+trans
                    j[1]=l
                    matriz[i]=j
                    i=i+1
                    print(matriz[0:10])
                    c=1


        if re.search("(\(?.*#.*\)?)$" ,lineas[cont]) and c==0:

            print("Es igual a cuaquier cosa   EQU")
        
            if (p==1):
                    temp=lineas[cont].split(" ")
                    b=lineas[cont].replace(temp[1],"n")
                    print("Entra pasada 1")
                    g=buscarCLTODAS(b)
                    g=str(g)
                    arreglo=["0","0","0"]
                    arreglo[0]=CL
                    arreglo[2]=lineas[cont]
                    matriz[i]=arreglo
                    CL=CL+g
                    i=i+1
                    print("CL ", CL)
                    c=1

            if (p==2):
                    print("Entra pasada 2")
                    temp=lineas[cont].split(" ")
                    b=lineas[cont].replace(temp[1]," n")
                    m=temp[1]
                    h=buscarCOTODAS(lineas[cont])
                    j=matriz[i]
                    l=h+trans
                    j[1]=h 
                    matriz[i]=j
                    i=i+1
                    c=1



        if re.match("([A-Z]{1,5})$",lineas[cont]) and c==0:#Hay que quitar la eti antes
        
            print("Es igual a cualquier cosa sola")
        
                    
            print(lineas[cont])
            if (p==1):
                print("Entra pasada 1")
                g=buscarCLTODAS(lineas[cont])
                g=str(g)
                arreglo=["0","0","0"]
                arreglo[0]=CL
                arreglo[2]=lineas[cont]
                matriz[i]=arreglo
                CL=sumaHexa(CL, g)
                i=i+1
                print("CL ", CL)
                print(matriz[0:7])
                c=1

            if (p==2):
                print("Entra pasada 2")
                m=re.search("[A-Z]{1,5}",lineas[cont])
                h=buscarCOTODAS(lineas[cont])
                h=str(h)
                j=matriz[i]
                l=h
                j[1]=l
                matriz[i]=j
                i=i+1
                print(matriz[0:10])
                c=1

        if re.search("([A-Z]{1,5}) ([A-Z]{1,3})$" ,lineas[cont]) and c==0:
            print("Es igual a cualquier cosa espacio y cualquier cosa")
            if (p==1):
                print(lineas[cont])
                print("Entra pasada 1")
                g=buscarCLTODAS(lineas[cont])
                g=str(g)
                arreglo=["0","0","0"]
                arreglo[0]=CL
                arreglo[2]=lineas[cont]
                matriz[i]=arreglo
                CL=sumaHexa(g,CL)
                i=i+1
                print("CL ", CL)
                c=1

            if (p==2):
                print("Entra pasada 2")
                h=buscarCOTODAS(lineas[cont])
                j=matriz[i]
                j[1]=h 
                matriz[i]=j
                i=i+1
                c=1
                
        if c==0:
            print("Es igual a cualquier otra cosa restante")
            if (p==1):
                print(lineas[cont])
                print("Entra pasada 1")
                g=buscarCLTODAS(lineas[cont])
                g=str(g)
                arreglo=["0","0","0"]
                arreglo[0]=CL
                arreglo[2]=lineas[cont]
                matriz[i]=arreglo
                CL=sumaHexa(g,CL)
                i=i+1
                print("CL ", CL)
                c=1

            if (p==2):
                print("Entra pasada 2")
                h=buscarCOTODAS(lineas[cont])
                j=matriz[i]
                j[1]=h 
                matriz[i]=j
                i=i+1
                c=1


i=0
for var in matriz:
    matriz[i][0]= formatoHexaSinCambiar(str(var[0]))
    i=i+1
    if var ==["0000","0","0"]:
        print("Si es")

print(matriz)

arrOfArrToText(matriz,tS)
dochex(juntarCO(matriz),"0000")

#bucle1
#Bucle2
#Agregar un arreglo extra solo con CL


#Al finalizar los dos blucles se tendra la matriz llena de todas las instrucciones
#Se copiara el primer arreglo de la matriz en la primera linea
#El segundo en la segunda y asi sucesivamnte
#Cuando se acabe de copiar el arrglo se copiara la tabla de simbolos
#Cada arreglo tendra [CL,CO,nombre instruccion]
