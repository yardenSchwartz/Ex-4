import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as go

py.sign_in('schyarde', 'QFqZeNqpcn2OaFftFKfY')

# df_data = ""

# print(df_data.head())
# df_data = pd.read_csv("Dataset.csv")
# features = df_data.copy()


def fillNaValuesWithAvg(df_data):
    cols = list(df_data.columns.values)
    cols.pop(0)
    cols.pop(0)
    # print(cols)
    for column in cols:
        meanCol = df_data[column].mean()
        df_data[column] = df_data[column].fillna(meanCol)

def standardize(df_data):
    cols = list(df_data.columns.values)
    cols.pop(0)
    cols.pop(0)
    # print(cols)
    for column in cols:
        series = df_data.loc[:, column]
        avg = series.mean()
        stdv = series.std()
        series_standardized = (series - avg) / stdv
        df_data[column] = series_standardized

def preprocessing(path):
    """convert excel to csv file"""
    df_data = pd.read_excel(path)
    df_data.to_csv('Dataset.csv', sep=",")

    fillNaValuesWithAvg(df_data)
    standardize(df_data)

    df_data = df_data.groupby('country', as_index=False).mean()
    df_data = df_data.drop('year', axis=1)

    df_data.to_csv("Dataset.csv", index=False, header=True)


    return (df_data, "success")
    # print(df_data.head())

def kmeansCalc(df_data, numOfClusters, init):
    kmeans = KMeans(n_clusters=numOfClusters, n_init=init)

    dataToKMeans = df_data.copy()
    dataToKMeans = dataToKMeans.drop('country', axis=1)

    kmeans.fit(dataToKMeans)
    clust_labels = kmeans.predict(dataToKMeans)
    df_data['KMeans'] = pd.Series(clust_labels, index=df_data.index)
    return "success"
# 3.2+3.3
# kmeansCalc(df_data, 4, 2)







