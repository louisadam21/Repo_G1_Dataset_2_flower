import math
import pandas as pd
import logging
logging.basicConfig(filename='LOGTEST.log', level=logging.INFO)
from py2neo import Graph,Node, Relationship
graph=Graph("http://localhost:7474/", auth=None)

def dfcsv(dataframe,csv):
    """

    :param dataframe: pandas.dataframe
    :param csv: type de dataframe
    :return: dataframe
    """
    dataframe=pd.read_csv(dataframe,sep=csv)
    return dataframe

def listeType(dataframe):
    """

    :param dataframe: pandas.dataframe
    :return:
    """
    print(dataframe.dtypes)

def control(dataframe,p):
    """

    :param dataframe: pandas.dataframe
    :param p:
    :return:
    """
    if p == "isnull":
        print(dataframe.isnull().any())
    if p == "isna":
        print(dataframe.isna().any())


def counts(dataframe,liste):
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return:
    """
    for i in liste:
        dataframe[i].value_counts()
        #print(countcolumn)
    return

def drop(dataframe,liste):
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return:
    """

    for i in liste:
        dataframe=dataframe.drop(i,axis=1)
    logging.info(liste)
    return dataframe

def convertTYPE(dataframe,colonne,x):
    """

    :param dataframe: pandas.dataframe
    :param colonne:
    :param x:
    :return:
    """
    dataframe = dataframe.astype({colonne:x})
    return dataframe

def convertNAN(dataframe,x):
    """

    :param dataframe: pandas.dataframe
    :param x: colone
    :return:
    """
    y=dataframe[x].dtypes
    if y != float:
        dataframe[x]=math.nan
        print("CONVERTER EFFECTUE")
        print(dataframe[x])
    else: print ("CONVERTER IMPOSSIBLE DTYPES =",(dataframe[x].dtypes))
    return dataframe

def NONENAN(dataframe, colonne,x):
    """

    :param dataframe: df
    :param colonne: nom de la colonne
    :param x:
    :return:
    """
    dataframe.loc[(dataframe[colonne]==x),colonne]=math.nan
    return dataframe

def moyenneCOLONNE(dataframe,colonne):
    """

    :param dataframe: df
    :param colonne: nom de la colonne
    :return:
    """
    moy=dataframe[colonne].mean()
    dataframe[colonne]=dataframe[colonne].fillna(moy)
    return dataframe

#dataframe.loc[(dataframe[colonne]=='None'),colonne]=math.nan


def remplacevaleurcolonne(dataframe,x,y,colonne,z):
    """

    :param dataframe: df
    :param x: colonnne dans le dataframme
    :param y: valeur ajouté
    :param colonne: nom de la colonne
    :param z: type de la colonne
    :return:
    """
    for i in dataframe.axes[x]:
        dataframe[colonne][i] = i+y
    dataframe = dataframe.astype({colonne:z})
    return dataframe
"""
def defrandomf(dataframe,xloc1,xloc2,xloc3,tsize,nb_arbre):
    

    :param dataframe:
    :param xloc1:
    :param xloc2:
    :param xloc3:
    :param tsize:
    :param nb_arbre:
    :return:

    x=dataframe.iloc[:, xloc1 : xloc2]
    y=dataframe.iloc[:, xloc3]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=tsize)
    clf = RandomForestClassifier(n_estimators=nb_arbre, oob_score=True)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    predrf=print("accuracy {:.10f}".format(accuracy_score(y_test, y_pred)))
    return predrf
"""

def createGraph(dataframe,nodeId,idx,dico): #Fonction qui permet la création de la relation entre l'Id de la fleur et les tailles de petales,sépales
    """
    :param dataframe: pandas.Dataframe
    :param nodeId: int
    :param idx: int
    :param dico: dictionnary
    :return:
    """
    for key,value in dico.items(): #Parcourt le dictionnaire
        graph.create(Relationship(nodeId, key, Node(key, name=dataframe.iloc[idx, value])))
    return