import matplotlib.pyplot as plt
import base64
from io import BytesIO

def chart_vol(somaU, somaA):
    usado = somaU
    disponivel = somaA

    labels = ['Usado', 'Disponível']
    vals = [usado, disponivel]
    colors = ['red', 'green']
    
    fig, ax = plt.subplots(figsize=(9,5))

    ax.pie(vals, autopct="%.2f%%", colors=colors, shadow=True, explode=(0, 0.1))
    ax.set_title('Volumes', fontsize=20)
    plt.legend(labels=labels, prop = {'size' : 12}, loc = 'lower right',)
    
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    html = '<img src=\'data:image/png;base64,{}\'/>'.format(encoded)

    with open('templates/chart_vol.html', 'w') as f:
        f.write(html)

def chart_snap(somaU_snap, somaA_snap):
    usado = somaU_snap
    disponivel = somaA_snap

    labels = ['Usado', 'Disponível']
    vals = [usado, disponivel]
    colors = ['red', 'green']
    
    fig, ax = plt.subplots(figsize=(9,5))

    ax.pie(vals, autopct="%.2f%%", colors=colors, shadow=True, explode=(0.1, 0.1))
    ax.set_title('Snaps', fontsize=20)
    plt.legend(labels=labels, prop = {'size' : 12}, loc = 'lower right',)
    
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    html = '<img src=\'data:image/png;base64,{}\'/>'.format(encoded)

    with open('templates/chart_snap.html', 'w') as f:
        f.write(html)
        
# def chart_storage(totalDadosArmz, totalDispoArmz):
#     utilizado = totalDadosArmz
#     disponivel = totalDispoArmz

#     labels = ['Usado', 'Disponível']
#     vals = [utilizado, disponivel]
#     colors = ['red', 'green']
    
#     fig, ax = plt.subplots(figsize=(9,5))

#     ax.pie(vals, autopct="%.2f%%", colors=colors, shadow=True, explode=(0.1, 0.1))
#     plt.legend(labels=labels, prop = {'size' : 12}, loc = 'lower right',)
    
#     tmpfile = BytesIO()
#     fig.savefig(tmpfile, format='png')
#     encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

#     html = '<img src=\'data:image/png;base64,{}\'/>'.format(encoded)

#     with open('templates/chart_storage.html', 'w') as f:
#         f.write(html)
        
# def chart_landsat():
#     utilizado = totalDadosArmz
#     disponivel = totalDispoArmz

#     labels = ['Usado', 'Disponível']
#     vals = [utilizado, disponivel]
#     colors = ['red', 'green']
    
#     fig, ax = plt.subplots(figsize=(9,5))

#     ax.pie(vals, autopct="%.2f%%", colors=colors, shadow=True, explode=(0.1, 0.1))
#     plt.legend(labels=labels, prop = {'size' : 12}, loc = 'lower right',)
    
#     tmpfile = BytesIO()
#     fig.savefig(tmpfile, format='png')
#     encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

#     html = '<img src=\'data:image/png;base64,{}\'/>'.format(encoded)

#     with open('templates/chart_landsat.html', 'w') as f:
#         f.write(html)