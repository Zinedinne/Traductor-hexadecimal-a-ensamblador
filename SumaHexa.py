# -*- coding: utf-8 -*-


def sumaHexa(a, b):#parametros son str
   da = int(a, 16)
   db = int(b, 16)
   suma = da + db
   resultado = (hex(suma)).replace("0x", "").upper()
   return resultado

