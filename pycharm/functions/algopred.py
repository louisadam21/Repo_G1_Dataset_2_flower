from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

def algodf(colx,coly,tsize,choixalgo,nesti):

    # Sépare de dataset en 2 sets training et test
    x_train, x_test, y_train, y_test = train_test_split(colx, coly, test_size=tsize)  #Proportion de test et train
    if choixalgo == "rf":
        clf = RandomForestClassifier()
        param_grid = {'n_estimators': nesti} #Nb d'arbres dans le Random Forest
        search = GridSearchCV(clf, param_grid,verbose=1)
        search.fit(x_train, y_train)
    elif choixalgo == "lg":
        clf = LogisticRegression()

    y_pred = search.predict(x_test)

    print("Accuracy {:.10f}".format(accuracy_score(y_test, y_pred)))
    return

