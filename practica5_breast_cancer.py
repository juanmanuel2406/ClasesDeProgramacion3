"""
Programación 3 - PRÁCTICA 5: Dataset real Breast Cancer Wisconsin
=================================================================
Pipeline completo con KNN (K = 5) sobre un dataset real de
clasificación binaria (tumor benigno / maligno), evaluado con
accuracy y matriz de confusión.

Correr: python practica5_breast_cancer.py
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# ----------------------------------------------------------------------
# 1) CARGA Y EXPLORACIÓN DEL DATASET
# ----------------------------------------------------------------------
data = load_breast_cancer()

X = data.data
y = data.target

print("=" * 56)
print("Breast Cancer Wisconsin")
print(f"  X.shape        = {X.shape}")
print(f"  y.shape        = {y.shape}")
print(f"  target_names   = {data.target_names}")
print(f"  feature_names  = {list(data.feature_names[:5])} ...")
print("=" * 56)

# ----------------------------------------------------------------------
# 2) SEPARACIÓN CON ESTRATIFICACIÓN (test = 20%)
# ----------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# ----------------------------------------------------------------------
# 3) MODELO: PIPELINE = STANDARDSCALER + KNN (K=5)
# ----------------------------------------------------------------------
modelo = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5),
)
modelo.fit(X_train, y_train)

# ----------------------------------------------------------------------
# 4) PREDICCIÓN Y EVALUACIÓN
# ----------------------------------------------------------------------
y_pred = modelo.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"Accuracy sobre TEST: {acc:.3f}")

# ----------------------------------------------------------------------
# 5) MATRIZ DE CONFUSIÓN
# ----------------------------------------------------------------------
disp = ConfusionMatrixDisplay.from_estimator(
    modelo,
    X_test,
    y_test,
    display_labels=data.target_names,
    cmap="Blues",
)
disp.ax_.set_title("Matriz de confusión - Breast Cancer (KNN K=5)")
plt.savefig("figures/confusion_breast.png", dpi=150, bbox_inches="tight")
plt.close()

print("Figura guardada: figures/confusion_breast.png")