# -*- coding: utf-8 -*-

XY=raw_input('GENERO')
dni=raw_input('DNI')

'''
Se determina XY con las siguientes reglas
Masculino:20
Femenio:27
'''

if XY=='MASCULINO':
    cuil1='20'

elif XY=='FEMENINO':
    cuil1='27'

'''
Se multiplica XY 12345678 por un numero de forma separada:
X * 5
Y * 4
1 * 3
2 * 2
3 * 7
4 * 6
5 * 5
6 * 4
7 * 3
8 * 2
'''

a=float(cuil1[0])*5
b=float(cuil1[1])*4
c=float(dni[0])*3
d=float(dni[1])*2
e=float(dni[2])*7
f=float(dni[3])*6
g=float(dni[4])*5
h=float(dni[5])*4
i=float(dni[6])*3
j=float(dni[7])*2

'''
Se suman dichos resultados. El resultado obtenido se divide por 11. De esa división se obtiene un Resto que determina Z
Si el resto es 0= Entoces Z=0 Si el resto es 1= Entonces se aplica la siguiente regla:
*Si es hombre: Z=9 y XY pasa a ser 23 *Si es mujer: Z=4 y XY pasa a ser 23
Caso contrario XY pasa a ser (11- Resto).
'''
#Realizar la suma
suma=a+b+c+d+e+f+g+h+i+j

cociente_division=float(suma/11)
resto_division=float(suma%11)

if resto_division==0:
    Z=0

elif int(resto_division)==1:
    if XY=='MASCULINO':
        Z=9
        cuil1='23'
        
    elif XY=='FEMENINO':
        Z=4
        cuil1='23'

elif resto_division>1:
    resto2=int(suma-(int(cociente_division)*11))
    Z=(11-resto2)

print str(cuil1)+str(dni)+str(Z)

