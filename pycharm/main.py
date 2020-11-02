import pandas as pd
from pycharm.functions import fct, algopred
import warnings


warnings.filterwarnings('ignore')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

chemin="C:/Users/fidan/Documents/PYTHON/Repo_G1_Dataset_2_flower/Dataset_2_flower.csv"
df=fct.dfcsv(chemin, "|")
#print("FONCTION CHEMIN \n",df)

fct.listeType(df)
fct.control(df,"isna")

dropColumns = ["index", "Unnamed: 0", "Unnamed: 0.1", "Unnamed: 0.1.1", "level_0", "Unnamed: 0.1.1.1"]
df=fct.drop(df, dropColumns)
#print("FONCTION dropColumns \n",df)

listColumns = ["Id", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
#print("FONCTION listColumns \n")
fct.counts(df, listColumns)

df=fct.convertNAN(df,"Id")
df=fct.convertTYPE(df,"Id",float)

df=fct.NONENAN(df,"SepalLengthCm","None")
df=fct.convertTYPE(df,"SepalLengthCm",float)

df=fct.moyenneCOLONNE(df,"SepalLengthCm")
print(df)
#print("FONCTION moyenne \n",df)

df=fct.remplacevaleurcolonne(df,0,1,"Id",int)
print("FONCTION nettoyage \n",df)

#fct.defrandomf(df,1,4,5,0.30,10)

listealgopred=[10,100,1000]
algopred.algopred(df,1,4,5,0.3,"rf",listealgopred)