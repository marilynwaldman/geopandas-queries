import plotly.graph_objects as go # or plotly.express as px
#fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import pandas as pd
import dash
from dash import html
from dash import dcc
#import dash_core_components as dcc
#import dash_html_components as html

app = dash.Dash()

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
print(us_cities.head())
import plotly.express as px
center = {'lat': 39.7, 'lon':-104.9}
df = pd.DataFrame()
data = {'lat': 39.7, 'lon':-104.9, 'marker': 10}
df = df.append(data, ignore_index=True)

fig = px.scatter_mapbox(df, center=center, lat="lat", lon="lon",
                        size="marker",
                        color_discrete_sequence=["blue"], zoom=12, width=800,height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":50,"t":50,"l":50,"b":50})
#fig.show()

app.layout = html.Div([
    dcc.Graph(figure=fig)
])


if __name__ == "__main__":
    
    app.run_server(debug=True,port=8000,host='0.0.0.0')

#app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter