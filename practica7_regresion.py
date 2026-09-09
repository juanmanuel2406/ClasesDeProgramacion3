"""
Programación 3 - PRÁCTICA 7: KNN Regression
============================================
Usamos KNN para REGRESIÓN sobre una función seno con ruido.

En regresión KNN no vota: predice el PROMEDIO del target de los
K vecinos más cercanos.

Probamos K = 1, 5 y 20 y comparamos las curvas de predicción.

Correr: python practica7_regresion.py
"""

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor


# ----------------------------------------------------------------------
# 1) DATOS SINTÉTICOS: SENO + RUIDO
# ----------------------------------------------------------------------
X = np.linspace(0, 10, 100).reshape(-1, 1)

rng = np.random.default_rng(42)  # reproducible
y = np.sin(X).ravel() + rng.normal(0, 0.2, 100)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# ----------------------------------------------------------------------
# 2) ENTRENAR KNN REGRESSOR CON K = 1, 5 Y 20
# ----------------------------------------------------------------------
valores_k = [1, 5, 20]

print("=" * 56)
print(f"{'K':>4} | {'MAE sobre test':>14}")
print("-" * 56)

fig, ejes = plt.subplots(1, len(valores_k), figsize=(15, 4), sharey=True)

for i, k in enumerate(valores_k):
    modelo = KNeighborsRegressor(n_neighbors=k)
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    mae = np.mean(np.abs(y_test - y_pred))

    print(f"{k:>4} | {mae:>14.3f}")

    # ordenamos X_test para dibujar la curva sin "zigzag"
    orden = np.argsort(X_test.ravel())
    ejes[i].scatter(X_test, y_test, alpha=0.5, label="test real")
    ejes[i].plot(X_test[orden], y_pred[orden], color="red", label="predicción")
    ejes[i].set_title(f"K = {k}  (MAE = {mae:.3f})")
    ejes[i].set_xlabel("X")
    ejes[i].legend()

ejes[0].set_ylabel("y")
plt.tight_layout()
plt.savefig("figures/regresion_knn.png", dpi=150, bbox_inches="tight")
plt.close()

print("=" * 56)
print(
    "\nAnalisis:\n"
    "  - K = 1  : la curva copia el ruido punto a punto -> OVERFITTING\n"
    "  - K = 20 : la curva se suaviza demasiado y pierde detalles -> UNDERFITTING\n"
    "  - K = 5  : punto intermedio razonable."
)
print("Figura guardada: figures/regresion_knn.png")