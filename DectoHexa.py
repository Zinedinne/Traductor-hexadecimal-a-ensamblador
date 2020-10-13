# -*- coding: utf-8 -*-


def CambiarDigitos(digitos):
    decimales = [10, 11, 12, 13, 14, 15]
    hexadecimales = ["A", "B", "C", "D", "E", "F"]
    for c  in range(7):
        if digitos == decimales[c-1]:
            digitos = hexadecimales[c-1]
    return digitos
def DecimalAHexa(num):
    esExa = num.find("h")
    if esExa == len(num)-1:
        if len(num)==2:
            xc = num[0:len(num)-1]
            return "0" + xc + "00"
        elif len(num) == 3:
            xc = num[0:len(num)-1]
            return xc + "00"
        elif len(num) == 4:
            xc = num[0:len(num)-1]
            return xc[1] + xc [2] + "0" + xc[0]
        elif len(num) == 5:
            xc = num[0:len(num)-1]
            return xc[2] + xc[3] + xc[0] + xc[1]
        else:
            print("Hexadecimal inválido")
    elif num.isdigit() == False:
        print("Número inválido")
    else:
        hexadecimal = ""
        while num != 0:
            rem = CambiarDigitos(int(num) % 16)
            hexadecimal = str(rem) + hexadecimal
            num = int(int(num)/16)
        if len(hexadecimal) == 1:
            return "0" + hexadecimal         
        else:
            return hexadecimal
        
def main():#Ejemplo de como usar el método DecimalAHexa, DecimalAHexa devuelve el valor en hexa con el formaro 00
    numero = "22CCh" 
    conversion = DecimalAHexa(numero)
    print (conversion)

main()


        
