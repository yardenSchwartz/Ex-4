import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as go

py.sign_in('schyarde', 'QFqZeNqpcn2OaFftFKfY')

def scatterPlot(df_data):
    plt.title("Generosity as dependents in Social support")
    plt.scatter(x=df_data['Social support'], y=df_data['Generosity'], c=df_data['KMeans'], s=50, alpha=0.5)
    plt.xlabel("Social support")
    plt.ylabel("Generosity")
    plt.savefig('scatterPlot.png')
    # plt.show()

def horoplethMap(df_data):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
    fig = go.Figure(data=go.Choropleth(
        locations=df['CODE'],
        z=df_data['KMeans'],
        text=df_data['country'],
        colorscale='Blues',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='Clustering',
    ))

    fig.update_layout(
        title_text='KMeans Clustering Plot',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations=[dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
                CIA World Factbook</a>',
            showarrow=False
        )]
    )
    py.image.save_as(fig, filename='horoplethMap.png')
    # fig.show()