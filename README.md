# Traductor-hexadecimal-a-ensamblador
Este proyecto permite transformar instrucciones ingresadas en código hexadecimal a instrucciones en lenguaje ensamblador entendibles para el simulador Z80
 
 GUÍA DE USUARIO
- El programa se ejecuta desde un IDE.
- Se leerá una instrucción por línea.
- Cada línea de instrucción debe estar seguida de la anterior. Es decir justo en la siguiente línea.
- Solo aceptará las instrucciones definidas para el procesador Z-80.
- Las instrucciones que separan dos elementos por una coma deben de ser separados cada uno por un espacio (por ejemplo, se tomará en cuenta LD A, B no LD A,B).
- Para definir una etiqueta se deberá poner justo antes de la instrucción sin dejar ningún espacio y con el formato eti$. $ representa cualquier número.
- Para referirse a una posición de memoria se deberá ingresar el número en hexadecimal seguido de un h.
-  La etiqueta de la pseudoinstrucción  EQU y DB debe empezar con el símbolo #.
- La declaración de algún número que no haga referencia a memoria se hará en número decimal.
