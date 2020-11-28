import math
import pandas as pd
import logging
logging.basicConfig(filename='test_log.log',level=logging.INFO,format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
from py2neo import Node, Relationship,Graph
graphFlower = Graph("bolt://localhost:7687", auth=None)

def dfcsv(chemin,separ): #Fonction qui permet de lire un csv et le convertir en dataframe
    """

    :param chemin: string(url)
    :param separ: pandas.dataframe
    :return: dataframe
    """
    dataframe = pd.read_csv(chemin, sep=separ)

    return dataframe

def counts(dataframe, liste): #Fonction qui permet de verifier le contenu des champs du dataframe
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return:
    """
    logging.info("Fct counts")
    for i in liste:
        countColumn = dataframe[i].value_counts() # Permet d'analyser les données des colonnes de la liste.
        print(countColumn)
    logging.info("Contenu de la liste"+liste)
    return


def dropColumns(dataframe, liste): #Permet de supprimer les colonnes inutiles
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return: dataframe
    """
    logging.info("Fct dropColumns")
    col=[]
    for i in liste:
        col.append(i)
    logging.info("Contenu de la variable col")
    logging.info(col)
    dataframe=dataframe.drop(col, axis=1) # Supprime les colonnes présentes dans liste
    return dataframe


def cleanCol(dataframe, colonne): #Fonction qui permet de nettoyer la ou les colonnes exploitables
    """

    :param dataframe: pandas.Dataframe
    :param colonne: string
    :return: dataframe
    """
    logging.info("Fct cleanCol")
    dataframe.loc[(dataframe[colonne] == 'None'), colonne] = math.nan #remplace les None par NaN dans les colonnes saisies
    dataframe=dataframe.astype({colonne: float}) # Convertit tout en float
    moy = dataframe[colonne].mean() # Avoir la moyenne de la colonne
    dataframe[colonne] = dataframe[colonne].fillna(moy) # Remplace les Nan par la moyenne
    logging.info("Moyenne :")
    logging.info(moy)
    return dataframe

def cleanId(dataframe,colonne): #Fonction qui permet de rendre la colonne Id exploitable et pertinente
    """

    :param dataframe: pandas.Dataframe
    :param colonne: liste
    :return: dataframe
    """

    for i in dataframe.axes[0]:
        dataframe[colonne][i] = i + 1
    dataframe=dataframe.astype({colonne: int})
    logging.info("Fct cleanId")
    return dataframe

def isNan(dataframe): #Fonction qui permet de voir les lignes contenant Nan
    """

    :param dataframe: pandas.Dataframe
    :return:
    """

    is_NaN = dataframe.isnull()
    row_has_NaN = is_NaN.any(axis=1)
    rows_with_NaN = dataframe[row_has_NaN]
    isempty = rows_with_NaN.empty
    print(rows_with_NaN)
    print("Le dataset ne contient pas de Nan :", isempty)
    return

def createGraph(dataframe,nodeId,idx,dico): #Fonction qui permet la création de la relation entre l'Id de la fleur et les tailles de petales,sépales
    """

    :param dataframe: pandas.Dataframe
    :param nodeId: int
    :param idx: int
    :param dico: dictionnary
    :return:
    """
    for key,value in dico.items(): #Parcourt le dictionnaire
        graphFlower.create(Relationship(nodeId, key, Node(key, name=dataframe.iloc[idx, value])))
    return