from connection import * 
import numpy as np

rackRv2Array = []
quantidadeRv2Array = []
responsavelRv2Array = []
marca_maquinaRv2Array = []
modelo_maquinaRv2Array = []
potenciaMaxima_maquinaRv2Array = []
tarifaMensal_maquinaRv2Array = []
diarioRack_Rv2Array = []
mensalRack_Rv2Array = []
anualRack_Rv2Array = []

for x in myresultRacks_v2: 
    rackRv2Array = np.append(rackRv2Array, x[0])
    quantidadeRv2Array = np.append(quantidadeRv2Array, x[1])
    responsavelRv2Array = np.append(responsavelRv2Array, x[2])
    marca_maquinaRv2Array = np.append(marca_maquinaRv2Array, x[3])
    modelo_maquinaRv2Array = np.append(modelo_maquinaRv2Array, x[4])
    potenciaMaxima_maquinaRv2Array = np.append(potenciaMaxima_maquinaRv2Array, x[5])
    tarifaMensal_maquinaRv2Array = np.append(tarifaMensal_maquinaRv2Array, x[6])
    diarioRack_Rv2Array = np.append(diarioRack_Rv2Array, x[7])
    mensalRack_Rv2Array = np.append(mensalRack_Rv2Array, x[8])
    anualRack_Rv2Array = np.append(anualRack_Rv2Array, x[9])

arrayRacks_v2 = np.column_stack((rackRv2Array, quantidadeRv2Array, responsavelRv2Array, marca_maquinaRv2Array, modelo_maquinaRv2Array, potenciaMaxima_maquinaRv2Array, tarifaMensal_maquinaRv2Array, diarioRack_Rv2Array, mensalRack_Rv2Array, anualRack_Rv2Array))