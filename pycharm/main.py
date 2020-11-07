import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from pycharm.functions import fct
from pycharm.functions import algopred
from py2neo import Node, Relationship,Graph
graphFlower = Graph("bolt://localhost:7687", auth=None)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

chemin = "/Users/louisadam/Documents/GitHub/Repo_G1_Dataset_2_flower/Dataset_2_flower.csv"

dataframe = fct.dfcsv(chemin, "|")

listColumnsOk = ["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]  # Colonne
listColumnsNonOk = ["index", "Unnamed: 0", "Unnamed: 0.1", "Unnamed: 0.1.1", "level_0", "Unnamed: 0.1.1.1"]
speciesNeo=["Iris-setosa","Iris-versicolor","Iris-virginica"]
#print(fct.counts(dataframe, listColumnsOk))

dataframe = fct.dropColumns(dataframe, listColumnsNonOk)

dataframe=fct.cleanCol(dataframe, "SepalLengthCm")

dataframe=fct.cleanId(dataframe, "Id")
#print(dataframe)

colrfx = dataframe[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]  # Colonnes utilisées pour la prédiction
colrfy = dataframe['Species']  # Le champs que l'on veut prédire
"""
collrx = dataframe.iloc[:, 1:-1]  # Champs des longuers et largeurs des pétales, sépales
collry = dataframe.iloc[:, -1]  # Champs Species
"""
#listeesti=[10, 100, 1000]
#algopred.algodf(colrfx, colrfy, 0.3, "rf",listeesti)

#fct.isNan(dataframe)

lstgenre=[]
for i in range(len(dataframe)):
    #print(dataframe.iloc[i,1])
    nodeId=Node("Id", name=i)
    if (dataframe.iloc[i,[5]]).values == "Iris-versicolor":
        if "Iris-versicolor" not in lstgenre:
            lstgenre.append("Iris-versicolor")
            nodeVersi = Node("Species", name="Iris-versicolor")
            relIdVersi = Relationship(nodeId, "type", nodeVersi)
            graphFlower.create(relIdVersi)
        elif "Iris-versicolor" in lstgenre:
            relIdVersi = Relationship(nodeId, "type", nodeVersi)
        graphFlower.create(relIdVersi)
        nodeVersiSW = Node("Sepal Width",name=dataframe.iloc[i,2])
        nodeVersiSL = Node("Sepal Length",name=dataframe.iloc[i,1])
        nodeVersiPW = Node("Petal Width",name=dataframe.iloc[i,4])
        nodeVersiPL = Node("Petal Length",name=dataframe.iloc[i,3])
        relIdVersiSW = Relationship(nodeId, "taille", nodeVersiSW)
        relIdVersiSL = Relationship(nodeId, "taille", nodeVersiSL)
        relIdVersiPW = Relationship(nodeId, "taille", nodeVersiPW)
        relIdVersiPL = Relationship(nodeId, "taille", nodeVersiPL)
        graphFlower.create(relIdVersiSW)
        graphFlower.create(relIdVersiSL)
        graphFlower.create(relIdVersiPW)
        graphFlower.create(relIdVersiPL)
    elif (dataframe.iloc[i,[5]]).values == "Iris-setosa":
        if "Iris-setosa" not in lstgenre:
            lstgenre.append("Iris-setosa")
            nodeSeto = Node("Species", name="Iris-setosa")
            relIdSeto = Relationship(nodeId, "type", nodeSeto)
            graphFlower.create(relIdSeto)
        elif "Iris-setosa" in lstgenre:
            relIdSeto = Relationship(nodeId, "type", nodeSeto)
            graphFlower.create(relIdSeto)
        nodeSetoSW = Node("Sepal Width",name=dataframe.iloc[i,2])
        nodeSetoSL = Node("Sepal Length",name=dataframe.iloc[i,1])
        nodeSetoPW = Node("Petal Width",name=dataframe.iloc[i,4])
        nodeSetoPL = Node("Petal Length",name=dataframe.iloc[i,3])
        relIdSetoSW = Relationship(nodeId, "taille", nodeSetoSW)
        relIdSetoSL = Relationship(nodeId, "taille", nodeSetoSL)
        relIdSetoPW = Relationship(nodeId, "taille", nodeSetoPW)
        relIdSetoPL = Relationship(nodeId, "taille", nodeSetoPL)
        graphFlower.create(relIdSetoSW)
        graphFlower.create(relIdSetoSL)
        graphFlower.create(relIdSetoPW)
        graphFlower.create(relIdSetoPL)
    elif (dataframe.iloc[i,[5]]).values == "Iris-virginica":
        if "Iris-virginica" not in lstgenre:
            lstgenre.append("Iris-virginica")
            nodeVirgi = Node("Species", name="Iris-virginica")
            relIdVirgi = Relationship(nodeId, "type", nodeVirgi)
            graphFlower.create(relIdVirgi)
        elif "Iris-virginica" in lstgenre:
            relIdVirgi = Relationship(nodeId, "type", nodeVirgi)
            graphFlower.create(relIdVirgi)
        nodeVirgiSW = Node("Sepal Width",name=dataframe.iloc[i,2])
        nodeVirgiSL = Node("Sepal Length",name=dataframe.iloc[i,1])
        nodeVirgiPW = Node("Petal Width",name=dataframe.iloc[i,4])
        nodeVirgiPL = Node("Petal Length",name=dataframe.iloc[i,3])
        relIdVirgiSW = Relationship(nodeId, "taille", nodeVirgiSW)
        relIdVirgiSL = Relationship(nodeId, "taille", nodeVirgiSL)
        relIdVirgiPW = Relationship(nodeId, "taille", nodeVirgiPW)
        relIdVirgiPL = Relationship(nodeId, "taille", nodeVirgiPL)
        graphFlower.create(relIdVirgiSW)
        graphFlower.create(relIdVirgiSL)
        graphFlower.create(relIdVirgiPW)
        graphFlower.create(relIdVirgiPL)
