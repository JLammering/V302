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
print(' ')
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

print(' ')
#Aufgabe b

print('Aufgabe b')

#Wert 1

print('Wert 1: ')

print('1.Messung:')

C2 = ufloat(399e-9, 399e-9*0.002)
R4 = ufloat(625, 625*0.005)
R3 = ufloat(375, 375*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('2.Messung:')

C2 = ufloat(750e-9, 750e-9*0.002)
R4 = ufloat(470, 470*0.005)
R3 = ufloat(530, 530*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('3.Messung:')

C2 = ufloat(992e-9, 992e-9*0.002)
R4 = ufloat(399, 399*0.005)
R3 = ufloat(601, 601*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

#Wert 3
print(' ')
print('Wert 3: ')

print('1.Messung:')

C2 = ufloat(399e-9, 399e-9*0.002)
R4 = ufloat(514, 514*0.005)
R3 = ufloat(486, 486*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('2.Messung:')

C2 = ufloat(750e-9, 750e-9*0.002)
R4 = ufloat(360, 360*0.005)
R3 = ufloat(640, 640*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('3.Messung:')

C2 = ufloat(992e-9, 992e-9*0.002)
R4 = ufloat(297, 297*0.005)
R3 = ufloat(703, 703*0.005)

Cx = C2*R4/R3

print('Cx =', Cx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

#Wert 9(Cx mit Rx)
print(' ')
print('Wert 3: ')

print('1.Messung:')

C2 = ufloat(399e-9, 399e-9*0.002)
R2 = ufloat(512, 512*0.03)
R4 = ufloat(521, 521*0.005)
R3 = ufloat(479, 479*0.005)

Cx = C2*R4/R3
Rx = R2*R3/R4

print('Cx =', Cx,'  Rx =',Rx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('2.Messung:')

C2 = ufloat(750e-9, 750e-9*0.002)
R2 = ufloat(270, 270*0.03)
R4 = ufloat(367, 367*0.005)
R3 = ufloat(633, 633*0.005)

Cx = C2*R4/R3
Rx = R2*R3/R4

print('Cx =', Cx,'  Rx =',Rx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('3.Messung:')

C2 = ufloat(992e-9, 992e-9*0.002)
R2 = ufloat(207, 207*0.03)
R4 = ufloat(306, 306*0.005)
R3 = ufloat(694, 694*0.005)

Cx = C2*R4/R3
Rx = R2*R3/R4

print('Cx =', Cx,'  Rx =',Rx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

#Aufgabe c

print(' ')
print('Aufgabe c:')

print('Wert 17: ')

print('1.Messung:')

L2 = ufloat(14.6e-3, 14.6e-3*0.002)
R2 = ufloat(34, 34*0.03)
R4 = ufloat(259, 259*0.005)
R3 = ufloat(741, 741*0.005)

Lx = L2*R3/R4
Rx = R2*R3/R4

print('Lx =', Lx,'  Rx =',Rx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)

print('2.Messung:')

L2 = ufloat(20.1e-3, 20.1e-3*0.002)
R2 = ufloat(41, 41*0.03)
R4 = ufloat(324, 324*0.005)
R3 = ufloat(676, 676*0.005)

Lx = L2*R3/R4
Rx = R2*R3/R4

print('Lx =', Lx,'  Rx =',Rx,'  C2 =', C2,'  R4 =',R4,'  R3 =', R3)
