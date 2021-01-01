import dash
import dash_html_components as html
import dash_core_components as dcc
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
	dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1", style={'display':'none'})
    ),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
	
])

@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('loading-output-1', 'children')],
    #[dash.dependencies.State('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value')])
def update_output( n_clicks, value):
    print (n_clicks, value)
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


@app.callback(
    dash.dependencies.Output('loading-output-1', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],)
def loading(n_clicks):
    time.sleep(5)
    return  n_clicks


if __name__ == '__main__':
    app.run_server(debug=True)
