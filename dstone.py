import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, html

app = Dash(external_stylesheets=[dbc.themes.SLATE])

collapse = html.Div(
    [
        dbc.Button(
            "DS",
            id="horizontal-collapse-button",
            className="mb-3",
            color="secondary",
            n_clicks=0,
        ),
        html.Div(
            dbc.Collapse(
                dbc.Card(
                    dbc.CardBody(
                        "This content appeared horizontally due to the "
                        "`dimension` attribute"
                    ),
                    style={"width": "400px"},
                ),
                id="horizontal-collapse",
                is_open=False,
                dimension="width",
            ),
            style={"minHeight": "100px"},
        ),
    ]
)

app.layout = collapse

@app.callback(
    Output("horizontal-collapse", "is_open"),
    [Input("horizontal-collapse-button", "n_clicks")],
    [State("horizontal-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run(debug=True)
