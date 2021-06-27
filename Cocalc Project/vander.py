import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# define la funcion o dinamica de vanderpol
def vdp1(t, y):
    return np.array([y[1], (1 - y[0]**2)*y[1] - y[0]])

ti, tf = 0, 20                 # tiempo de inicio y fin de solucion
t = np.linspace(ti, tf, 100)   # el vector tiempo t con 100 pasos
y0 = [2, 0]                    # condiciones inicial
y = np.zeros((len(t), len(y0)))   # define el arreglo de la solucion
y[0, :] = y0
r = integrate.ode(vdp1).set_integrator("dopri5")  # integracion
                                                  # numerica
r.set_initial_value(y0, ti)    # configura las condiciones iniciales
for i in range(1, t.size):
   y[i, :] = r.integrate(t[i]) # conseguir mas valores,
                               # completa el arreglo
   if not r.successful():
       raise RuntimeError("no se consigue integrar")
plt.plot(t, y)
plt.show()
