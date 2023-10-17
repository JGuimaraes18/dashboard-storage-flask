import numpy as np
import plotly.express  as  px 
from connection import * 
from dataframe_Divisoes import *
from func import *
import os

############################################### AGGREGATES ###############################################
                                    ############ - OLINDA - ############

somaLiqOlinda = int(0)
usedTotalOlinda = int(0)
dispoTotalOlinda = int(0)

nameAggOlindaArray = []
sizeAggOlindaArray = []
usedAggOlindaArray = []
dispoAggOlindaArray = []
percAggOlindaArray =[]

for agg in myresultAggregateOlinda:
    # Cria arrays para tratar os aggregates da Olinda
    # Nome dos Aggregates
    nameAggOlindaArray = np.append(nameAggOlindaArray, agg[0])
    
    # Tamanho Total
    sizeAgg = agg[1]
    c = format_bytes(sizeAgg)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    # resultConversion=str(resultConversion + " " + defUni)
    resultConversion=str(resultConversion)
    sizeAggOlindaArray = np.append(sizeAggOlindaArray, resultConversion)
    
    # Tamanho Usado
    usedAgg = agg[2]
    c = format_bytes(usedAgg)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    # resultConversion=str(resultConversion + " " + defUni)
    resultConversion=str(resultConversion)
    usedAggOlindaArray = np.append(usedAggOlindaArray, resultConversion)
    
    # Tamanho Disponivel
    dispoAgg = agg[3]
    c = format_bytes(dispoAgg)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    # resultConversion=str(resultConversion + " " + defUni)
    resultConversion=str(resultConversion)
    dispoAggOlindaArray = np.append(dispoAggOlindaArray, resultConversion)

    # Porcentagem Usada
    percAggOlindaArray = np.append(percAggOlindaArray, agg[4]) 

    # Somatoria dos Aggregates
    somaLiqOlinda = sizeAgg + somaLiqOlinda # Total
    usedTotalOlinda = usedAgg + usedTotalOlinda # Usado
    dispoTotalOlinda = dispoAgg + dispoTotalOlinda # Disponivel

# Montagem do Array dos Aggregates
arrayAggregatesOlinda = np.column_stack((nameAggOlindaArray, sizeAggOlindaArray, usedAggOlindaArray, dispoAggOlindaArray, percAggOlindaArray))

# Gera Porcentagem Usada e Disponivel
percentUsedConvertedOlinda = percVol(usedTotalOlinda, somaLiqOlinda)

percentDispoConvertedOlinda = percVol(dispoTotalOlinda, somaLiqOlinda)

# Formata valores de Byte para GB/TB/PB
fbTotalOlinda = format_bytes(somaLiqOlinda)
Unitliquid = fbTotalOlinda[1]
capacityLiqOlinda = converter(fbTotalOlinda)

fbUsadoOlinda = format_bytes(usedTotalOlinda)
UnitUsado = fbUsadoOlinda[1]
capacityUsadoOlinda = converter(fbUsadoOlinda)

fbDispOlinda = format_bytes(dispoTotalOlinda)
UnitDisponivel = fbDispOlinda[1]
capacityDisponivelOlinda = converter(fbDispOlinda)


### TESTE
arraymergeAggrOlinda = []

for a in nameAggOlindaArray:
    aggr = a.upper()
    volAggr = searchVolAgg(aggr)

######################PARAMOS AQUI ...TENTANDO IMPRIMIR OS VOLUMES ############333
    arraymergeAggrOlinda=np.append(arraymergeAggrOlinda, volAggr)

# print(volAggr)
# print(arraymergeAggrOlinda)
# print(arraymergeAggrOlinda)

# for teste in arraymergeAggrOlinda:
#     teste1=teste.rsplit(" - ")
#     # print(teste[1])
#     teste2 = np.append(teste2, teste1) 
    # teste1=np.append(teste1, teste)
# print(teste2)

                                    ####################################

                                    ########### - LANDSAT - ############

somaLiqLandsat = int(0)
usedTotalLandsat = int(0)
dispoTotalLandsat = int(0)

nameAggLandsatArray = []
sizeAggLandsatArray = []
usedAggLandsatArray = []
dispoAggLandsatArray = []
percAggLandsatArray =[]

for agg in myresultAggregateLandsat:
    # Cria arrays para tratar os aggregates da Landsat
    # Nome dos Aggregates
    nameAggLandsatArray = np.append(nameAggLandsatArray, agg[0])
    
    # Tamanho Total
    sizeAgg = agg[1]
    c = format_bytes(sizeAgg)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    resultConversion=str(resultConversion + " " + defUni)
    sizeAggLandsatArray = np.append(sizeAggLandsatArray, resultConversion)
    
    # Tamanho Usado
    usedAgg = agg[2]
    c = format_bytes(usedAgg)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    resultConversion=str(resultConversion + " " + defUni)
    usedAggLandsatArray = np.append(usedAggLandsatArray, resultConversion)
    
    # Tamanho Disponivel
    dispoAgg = agg[3]
    c = format_bytes(dispoAgg)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    resultConversion=str(resultConversion + " " + defUni)
    dispoAggLandsatArray = np.append(dispoAggLandsatArray, resultConversion)

    # Porcentagem Usada
    percAggLandsatArray = np.append(percAggLandsatArray, agg[4]) 

    # Somatoria dos Aggregates
    somaLiqLandsat= sizeAgg + somaLiqLandsat # Total
    usedTotalLandsat = usedAgg + usedTotalLandsat # Usado
    dispoTotalLandsat = dispoAgg + dispoTotalLandsat # Disponivel

# Montagem do Array dos Aggregates
arrayAggregatesLandsat = np.column_stack((nameAggLandsatArray, sizeAggLandsatArray, usedAggLandsatArray, dispoAggLandsatArray, percAggLandsatArray))

ArrayGeralNameAgg = np.append(nameAggOlindaArray, nameAggLandsatArray)
ArrayGeralSizeAgg = np.append(sizeAggOlindaArray, sizeAggLandsatArray)
ArrayGeralUsedAgg = np.append(usedAggOlindaArray, usedAggLandsatArray)
ArrayGeralDispoAgg = np.append(dispoAggOlindaArray, dispoAggLandsatArray)
ArrayGeralPercAgg = np.append(percAggOlindaArray, percAggLandsatArray)

ArrayGeralAggregate = np.column_stack((ArrayGeralNameAgg, ArrayGeralSizeAgg, ArrayGeralUsedAgg, ArrayGeralDispoAgg, ArrayGeralPercAgg))

# Gera Porcentagem Usada e Disponivel
percentUsedConvertedLandsat = percVol(usedTotalLandsat, somaLiqLandsat)

percentDispoConvertedLandsat = percVol(dispoTotalLandsat, somaLiqLandsat)

# Formata valores de Byte para GB/TB/PB
fbTotalLandsat = format_bytes(somaLiqLandsat)
Unitliquid = fbTotalLandsat[1]
capacityLiqLandsat = converter(fbTotalLandsat)

fbUsadoLandsat = format_bytes(usedTotalLandsat)
UnitUsado = fbUsadoLandsat[1]
capacityUsadoLandsat = converter(fbUsadoLandsat)

fbDispLandsat = format_bytes(dispoTotalLandsat)
UnitDisponivel = fbDispLandsat[1]
capacityDisponivelLandsat = converter(fbDispLandsat)

# SOMATORIA TOTAL OLINDA E LANDSAT
somatoriaStorage= somaLiqOlinda + somaLiqLandsat
fbSomatoriaStorage = format_bytes(somatoriaStorage)
UnitSomatoriaTotalSotage = fbSomatoriaStorage[1]
somatoriaTotalStorage = converter(fbSomatoriaStorage)
TotalAggregate = str(somatoriaTotalStorage) + ' ' + UnitSomatoriaTotalSotage

# USADO TOTAL OLINDA E LANDSAT
usedStorage= usedTotalOlinda + usedTotalLandsat
fbusedStorage = format_bytes(usedStorage)
UnitusedTotalSotage = fbusedStorage[1]
usedTotalStorage = converter(fbusedStorage)
UsedAggregate = str(usedTotalStorage) + ' ' + UnitusedTotalSotage

# DISPONIBILIDADE TOTAL OLINDA E LANDSAT
dispoStorage= dispoTotalOlinda + dispoTotalLandsat
fbdispoStorage = format_bytes(dispoStorage)
UnitdispoTotalSotage = fbdispoStorage[1]
dispoTotalStorage = converter(fbdispoStorage)
DispoAggregate = str(dispoTotalStorage) + ' ' + UnitdispoTotalSotage


############################### - FULL AGGREGATES - ######################


                                    ####################################

                                    ########## - AMAZONIA - ############

# somaLiqAmazonia = int(0)
# usedTotalAmazonia = int(0)
# dispoTotalAmazonia = int(0)

# nameAggAmazoniaArray = []
# sizeAggAmazoniaArray = []
# usedAggAmazoniaArray = []
# dispoAggAmazoniaArray = []
# percAggAmazoniaArray =[]

# for agg in myresultAggregateAmazonia:
#     # Cria arrays para tratar os aggregates da Landsat
#     # Nome dos Aggregates
#     nameAggAmazoniaArray = np.append(nameAggAmazoniaArray, agg[0])
    
#     # Tamanho Total
#     sizeAgg = agg[1]
#     c = format_bytes(sizeAgg)
#     conversion = c[1]
#     resultConversion = converter(c)
#     resultConversion = str(resultConversion)
#     defUni = c[1]
#     resultConversion=str(resultConversion + " " + defUni)
#     sizeAggAmazoniaArray = np.append(sizeAggAmazoniaArray, resultConversion)
    
#     # Tamanho Usado
#     usedAgg = agg[2]
#     c = format_bytes(usedAgg)
#     conversion = c[1]
#     resultConversion = converter(c)
#     resultConversion = str(resultConversion)
#     defUni = c[1]
#     resultConversion=str(resultConversion + " " + defUni)
#     usedAggAmazoniaArray = np.append(usedAggAmazoniaArray, resultConversion)
    
#     # Tamanho Disponivel
#     dispoAgg = agg[3]
#     c = format_bytes(dispoAgg)
#     conversion = c[1]
#     resultConversion = converter(c)
#     resultConversion = str(resultConversion)
#     defUni = c[1]
#     resultConversion=str(resultConversion + " " + defUni)
#     dispoAggAmazoniaArray = np.append(dispoAggAmazoniaArray, resultConversion)

#     # Porcentagem Usada
#     percAggAmazoniaArray = np.append(percAggAmazoniaArray, agg[4]) 

#     # Somatoria dos Aggregates
#     somaLiqAmazonia= sizeAgg + somaLiqAmazonia # Total
#     usedTotalAmazonia = usedAgg + usedTotalAmazonia # Usado
#     dispoTotalAmazonia = dispoAgg + dispoTotalAmazonia # Disponivel

# # Montagem do Array dos Aggregates
# arrayAggregatesAmazonia = np.column_stack((nameAggAmazoniaArray, sizeAggAmazoniaArray, usedAggAmazoniaArray, dispoAggAmazoniaArray, percAggAmazoniaArray))

# # Gera Porcentagem Usada e Disponivel
# percentUsedConvertedAmazonia = percVol(usedTotalAmazonia, somaLiqAmazonia)

# percentDispoConvertedAmazonia = percVol(dispoTotalAmazonia, somaLiqAmazonia)

# # Formata valores de Byte para GB/TB/PB
# fbTotalAmazonia = format_bytes(somaLiqAmazonia)
# Unitliquid = fbTotalAmazonia[1]
# capacityLiqAmazonia = converter(fbTotalAmazonia)

# fbUsadoAmazonia = format_bytes(usedTotalAmazonia)
# UnitUsado = fbUsadoAmazonia[1]
# capacityUsadoAmazonia = converter(fbUsadoAmazonia)

# fbDispAmazonia = format_bytes(dispoTotalAmazonia)
# UnitDisponivel = fbDispAmazonia[1]
# capacityDisponivelAmazonia = converter(fbDispAmazonia)
##########################################################################################################

################################################# VOLUMES ################################################
                                    ########## - OLINDA - ############

# Declara Array
nameArrayOlinda = []
sizeArrayOlinda = []
usedArrayOlinda = []
avaArrayOlinda = []
departArrayOlinda = []
plotgraficoOlinda = []

# Define Dados 
for v in myresultVolumesOlinda:
    # Nome Volumes
    nameArrayOlinda = np.append(nameArrayOlinda,v[0])
    
    # Volume Total
    volumeTotal = v[1]
    c = format_bytes(volumeTotal)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    resultConversion=str(resultConversion + " " + defUni)
    sizeArrayOlinda = np.append(sizeArrayOlinda, resultConversion)
        
    # Volume Usado 
    volumeUsado = v[2]
    c = format_bytes(volumeUsado)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    percUsadoVolumes = str(v[4])
    resultConversion=str(resultConversion + " " + defUni + " " + " - " + percUsadoVolumes + "%")
    usedArrayOlinda = np.append(usedArrayOlinda, resultConversion)
    
    # Array da Porcentagem Usada para Grafico
    percInt = int(percUsadoVolumes)
    plotgraficoOlinda = np.append(plotgraficoOlinda, percInt)
    
    # Volume Disponivel 
    volumeDisponivel = v[3]
    c = format_bytes(volumeDisponivel)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    percDisponivelVolumes = 100 - v[4]
    percDisponivelVolumes = str(percDisponivelVolumes)
    resultConversion=str(resultConversion + " " + defUni + " " + " - " + percDisponivelVolumes + "%")
    avaArrayOlinda = np.append(avaArrayOlinda, resultConversion)
    
    # Array de Grupos 
    nomeDepart = v[6].upper()
    departArrayOlinda = np.append(departArrayOlinda, nomeDepart)

# Gera Array de Todas as Informacoes
arrayVolumesOlinda = np.column_stack((nameArrayOlinda, departArrayOlinda, sizeArrayOlinda, usedArrayOlinda, avaArrayOlinda))

# Define variaveis para SOMA dos VALORES do storage
somaSOlinda= int(0)
somaUOlinda = int(0)
somaAOlinda = int(0)
somaS_snapOlinda = int(0)
somaU_snapOlinda = int(0)
somaA_snapOlinda = int(0)

for x in myresultVolumesOlinda: 
    # Valor total
    size = x[1]
    somaSOlinda = somaSOlinda + size
    c = format_bytes(size)
    conversion = c[1]
    result = converter(c)
    
    # Valor usado
    used = x[2]
    somaUOlinda = somaUOlinda + used
    c = format_bytes(used)
    conversion = c[1]
    result = converter(c)
    
    # Valor disponível
    ava = x[3]
    somaAOlinda = somaAOlinda + ava
    c = format_bytes(ava)
    conversion = c[1]
    result = converter(c)
    
    # --------------------------------------------------------
    
    # Valor total SNAP
    sizeSnap = x[8]
    somaS_snapOlinda = somaS_snapOlinda + sizeSnap
    c = format_bytes(sizeSnap)
    conversion = c[1]
    result = converter(c)
    
    # Valor usado SNAP
    usedSnap = x[9]
    somaU_snapOlinda = somaU_snapOlinda + usedSnap
    c = format_bytes(usedSnap)
    conversion = c[1]
    result = converter(c)
    
    # Valor disponível SNAP
    avaSnap = x[10]
    somaA_snapOlinda = somaA_snapOlinda + avaSnap
    c = format_bytes(avaSnap)
    conversion = c[1]
    result = converter(c)
    
# Volumes
totalSOlinda = format_bytes(somaSOlinda)
totalUOlinda = format_bytes(somaUOlinda)
totalAOlinda = format_bytes(somaAOlinda)
convertTotalSOlinda = converter(totalSOlinda)
convertTotalUOlinda = converter(totalUOlinda)
convertTotalAOlinda = converter(totalAOlinda)

# print(somaSOlinda)

# SNAPs
totalS_snapOlinda = format_bytes(somaS_snapOlinda)
totalU_snapOlinda = format_bytes(somaU_snapOlinda)
totalA_snapOlinda = format_bytes(somaA_snapOlinda)
convertTotalS_snapOlinda = converter(totalS_snapOlinda)
convertTotalU_snapOlinda = converter(totalU_snapOlinda)
convertTotalA_snapOlinda = converter(totalA_snapOlinda)

# Soma dos dados
totalDadosArmz = somaSOlinda + somaS_snapOlinda
totalDadosArmz_Fb = format_bytes(totalDadosArmz)
totalDadosArmz_FbC = converter(totalDadosArmz_Fb)

# Subtração dos dados
totalDispoArmz = somaLiqOlinda - totalDadosArmz
totalDispoArmz_Fb = format_bytes(totalDispoArmz)
totalDispoArmz_FbC = converter(totalDispoArmz_Fb)

##########################################################################################################
                                    ########## - LANDSAT - ############

# Declara Array
nameArrayLandsat = []
sizeArrayLandsat = []
usedArrayLandsat = []
avaArrayLandsat = []
departArrayLandsat = []
plotgraficoLandsat = []

# Define Dados 
for v in myresultVolumesLandsat:
    # Nome Volumes
    nameArrayLandsat = np.append(nameArrayLandsat,v[0])
    
    # Volume Total
    volumeTotal = v[1]
    c = format_bytes(volumeTotal)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    resultConversion=str(resultConversion + " " + defUni)
    sizeArrayLandsat = np.append(sizeArrayLandsat, resultConversion)
        
    # Volume Usado 
    volumeUsado = v[2]
    c = format_bytes(volumeUsado)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    percUsadoVolumes = str(v[4])
    resultConversion=str(resultConversion + " " + defUni + " " + " - " + percUsadoVolumes + "%")
    usedArrayLandsat = np.append(usedArrayLandsat, resultConversion)
    
    # Array da Porcentagem Usada para Grafico
    percInt = int(percUsadoVolumes)
    plotgraficoLandsat = np.append(plotgraficoLandsat, percInt)
    
    # Volume Disponivel 
    volumeDisponivel = v[3]
    c = format_bytes(volumeDisponivel)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    percDisponivelVolumes = 100 - v[4]
    percDisponivelVolumes = str(percDisponivelVolumes)
    resultConversion=str(resultConversion + " " + defUni + " " + " - " + percDisponivelVolumes + "%")
    avaArrayLandsat = np.append(avaArrayLandsat, resultConversion)
    
    # Array de Grupos 
    nomeDepart = v[6].upper()
    departArrayLandsat = np.append(departArrayLandsat, nomeDepart)

# Gera Array de Todas as Informacoes
arrayVolumesLandsat = np.column_stack((nameArrayLandsat, departArrayLandsat, sizeArrayLandsat, usedArrayLandsat, avaArrayLandsat))

# Define variaveis para SOMA dos VALORES do storage
somaSLandsat= int(0)
somaULandsat = int(0)
somaALandsat = int(0)
somaS_snapLandsat = int(0)
somaU_snapLandsat = int(0)
somaA_snapLandsat = int(0)

for x in myresultVolumesLandsat: 
    # Valor total
    size = x[1]
    somaSLandsat = somaSLandsat + size
    c = format_bytes(size)
    conversion = c[1]
    result = converter(c)
    
    # Valor usado
    used = x[2]
    somaULandsat = somaULandsat + used
    c = format_bytes(used)
    conversion = c[1]
    result = converter(c)
    
    # Valor disponível
    ava = x[3]
    somaALandsat = somaALandsat + ava
    c = format_bytes(ava)
    conversion = c[1]
    result = converter(c)
    
    # --------------------------------------------------------
    
    # Valor total SNAP
    sizeSnap = x[8]
    somaS_snapLandsat = somaS_snapLandsat + sizeSnap
    c = format_bytes(sizeSnap)
    conversion = c[1]
    result = converter(c)
    
    # Valor usado SNAP
    usedSnap = x[9]
    somaU_snapLandsat = somaU_snapLandsat + usedSnap
    c = format_bytes(usedSnap)
    conversion = c[1]
    result = converter(c)
    
    # Valor disponível SNAP
    avaSnap = x[10]
    somaA_snapLandsat = somaA_snapLandsat + avaSnap
    c = format_bytes(avaSnap)
    conversion = c[1]
    result = converter(c)
    
# Volumes
totalSLandsat = format_bytes(somaSLandsat)
totalULandsat = format_bytes(somaULandsat)
totalALandsat = format_bytes(somaALandsat)
convertTotalSLandsat = converter(totalSLandsat)
convertTotalULandsat = converter(totalULandsat)
convertTotalALandsat = converter(totalALandsat)

# SNAPs
totalS_snapLandsat = format_bytes(somaS_snapLandsat)
totalU_snapLandsat = format_bytes(somaU_snapLandsat)
totalA_snapLandsat = format_bytes(somaA_snapLandsat)
convertTotalS_snapLandsat = converter(totalS_snapLandsat)
convertTotalU_snapLandsat = converter(totalU_snapLandsat)
convertTotalA_snapLandsat = converter(totalA_snapLandsat)

# Soma dos dados
totalDadosArmz = somaSLandsat + somaS_snapLandsat
totalDadosArmz_Fb = format_bytes(totalDadosArmz)
totalDadosArmz_FbC = converter(totalDadosArmz_Fb)

# Subtração dos dados
totalDispoArmz = somaLiqLandsat - totalDadosArmz
totalDispoArmz_Fb = format_bytes(totalDispoArmz)
totalDispoArmz_FbC = converter(totalDispoArmz_Fb)

##########################################################################################################
                                    ########### - AMAZONIA - ###########

# Declara Array
nameArrayAmazonia = []
sizeArrayAmazonia = []
usedArrayAmazonia = []
avaArrayAmazonia = []
departArrayAmazonia = []
plotgraficoAmazonia = []

# Define Dados 
for v in myresultVolumesAmazonia:
    # Nome Volumes
    nameArrayAmazonia = np.append(nameArrayAmazonia,v[0])
    
    # Volume Total
    volumeTotal = v[1]
    c = format_bytes(volumeTotal)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    resultConversion=str(resultConversion + " " + defUni)
    sizeArrayAmazonia = np.append(sizeArrayAmazonia, resultConversion)
        
    # Volume Usado 
    volumeUsado = v[2]
    c = format_bytes(volumeUsado)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    percUsadoVolumes = str(v[4])
    resultConversion=str(resultConversion + " " + defUni + " " + " - " + percUsadoVolumes + "%")
    usedArrayAmazonia = np.append(usedArrayAmazonia, resultConversion)
    
    # Array da Porcentagem Usada para Grafico
    percInt = int(percUsadoVolumes)
    plotgraficoAmazonia = np.append(plotgraficoAmazonia, percInt)
    
    # Volume Disponivel 
    volumeDisponivel = v[3]
    c = format_bytes(volumeDisponivel)
    conversion = c[1]
    resultConversion = converter(c)
    resultConversion = str(resultConversion)
    defUni = c[1]
    percDisponivelVolumes = 100 - v[4]
    percDisponivelVolumes = str(percDisponivelVolumes)
    resultConversion=str(resultConversion + " " + defUni + " " + " - " + percDisponivelVolumes + "%")
    avaArrayAmazonia = np.append(avaArrayAmazonia, resultConversion)
    
    # Array de Grupos 
    nomeDepart = v[6].upper()
    departArrayAmazonia = np.append(departArrayAmazonia, nomeDepart)

# Gera Array de Todas as Informacoes
arrayVolumesAmazonia = np.column_stack((nameArrayAmazonia, departArrayAmazonia, sizeArrayAmazonia, usedArrayAmazonia, avaArrayAmazonia))

# Define variaveis para SOMA dos VALORES do storage
somaSAmazonia= int(0)
somaUAmazonia = int(0)
somaAAmazonia = int(0)
somaS_snapAmazonia = int(0)
somaU_snapAmazonia = int(0)
somaA_snapAmazonia = int(0)

for x in myresultVolumesAmazonia: 
    # Valor total
    size = x[1]
    somaSAmazonia = somaSAmazonia + size
    c = format_bytes(size)
    conversion = c[1]
    result = converter(c)
    
    # Valor usado
    used = x[2]
    somaUAmazonia = somaUAmazonia + used
    c = format_bytes(used)
    conversion = c[1]
    result = converter(c)
    
    # Valor disponível
    ava = x[3]
    somaAAmazonia = somaAAmazonia + ava
    c = format_bytes(ava)
    conversion = c[1]
    result = converter(c)
    
    # --------------------------------------------------------
    
    # Valor total SNAP
    sizeSnap = x[8]
    somaS_snapAmazonia = somaS_snapAmazonia + sizeSnap
    c = format_bytes(sizeSnap)
    conversion = c[1]
    result = converter(c)
    
    # Valor usado SNAP
    usedSnap = x[9]
    somaU_snapAmazonia = somaU_snapAmazonia + usedSnap
    c = format_bytes(usedSnap)
    conversion = c[1]
    result = converter(c)
    
    # Valor disponível SNAP
    avaSnap = x[10]
    somaA_snapAmazonia = somaA_snapAmazonia + avaSnap
    c = format_bytes(avaSnap)
    conversion = c[1]
    result = converter(c)
    
# Volumes
totalSAmazonia = format_bytes(somaSAmazonia)

totalUAmazonia = format_bytes(somaUAmazonia)
totalAAmazonia = format_bytes(somaAAmazonia)
convertTotalSAmazonia = converter(totalSAmazonia)
convertTotalUAmazonia = converter(totalUAmazonia)
convertTotalAAmazonia = converter(totalAAmazonia)

# SNAPs
totalS_snapAmazonia = format_bytes(somaS_snapAmazonia)
totalU_snapAmazonia = format_bytes(somaU_snapAmazonia)
totalA_snapAmazonia = format_bytes(somaA_snapAmazonia)
convertTotalS_snapAmazonia = converter(totalS_snapAmazonia)
convertTotalU_snapAmazonia = converter(totalU_snapAmazonia)
convertTotalA_snapAmazonia = converter(totalA_snapAmazonia)

# Soma dos dados
totalDadosArmz = somaSAmazonia + somaS_snapAmazonia
totalDadosArmz_Fb = format_bytes(totalDadosArmz)
totalDadosArmz_FbC = converter(totalDadosArmz_Fb)

# # Subtração dos dados
# totalDispoArmz = somaLiqAmazonia - totalDadosArmz
# totalDispoArmz_Fb = format_bytes(totalDispoArmz)
# totalDispoArmz_FbC = converter(totalDispoArmz_Fb)



################################################ DIVISOES ################################################

arrayDivOlinda = []
arrayTotalmergeDivOlinda = []
arrayUsadomergeDivOlinda = []
arrayDisponivelmergeDivOlinda = []

volumesDiv = []
somaTotalOlinda=int(0)
somaUsadoOlinda=int(0)
somaDisponivelOlinda=int(0)


# Creating the HTML file
varDiv = 'templates/teste.html'
if os.path.exists(varDiv):
    os.remove(varDiv)

file_html = open(varDiv, "a")

for d in myresultDivisoes:
    divOlinda = d[0].upper()
    arrayDivOlinda = np.append(arrayDivOlinda, divOlinda)
    somaForDiv = searchVolDiv(divOlinda)
    somaForDiv1 = str(somaForDiv[1])
    volumesForDiv = somaForDiv[2]

    somaTotalOlinda=somaTotalOlinda + somaForDiv[0]
    somaUsadoOlinda=somaUsadoOlinda + somaForDiv[3]
    somaDisponivelOlinda=somaDisponivelOlinda + somaForDiv[4]
    
    # Total
    somaTotalDivOlindaFB = format_bytes(somaForDiv[0])
    UnitDivTotal = somaTotalDivOlindaFB[1]
    somaTotalDivOlindaFBC = converter(somaTotalDivOlindaFB)
    somaTotalDivOlindaFBC=str(somaTotalDivOlindaFBC)
    mergeTotalDivOlinda =  somaTotalDivOlindaFBC + " " + UnitDivTotal
    arrayTotalmergeDivOlinda = np.append(arrayTotalmergeDivOlinda, mergeTotalDivOlinda)
    
    # Usado
    somaUsadoDivOlindaFB = format_bytes(somaForDiv[3])
    UnitDivUsado = somaUsadoDivOlindaFB[1]
    somaUsadoDivOlindaFBC = converter(somaUsadoDivOlindaFB)
    somaUsadoDivOlindaFBC=str(somaUsadoDivOlindaFBC)

    mergeUsadoDivOlinda =  somaUsadoDivOlindaFBC + " " + UnitDivUsado
    arrayUsadomergeDivOlinda = np.append(arrayUsadomergeDivOlinda, mergeUsadoDivOlinda)

    # Disponivel
    somaDisponivelDivOlindaFB = format_bytes(somaForDiv[4])
    UnitDivDisponivel = somaDisponivelDivOlindaFB[1]
    somaDisponivelDivOlindaFBC = converter(somaDisponivelDivOlindaFB)
    somaDisponivelDivOlindaFBC=str(somaDisponivelDivOlindaFBC)

    mergeDisponivelDivOlinda =  somaDisponivelDivOlindaFBC + " " + UnitDivDisponivel
    arrayDisponivelmergeDivOlinda = np.append(arrayDisponivelmergeDivOlinda, mergeDisponivelDivOlinda)



    table = 'table-' + divOlinda 
    table = pd.DataFrame(volumesForDiv)
    pd.set_option('colheader_justify', 'center')
    table.columns = ['Volumes', 'Total', 'Usado', 'Disponível']
    html = divOlinda
    html = generate_html_D(table, divOlinda)

    file_html.write(html)

    volumesDiv = np.append(volumesDiv, volumesForDiv)
    
file_html.close()

somaTotalOlindaFb = format_bytes(somaTotalOlinda)
unitTotalOlinda = somaTotalOlindaFb[1]
somaTotalOlindaFbC = converter(somaTotalOlindaFb)
somaTotalOlindaFbC=str(somaTotalOlindaFbC)

somaUsadoOlindaFb = format_bytes(somaUsadoOlinda)
unitUsadoOlinda = somaTotalOlindaFb[1]
somaUsadoOlindaFbC = converter(somaUsadoOlindaFb)
somaUsadoOlindaFbC=str(somaUsadoOlindaFbC)

somaDisponivelOlindaFb = format_bytes(somaDisponivelOlinda)
unitDisponivelOlinda = somaDisponivelOlindaFb[1]
somaDisponivelOlindaFbC = converter(somaDisponivelOlindaFb)
somaDisponivelOlindaFbC=str(somaDisponivelOlindaFbC)


exibeTotalOlinda = somaTotalOlindaFbC + " " + unitTotalOlinda
exibeUsadoOlinda = somaUsadoOlindaFbC + " " + unitUsadoOlinda
exibeDisponivelOlinda = somaDisponivelOlindaFbC + " " + unitDisponivelOlinda


arrayGeralDivOlinda = np.column_stack((arrayDivOlinda, arrayTotalmergeDivOlinda, arrayUsadomergeDivOlinda, arrayDisponivelmergeDivOlinda))
# arrayGeralDivOlinda = np.append(arrayDivOlinda.reshape(-1, 1), arraymergeDivOlinda.reshape(-1, 1), axis=1)

##########################################################################################################