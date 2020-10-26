import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from functions import fct

pd.set_option('display.max_columns', None)

df = pd.read_csv("/Users/fidan/Documents/PYTHON/Dataset_2_flower.csv",sep="|")

listColumns=["Id","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"]
fct.counts(df,listColumns)

dropColumns=["index","Unnamed: 0","Unnamed: 0.1","Unnamed: 0.1.1","level_0","Unnamed: 0.1.1.1"]
fct.drop(df,dropColumns)

fct.moyenne(df,"SepalLengthCm")

fct.nettoyage(df,"Id")

