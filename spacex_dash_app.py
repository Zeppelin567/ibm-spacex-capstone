"""SpaceX launch dashboard, using the official 56-row dashboard dataset."""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

BASE=Path(__file__).resolve().parent
df=pd.read_csv(BASE/'spacex_launch_dash.csv')
app=Dash(__name__)
app.title='SpaceX Launch Dashboard'
app.layout=html.Main([
    html.H1('SpaceX Launch Dashboard'),
    html.P('Historical course snapshot: 56 launches. Select a site and payload range to explore outcomes.'),
    html.Label('Launch site',htmlFor='site-dropdown'),
    dcc.Dropdown(id='site-dropdown',options=[{'label':'All Sites','value':'ALL'}]+[{'label':s,'value':s} for s in sorted(df['Launch Site'].unique())],value='ALL',clearable=False,searchable=True),
    dcc.Graph(id='success-pie-chart',style={'height':'410px'}),
    html.Label('Payload mass range (kg)'),
    dcc.RangeSlider(id='payload-slider',min=0,max=10000,step=1000,marks={i:str(i) for i in range(0,10001,1000)},value=[0,10000],allowCross=False),
    dcc.Graph(id='success-payload-scatter-chart',style={'height':'400px'}),
    html.P('Source: IBM Skills Network spacex_launch_dash.csv. Class 1 denotes success in this historical dataset.')
],style={'maxWidth':'1180px','margin':'25px auto','fontFamily':'Arial','color':'#162c48'})

@app.callback(Output('success-pie-chart','figure'),Input('site-dropdown','value'))
def get_pie_chart(site):
    if site=='ALL':
        counts=df.groupby('Launch Site',as_index=False)['class'].sum()
        fig=px.pie(counts,names='Launch Site',values='class',title='Successful launches by site')
    else:
        filtered=df[df['Launch Site'].eq(site)]
        counts=filtered['class'].value_counts().reindex([0,1],fill_value=0).rename_axis('class').reset_index(name='Count')
        counts['Outcome']=counts['class'].map({0:'Unsuccessful',1:'Successful'})
        fig=px.pie(counts,names='Outcome',values='Count',title=f'Launch outcomes: {site}',color='Outcome',color_discrete_map={'Successful':'#0072b2','Unsuccessful':'#d55e00'})
    fig.update_traces(textinfo='label+percent+value')
    return fig

@app.callback(Output('success-payload-scatter-chart','figure'),Input('site-dropdown','value'),Input('payload-slider','value'))
def get_scatter_chart(site,payload_range):
    filtered=df[df['Payload Mass (kg)'].between(*payload_range)]
    if site!='ALL':filtered=filtered[filtered['Launch Site'].eq(site)]
    fig=px.scatter(filtered,x='Payload Mass (kg)',y='class',color='Booster Version Category',hover_data=['Launch Site'],title=f'Payload versus launch outcome: {site}')
    fig.update_yaxes(tickvals=[0,1],ticktext=['Unsuccessful','Successful'])
    fig.update_traces(marker={'size':10,'opacity':.8})
    return fig

if __name__=='__main__':app.run(host='127.0.0.1',port=8051,debug=False)
