from dash import Dash
from dash import html
from dash import dcc


from random import randint 

from dash.dcc import Dropdown

N= 20

database = {
    'index' : list(range(N)),
    'maiores': [randint(1,1000) for _ in range(1000)],
    'menores': [randint(1,1000) for _ in range(1000)]
}

##Biblioteca externa para visual
external_stylesheets= ['https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css']

#instanciando um dashboard
app = Dash(__name__ , external_stylesheets = external_stylesheets)


##Criando o layout do Dashboard
app.layout = html.Div(
    children =
    [html.H1("Olá Mundo"),
     html.P("Bem vindo ao Dash"),
     Dropdown(
         options
         = [
             { 'label' : 'Maiores', 'value': 'Maiores'},
             { 'label' : 'Menores', 'value': 'Menores'},
             { 'label' : 'Teste', 'value': 'Teste'}
        ],
            value='Menores'
     ),

    #Testando o botão de Slider
     dcc.Slider(
       min= 0,
        max = 10,
        step=1,
        value = 5

     ),

    #Testando o botão de Checklist
    dcc.Checklist(
      options= [
          {'label': 'Maiores', 'value': 'Maiores'},
          {'label': 'Menores', 'value': 'Menores'},
          {'label': 'Teste', 'value': 'Teste'}
      ] , value = ['Teste']
    ),


    #Criando um gráfico
     dcc.Graph(
         config= {'displayModeBar': False},
         figure={
             'data': [
                 {
                     'y': database['maiores'],
                     'x': database['index'],
                     'type': 'line',
                     'name': 'Maiores'
                 },
             ],
             'layout': {
             }
         }
     )

     ]
)





app.run_server(debug=True)
