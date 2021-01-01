import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

def app_layout():
    return(
            html.Div([
                    dcc.Tabs(
                            children=[
								 dcc.Tab(label= 'Pie1', value=1),
								 dcc.Tab(label= 'Pie2', value=2),
								 dcc.Tab(label= 'Pie3', value=3),
								 dcc.Tab(label= 'Pie4', value=4),
                                  ],
                            value=1,
                            id='tabs'
                            ),
                    html.Div(id='output-tab')
                    ])
    )

app.layout=app_layout()

@app.callback(Output('output-tab', 'children'),
              [Input('tabs', 'value')])
def display_content(value):
    labels = [['a','b'],['c','d'],['e','f'],['g','h']][int(value)-1]
    print (labels)
    data = [
        {
            'values': [[10,90],[5, 95],[15,85],[20,80]][int(value)-1],
            'labels': labels, 
            'type': 'pie',
        },
    ]

    return html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        )
    ])
if __name__ == '__main__':
    app.server.run(debug=True)
