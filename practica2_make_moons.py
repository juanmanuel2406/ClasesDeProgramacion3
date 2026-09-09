"""
Programación 3 - PRÁCTICA 2: Visualizando KNN con Make Moons
=============================================================
Visualizamos las fronteras de decisión de KNN sobre un dataset
sintético en forma de dos lunas (make_moons).

Consigna:
    - Visualizar el dataset.
    - Separar los datos en train y test.
    - Entrenar KNN con K = 1, 3, 5, 15 y 50.
    - Comparar el accuracy.
    - Visualizar las fronteras de decisión.

Correr: python practica2_make_moons.py
"""

import matplotlib
matplotlib.use("Agg")  # sin ventana, guardamos las figuras en disco

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def graficar_frontera(ax, modelo, X, y, titulo):
    """Dibuja la frontera de decisión del modelo sobre el plano X1-X2."""
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 300),
        np.linspace(y_min, y_max, 300),
    )
    Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.3, cmap="viridis")
    ax.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", cmap="viridis", s=15)
    ax.set_title(titulo)
    ax.set_xlabel("X1")
    ax.set_ylabel("X2")


# ----------------------------------------------------------------------
# 1) DATASET SINTÉTICO MAKE MOONS
# ----------------------------------------------------------------------
X, y = make_moons(n_samples=300, noise=0.25, random_state=42)

plt.figure(figsize=(5, 5))
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", cmap="viridis")
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Dataset make_moons (300 muestras, noise=0.25)")
plt.savefig("figures/datos_make_moons.png", dpi=150, bbox_inches="tight")
plt.close()

# ----------------------------------------------------------------------
# 2) SEPARAR TRAIN / TEST
# ----------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# ----------------------------------------------------------------------
# 3) ENTRENAR KNN CON DISTINTOS K Y COMPARAR ACCURACY
# ----------------------------------------------------------------------
valores_k = [1, 3, 5, 15, 50]

print("=" * 56)
print(f"{'K':>4} | {'Acc train':>10} | {'Acc test':>10}")
print("-" * 56)

fig, ejes = plt.subplots(1, len(valores_k), figsize=(18, 3.5))

for i, k in enumerate(valores_k):
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X_train, y_train)

    acc_train = modelo.score(X_train, y_train)
    acc_test = modelo.score(X_test, y_test)

    print(f"{k:>4} | {acc_train:>10.3f} | {acc_test:>10.3f}")
    graficar_frontera(ejes[i], modelo, X, y, f"K = {k}")

plt.tight_layout()
plt.savefig("figures/fronteras_knn.png", dpi=150, bbox_inches="tight")
plt.close()

print("=" * 56)
print(
    "Figuras guardadas:\n"
    "  - figures/datos_make_moons.png\n"
    "  - figures/fronteras_knn.png"
)