import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from functions import fct
from functions import algopred
from py2neo import Node, Relationship,Graph
graphFlower = Graph("bolt://localhost:7687", auth=None)

pd.set_option('display.max_columns', None) #Options pour rendre plus ou moins lisible l'output du dataframe (colonnes)
pd.set_option('display.max_rows', 1000) #Options pour rendre plus ou moins lisible l'output du dataframe (lignes)

chemin = "Dataset_2_flower.csv" #Chemin du csv
#chemin = "/usr/src/app/pycharm/Dataset_2_flower.csv" #Chemin du csv

#Exécution de la fonction dfcsv
dataframe = fct.dfcsv(chemin, "|")

listColumnsOk = ["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]  #Colonne à exploiter
listColumnsNonOk = ["index", "Unnamed: 0", "Unnamed: 0.1", "Unnamed: 0.1.1", "level_0", "Unnamed: 0.1.1.1"] #Colonnes non exploitables

#print(fct.counts(dataframe, listColumnsOk)) #Execute la fonction counts sur les colonnes de la liste listColumnsOk

dataframe = fct.dropColumns(dataframe, listColumnsNonOk) #Execute la fonction dropColumns sur les colonnes de la liste listColumnsNonOk
print(dataframe)
dataframe=fct.cleanCol(dataframe, "SepalLengthCm") #Execute la fonction cleanCol sur la colonne SepalLengthCm

dataframe=fct.cleanId(dataframe, "Id") #Execute la fonction cleanId sur la colonne Id

colrfx = dataframe[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]  #Colonnes utilisées pour la prédiction
colrfy = dataframe['Species']  #Le champs que l'on veut prédire

"""
colrx = dataframe.iloc[:, 1:-1]  #Colonnes utilisées pour la prédiction
colry = dataframe.iloc[:, -1]  #Le champs que l'on veut prédire
"""

listeesti=[10, 100, 1000] #GridSearch sur la variable n_estimators (nb d'armes)
algopred.algodf(colrfx, colrfy, 0.3, "rf",listeesti) #Exécution de la fonction algodf

fct.isNan(dataframe) #Exécute la fonction isNan

# dictCm = {
#     "SepalLengthCm": 1,
#     "SepalWidthCm": 2,
#     "PetalLengthCm": 3,
#     "PetalWidthCm": 4
# }
#
# lstspec=[]
# for i in range(len(dataframe)): #Parcourt chaque ligne du dataframe
#     nodeId=Node("Id", name=i) #Créé un noeud pour chaque ligne
#     if (dataframe.iloc[i,[5]]).values == "Iris-versicolor": #Si la fleur est de type versicolor
#         if "Iris-versicolor" not in lstspec: #Si iris-versicolor est dans lstspec
#             lstspec.append("Iris-versicolor") #On ajoute le Species dans lstspec
#             nodeVersi = Node("Species", name="Iris-versicolor") #Créé un noeud Iris-Versicolor
#             relIdVersi = Relationship(nodeId, "type", nodeVersi) #Fait la relation entre l'id de la fleur et le type de la fleur
#             graphFlower.create(relIdVersi)
#         elif "Iris-versicolor" in lstspec: #Si Iris-versicolor n'est pas dans lstspec, pas besoin de recréer le noeud
#             relIdVersi = Relationship(nodeId, "type", nodeVersi) #On créé seulement la relation
#         graphFlower.create(relIdVersi)
#
#         fct.createGraph(dataframe,nodeId,i,dictCm)
#
#     elif (dataframe.iloc[i,[5]]).values == "Iris-setosa": #Si la fleur est de type setosa
#         if "Iris-setosa" not in lstspec: #Si iris-setosa est dans lstspec
#             lstspec.append("Iris-setosa") #On ajoute le Species dans lstspec
#             nodeSeto = Node("Species", name="Iris-setosa") #Créé un noeud Iris-setosa
#             relIdSeto = Relationship(nodeId, "type", nodeSeto) #Fait la relation entre l'id de la fleur et le type de la fleur
#             graphFlower.create(relIdSeto)
#         elif "Iris-setosa" in lstspec:#Si Iris-setosa n'est pas dans lstspec, pas besoin de recréer le noeud
#             relIdSeto = Relationship(nodeId, "type", nodeSeto)#On créé seulement la relation
#             graphFlower.create(relIdSeto)
#
#         fct.createGraph(dataframe, nodeId, i, dictCm)
#
#     elif (dataframe.iloc[i,[5]]).values == "Iris-virginica": #Si la fleur est de type virginica
#         if "Iris-virginica" not in lstspec: #Si iris-virginica est dans lstspec
#             lstspec.append("Iris-virginica") #On ajoute le Species dans lstspec
#             nodeVirgi = Node("Species", name="Iris-virginica") #Créé un noeud Iris-virginica
#             relIdVirgi = Relationship(nodeId, "type", nodeVirgi) #Fait la relation entre l'id de la fleur et le type de la fleur
#             graphFlower.create(relIdVirgi)
#         elif "Iris-virginica" in lstspec:#Si Iris-virginica n'est pas dans lstspec, pas besoin de recréer le noeud
#             relIdVirgi = Relationship(nodeId, "type", nodeVirgi)#On créé seulement la relation
#             graphFlower.create(relIdVirgi)
#
#         fct.createGraph(dataframe, nodeId, i, dictCm)
