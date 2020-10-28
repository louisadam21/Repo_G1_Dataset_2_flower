import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from pycharm.functions import fct
from pycharm.functions import algopred

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

chemin = "/Users/louisadam/Documents/GitHub/Repo_G1_Dataset_2_flower/Dataset_2_flower.csv"

dataframe = fct.dfcsv(chemin, "|")

listColumnsOk = ["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]  # Colonne
listColumnsNonOk = ["index", "Unnamed: 0", "Unnamed: 0.1", "Unnamed: 0.1.1", "level_0", "Unnamed: 0.1.1.1"]

print(fct.counts(dataframe, listColumnsOk))

dataframe = fct.dropColumns(dataframe, listColumnsNonOk)

dataframe=fct.moyenne(dataframe, "SepalLengthCm")

dataframe=fct.cleanId(dataframe, "Id")
print(dataframe)

colrfx = dataframe[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]  # Colonnes utilisées pour la prédiction
colrfy = dataframe['Species']  # Le champs que l'on veut prédire
"""
collrx = dataframe.iloc[:, 1:-1]  # Champs des longuers et largeurs des pétales, sépales
collry = dataframe.iloc[:, -1]  # Champs Species
"""
algopred.algodf(colrfx, colrfy, 0.3, "rf")
