import numpy as np #Utilizado para operaciones numéricas
import matplotlib.pyplot as plt #Utilizado para crear gráficos
import seaborn as sns #Utilizado para mejorar la visualización de los gráficos

#Función para calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(punto1, punto2):
    return np.sqrt(np.sum((punto1 - punto2) ** 2))

#Función para generar datos aleatorios en un espacio de una dimensión d
def generar_datos(num_puntos, dimension):
    datos = np.random.rand(num_puntos, dimension) #Genera datos aleatorios en un espacio de 'dimension' dimensiones
    return datos

#Función para calcular las distancias entre todos los pares de puntos
def calcular_distancias(datos):
    num_puntos = datos.shape[0] #Obtiene el número de puntos (filas) en la matriz 'datos'
    distancias = [] #Se inicializa una lista para almacenar las distancias calculadas
    for i in range(num_puntos):
        #En este bucle evita calcular la distancia de un punto a sí mismo y evita duplicados
        for j in range(i + 1, num_puntos):  
            distancia = distancia_euclidiana(datos[i], datos[j]) #Calcula la distancia euclidiana entre los puntos i y j
            distancias.append(distancia) #Agrega la distancia calculada a la lista 'distancias'
    return distancias

#Dimensiones que se analizaran
dimensiones = [10, 50, 100, 500, 1000, 2000, 5000]

#Genera histogramas y análisis para cada dimensión
for dimension in dimensiones:
    #Genera 100 puntos aleatorios en un espacio de 'dimension' dimensiones
    datos = generar_datos(100, dimension)
    distancias = calcular_distancias(datos) #Calcula las distancias entre todos los pares de puntos
    
    #Crea un histograma con barras de color púrpura
    plt.figure(figsize=(8, 6)) #Crea una nueva figura de tamaño 8x6 pulgadas
    sns.histplot(distancias, bins=10, kde=True, color='purple') #Crea el histograma usando Seaborn
    plt.title(f"Histograma de las distancias entre puntos con dimension {dimension}") #Establece el título del gráfico
    plt.xlabel("Distancia") #Etiqueta del eje x
    plt.ylabel("Frecuencia") #Etiqueta del eje y
    
    #Establece límites del eje x
    plt.xlim(0, max(distancias)) #Establece los límites del eje x desde 0 hasta la distancia máxima
    plt.show() #Muestra el gráfico
    
    #Analisis de las distancias entre puntos con dimension d
    print(f"ANALISIS DE LAS DISTANCIAS ENTRE PUNTOS CON DIMENSION {dimension}") #Imprime el título del análisis en cada dimension
    print(f"----------------------------------------------------------") #Línea divisoria
    print(f"Distancia Promedio: {np.mean(distancias)}") #Calcula y muestra la distancia promedio
    print(f"Distancia Mínima: {np.min(distancias)}") #Calcula y muestra la distancia mínima
    print(f"Distancia Máxima: {np.max(distancias)}") #Calcula y muestra la distancia máxima
    print(f"Desviación Estándar: {np.std(distancias)}\n") #Calcula y muestra la desviación estándar