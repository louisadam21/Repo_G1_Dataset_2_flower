import math
import pandas as pd


def dfcsv(chemin,separ):
    dataframe = pd.read_csv(chemin, sep=separ)
    return dataframe

def counts(dataframe, liste):
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return: countColumns
    """
    for i in liste:
        countColumn = dataframe[i].value_counts() # Permet d'analyser les données des colonnes de la liste.
        print(countColumn)
    return


def dropColumns(dataframe, liste):
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return: countColumns
    """
    col=[]
    for i in liste:
        col.append(i)
    dataframe=dataframe.drop(col, axis=1) # Supprime les colonnes présentes dans liste
    return dataframe


def moyenne(dataframe, colonne):
    """

    :param dataframe: pandas.Dataframe
    :param colonne: string
    :return:
    """
    dataframe.loc[(dataframe[colonne] == 'None'), colonne] = math.nan #remplace les None par NaN dans les colonnes saisies
    dataframe=dataframe.astype({colonne: float}) # Convertit tout en float
    moy = dataframe[colonne].mean() # Avoir la moyenne de la colonne
    dataframe[colonne]=dataframe[colonne].fillna(moy) # Remplace les Nan par la moyenne

    return dataframe


def cleanId(dataframe,colonne):
    """

    :param dataframe: pandas.dataframe
    :return:
    """
    #dataframe[colonne] = math.nan
    for i in dataframe.axes[0]:
        dataframe[colonne][i] = i + 1
    dataframe=dataframe.astype({colonne: int})
    return dataframe