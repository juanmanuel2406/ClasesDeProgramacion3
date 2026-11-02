from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


wine = load_wine()

X = wine.data
Y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.25,
    random_state=314159,
    stratify=Y
)

model = GaussianNB()

model.fit(X_train, y_train)

y_prod = model.predict(X_test)

print(accuracy_score(y_test, y_prod))

print(confusion_matrix(y_test, y_prod))

print(classification_report(
    y_test,
    y_prod,
    target_names=wine.target_names
))
