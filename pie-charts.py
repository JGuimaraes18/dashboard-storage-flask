# from dash import Dash, dcc, html, Input, Output
# import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from table_Volumes1 import *
from connection import * 


app = Dash(__name__)


nameArray = []
sizeArray = []
i = 0
while i <len (department):
    testeporexemplo = department[i].split(",")
    print(testeporexemplo)
    saidaBd = searchBd(department[i])
    i+=1
    # print(saidaBd)


for v in myresult:
    nameArray = np.append(nameArray,v[0])
    sizeArray = np.append(sizeArray, v[1])
    
fig = px.pie(values=sizeArray, names=nameArray) 
# fig.show()



# app.layout = html.Div([
#     html.H4('Analysis of the restaurant sales'),
#     dcc.Graph(id="pie-charts-x-graph"),
#     html.P("Names:"),
#     dcc.Dropdown(id='pie-charts-x-names',
#         options=[somaU],
#         value='day', clearable=False),
#     html.P("Values:"),
#     dcc.Dropdown(id='pie-charts-x-values',
#         options=[somaA],
#         value='total_bill', clearable=False)
# ])


# @app.callback(
#     Output("pie-charts-x-graph", "figure"), 
#     Input("pie-charts-x-names", "value"),
#     Input("pie-charts-x-values", "value"))
# def generate_chart(names, values):
#     df = px.data.tips() # replace with your own data source
#     fig = px.pie(df, values=values, names=names, hole=.3)
#     return fig


if __name__ == "__main__":
    app.run_server(debug=True)
