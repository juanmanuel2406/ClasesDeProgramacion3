import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"

df = pd.read_csv(
    url,
    compression="zip",
    sep="\t",
    header=None,
    names=["label","message"],
    encoding="utf-8"
)

#print(df["label"].value_counts())

x = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=314159,
    stratify=y
)

vectorizer = CountVectorizer()

X_train_vect = vectorizer.fit_transform(X_train)

X_test_vect = vectorizer.transform(X_test)

#print(X_train_vect.shape)

model = MultinomialNB()
model.fit(X_train_vect, y_train)

y_predict = model.predict(X_test_vect)

#print(y_predict[:10])

print(accurasy_score(y_test, y_predict))
print(confusion_matrix(y_test, y_predict))

mensajes = [
    "Congratulations! You won a Free Prize, Claim Now!!"
    "Hello, lets meet tommorow morning",
    "I won a prize! im very glad!"
]

mensajes_vect = vectorizer.transform(mensajes)

prediccion = model.predict(mensajes_vect)

print(prediccion)
