from connection import * 
import numpy as np

labelPoolArray = []
hostArray = []
nome_vmArray = []
descr_vmArray = []
so_vmArray = []
ncpu_vmArray = []
memoria_vmArray = []
status_vmArray = []

for x in myresultServers: 
    labelPoolArray = np.append(labelPoolArray, x[0])
    hostArray = np.append(hostArray, x[1])
    nome_vmArray = np.append(nome_vmArray, x[2])
    descr_vmArray = np.append(descr_vmArray, x[3])
    so_vmArray = np.append(so_vmArray, x[4])
    ncpu_vmArray = np.append(ncpu_vmArray, x[5])
    memoria_vmArray = np.append(memoria_vmArray, x[6])
    status_vmArray = np.append(status_vmArray, x[7])

arrayServidores = np.column_stack((labelPoolArray, hostArray, nome_vmArray, descr_vmArray, so_vmArray, ncpu_vmArray, memoria_vmArray, status_vmArray))