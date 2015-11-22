import matplotlib.pyplot as plt
import numpy as np

v, U_Br = np.genfromtxt('datene.txt', unpack=True)

omega = v/240

plt.plot(omega, (np.absolute(U_Br/4.36))**2,'.', label='Messwerte')
plt.yscale('log')
plt.xlim(0, 10)
plt.ylabel(r'$(U_BR/U_S) / 1$')
plt.xlabel(r'$\omega / 1$')
plt.legend(loc='best')

v = np.linspace(0,1000000, 100000)
v_0 = 1/(2*np.pi*1000*(6.629e-7))
print('v_0=  ', v_0)
omega = v/v_0
y=(1/9)*(((omega**2)-1)**2)/((1-(omega**2)**2)+9*(omega**2))
plt.plot(omega, np.absolute(y),'-', label='theorie-Kurve')
plt.xlim(0, 10)
plt.ylabel(r'$U_BR/U_S / 1$')
plt.xlabel(r'$\omega / 1$')
plt.legend(loc='best')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plote.pdf')
