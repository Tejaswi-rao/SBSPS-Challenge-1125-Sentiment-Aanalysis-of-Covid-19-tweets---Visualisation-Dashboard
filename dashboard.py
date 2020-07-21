import dash
from dash.dependencies import Input,Output
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
# import gettweets
# print("hello")`1`
# emotions = {  "Sadness" : 6.028048999999999, 
# "Confident" : 13.643693999999998, "Joy" : 18.119237000000002,
#  "Analytical" : 12.695936, "Tentative" : 6.039631000000001, "Fear" : 0.621125 }
# emotions = gettweets.emotions_score
for i in range(1,5):
    emotions = {'1':i,'2':i+2,'3':i+4}

    app.layout = html.Div(children=[
        html.H1('Sentiment Analysis'),
        dcc.Graph(id='example',figure={
            # 'data': [{'x':[1,2,3,4,5],'y':[2,4,8,10,12,14],'type':'line','name':'boats'},
            # {'x':[7,4,5,9],'y':[4,12,9,7,5,3],'type':'bar','name':'cars'}
            'data':[
            # {'y':[215.541778999,72.755455,141.1583,196.285787,9.22625,96.045295],
            { 'y':list(emotions.values()),
            'x':list(emotions.keys()),
            #  'x':['Joy',
            #             'Sadness',
            #             'Tentative',
            #             'Analytical',
            #             'Fear',
            #             'Confident',
            #             'Anger'  ]
            
            'type':'line','name':'lockdown3',
            }],

        'layout': {
            'title': 'Lockdown3'
        }
        })
        ])
# colors={
#     'background':'blueviolet',
#     'text':'#7FDBFF'
# }
# app.layout = html.Div(style={'backgroundColor':colors['background']},children=[
#     dcc.Input(id='input',value='Enter something',type='text',style = {
#         'textAlign':'center',
#         'color':colors['text']
#     }),
#     html.Div(id='output')
# ])
# @app.callback(
#     Output(component_id='output',component_property='children'),
#     [Input(component_id='input',component_property='value')])
# def update_value(input_data):
#     return "Input: {}".format(input_data)
if __name__ == "__main__":
    app.run_server(debug=True)
