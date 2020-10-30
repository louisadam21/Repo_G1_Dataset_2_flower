import math
import pandas as pd
import logging
logging.basicConfig(filename='LOGTEST.log', level=logging.INFO)

def dfcsv(dataframe,csv):
    dataframe=pd.read_csv(dataframe,sep=csv)
    return dataframe

def counts(dataframe,liste):
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return:
    """
    for i in liste:
        countcolumn=dataframe[i].value_counts()
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



def moyenne(dataframe,colonne):
    """

    :param dataframe: pandas.dataframe
    :param colonne: nom de colonne en string
    :return:
    """
    dataframe.loc[(dataframe[colonne]=='None'),colonne]=math.nan
    dataframe = dataframe.astype({colonne: float})
    moy=dataframe[colonne].mean()
    dataframe[colonne]=dataframe[colonne].fillna(moy)
    return dataframe


def nettoyage(dataframe,colonne):
    """

    :param dataframe: pandas.dataframe
    :param colonne: nom de colonne en string
    :return:
    """
    dataframe[colonne] = math.nan
    for i in dataframe.axes[0]:
        dataframe[colonne][i] = i+1
    dataframe = dataframe.astype({colonne: int})
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