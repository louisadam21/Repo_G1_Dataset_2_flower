
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

def algopred(dataframe,xloc1,xloc2,xloc3,tsize,choixalgo,liste):

    x=dataframe.iloc[:, xloc1 : xloc2]
    y=dataframe.iloc[:, xloc3]
    # Sépare de dataset en 2 sets training et test
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=tsize)  # 70% training et 30% test
    if choixalgo == "rf":
        clf = RandomForestClassifier()  # Utilisation de 10 arbres dans la forêt
        param_grid = {'n_estimators': liste}
        search = GridSearchCV(clf, param_grid,verbose=1)
        search.fit(x_train, y_train)
    elif choixalgo == "lg":
        clf = LogisticRegression()
    #clf.fit(x_train, y_train)

    y_pred = search.predict(x_test)

    print("Accuracy {:.10f}".format(accuracy_score(y_test, y_pred)))
    return