from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = load_iris()

#print(iris)
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=314159,
    stratify = Y
)

#print(X.shape)

model = KNeighborsClassifier(n_neighbors=25)

#model.fit(X,Y)

model.fit(X_train, Y_train)

#y_prec = model.predict([[2.3,2.0,4.0,1.5]])

#print(y_prec)

y_model = model.predict(X_test)

print(accuracy_score(Y_test,y_model))