import pandas as pd
from pycharm.functions import fct, algopred
import warnings
from py2neo import Graph,Node, Relationship
graph=Graph("http://localhost:7474/", auth=None)

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
#print(df)
#print("FONCTION moyenne \n",df)

df=fct.remplacevaleurcolonne(df,0,1,"Id",int)
#print("FONCTION nettoyage \n",df)

#fct.defrandomf(df,1,4,5,0.30,10)

#listealgopred=[10,100,1000]
#algopred.algopred(df,1,4,5,0.3,"rf",listealgopred)

#typeflower=["Iris-setosa", "Iris-versicolor","Iris-virginica"]

#list_Id=[]

#for i in df["Id"]:
        #list_Id.append(i)
#print(list_Id)

#count=0
#for i in df["Id"]:
        #node_Id = Node('Id', name="Id")
       # graph.create(node_Id)
       # for i in df["Species"]:
         #  if df["Species"].iloc[count]=="Iris-setosa":
           #     node_seto = Node("Species", name="Iris-setosa")
           #     #print(df.iloc[count])
           #     graph_Id_Seto = Relationship(node_seto, "GENRE", node_Id)
            #    graph.create(graph_Id_Seto)
           # elif df["Species"].iloc[count]=="Iris-versicolor":
           #     node_versi = Node("Species", name="Iris-versicolor")
               #print(df.iloc[count])
           #     graph_Id_Versi = Relationship(node_versi, "GENRE", node_Id)
            #    graph.create(graph_Id_Versi)
           # elif df["Species"].iloc[count]=="Iris-virginica":
             #   node_vrigi = Node("Species", name="Iris-virginica")
                #print(df.iloc[count])
              #  graph_Id_Virgi = Relationship(node_vrigi,"GENRE", node_Id)
              #  graph.create(graph_Id_Virgi)

#count=count+1

dictCm = {
    "SepalLengthCm": 1,
    "SepalWidthCm": 2,
    "PetalLengthCm": 3,
    "PetalWidthCm": 4
 }

lstspec=[]
for i in range(len(df)): #Parcourt chaque ligne du dataframe
    nodeId=Node("Id", name=i) #Créé un noeud pour chaque ligne
    if (df.iloc[i,[5]]).values == "Iris-versicolor": #Si la fleur est de type versicolor
        if "Iris-versicolor" not in lstspec: #Si iris-versicolor est dans lstspec
            lstspec.append("Iris-versicolor") #On ajoute le Species dans lstspec
            nodeVersi = Node("Species", name="Iris-versicolor") #Créé un noeud Iris-Versicolor
            relIdVersi = Relationship(nodeId, "type", nodeVersi) #Fait la relation entre l'id de la fleur et le type de la fleur
            graph.create(relIdVersi)
        elif "Iris-versicolor" in lstspec: #Si Iris-versicolor n'est pas dans lstspec, pas besoin de recréer le noeud
            relIdVersi = Relationship(nodeId, "type", nodeVersi) #On créé seulement la relation
            graph.create(relIdVersi)

        fct.createGraph(df,nodeId,i,dictCm)

    elif (df.iloc[i,[5]]).values == "Iris-setosa": #Si la fleur est de type setosa
        if "Iris-setosa" not in lstspec: #Si iris-setosa est dans lstspec
            lstspec.append("Iris-setosa") #On ajoute le Species dans lstspec
            nodeSeto = Node("Species", name="Iris-setosa") #Créé un noeud Iris-setosa
            relIdSeto = Relationship(nodeId, "type", nodeSeto) #Fait la relation entre l'id de la fleur et le type de la fleur
            graph.create(relIdSeto)
        elif "Iris-setosa" in lstspec:#Si Iris-setosa n'est pas dans lstspec, pas besoin de recréer le noeud
            relIdSeto = Relationship(nodeId, "type", nodeSeto)#On créé seulement la relation
            graph.create(relIdSeto)

        fct.createGraph(df, nodeId, i, dictCm)

    elif (df.iloc[i,[5]]).values == "Iris-virginica": #Si la fleur est de type virginica
        if "Iris-virginica" not in lstspec: #Si iris-virginica est dans lstspec
            lstspec.append("Iris-virginica") #On ajoute le Species dans lstspec
            nodeVirgi = Node("Species", name="Iris-virginica") #Créé un noeud Iris-virginica
            relIdVirgi = Relationship(nodeId, "type", nodeVirgi) #Fait la relation entre l'id de la fleur et le type de la fleur
            graph.create(relIdVirgi)
        elif "Iris-virginica" in lstspec:#Si Iris-virginica n'est pas dans lstspec, pas besoin de recréer le noeud
            relIdVirgi = Relationship(nodeId, "type", nodeVirgi)#On créé seulement la relation
            graph.create(relIdVirgi)

        fct.createGraph(df, nodeId, i, dictCm)
