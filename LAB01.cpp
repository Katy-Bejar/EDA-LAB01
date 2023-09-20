#include <iostream>
#include <vector>
#include <cmath>
#include <random>

using namespace std;

//Función para calcular la distancia euclidiana entre dos puntos
double distanciaEuclidiana(const vector<double>& punto1, const vector<double>& punto2) {
    double distancia = 0.0;
    for (size_t i = 0; i < punto1.size(); ++i) {
        distancia += pow(punto1[i] - punto2[i], 2); //Calcula la distancia euclidiana en cada dimensión y la suma
    }
    return sqrt(distancia); //Calcula la raíz cuadrada de la suma de las distancias al cuadrado
}

int main() {
    //Dimensiones para las cuales se calcularán las distancias
    const int dimensiones[] = {10, 50, 100, 500, 1000, 2000, 5000};
    
    //Recorre las dimensiones
    for (int dim : dimensiones) {
        //Imprime un título que indica la dimensión actual
        cout << "Distancias entre puntos con dimensión " << dim << ":" << endl;

        //Número de puntos aleatorios a generar
        const int numPuntos = 100;
        
        //Inicializa un generador de números aleatorios
        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<double> dis(0.0, 1.0); //Genera numeros aleatorios entre 0 y 1

        //Genera puntos aleatorios en el espacio de la dimensión actual
        vector<vector<double>> puntos(numPuntos, vector<double>(dim));
        for (int i = 0; i < numPuntos; ++i) {
            //Genera coordenadas aleatorias en cada dimensión
            for (int j = 0; j < dim; ++j) {
                puntos[i][j] = dis(gen);
            }
        }

        //Calcula las distancias entre todos los pares de puntos
        for (int i = 0; i < numPuntos; ++i) {
            for (int j = i + 1; j < numPuntos; ++j) {
                //Calcula la distancia euclidiana entre dos puntos
                double distancia = distanciaEuclidiana(puntos[i], puntos[j]);
                //Imprime la distancia entre los puntos i y j
                cout << "Distancia entre el P" << (i + 1) << " y el P" << (j + 1) << ": " << distancia << endl;
            }
        } 
        cout << endl; //Separa las distancias de diferentes dimensiones con una línea en blanco
    }
    return 0;
}