import math
import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


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
    #for i in liste:
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
    dataframe[colonne] = math.nan
    for i in dataframe.axes[0]:
        dataframe[colonne][i] = i + 1
    dataframe=dataframe.astype({colonne: int})
    return dataframe

def rfdf(colx,coly,tsize,nbarb):


    # Sépare de dataset en 2 sets training et test
    x_train, x_test, y_train, y_test = train_test_split(colx, coly, test_size=tsize)  # 70% training et 30% test

    clf = RandomForestClassifier(n_estimators=nbarb, oob_score=True)  # Utilisation de 10 arbres dans la forêt

    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    print("Random forest accuracy {:.10f}".format(accuracy_score(y_test, y_pred)))
    return

def lgdf(colx,coly,tsize):

    x_train, x_test, y_train, y_test = train_test_split(colx, coly, test_size=tsize, random_state=42)  # Sépare le dataset en 2 sets train et test(20% du dataset)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    print("Logistic regression accuracy {:.10f}".format(accuracy_score(y_test,predictions)))  # Affiche la fiabilité de l'aglorithme de prédiction, plsu l'indice est proche de 1, plus                                                             l'algo est fiable
    return
