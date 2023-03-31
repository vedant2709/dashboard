#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# In[2]:


# initiate the app
app=dash.Dash(external_stylesheets=[dbc.themes.UNITED,dbc.icons.BOOTSTRAP])


# In[3]:


# read files
df=pd.read_csv('count.csv')
df1=pd.read_csv('data.csv')


# In[4]:


# build components
Header_component=html.H1("Traffic Analysis Dashboard",style={'color':'darkcyan','text-align':'center','font-size':'72px'})


# In[5]:


# component1
countfig=go.FigureWidget()
countfig.add_scatter(name='bus',x=df["Time"],y=df["bus"],fill="tonexty",line_shape='spline')
countfig.add_scatter(name='car',x=df["Time"],y=df["car"],fill="tonexty",line_shape='spline')

countfig.update_layout(title="Vehicle Time Line")


# In[6]:


# component2
countfig_cum=go.FigureWidget()
countfig_cum.add_scatter(name='bus',x=df["Time"],y=df["bus"].cumsum(),fill="tonexty",line_shape='spline')
countfig_cum.add_scatter(name='car',x=df["Time"],y=df["car"].cumsum(),fill="tonexty",line_shape='spline')

countfig_cum.update_layout(title="Cumulative Traffic")


# In[7]:


# component3
indicator=go.FigureWidget(
    go.Indicator(
        mode="gauge+number",
        value=df1["car"].mean(),
        title={'text':'Speed km/h'},
        gauge={'bar':{'color':'red'}}
    )
)
indicator.update_layout(title="Average Car Speed")


# In[8]:


# component4
indicator1=go.FigureWidget(
    go.Indicator(
        mode="gauge+number",
        value=df1["bus"].mean(),
        title={'text':'Speed km/h'},
        
    )
)
indicator1.update_layout(title="Average Bus Speed")


# In[9]:


# component5
piefig=go.FigureWidget(
    px.pie(
        labels=["car","bus"],
        values=[df['car'].sum(),df['bus'].sum()],
        hole=0.4
    )
)

piefig.update_layout(title="Traffic Distribution")


# In[10]:


app.layout=html.Div(
    [
        dbc.Row(
            Header_component
        ),
        dbc.Row(
            [dbc.Col(
                [dcc.Graph(figure=countfig)]
            ),dbc.Col(
                [dcc.Graph(figure=countfig_cum)]
            )]
        ),
        dbc.Row(
            [dbc.Col(
                [dcc.Graph(figure=indicator)]
            ),dbc.Col(
                [dcc.Graph(figure=indicator1)]
            ),dbc.Col(
                [dcc.Graph(figure=piefig)]
            )]
        ),
    ]
)


# In[11]:


if __name__=='__main__':
    app.run_server()


# In[ ]:




