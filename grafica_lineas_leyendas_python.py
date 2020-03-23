import math
import matplotlib.pyplot as plt

#Creo la lista 1 con 8 datos
lista1 = [11,2,3,15,8,13,21,34]
plt.plot(lista1)   # Dibuja el gráfico
plt.show()

#Creo la lista 2 con 8 datos
lista2 = [2,3,4,2,3,6,4,10]
plt.plot(lista2)   # No dibuja datos de lista2
plt.show()

#Creo la lista 3 con 8 datos
lista3 = [9,15,9,15,9,15,9,15]
plt.plot(lista3)   # No dibuja datos de lista3
plt.show()


#Leyendas
plt.xlabel("abscisa")   # Inserta el título del eje X 
plt.ylabel("ordenada")   # Inserta el título del eje Y
plt.title("Gráfica")   # Establece nuevo título pero no muestra en gráfico
plt.plot(lista1, marker='x', linestyle=':', color='b', label = "Enero") #Asigna una leyenda a los datos de la lista 1
plt.plot(lista2, marker='*', linestyle='--', color='g', label = "Febrero")
plt.plot(lista3, marker='o', linestyle=':', color='r', label = "Marzo")
plt.legend(loc = "upper left") #Permite que las leyendas se muestren
#en la posición que se elija, si no se agrega la posición por defecto la pone
#en la parte superior izquierda (upper left)
#plt.show()

#Posición de leyendas (loc=):
#upper, arriba
#lower, abajo
#center, centro
#left, izquierda y 
#right, derecha

#Marcadores: Marcadores (marker=):
#+, Cruz
#., Punto
#o,Círculo
#*, Estrellas
#p, Pentágonos
#s, cuadrados
#x, Tachados
#D, Diamantes
#h, Hexágonos y
#^, Triángulos

#Colores (color=):
#b, blue
#g, green
#r, red
#c, cyan
#m, magenta
#y, yellow
#k, black
#w, white

#Activar cuadrícula
plt.grid(color='k',linestyle='--',linewidth=1)  # Activa cuadrícula del gráfico pero no se muestra

#Activo el modo interactivo de dibujo
plt.show()
