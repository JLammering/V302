import numpy as np
from uncertainties import ufloat

print('Aufgabe a')

#Aufgabe a

#Wert 13

print('Wert 13: ')

print('1.Messung:')

R2 = ufloat(332, 332*0.002)
R3 = ufloat(489, 489*0.005)
R4 = ufloat(511, 511*0.005)

Rx = R2*R3/R4

print('Rx =', Rx,'  R2 =', R2,'  R3 =', R3,'  R4 =',R4)

print('2.Messung:')

R2 = ufloat(664, 664*0.002)
R3 = ufloat(326, 326*0.005)
R4 = ufloat(674, 674*0.005)

Rx = R2*R3/R4

print('Rx =', Rx,'  R2 =', R2,'  R3 =', R3,'  R4 =',R4)

print('3.Messung:')

R2 = ufloat(1000, 1000*0.002)
R3 = ufloat(241, 241*0.005)
R4 = ufloat(759, 759*0.005)

Rx = R2*R3/R4

print('Rx =', Rx,'  R2 =', R2,'  R3 =', R3,'  R4 =',R4)

#Wert 12

print('Wert 12: ')

print('1.Messung:')

R2 = ufloat(332, 332*0.002)
R3 = ufloat(540, 540*0.005)
R4 = ufloat(460, 460*0.005)

Rx = R2*R3/R4

print('Rx =', Rx,'  R2 =', R2,'  R3 =', R3,'  R4 =',R4)

print('2.Messung:')

R2 = ufloat(664, 664*0.002)
R3 = ufloat(369, 369*0.005)
R4 = ufloat(631, 631*0.005)

Rx = R2*R3/R4

print('Rx =', Rx,'  R2 =', R2,'  R3 =', R3,'  R4 =',R4)

print('3.Messung:')

R2 = ufloat(1000, 1000*0.002)
R3 = ufloat(279, 279*0.005)
R4 = ufloat(721, 721*0.005)

Rx = R2*R3/R4

print('Rx =', Rx,'  R2 =', R2,'  R3 =', R3,'  R4 =',R4)


#Aufgabe b

print('Aufgabe b')

#Wert 1

print('Wert 1: ')

print('1.Messung:')

C2 = ufloat(399, 399*0.002)
R4 = ufloat(625, 625*0.005)
R3 = ufloat(375, 375*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('2.Messung:')

C2 = ufloat(750, 750*0.002)
R4 = ufloat(470, 470*0.005)
R3 = ufloat(530, 530*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('3.Messung:')

C2 = ufloat(992, 992*0.002)
R4 = ufloat(399, 399*0.005)
R3 = ufloat(601, 601*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)
