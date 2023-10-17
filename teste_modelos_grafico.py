
import plotly.express as  px
import pandas as pd


# fig = px.bar (x = '1', y = '2', labels={'x': 'Volumes', 'y': 'Usado - %'}, color_discrete_sequence=px.colors.qualitative.G10,template='plotly')
# fig.update_layout(font = {'family': 'Arial','size': 12,'color': 'black'})
# fig.write_html('templates/graficoVolumes.html')

# chart_A = px.box(values=['5', '5'], names=['usado', 'disponivel'], color_discrete_sequence=px.colors.qualitative.Light24)
# chart_A.write_html('templates/graficoStorage.html')

x='3'
y='6'
A = pd.DataFrame({x, y}, index={'teste', 'teste1'}, rot=0).plot.bar


A.show()


# speed = [0.1, 17.5, 40, 48, 52, 69, 88]
# lifespan = [2, 8, 70, 1.5, 25, 12, 28]
# index = ['snail', 'pig', 'elephant',
#          'rabbit', 'giraffe', 'coyote', 'horse']
# df = pd.DataFrame({'speed': speed,
#                    'lifespan': lifespan}, index=index)
# ax = df.plot.bar(rot=0)


# how()