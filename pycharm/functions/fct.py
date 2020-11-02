import math
import pandas as pd
import logging
logging.basicConfig(filename='LOGTEST.log', level=logging.INFO)

def dfcsv(dataframe,csv):
    dataframe=pd.read_csv(dataframe,sep=csv)
    return dataframe

def listeType(dataframe):
        print(dataframe.dtypes)

def control(dataframe,p):
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
    dataframe = dataframe.astype({colonne:x})
    return dataframe

def convertNAN(dataframe,x):
    y=dataframe[x].dtypes
    if y != float:
        dataframe[x]=math.nan
        print("CONVERTER EFFECTUE")
        print(dataframe[x])
    else: print ("CONVERTER IMPOSSIBLE DTYPES =",(dataframe[x].dtypes))
    return dataframe

def NONENAN(dataframe, colonne,x):
    dataframe.loc[(dataframe[colonne]==x),colonne]=math.nan
    return dataframe

def moyenneCOLONNE(dataframe,colonne):
    """

    :param dataframe: pandas.dataframe
    :param colonne: nom de colonne en string
    :return:
    """
    moy=dataframe[colonne].mean()
    dataframe[colonne]=dataframe[colonne].fillna(moy)
    return dataframe

#dataframe.loc[(dataframe[colonne]=='None'),colonne]=math.nan


def remplacevaleurcolonne(dataframe,x,y,colonne,z):
    """

    :param dataframe: pandas.dataframe
    :param colonne: nom de colonne en string
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