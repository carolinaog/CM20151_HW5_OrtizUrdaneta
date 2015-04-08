
# coding: utf-8

# In[1]:

import pylab
from pylab import *
import numpy as np


# In[2]:

xp, yp, zp =np.genfromtxt('Serena-Venus.txt',unpack=True, dtype=None, usecols=(1,2,3))
#print xp, yp, zp


# In[3]:

#Dimensiones de los vectores xp, yp,zp
l_x=len(xp)
l_y=len(yp)
l_z=len(zp)

#dimension de matriz
dim=100

#print l_x, l_y, l_z, dim


# In[4]:

#Eje x
max_x=max(xp)
min_x=min(xp)
lado_x=(max_x - min_x)

#Eje y
max_y=max(yp)
min_y=min(yp)
lado_y=(max_y - min_y)

#Eje z
max_z=max(zp)
min_z=min(zp)
lado_z=(max_z - min_z)

#print lado_x, lado_y, lado_z
#print min_x, min_y, min_z
#print max_x, max_y, max_z


# In[5]:

#La matriz es de 1000*1000*1000 por lo cual:
#Eje x
delta_x=(lado_x/float(dim))

#Eje y
delta_y=(lado_y/float(dim))

#Eje z
delta_z=(lado_z/float(dim))


#print delta_x, delta_y, delta_z


# In[6]:

#Funcion que determina el x_i, y_i, z_i en terminos de coordendas
#Eje x
def celda_x(i):
    x_i=min_x+(delta_x/2)+(i*delta_x)
    return x_i

#Eje y
def celda_y(i):
    y_i=min_y+(delta_y/2)+(i*delta_y)
    return y_i

#Eje z
def celda_z(i):
    z_i=min_z+(delta_z/2)+(i*delta_z)
    return z_i


# In[7]:

#Probar funcion anterior
#print (celda_x(1)-celda_x(0))-delta_x
#print (celda_x(2)-celda_x(1))-delta_x
#print (celda_y(1)-celda_y(0))-delta_y
#print (celda_y(2)-celda_y(1))-delta_y
#print (celda_z(1)-celda_z(0))-delta_z
#print (celda_z(2)-celda_z(1))-delta_z


# In[8]:

#pasar de funciones a arreglos
xi=[]
for i in range(dim):
    x_i=celda_x(i)
    xi.append(x_i)
#print xi[0]

yi=[]
for i in range(dim):
    y_i=celda_y(i)
    yi.append(y_i)
#print yi[0]

zi=[]
for i in range(dim):
    z_i=celda_z(i)
    zi.append(z_i)
#print zi[0]


# In[9]:

#x, y, z es la relacion entre i (celda) y la posicion de la particula (p), se determina que x_r=xi-xp
def real_x(j):
    x=[]
    for p in range(l_x):
        x_r=xi[j]-xp[p]
        x.append(x_r)
    return x

def real_y(j):
    y=[]
    for p in range(l_y):
        y_r=yi[j]-yp[p]
        y.append(y_r)
    return y

def real_z(j):
    z=[]
    for p in range(l_z):
        z_r=zi[j]-zp[p]
        z.append(z_r)
    return z


# In[10]:

#Se genera el Wx, Wy y Wz a partir de las condicion dada inicialmente xi-xp<delta x genera un W=W_xi+(1-(|x|/delta x)) para el caso del eje x, se va haciendo la sumatoria de las N particulas, sumando el contador W_x
W_x=[]
for i in range(dim):
    W_xi=0
    X_R=np.abs(real_x(i)) 
    #int X_R
    for j in range(l_x):
        if(X_R[j]< delta_x):
            x_r=X_R[j]
            W_xi=W_xi+(1-(x_r)/delta_x)
            #print W_xi
    W_x.append(W_xi)
#print W_x

W_y=[]
for i in range(dim):
    W_yi=0
    Y_R=np.abs(real_y(i))
    #print Y_R
    for j in range(l_y):
        if(Y_R[j]< delta_y):
            y_r=Y_R[j]
            W_yi=W_yi+(1-(y_r)/delta_y)
            #print W_yi
    W_y.append(W_yi)
#print W_y 

W_z=[]
for i in range(dim):
    W_zi=0
    Z_R=np.abs(real_z(i))
    #print Z_R
    for j in range(l_z):
        if(Z_R[j]< delta_z):
            z_r=Z_R[j]
            W_zi=W_zi+(1-(z_r)/delta_z)
            #print W_zi
    W_z.append(W_zi)
#print W_z 


# In[11]:

Matriz_rho = zeros((dim,dim,dim))
deltas=1/(delta_x*delta_y*delta_z)
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            Matriz_rho[i][j][k]=((W_x[i])*(W_y[j])*(W_z[k]))*deltas
#print Matriz_rho


# In[12]:

#Verifica la matriz
b=W_x[0]
c=W_y[0]
d=W_z[0]
a=deltas*b*c*d
#print b
#print c
#print d
#print a


# In[35]:

#Imprime matriz de densidades en archivo llamado densidades.txt
# Exportamos la cuadrícula de 100*100*100 con la densidad generada, a un archivo llamado densidades.txt
with file('densidades.txt', 'w') as outfile:
    outfile.write('# Array shape: {0}\n'.format(Matriz_rho.shape))

    #Se itera a través de unn arreglo n-dimensiones que produce "tajadas" de la matriz 100*100*100
    for data_slice in Matriz_rho:

        # Se escriben los valores con 2 decimales  
        np.savetxt(outfile, data_slice, fmt='%-7.12f')
        #np.savetxt(outfile, data_slice)

        # Cada vez que hay una "tajada diferente" se desplaza con \n 
        outfile.write('# New slice\n')
        
#fuente= http://stackoverflow.com/questions/3685265/how-to-write-a-multidimensional-array-to-a-text-file


# In[37]:

#Punto 1.b Determinar el potencial gravitacional a partir de la relación de phi=-rho.
from pylab import *
from numpy.fft import ifftn

Matriz_phi_gorrito= zeros((dim,dim,dim))
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            Matriz_phi_gorrito[i,j,k]=Matriz_rho[i,j,k]*-1        
            
Matriz_phi=np.abs(ifftn(Matriz_phi_gorrito))
#print Matriz_phi


# In[38]:

#Imprime matriz de potenciales (phi) en archivo llamado potenciales.txt
# Exportamos la cuadrícula de 100*100*100 con la densidad generada, a un archivo llamado potenciales.txt
with file('potenciales.txt', 'w') as outfile:
    outfile.write('# Array shape: {0}\n'.format(Matriz_rho.shape))

    #Se itera a través de unn arreglo n-dimensiones que produce "tajadas" de la matriz 100*100*100
    for data_slice in Matriz_phi:

        # Se escriben los valores con 2 decimales  
        np.savetxt(outfile, data_slice, fmt='%-7.12f')
        #np.savetxt(outfile, data_slice)

        # Cada vez que hay una "tajada diferente" se desplaza con \n 
        outfile.write('# New slice\n')
        
#fuente= http://stackoverflow.com/questions/3685265/how-to-write-a-multidimensional-array-to-a-text-file


# In[14]:

#Se calcula la fuerza gravitacional a partir del gradiente del potencial, siguiendo la ecuación
Fx, Fy, Fz=np.gradient(Matriz_phi, delta_x,delta_y,delta_z)
Fx=-Fx
Fy=-Fy
Fz=-Fz
Fuerza_gravitacional=sqrt(Fx**2+Fy**2+Fz**2)
#print Fuerza_gravitacional[0][0][0]
#print Fuerza_gravitacional



# In[15]:

#Funcion que determina los planos del cubo, de acuerdo a un z fijado que entra por parámetro
def FUERZA_G(z):
    F_gravitacional=zeros((dim,dim))
    for i in range(dim):
        for j in range(dim):
            F_gravitacional[i][j]=Fuerza_gravitacional[i][j][z]
    return F_gravitacional


# In[34]:

# Exportamos la cuadrícula de 100*100*100 con la fuerza gravitacional generada, a un archivo llamado Fuerza.txt que será leido en el sigiente codigo
with file('Fuerza.txt', 'w') as outfile:
    outfile.write('# Array shape: {0}\n'.format(Fuerza_gravitacional.shape))

    #Se itera a través de unn arreglo n-dimensiones que produce "tajadas" de la matriz 100*100*100
    for data_slice in Fuerza_gravitacional:

        # Se escriben los valores con 2 decimales  
        np.savetxt(outfile, data_slice, fmt='%-7.12f')
        #np.savetxt(outfile, data_slice)

        # Cada vez que hay una "tajada diferente" se desplaza con \n 
        outfile.write('# New slice\n')
        
#fuente= http://stackoverflow.com/questions/3685265/how-to-write-a-multidimensional-array-to-a-text-file


# In[ ]:



