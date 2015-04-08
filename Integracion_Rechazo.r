library(ggplot2)
#Punto 2A. Se genera una funcion que determina el area debajo de la curva, por medio de el metodo del descarte. En el fondo lo que saca esta funcion es una integral
#Funcion de prueba
lm<-function(x,y){
  #Entra la funcion despejada con el fin de obtener F(x)-X=0
  return(y-x**2)
}

lm_2<-function(x){
  return(x**2)
}

#FUNCION - METODO DEL RECHAZO
integral<-function(puntos,lm,lim_x, lim_y)
{
  adentro_x<-c()
  adentro_y<-c()
  afuera_x<-c()
  afuera_y<-c()
  
  for (n in 1:puntos)
    {
    x <- lim_x*runif(1,0,1)
    y <- lim_y*runif(1,0,1)
    a=lim_x*lim_y
    if (lm(x,y)<0){
      adentro_x=append(adentro_x, (x))
      adentro_y=append(adentro_y, (y))
      } else
        {
        afuera_x=append(afuera_x, (x))
        afuera_y=append(afuera_y, (y))
        }
  }
  p<-qplot(adentro_x, adentro_y,xlab="X", ylab="F(X)",main="Metodo del Rechazo")
  show(p)
  return((length(adentro_x)/puntos)*a)
}

#Resultado de prueba
integral(10000,lm,1,1)
#Resultado por funcion integrate
integrate(lm_2,0,1)

#Esta función sirve para las integrales que tengan dominios definidos, por ello en el caso de tener integrales al infinito, se deben aplicar metodos de sustitución como el que se presenta en los otros puntos.

#Punto 2B. Se realiza la integral por medio del metodo del descarte de la siguiente funcion H(x)=[cos(50x)+sin(20x)]**2
lm<-function(x,y){
  x=cos(50*x)+sin(20*x)
  return(y-x**2)
}

lm_2<-function(x){
  x=cos(50*x)+sin(20*x)
  return(x**2)
}
#Resultado por metodo del rechazo
integral(10000,lm,1,5)
#Resultado por funcion integrate
integrate(lm_2,0,1)

#PUNTO 2C.Basandose en la transformacion de limites planteada en http://www.cceb.upenn.edu/pages/courses/BSTA670/2009/18_NumInt.pdf
pi<-3.14
lm<-function(x,y){
  return((y*pi)+(pi*y*(x**(-2)))-(x**(-2)))
}

lm_2<-function(x){
  return((1/(pi+(pi*x**2))))
}

#Resultado por metodo del rechazo
integral(10000,lm,0.5,3.5)
#Resultado por funcion integrate
integrate(lm_2,2,Inf)