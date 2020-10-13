                 


def arrOfArrToText(a,tS):
    f = open ('nuestro1.LST', 'w')
    for x in range (0, len(a)):
        for y in range (0, 3):
            m = a[x][y]
            f.write(str(m))
            if y < 2:
                f.write('                         ')
        if x < len(a)-1:
            f.write('\n')
    
    f.write('\n')
    f.write('\n')
    f.write('\n')        

    f.write('Tabla de simbolos\n')     
    for key in tS:
        f.write(key)
        f.write('  ')
        f.write(tS[key])
        f.write("\n")
        
           
    f.close()
## Inicia ejemplo de como usarlo, crea un archivo lst con el arreglo de arreglos que recibe
def main():
    a = [["a", "CD", "2055"], ["b", "FG", "6589"], ["c", "YT", "1566"]]
    tS={"ECU":"344","ECy":"44","EttU":"111"}
    arrOfArrToText(a,tS)

##main()
