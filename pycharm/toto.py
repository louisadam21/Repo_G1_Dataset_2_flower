import pandas as pd
import math
from functions import fct

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 1000)

df = pd.read_csv("/Users/louisadam/Documents/GitHub/Repo_G1_Dataset_2_flower/Dataset_2_flower.csv", sep="|")

listColumnsOk = ["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"] # Colonne
listColumnsNonOk = ["index", "Unnamed: 0", "Unnamed: 0.1", "Unnamed: 0.1.1", "level_0", "Unnamed: 0.1.1.1"]

fct.counts(df, listColumnsOk)
fct.dropColumns(df, listColumnsNonOk)
fct.moyenne(df, "SepalLengthCm")
fct.cleanId(df)