from connection import * 
import numpy as np

rackArray = []
nomeArray = []
marca_maquinaArray = []
modelo_maquinaArray = []
responsavel_maquinaArray = []
# status_maquinaArray = []
servicetag_maquinaArray = []
statusgarantia_maquinaArray = []
datagarantia_maquinaArray = []
patrimonio_maquinaArray = []
detentor_maquinaArray = []
processadores_maquinaArray = []
potenciaMaxima_maquinaArray = []
tarifaMensal_maquinaArray = []
tarifaDiaria_maquinaArray = []
tarifaAnual_maquinaArray = []

for x in myresultEquipamentos: 
    rackArray = np.append(rackArray, x[0])
    nomeArray = np.append(nomeArray, x[1])
    marca_maquinaArray = np.append(marca_maquinaArray, x[2])
    modelo_maquinaArray = np.append(modelo_maquinaArray, x[3])
    responsavel_maquinaArray = np.append(responsavel_maquinaArray, x[4])
    # status_maquinaArray = np.append(status_maquinaArray, x[5])
    servicetag_maquinaArray = np.append(servicetag_maquinaArray, x[5])
    statusgarantia_maquinaArray = np.append(statusgarantia_maquinaArray, x[6])
    datagarantia_maquinaArray = np.append(datagarantia_maquinaArray, x[7])
    patrimonio_maquinaArray = np.append(patrimonio_maquinaArray, x[8])
    detentor_maquinaArray = np.append(detentor_maquinaArray, x[9])
    # processadores_maquinaArray = np.append(processadores_maquinaArray, x[10])
    # potenciaMaxima_maquinaArray = np.append(potenciaMaxima_maquinaArray, x[11])
    tarifaDiaria_maquinaArray = np.append(tarifaDiaria_maquinaArray, x[12])
    tarifaMensal_maquinaArray = np.append(tarifaMensal_maquinaArray, x[13])
    tarifaAnual_maquinaArray = np.append(tarifaAnual_maquinaArray, x[14])

# arrayEquipamentos = np.column_stack((rackArray, nomeArray, marca_maquinaArray, modelo_maquinaArray, responsavel_maquinaArray, servicetag_maquinaArray, statusgarantia_maquinaArray, datagarantia_maquinaArray, patrimonio_maquinaArray, detentor_maquinaArray, processadores_maquinaArray, potenciaMaxima_maquinaArray, tarifaDiaria_maquinaArray, tarifaMensal_maquinaArray, tarifaAnual_maquinaArray))

arrayEquipamentos = np.column_stack((rackArray, nomeArray, marca_maquinaArray, modelo_maquinaArray, responsavel_maquinaArray, servicetag_maquinaArray, statusgarantia_maquinaArray, datagarantia_maquinaArray, patrimonio_maquinaArray, detentor_maquinaArray, tarifaDiaria_maquinaArray, tarifaMensal_maquinaArray, tarifaAnual_maquinaArray))