"""
Programación 3 - PRÁCTICA 4: Encontrar el mejor K
==================================================
Usamos Cross Validation SOLO sobre el conjunto de entrenamiento
para elegir K. El conjunto de test queda reservado exclusivamente
para la evaluación final del modelo elegido.

Correr: python practica4_mejor_k.py
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# ----------------------------------------------------------------------
# 1) DATOS Y SEPARACIÓN
# ----------------------------------------------------------------------
X, y = make_moons(n_samples=300, noise=0.25, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# ----------------------------------------------------------------------
# 2) CROSS VALIDATION (k = 1..30) SOBRE TRAIN
# ----------------------------------------------------------------------
resultados = []

for k in range(1, 31):
    modelo = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=k),
    )

    scores = cross_val_score(modelo, X_train, y_train, cv=5)
    resultados.append(scores.mean())

# ----------------------------------------------------------------------
# 3) MEJOR K SEGÚN EL PROMEDIO DE VALIDACIÓN CRUZADA
# ----------------------------------------------------------------------
mejor_k = resultados.index(max(resultados)) + 1

print("=" * 56)
print(f"{'K':>4} | {'Accuracy promedio (CV)':>22}")
print("-" * 56)
for k, valor in enumerate(resultados, start=1):
    marca = "  <-- mejor" if k == mejor_k else ""
    print(f"{k:>4} | {valor:>22.4f}{marca}")
print("=" * 56)
print(f"Mejor K segun Cross Validation (train): K = {mejor_k}")

# ----------------------------------------------------------------------
# 4) EVALUACIÓN FINAL CON EL MEJOR K SOBRE TEST
# ----------------------------------------------------------------------
modelo_final = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=mejor_k),
)
modelo_final.fit(X_train, y_train)
acc_test = modelo_final.score(X_test, y_test)

print(f"Accuracy del modelo final sobre TEST: {acc_test:.3f}")

# ----------------------------------------------------------------------
# 5) GRÁFICO DE LA CURVA
# ----------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(range(1, 31), resultados, marker="o")
plt.axvline(mejor_k, color="red", linestyle="--", label=f"mejor K = {mejor_k}")
plt.xlabel("K")
plt.ylabel("Accuracy promedio (cross validation)")
plt.title("Elección de K con Cross Validation")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("figures/curva_cv_knn.png", dpi=150, bbox_inches="tight")
plt.close()

print("Figura guardada: figures/curva_cv_knn.png")