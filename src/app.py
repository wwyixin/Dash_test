#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the necessary libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


# In[2]:

df_sb_off = pd.read_csv('Mid-weekday SB Corridor Travel Time_Off.csv')
df_sb_on = pd.read_csv('Mid-weekday SB Corridor Travel Time_On.csv')


# In[5]:


df_nb_off = pd.read_csv('Mid-weekday NB Corridor Travel Time_Off.csv')
df_nb_on = pd.read_csv(r'Mid-weekday NB Corridor Travel Time_On.csv')


# In[6]:


# Create a Dash app
app = dash.Dash(__name__)
server = app.server

# Load your data (replace this with your data loading code)
# df_off = ...
# df_on = ...

# Define color scales for the lines
color_scale = ['#458B74', '#86b8dc','#bc6ca7','#ac7c60', '#FFA500',]

# Define the app layout
app.layout = html.Div([
    html.H1("I-880 Corridor Travel Time"),
    # First figure
    dcc.Graph(
        id='Corridor-TT-NB',
        figure={
            'data': [
                {
                    'x': df_nb_off['time'], 'y': df_nb_off['TT_mean'], 'type': 'line', 'name': 'ARM Off: Apr 2023',
                    'line': {'color': '#838B8B', 'dash': 'dot', 'width': 3},
                    'hovertemplate': 'Time: %{x}<br>Travel Time: %{y:.1f}'
                }] +
                [{
                    'x': df_nb_on[df_nb_on['Scenario'] == scenario]['time'],
                    'y': df_nb_on[df_nb_on['Scenario'] == scenario]['TT_mean'],
                    'type': 'line',
                    'name': scenario,
                    'line': {'color': color_scale[i], 'dash': 'solid'},
                    'hovertemplate': 'Time: %{x}<br>Travel Time: %{y:.1f}'
                }
                for i, scenario in enumerate(df_nb_on['Scenario'].unique())
            ],
            'layout': {
                'title': 'NB Corridor Travel Time from I-580 to I-280, Mid-weekday',
                'xaxis': {
                    'title': '',
                    'tickmode': 'array',
                    'tickvals': df_nb_on['time'].unique()[::12],
                    'ticktext': df_nb_on['time'][::12],
                    'tickangle': 270,
                },
                'yaxis': {'title': 'Travel Time (min)'},
                'legend': {'x': 1, 'y': 1}
            }
        }
    ),

    dcc.Graph(
        id='Corridor-TT-SB',
        figure={
            'data': [
                {
                    'x': df_sb_off['time'], 'y': df_sb_off['TT_mean'], 'type': 'line', 'name': 'ARM Off: Apr 2023',
                    'line': {'color': '#838B8B', 'dash': 'dot', 'width': 3},
                    'hovertemplate': 'Time: %{x}<br>Travel Time: %{y:.1f}'
                }] +
                [{
                    'x': df_sb_on[df_sb_on['Scenario'] == scenario]['time'],
                    'y': df_sb_on[df_sb_on['Scenario'] == scenario]['TT_mean'],
                    'type': 'line',
                    'name': scenario,
                    'line': {'color': color_scale[i], 'dash': 'solid'},
                    'hovertemplate': 'Time: %{x}<br>Travel Time: %{y:.1f}'
                }
                for i, scenario in enumerate(df_sb_on['Scenario'].unique())
            ],
            'layout': {
                'title': 'SB Corridor Travel Time from I-580 to I-280, Mid-weekday',
                'xaxis': {
                    'title': '',
                    'tickmode': 'array',
                    'tickvals': df_sb_on['time'].unique()[::12],
                    'ticktext': df_sb_on['time'][::12],
                    'tickangle': 270,
                },
                'yaxis': {'title': 'Travel Time (min)'},
                'legend': {'x': 1, 'y': 1}
            }
            }    

    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)