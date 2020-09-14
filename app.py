# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import parser.series_notam as mp_parser
import osm_maps.main as osm_map

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

osm_map_repr = osm_map.generate()

app.layout = html.Div(children=[

    html.H1(children= 'NOTAM app with dash'),

    html.Iframe(srcDoc = osm_map.generate()._repr_html_(), width='100%', height='600'),

    html.Div(children= list(map(lambda s: html.Div(children= s), mp_parser.parse()))),
])


if __name__ == '__main__':
    app.run_server(debug=True)