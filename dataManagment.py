import pandas as pd
import numpy as np
import xlrd

"""convert excel to csv file"""
# df_data = pd.read_excel("Dataset.xlsx")
# df_data.to_csv('Dataset.csv', sep=",")
# print(df_data.head())
df_data = pd.read_csv("Dataset.csv")

# def fillNaValuesWithAvg():
#     cols = list(df_data.columns.values)
#     # print(cols)
#     for column in cols:
#         df_data[column] = df_data[column].fillna(df_data[column].mean())

# fillNaValuesWithAvg()

# df_data['Life Ladder'] = df_data['Life Ladder'].fillna(df_data['Life Ladder'].mean())
# df_data['Log GDP per capita'] = df_data['Log GDP per capita'].fillna(df_data['Log GDP per capita'].mean())
# print(df_data.head())