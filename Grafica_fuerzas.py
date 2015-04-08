
# coding: utf-8

# In[27]:

import numpy as np
import pylab
from pylab import *
# Read the array from disk
Fuerza_G = np.loadtxt('Fuerza.txt')

# Note that this returned a 2D array!
#print new_data.shape

# However, going back to 3D is easy if we know the 
# original shape of the array
Fuerza_G = Fuerza_G.reshape((100,100,100))

# Just to check that they're the same...
#assert np.all(new_data == data)
#print Fuerza_G
dim=100


# In[28]:

#print shape(Fuerza_G)


# In[29]:

#Maximo - Minimo  Global, se toma este valor porque en realidad lo que se busca es obtener el lugar donde la fuerza gravitacional es considerablemente mayor o menor.
Min_Fuerza_gravitacional=Fuerza_G.min()
Max_Fuerza_gravitacional=Fuerza_G.max()

print "Minimo= ", Min_Fuerza_gravitacional
print "Maximo=", Max_Fuerza_gravitacional


# In[51]:

#Funcion que nos da un plano del cubo, de acuerdo a un z fijado que entra por parámetro
def FUERZA_G(z):
    F_gravitacional=zeros((dim,dim))
    for i in range(dim):
        for j in range(dim):
            F_gravitacional[i][j]=Fuerza_G[i][j][z]
    return F_gravitacional


# In[52]:

V=FUERZA_G(0)


# In[53]:

x, y = mgrid[0:100:1, 0:100:1]


# In[ ]:

imshow(V, origin='lower')

colorbar()

contour(x,y, V,25, colors='white', linewidth=.05)

title("FUERZA GRAVITACIONAL")
xlabel("POSICION X")
ylabel("POSICION Y")
savefig("fuerza.png")
show()

#Fuente=http://nbviewer.ipython.org/url/elektromagnetisme.no/wp-content/uploads/2013/09/spherePotential-preview2.ipynb


# In[ ]:



