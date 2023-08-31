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


df_sb = pd.read_csv('Mid-weekday SB Corridor Travel Time all_sce.csv')


# In[3]:


df_sb_off = df_sb[df_sb['Scenario'] == 'ARM off - Apr 2023']
df_sb_on = df_sb[df_sb['Scenario'] != 'ARM off - Apr 2023']


# In[4]:


df_nb = pd.read_csv('Mid-weekday NB Corridor Travel Time all_sce.csv')

# In[5]:


df_nb_off = df_nb[df_nb['Scenario'] == 'ARM off - Apr 2023']
df_nb_on = df_nb[df_nb['Scenario'] != 'ARM off - Apr 2023']


# In[6]:


# Create a Dash app
app = dash.Dash(__name__)
server = app.server

# Load your data (replace this with your data loading code)
# df_off = ...
# df_on = ...

# Define color scales for the lines
color_scale = ['#458B74', '#838B8B','#66CDAA', '#E3CF57','#636EFA', '#00CC96',]

# Define the app layout
app.layout = html.Div([
    html.H1("I-880 Corridor Travel Time"),
    # first figure
        dcc.Graph(
        id='Corridor-TT-NB',
        figure={
            'data': [
                {
                    'x': df_nb_off['time'], 'y': df_nb_off['TT_mean'], 'type': 'line', 'name': 'ARM off - Apr 2023',
                    'line': {'color': 'orangered', 'dash': 'dot', 'width': 3}
                }] +
                [{
                    'x': df_nb_on[df_nb_on['Scenario'] == scenario]['time'],
                    'y': df_nb_on[df_nb_on['Scenario'] == scenario]['TT_mean'],
                    'type': 'line',
                    'name': scenario,
                    'line': {'color': color_scale[i], 'dash': 'solid'}
                }
                for i, scenario in enumerate(df_nb_on['Scenario'].unique())
            ],
            'layout': {
                'title': 'NB Corridor Travel Time from I-580 to I-280, Mid-weekday',
                'xaxis': {
                    'title': '',
                    'tickmode': 'array',
                    'tickvals': df_nb['time'].unique()[::12],
                    'ticktext': df_nb['time'][::12],
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
                    'x': df_sb_off['time'], 'y': df_sb_off['TT_mean'], 'type': 'line', 'name': 'ARM off - Apr 2023',
                    'line': {'color': 'orangered', 'dash': 'dot', 'width': 3}
                }] +
                [{
                    'x': df_sb_on[df_sb_on['Scenario'] == scenario]['time'],
                    'y': df_sb_on[df_sb_on['Scenario'] == scenario]['TT_mean'],
                    'type': 'line',
                    'name': scenario,
                    'line': {'color': color_scale[i], 'dash': 'solid'}
                }
                for i, scenario in enumerate(df_sb_on['Scenario'].unique())
            ],
            'layout': {
                'title': 'SB Corridor Travel Time from I-580 to I-280, Mid-weekday',
                'xaxis': {
                    'title': '',
                    'tickmode': 'array',
                    'tickvals': df_sb['time'].unique()[::12],
                    'ticktext': df_sb['time'][::12],
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