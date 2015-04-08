all: fuerza.png
fuerza.png: Grafica_fuerzas.py
	python Grafica_fuerzas.py
Grafica_fuerzas.py: Fuerza.txt
Fuerza.txt:	Solucion_Poisson.py
	python Solucion_Poisson.py
clear:
	rm -f *.png *.txt
