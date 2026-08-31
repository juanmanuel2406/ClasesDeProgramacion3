"""
Programación 3 - Machine Learning con Scikit-Learn
==================================================
Ejemplo: predicción de abandono de clientes bancarios (churn prediction).

Idea central:
    Aprender del PASADO (datos etiquetados) para predecir o tomar
    mejores decisiones en el FUTURO (datos no etiquetados).

Conceptos que se muestran:
    - Dataset bidimensional: filas = samples, columnas = features
    - X (features matrix: [n_samples, n_features])
    - y (target array: la columna que queremos predecir)
    - train_test_split (separar training / testing)
    - model.fit()  -> training (aprende patrones del pasado)
    - model.predict() -> predice el target de datos nuevos
    - score() -> puntaje de precisión (evaluación)
    - Los hiperparámetros son las "perillas" del modelo

Correr desde PowerShell (en la raiz del proyecto):
    .\\.venv\\Scripts\\python.exe churn_prediction.py
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# ----------------------------------------------------------------------
# 1) DATOS: representados como tabla -> filas y columnas
#
#    sample(fila)  Antiguedad  Ciudad  Periodos  Edad  Deudas  | se_fue(target)
#    Cliente 1         2        0       24       30    5000    |     1
#    Cliente 2         5        1       60       45       0    |     0
#    Cliente 3         1        2       12       25   12000    |     1
#    ...
#
#    - filas     = samples (clientes)
#    - columnas  = features (datos en los que nos basamos)
#    - 'se_fue'  = target (lo que queremos PREDECIR)
# ----------------------------------------------------------------------

# Simulamos 1000 clientes con un patron REAL escondido:
#   - a MAS deudas, MAS probable que se vaya
#   - a MENOS antiguedad, MAS probable que se vaya
# Las features tienen algo de ruido, para que sea realista (no trivial).

rng = np.random.default_rng(42)
n_clientes = 1000
X = rng.integers(1, 9, size=(n_clientes, 1))       # Antiguedad (1 a 8 anios)
X = np.hstack([X, rng.integers(0, 3, size=(n_clientes, 1))])  # Ciudad 0,1,2
X = np.hstack([X, rng.integers(6, 100, size=(n_clientes, 1))])  # Periodos
X = np.hstack([X, rng.integers(18, 70, size=(n_clientes, 1))])  # Edad
X = np.hstack([X, rng.integers(0, 25000, size=(n_clientes, 1))])  # Deudas

# Target: 1 = se fue, 0 = no se fue
# Probabilidad de irse crece con las deudas y baja con la antiguedad.
deuda  = X[:, 4]
anios  = X[:, 0]
prob_irse = np.clip(0.05 + deuda / 30000 - anios / 20, 0, 1)
y = (rng.random(n_clientes) < prob_irse).astype(int)

print("Forma del dataset (n_samples, n_features):", X.shape)
print("Target (n_samples,):", y.shape)
print("Cantidad de 'se fue' (1):", int(y.sum()), "| 'no se fue' (0):", int((y == 0).sum()), "\n")

# ----------------------------------------------------------------------
# 2) NUESTRO TRABAJO: filtrar / dejar un buen set de entrenamiento.
#
#    Dividimos en TRAINING (para que el modelo aprenda) y
#    TESTING (para evaluar como predice datos que NUNCA vio).
# ----------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,      # 25% para testing
    random_state=42,     # para que el resultado sea reproducible
)

print("Training - features:", X_train.shape, "- target:", y_train.shape)
print("Testing  - features:", X_test.shape, "- target:", y_test.shape, "\n")

# ----------------------------------------------------------------------
# 3) MODELO: la "identidad" / maquina con perillas (hiperparametros).
#
#    RandomForestClassifier es un modelo ya implementado por scikit-learn.
#    A este modelo LO ALIMENTAMOS con datos etiquetados (training).
#    (Despues podremos ajustar sus hiperparametros = el tuning)
# ----------------------------------------------------------------------
modelo = RandomForestClassifier()   # usa valores por default en las "perillas"

# ---------- TRAINING ----------
# El modelo aprende el patron entre X (pasado) e y (resultado observado).
modelo.fit(X_train, y_train)

# ---------- PREDICCION ----------
# Ahora entra el dato NO ETIQUETADO: conozco las features, NO el target.
# El modelo predice el target usando lo que aprendio en el training.
predicciones = modelo.predict(X_test)
print("Target real      :", y_test)
print("Target predicho  :", predicciones, "\n")

# ----------------------------------------------------------------------
# 4) EVALUACION: puntaje de precision (accuracy)
#    = cuantas veces acerto sobre el total del set de testing.
# ----------------------------------------------------------------------
precision = accuracy_score(y_test, predicciones)
print(f"Puntaje de precision (accuracy): {precision:.1%}")

# Tambien lo podemos pedir directo al modelo:
print(f"Score del modelo: {modelo.score(X_test, y_test):.1%}")
