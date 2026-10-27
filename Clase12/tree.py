import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


#cargar los datos
df = pd.read_csv("Titanic-Dataset.csv")

#print(df.head())

#Primer laburo que tenemos hacer: porque no todos los datos son relevantes, para saber la etiqueta de un dato. Nuestro trabajo es limitarlo, es filtrarlo
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]

x = df[features].copy()

#Definomos que queremos predecir
y = df["Survived"]

#mapemos de categoria a numero, para que sea más rapdido seleccionar si era hombre/mujer con numeros
x["Sex"] = x["Sex"].map({
    "male":0,
    "female":1
})

#print(x.head())

#Ahora sacamos el promedio de la edad para ver que más podemos limpiar. Llenamos valores faltantes de la edad con la mediana
x["Age"] = x["Age"].fillna(x["Age"].median())

x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state = 214159,
    stratify = y
)

model = DecisionTreeClassifier(
    random_state= 1414213,
    max_depth=3
)

#model.fit(x_train, y_train)

#plt.figure(figsize=(22,12))

#plot_tree(
    #model,
    #ture_names=features,
    #class_names=["No sobrevivio", "Si sobrevivio"],
   # filled=True,
  #  rounded=True,
 #   fontsize=9
#
#)

#plt.show()

#y_pred = model.predict(x_test)

#print(accuracy_score(y_test, y_pred))


params = {
    "max_depth": [2,3,4,5,8,None],
    "min_samples_split":[2,10,20],
    "min_samples_leaf":[1,5,10],
    "criterion":["gini","entropy"]
}

search = GridSearchCV(
    estimator = model,
    param_grid = params,
    cv = 5,
    scoring = "accuracy",
    n_jobs = -1,
)

search.fit(x_train,y_train)

print(search.best_params_)

print(search.best_score_)

print(search.best_estimator_.score(x_test,y_test))

#plt.figure(figsize=(22,12))

plt.figure(figsize=(16, 8))
plot_tree(
    search.best_estimator_,
    feature_names=features,
    class_names=["No sobrevivio", "Si sobrevivio"],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.show()

y_pred = model.predict(x_test)

print(accuracy_score(y_test, y_pred))
