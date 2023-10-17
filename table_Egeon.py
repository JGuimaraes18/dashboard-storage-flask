from connection import * 
import numpy as np

rackArray = []
nome_maquinaArray = []
marca_maquinaArray = []
modelo_maquinaArray = []
processadores_maquinaArray = []
memoria_maquinaArray = []
potenciaMaxima_maquinaArray = []
tarifaMensal_maquinaArray = []

for x in myresultEgeon: 
    rackArray = np.append(rackArray, x[0])
    nome_maquinaArray = np.append(nome_maquinaArray, x[1])
    marca_maquinaArray = np.append(marca_maquinaArray, x[2])
    modelo_maquinaArray = np.append(modelo_maquinaArray, x[3])
    processadores_maquinaArray = np.append(processadores_maquinaArray, x[4])
    memoria_maquinaArray = np.append(memoria_maquinaArray, x[5])
    potenciaMaxima_maquinaArray = np.append(potenciaMaxima_maquinaArray, x[6])
    tarifaMensal_maquinaArray = np.append(tarifaMensal_maquinaArray, x[7])

arrayEgeon = np.column_stack((rackArray, nome_maquinaArray, marca_maquinaArray, modelo_maquinaArray, processadores_maquinaArray, memoria_maquinaArray, potenciaMaxima_maquinaArray, tarifaMensal_maquinaArray))