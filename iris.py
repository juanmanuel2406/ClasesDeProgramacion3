"""
Programa 3 - Clasificacion con el dataset IRIS
==============================================
Dataset de las flores (Iris), el mas clasico para aprender ML.

Idea central:
    Aprender del PASADO (flores ya clasificadas) para predecir
    la especie de flores NUEVAS (no etiquetadas).

Dataset IRIS:
    - 150 samples = 150 flores (cada fila es una flor)
    - 4 features  = sepal_length, sepal_width, petal_length, petal_width
    - target      = especie: setosa(0), versicolor(1), virginica(2)

Correr: .\\venv\\Scripts\\python.exe iris.py
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ----------------------------------------------------------------------
# 1) CARGAR EL DATASET (viene incluido en scikit-learn)
# ----------------------------------------------------------------------
iris = load_iris()
X = iris.data          # features matrix [150, 4]
y = iris.target        # target array [150]

print("Features (X):", X.shape)
print("Target (y):", y.shape)
print("Especies:", iris.target_names, "\n")

# ----------------------------------------------------------------------
# 2) SEPARAR TRAINING / TESTING
# ----------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.30,      # 30% para testing (datos que el modelo nunca vera)
    random_state=42,
    stratify=y,          # mantiene la misma proporcion de cada especie
)

print("Training:", X_train.shape)
print("Testing:", X_test.shape, "\n")

# ----------------------------------------------------------------------
# 3) MODELO + TRAINING + PREDICCION
# ----------------------------------------------------------------------
modelo = LogisticRegression(max_iter=200)
modelo.fit(X_train, y_train)          # aprende del pasado (etiquetado)

predicciones = modelo.predict(X_test) # predice flores nuevas (no etiquetadas)

# ----------------------------------------------------------------------
# 4) EVALUACION: puntaje de precision
# ----------------------------------------------------------------------
precision = accuracy_score(y_test, predicciones)
print(f"Precision (accuracy): {precision:.1%}\n")

# Mostramos las primeras flores de testing: real vs predicha
print("Primeros 10 del set de testing:")
print("  Real     :", iris.target_names[y_test[:10]])
print("  Predicha :", iris.target_names[predicciones[:10]])
