# -*- coding: utf-8 -*-


def formatoHexaSinCambiar(cdl):
    if len(cdl) == 1:
        return "0" + "0" + "0" + cdl
    if len(cdl) == 2:
        return "0" + "0" + cdl
    if len(cdl) == 3:
        return "0" + cdl
    if len(cdl) == 4:
        return cdl

print(formatoHexaSinCambiar("ABA"))
