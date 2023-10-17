import plotly.express  as  px 
import pandas as pd

from flask import Flask, render_template
from gevent.pywsgi import WSGIServer
from chart import *
from dataframe_Aggregate import *
from table_Volumes1 import *
from dataframe_Volumes import *
from table_Egeon import *
from dataframe_Egeon import *
from table_Equipamentos import *
from dataframe_Equipamentos import *
from table_Racksv2 import *
from dataframe_Racksv2 import *
from dataframe_VmAmbiente import *
from dataframe_VmsHosts import *
from dataframe_VmsCoids import *
from dataframe_NCpus import *
from dataframe_NCpusAmbiente import *
from dataframe_Cpus import *
from dataframe_MemoriaAmbiente import *
from dataframe_MemoriaHosts import *
from dataframe_MemoriaCoids import *

# from table_AmbienteVIrtual import *
# from dataframe_AmbienteVirtual import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/vmsporambiente")
def vms_por_ambiente():
    
    html_VmAmbiente = generate_html_VmAmbiente(df_VmAmbiente)

    open("templates/render_vmPorAmbiente.html", "w").write(html_VmAmbiente)
    return render_template('render_vmPorAmbiente.html')

@app.route("/vmshosts")
def vms_hosts():
    
    html_Vmshosts = generate_html_VmsHosts(df_VmsHosts)

    open("templates/render_vmsHosts.html", "w").write(html_Vmshosts)
    return render_template('render_vmsHosts.html')

@app.route("/vmscoids")
def vms_coids():
    
    html_VmsCoids = generate_html_VmsCoids(df_VmsCoids)

    open("templates/render_vmsCoids.html", "w").write(html_VmsCoids)
    return render_template('render_vmsCoids.html')

@app.route("/ncpus")
def ncpus():
    
    html_NCpus = generate_html_NCpus(df_NCpus)

    open("templates/render_nCpus.html", "w").write(html_NCpus)
    return render_template('render_nCpus.html')

@app.route("/ncpusambiente")
def ncpus_ambiente():
    
    html_NCpusAmbiente = generate_html_NCpusAmbiente(df_NCpusAmbiente)

    open("templates/render_nCpusAmbiente.html", "w").write(html_NCpusAmbiente)
    return render_template('render_nCpusAmbiente.html')

@app.route("/cpu")
def cpu():
    
    html_Cpus = generate_html_Cpus(df_Cpus)

    open("templates/render_cpus.html", "w").write(html_Cpus)
    return render_template('render_cpus.html')

@app.route("/memoriaporambiente")
def memoria_por_ambiente():
    
    html_MemoriaAmbiente = generate_html_MemoriaAmbiente(df_MemoriaAmbiente)

    open("templates/render_memoriaAmbiente.html", "w").write(html_MemoriaAmbiente)
    return render_template('render_memoriaAmbiente.html')

@app.route("/memoriahosts")
def memoria_hosts():
    
    html_MemoriaHosts = generate_html_MemoriaHosts(df_MemoriaHosts)

    open("templates/render_memoriaHosts.html", "w").write(html_MemoriaHosts)
    return render_template('render_memoriaHosts.html')

@app.route("/memoriacoids")
def memoria_coids():
    
    html_MemoriaCoids = generate_html_MemoriaCoids(df_MemoriaCoids)

    open("templates/render_memoriaCoids.html", "w").write(html_MemoriaCoids)
    return render_template('render_memoriaCoids.html')

@app.route("/divisoes")
def divisoes():

    # Gera Tabela Aggregates 
    dfAggGeral = pd.DataFrame(ArrayGeralAggregate)
    pd.set_option('colheader_justify', 'left')
    dfAggGeral.columns = ['Aggregate', 'Total', 'Usado', 'Disponível', '% Usado']



    html_G = generate_html_G(dfAggGeral, arrayGeralDivOlinda, exibeTotalOlinda, exibeUsadoOlinda, exibeDisponivelOlinda, TotalAggregate, UsedAggregate, DispoAggregate, percentUsedConvertedOlinda, percentDispoConvertedOlinda)
    

    open("templates/table_AggGeral.html", "w").write(html_G)
    return render_template('table_AggGeral.html')
    # return render_template('teste.html')

    # return render_template('table_divisoes.html', div=arrayGeralDivOlinda, total=exibeTotalOlinda, usado=exibeUsadoOlinda, disponivel=exibeDisponivelOlinda, )

# @app.route("/divisoes")
# def divisoes():
#     return render_template('table_divisoes.html', div=arrayGeralDivOlinda, total=exibeTotalOlinda, usado=exibeUsadoOlinda, disponivel=exibeDisponivelOlinda)

@app.route("/armazenamento")
def armazenamento():
    
    ############################################### - OLINDA - ##############################################

    appTipoUnidadeOlinda = fbUsadoOlinda[1]
    appTipoUnidadeDispoOlinda = fbDispOlinda[1]
    

    #  Trabalhando com Volumes
    #  Conversão de valores INT para STRING
    appConTotalS_volOlinda = str(convertTotalSOlinda)
    appConTotalU_volOlinda = str(convertTotalUOlinda)
   
    # "Conversão" de string para string dos tipos de dados
    appTipoS_volOlinda = totalSOlinda[1]
    appTipoU_volOlinda = totalUOlinda[1]
    
    #  Trabalhando com Snaps
    #  Conversão de valores INT para STRING
    appConTotalS_snapOlinda = str(convertTotalS_snapOlinda)
    appConTotalU_snapOlinda = str(convertTotalU_snapOlinda)

    
    # "Conversão" de string para string dos tipos de dados
    appTipoU_snapOlinda = totalU_snapOlinda[1]
    appTipoS_snapOlinda = totalS_snapOlinda[1]

    # Grafico Volumes
    fig = px.bar (x = nameArrayOlinda, y = plotgraficoOlinda, labels={'x': 'Volumes', 'y': 'Usado - %'}, color_discrete_sequence=px.colors.qualitative.G10,template='plotly')
    fig.update_layout(font = {'family': 'Arial','size': 12,'color': 'black'})
    fig.write_html('templates/graficoVolumesOlinda.html')

    # Grafico Geral    
    chart_Olinda = px.pie(values=[usedTotalOlinda, dispoTotalOlinda], names=['usado', 'disponível'], color_discrete_sequence=px.colors.sequential.Blackbody_r)
    chart_Olinda.write_html('templates/graficoStorageOlinda.html')

    # Gera Tabela Aggregates 
    dfAggOlinda = pd.DataFrame(arrayAggregatesOlinda)
    pd.set_option('colheader_justify', 'left')
    dfAggOlinda.columns = ['Aggregate', 'Total (TB)', 'Usado (TB)', 'Disponível (TB)', '% Usado']

    ##########################################################################################################

    ############################################### - LANDSAT - ##############################################

    appTipoUnidadeLandsat = fbUsadoLandsat[1]
    appTipoUnidadeDispoLandsat = fbDispLandsat[1]


    #  Trabalhando com Volumes
    #  Conversão de valores INT para STRING
    appConTotalS_volLandsat = str(convertTotalSLandsat)
    appConTotalU_volLandsat = str(convertTotalULandsat)
    
    # "Conversão" de string para string dos tipos de dados
    appTipoS_volLandsat = totalSLandsat[1]
    appTipoU_volLandsat = totalULandsat[1]
    
    #  Trabalhando com Snaps
    #  Conversão de valores INT para STRING
    appConTotalS_snapLandsat = str(convertTotalS_snapLandsat)
    appConTotalU_snapLandsat = str(convertTotalU_snapLandsat)

    # "Conversão" de string para string dos tipos de dados
    appTipoS_snapLandsat = totalS_snapLandsat[1]
    appTipoU_snapLandsat = totalU_snapLandsat[1]
    
    # Grafico Volumes
    fig = px.bar (x = nameArrayLandsat, y = plotgraficoLandsat, labels={'x': 'Volumes', 'y': 'Usado - %'}, color_discrete_sequence=px.colors.qualitative.G10,template='plotly')
    fig.update_layout(font = {'family': 'Arial','size': 12,'color': 'black'})
    fig.write_html('templates/graficoVolumesLandsat.html')

    # Grafico Geral    
    chart_Landsat = px.pie(values=[usedTotalLandsat, dispoTotalLandsat], names=['usado', 'disponivel'], color_discrete_sequence=px.colors.sequential.Blackbody_r) 
    chart_Landsat.write_html('templates/graficoStorageLandsat.html')

    # Gera Tabela Aggregates 
    dfAggLandsat = pd.DataFrame(arrayAggregatesLandsat)
    pd.set_option('colheader_justify', 'left')
    dfAggLandsat.columns = ['Aggregate', 'Total', 'Usado', 'Disponível', '% Usado']

    ##########################################################################################################

    ############################################### - AMAZONIA - ##############################################

    # appTipoUnidadeAmazonia = fbUsadoAmazonia[1]
    # appTipoUnidadeDispoAmazonia = fbDispAmazonia[1]
    
    #  Trabalhando com Volumes
    #  Conversão de valores INT para STRING
    appConTotalS_volAmazonia = str(convertTotalSAmazonia)
    appConTotalU_volAmazonia = str(convertTotalUAmazonia)
    
    # "Conversão" de string para string dos tipos de dados
    appTipoS_volAmazonia = totalSAmazonia[1]
    appTipoU_volAmazonia = totalUAmazonia[1]
    
    #  Trabalhando com Snaps
    #  Conversão de valores INT para STRING
    appConTotalS_snapAmazonia = str(convertTotalS_snapAmazonia)
    appConTotalU_snapAmazonia = str(convertTotalU_snapAmazonia)
    
    # "Conversão" de string para string dos tipos de dados
    appTipoS_snapAmazonia = totalS_snapAmazonia[1]
    appTipoU_snapAmazonia = totalU_snapAmazonia[1]

    # # Grafico Geral    
    # chart_Amazonia = px.pie(values=[usedTotalAmazonia, dispoTotalAmazonia], names=['usado', 'disponivel'], color_discrete_sequence=px.colors.qualitative.Light24) 
    # chart_Amazonia.write_html('templates/graficoStorageAmazonia.html')
    
    # Grafico Volumes
    fig = px.bar (x = nameArrayAmazonia, y = plotgraficoAmazonia, labels={'x': 'Volumes', 'y': 'Usado - %'}, color_discrete_sequence=px.colors.qualitative.G10,template='plotly')
    fig.update_layout(font = {'family': 'Arial','size': 12,'color': 'black'})
    fig.write_html('templates/graficoVolumesAmazonia.html')
    
    # # Gera Tabela Aggregates 
    # dfAggAmazonia = pd.DataFrame(arrayAggregatesAmazonia)
    # pd.set_option('colheader_justify', 'left')
    # dfAggAmazonia.columns = ['Aggregate', 'Total', 'Usado', 'Disponível', '% Usado']
    
    ##########################################################################################################


    # Gera HTML 
    html_Agg = generate_html_Agg(dfAggOlinda, dfAggLandsat, capacityLiqOlinda, appTipoS_volOlinda, capacityUsadoOlinda, appTipoUnidadeOlinda, percentUsedConvertedOlinda, capacityDisponivelOlinda, appTipoUnidadeDispoOlinda, percentDispoConvertedOlinda, appConTotalS_volOlinda, appConTotalS_snapOlinda, appTipoS_snapOlinda, appConTotalU_volOlinda, appTipoU_volOlinda, appConTotalU_snapOlinda, appTipoU_snapOlinda, usedTotalOlinda, dispoTotalOlinda, capacityLiqLandsat, capacityUsadoLandsat, percentUsedConvertedLandsat, capacityDisponivelLandsat,  percentDispoConvertedLandsat, usedTotalLandsat, dispoTotalLandsat, appTipoUnidadeLandsat, appTipoUnidadeDispoLandsat, appConTotalS_volLandsat, appConTotalU_volLandsat, appTipoS_volLandsat, appTipoU_volLandsat, appConTotalS_snapLandsat, appConTotalU_snapLandsat, appTipoU_snapLandsat, appTipoS_snapLandsat, appConTotalS_volAmazonia, appConTotalU_volAmazonia, appTipoS_volAmazonia, appTipoU_volAmazonia, appConTotalS_snapAmazonia, appConTotalU_snapAmazonia, appTipoS_snapAmazonia, appTipoU_snapAmazonia)

    # html_Agg = generate_html_Agg(dfAggOlinda, dfAggLandsat, dfAggAmazonia, capacityLiqOlinda, appTipoS_volOlinda, capacityUsadoOlinda, appTipoUnidadeOlinda, percentUsedConvertedOlinda, capacityDisponivelOlinda, appTipoUnidadeDispoOlinda, percentDispoConvertedOlinda, appConTotalS_volOlinda, appConTotalS_snapOlinda, appTipoS_snapOlinda, appConTotalU_volOlinda, appTipoU_volOlinda, appConTotalU_snapOlinda, appTipoU_snapOlinda, usedTotalOlinda, dispoTotalOlinda, capacityLiqLandsat, capacityUsadoLandsat, percentUsedConvertedLandsat, capacityDisponivelLandsat,  percentDispoConvertedLandsat, usedTotalLandsat, dispoTotalLandsat, appTipoUnidadeLandsat, appTipoUnidadeDispoLandsat, capacityLiqAmazonia, capacityUsadoAmazonia, percentUsedConvertedAmazonia, capacityDisponivelAmazonia, percentDispoConvertedAmazonia, usedTotalAmazonia, dispoTotalAmazonia, appTipoUnidadeAmazonia, appTipoUnidadeDispoAmazonia, appConTotalS_volLandsat, appConTotalU_volLandsat, appTipoS_volLandsat, appTipoU_volLandsat, appConTotalS_snapLandsat, appConTotalU_snapLandsat, appTipoU_snapLandsat, appTipoS_snapLandsat, appConTotalS_volAmazonia, appConTotalU_volAmazonia, appTipoS_volAmazonia, appTipoU_volAmazonia, appConTotalS_snapAmazonia, appConTotalU_snapAmazonia, appTipoS_snapAmazonia, appTipoU_snapAmazonia)

    open("templates/table_aggregatePd.html", "w").write(html_Agg)
    return render_template('table_aggregatePd.html')

# # APRESENTAÇÃO DAS TABELAS
# # -------------------------------------------------------------------------------------
@app.route("/volumes")
def volumes():
    dfVolOlinda = pd.DataFrame(arrayVolumesOlinda)
    pd.set_option('colheader_justify', 'left')
    dfVolOlinda.columns = ['Volumes', 'Departamento', 'Total', 'Usado', 'Disponível']

    htmlVolOlinda = generate_html_V(dfVolOlinda)

    open("templates/table_volumesPd.html", "w").write(htmlVolOlinda)
    return render_template('table_volumesPd.html')

@app.route("/egeon")
def egeon():
    df_E = pd.DataFrame(arrayEgeon)
    pd.set_option('colheader_justify', 'left')
    df_E.columns = ['Rack', 'Nome', 'Marca', 'Modelo', 'Processadores', 'Memória', 'Potência Máxima - (W)', 'Tarifa/Mensal']

    html_E = generate_html_E(df_E)

    open("templates/table_EgeonPd.html", "w").write(html_E)
    return render_template('table_EgeonPd.html')

# @app.route("/racksv2")
# def racks_v2():
#     df_Rv2 = pd.DataFrame(arrayRacks_v2)
#     pd.set_option('colheader_justify', 'left')
#     df_Rv2.columns = ['Rack', 'Quantidade', 'Responsável', 'Marca', 'Modelo', 'Potência (W)', 'Tarifa Mensal', 'Diário/Rack', 'Mensal/Rack', 'Anual/Rack']

#     html_Rv2 = generate_html_Rv2(df_Rv2)

#     open("templates/table_Racksv2Pd.html", "w").write(html_Rv2)
#     return render_template('table_Racksv2Pd.html')

@app.route("/equipamentos")
def equipamentos():
    #def destaca_maiores_valores(valor): 
    #    cor = 'blue' if valor == "SEM GARANTIA" else 'black' 
    #    return f'color: {cor}'
    
    df_Eq = pd.DataFrame(arrayEquipamentos)
    pd.set_option('colheader_justify', 'left')
    #df_Eq.style.applymap(destaca_maiores_valores)
    # df_Eq.style.highlight_min
    
    df_Eq.columns = ['Rack', 'Nome', 'Marca', 'Modelo', 'Responsável / Aplicação', 'Service Tag', 'Status Garantia','Data Garantia', 'Patrimônio', 'Detentor', 'Custo Diário','Custo Mensal', 'Custo Anual']

    html_Eq = generate_html_Eq(df_Eq)

    open("templates/table_EquipamentosPd.html", "w").write(html_Eq)
    return render_template('table_EquipamentosPd.html')

# @app.route("/virtualizadores")
# def virtualizadores():
#     df_Av = pd.DataFrame(arrayServidores)
#     pd.set_option('colheader_justify', 'left')
#     df_Av.columns = ['POOL', 'HOST', 'VM', 'Descrição', 'SO','CPU', 'Memória', 'STATUS']

#     html_Av = generate_html_Av(df_Av)

#     open("templates/table_ambientevirtualPd.html", "w").write(html_Av)
#     return render_template('table_ambientevirtualPd.html')


if __name__ == '__main__':
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
