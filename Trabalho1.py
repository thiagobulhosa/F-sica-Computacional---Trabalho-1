from numpy import *
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import sys

def x1(tempo):
    return v0*tempo

def x2(tempo):
    return xm*tanh(tempo/r)

def y1(tempo):
    return (a*tempo**2)/2

def y2(tempo):
    return y0*exp(tempo/r)

def colisao_x(t):
    x1=v0*t
    x2=xm*tanh(t/r)
    return x1-x2

def colisao_y(y0,t):
    y1=(a*t*t)/2
    y2=y0*exp(t/r)
    return y1-y2

v0=10
a=5
xm=100
r=5
tempo=linspace(0,16,1000)
r1 = root_scalar (colisao_x,args=(),method='brentq', bracket=[1.e-8,1.e+8])
r2= root_scalar (colisao_y, args=(r1.root), method='brentq', bracket=[1.e-8,1.e+8])
y0=r2.root
print("y0=",y0)
plt.plot(tempo,"blue",label="obj1")
#plt.plot(x2(tempo),y2(tempo),"red",label='obj2')
plt.show()