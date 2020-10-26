import math

def counts(dataframe,liste):
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return:
    """
    for i in liste:
        countcolumn=dataframe[i].value_counts()
        print(countcolumn)
    return countcolumn

def drop(dataframe,liste):
    """

    :param dataframe: pandas.dataframe
    :param liste: string
    :return:
    """
    for i in liste:
        dataframe.drop(i,axis=1)
    print(dataframe)
    return

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
    print(dataframe)
    return


def nettoyage(dataframe,colonne):
    """

    :param dataframe: pandas.dataframe
    :param colonne: nom de colonne en string
    :return:
    """
    dataframe[colonne] = math.nan
    for i in dataframe.axes[0]:
        dataframe[colonne][i] = i+1
    dataframe=dataframe.astype({colonne: int})
    print(dataframe)
    return