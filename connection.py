import os
import pymysql.cursors
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from func import *

load_dotenv()

host=os.getenv('DB_HOST'),
user=os.getenv('DB_USER'),
password=os.getenv('DB_PASSWORD'),
db=os.getenv('DB_NAME')


con = pymysql.connect(host=host,database=db,user=user,password=password)
con1 = pymysql.connect(host=host,database=db,user=user,password=password)

try:    
    with con.cursor() as mycursor:
        mycursor.execute("SELECT * FROM racks_v2;")
        myresultRacks_v2 = mycursor.fetchall()
finally:
    con.close()
    
try:    
    with con1.cursor() as mycursor1:

        mycursor1.execute("SELECT * FROM egeon;")
        myresultEgeon = mycursor1.fetchall()

        mycursor1.execute("SELECT * FROM maquinas_fisicas;")
        myresultEquipamentos = mycursor1.fetchall()

        # OLINDA 
        # AGGREGATE
        mycursor1.execute("SELECT name_aggregate, fullSize_aggregate, usedSize_aggregate, availableSize_aggregate, usedCapacity_aggregate FROM aggregate WHERE nameStorage_aggregate LIKE 'OLINDA' AND name_aggregate NOT LIKE ('aggr_root_N%')")
        myresultAggregateOlinda = mycursor1.fetchall()

        # VOLUMES
        mycursor1.execute("SELECT name_volumes, full_volumes, used_volumes, available_volumes, percent_volumes, svm_volumes, department_volumes, groupDep_volumes, fullSnap_volumes, usedSnap_volumes, availableSnap_volumes, percentSnap_volumes, nameAggregate_volumes FROM volumes WHERE svm_volumes NOT IN ('calipso', 'cartosat', 'helios', 'olinda-01', 'olinda-02', 'olinda-03', 'olinda-04');")
        myresultVolumesOlinda = mycursor1.fetchall() 

        mycursor1.execute("SELECT name_volumes, full_volumes, used_volumes, available_volumes, percent_volumes, svm_volumes, department_volumes, groupDep_volumes, fullSnap_volumes, usedSnap_volumes, availableSnap_volumes, percentSnap_volumes FROM volumes WHERE svm_volumes NOT IN ('calipso', 'cartosat', 'helios', 'olinda-01', 'olinda-02', 'olinda-03', 'olinda-04');")
        myresultVolumesLandsat = mycursor1.fetchall() 

        mycursor1.execute("SELECT name_volumes, full_volumes, used_volumes, available_volumes, percent_volumes, svm_volumes, department_volumes, groupDep_volumes, fullSnap_volumes, usedSnap_volumes, availableSnap_volumes, percentSnap_volumes FROM volumes WHERE svm_volumes NOT IN ('calipso', 'cartosat', 'helios', 'olinda-01', 'olinda-02', 'olinda-03', 'olinda-04');")
        myresultVolumesAmazonia = mycursor1.fetchall()

        # LANDSAT 
        # AGGREGATE
        mycursor1.execute("SELECT name_aggregate, fullSize_aggregate, usedSize_aggregate, availableSize_aggregate, usedCapacity_aggregate FROM aggregate WHERE nameStorage_aggregate LIKE 'LANDSAT'")
        myresultAggregateLandsat = mycursor1.fetchall()

        # # AMAZONIA 
        # # AGGREGATE
        # mycursor1.execute("SELECT name_aggregate, fullSize_aggregate, usedSize_aggregate, availableSize_aggregate, usedCapacity_aggregate FROM aggregate WHERE nameStorage_aggregate LIKE 'AMAZONIA' AND name_aggregate NOT LIKE ('aggr0_root_0%')")
        # myresultAggregateAmazonia = mycursor1.fetchall()

        mycursor1.execute("SELECT DISTINCT department_volumes FROM volumes WHERE department_volumes NOT IN ('root', 'vol0', 'junctionpaths', 'int', '');")
        myresultDivisoes = mycursor1.fetchall() 
finally:
    con1.close()


def searchVolDiv(divisao):
    totalDivOlinda = int(0)
    UsadoDivOlinda = int(0)
    DisponivelDivOlinda = int(0)
    arrayDivName = []
    arraysizeDiv = []
    arrayuseDiv = [] 
    arrayavaDiv = [] 
    arraypercDiv = []

    con = pymysql.connect(host='mansidao.cptec.inpe.br',database='dash',user='dashboard',password='dash.q1w2e3r4')
    mycursor2 = con.cursor() 
    query = ("SELECT full_volumes, name_volumes, used_volumes, available_volumes, percent_volumes FROM volumes WHERE department_volumes='{}';").format(divisao)
    mycursor2.execute(query)
    volDivis = mycursor2.fetchall() 
    mycursor2.close()

    count = 0

    for x in volDivis:
        count = count +1
        sizeDiv=x[0]
        nameDiv=x[1]        
        usedDiv=x[2]
        avaiDiv=x[3]
        percentDiv1=x[4]
        percentDiv=int(percentDiv1)

        # Total
        c = format_bytes(x[0])
        resultConversion = converter(c)
        resultConversion = str(resultConversion)
        defUni = c[1]
        resultTotalConversion=str(resultConversion + " " + defUni)

        # Usado
        c = format_bytes(x[2])
        resultConversion = converter(c)
        resultConversion = str(resultConversion)
        defUni = c[1]
        percUsadoVolumes = str(percentDiv)
        resultUsedConversion=str(resultConversion + " " + defUni + " " + " - " + percUsadoVolumes + "%")

        # Disponivel
        c = format_bytes(x[3])
        resultConversion = converter(c)
        resultConversion = str(resultConversion)
        defUni = c[1]
        percDisponivelVolumes = 100 - percentDiv
        percDisponivelVolumes = str(percDisponivelVolumes)
        resultDisponivelConversion=str(resultConversion + " " + defUni + " " + " - " + percDisponivelVolumes + "%")

        arraysizeDiv = np.append(arraysizeDiv, resultTotalConversion)
        arrayuseDiv = np.append(arrayuseDiv, resultUsedConversion)
        arrayavaDiv = np.append(arrayavaDiv, resultDisponivelConversion)
        arraypercDiv = np.append(arraypercDiv, percentDiv)
        arrayDivName = np.append(arrayDivName, nameDiv)

        totalDivOlinda = totalDivOlinda + sizeDiv
        UsadoDivOlinda = UsadoDivOlinda + usedDiv
        DisponivelDivOlinda = DisponivelDivOlinda + avaiDiv

    # print(divisao)
    # print(totalDivOlinda)
    
    arrayFullDiv = np.column_stack((arrayDivName, arraysizeDiv, arrayuseDiv, arrayavaDiv))
    # print(teste)
    return totalDivOlinda, count, arrayFullDiv, UsadoDivOlinda, DisponivelDivOlinda


def searchVolAgg(aggr):#,sizeAggOlindaArray, usedAggOlindaArray, dispoAggOlindaArray, percAggOlindaArray):
    
    global arrayvolDiv
    global tamName 
    arrayvolName=[]
    global nameAgg
    nameAgg=[]
    global namevolAgg
    namevolAgg=[]
    global volfullAgg
    volfullAgg=[]
    global volusedAgg
    volusedAgg=[]
    global volavaAgg   
    volavaAgg=[]
    global percvolAgg
    percvolAgg=[]
    global volDivAgg
    volDivAgg=[]
    
    con2 = pymysql.connect(host='mansidao.cptec.inpe.br',database='dash',user='dashboard',password='dash.q1w2e3r4')
    mycursor2 = con2.cursor() 
    query = ("SELECT name_volumes, full_volumes, department_volumes, used_volumes, available_volumes, percent_volumes FROM volumes WHERE nameAggregate_volumes='{}';").format(aggr)
    mycursor2.execute(query)
    volAggr = mycursor2.fetchall() 
    mycursor2.close()

    # print(volAggr)
    for name in volAggr:
        vol=name[0]
        tamanhofull=name[1]
        div=name[2]
        div=div.upper()
        tamanhoused=name[3]
        tamanhoava=name[4]
        percused=str(name[5])
        tamanhofbfull=format_bytes(tamanhofull)
        tamanhofbcfull=converter(tamanhofbfull)
        tamanhofull=str(tamanhofbcfull)
        tamanhofull= tamanhofull + " " + tamanhofbfull[1]

        tamanhofbused=format_bytes(tamanhoused)
        tamanhofbcused=converter(tamanhofbused)
        tamanhoused=str(tamanhofbcused)
        tamanhoused= tamanhoused + " " + tamanhofbused[1]

        tamanhofbava=format_bytes(tamanhoava)
        tamanhofbcava=converter(tamanhofbava)
        tamanhoava=str(tamanhofbcava)
        tamanhoava= tamanhoava + " " + tamanhofbava[1]

        nameAgg = np.append(nameAgg, aggr)
        namevolAgg = np.append(namevolAgg, vol)
        volfullAgg = np.append(volfullAgg, tamanhofull)
        volusedAgg = np.append(volusedAgg, tamanhoused)
        volavaAgg = np.append(volavaAgg, tamanhoava)
        percvolAgg = np.append(percvolAgg, percused)
        volDivAgg = np.append(volDivAgg, div)


        # tamName=aggr + "-" + vol + "-" + tamanhofull + "-" + tamanhoused + "-" + tamanhoava + "-" + percused + "%-" + div

        arrayvolName = np.column_stack((nameAgg,namevolAgg,volfullAgg,volusedAgg,volavaAgg,percvolAgg,volDivAgg))
        # print(arrayvolName)

    # print(arrayvolName)
    return arrayvolName


# + sizeAggOlindaArray + "-" usedAggOlindaArray + "-" dispoAggOlindaArray + "-" percAggOlindaArray + "-" 
