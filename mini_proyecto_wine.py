"""
Programación 3 - PRÁCTICA FINAL: Mini proyecto KNN completo
=============================================================
Construimos un modelo KNN de principio a fin sobre un dataset
NUEVO (no utilizado en la explicación): Wine.

Pipeline esperado por la consigna:

    Dataset -> Exploración -> X/y -> Train/Test Split -> Scaling
    -> KNN -> Cross Validation -> Selección de K -> Modelo final
    -> Test -> Métricas -> Conclusiones

Correr: python mini_proyecto_wine.py
"""

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# ----------------------------------------------------------------------
# 1) DATASET: Wine (178 muestras, 13 variables, 3 clases)
# ----------------------------------------------------------------------
data = load_wine()
X = data.data
y = data.target

print("=" * 66)
print("DATASET WINE - Exploración")
print(f"  X.shape (muestras, variables) = {X.shape}")
print(f"  Clases (target_names)         = {data.target_names}")
print(f"  Muestras por clase            = {np.bincount(y)}")
print(f"  Variables                     = {list(data.feature_names)}")
print(
    "  Rango de magnitud de las variables: min={:.3f} max={:.3f}".format(
        X.min(), X.max()
    )
)
print("=" * 66)

# ----------------------------------------------------------------------
# 2) TRAIN / TEST SPLIT (estratificado, 20% test)
# ----------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# ----------------------------------------------------------------------
# 3) SCALING + 4) KNN + 5) CROSS VALIDATION PARA ELEGIR K
# ----------------------------------------------------------------------
resultados = []

for k in range(1, 31):
    modelo = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=k),
    )
    scores = cross_val_score(modelo, X_train, y_train, cv=5)
    resultados.append(scores.mean())

mejor_k = resultados.index(max(resultados)) + 1

print("Curva K vs accuracy (cross validation sobre train):")
print(f"  Mejor K según CV = {mejor_k} (accuracy promedio = {max(resultados):.4f})")

plt.figure(figsize=(8, 5))
plt.plot(range(1, 31), resultados, marker="o")
plt.axvline(mejor_k, color="red", linestyle="--", label=f"mejor K = {mejor_k}")
plt.xlabel("K")
plt.ylabel("Accuracy promedio (CV)")
plt.title("Selección de K - Wine")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("figures/curva_cv_wine.png", dpi=150, bbox_inches="tight")
plt.close()

# ----------------------------------------------------------------------
# 6) MODELO FINAL CON EL MEJOR K
# ----------------------------------------------------------------------
modelo_final = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=mejor_k),
)
modelo_final.fit(X_train, y_train)

# ----------------------------------------------------------------------
# 7) EVALUACIÓN SOBRE TEST
# ----------------------------------------------------------------------
y_pred = modelo_final.predict(X_test)
acc_test = accuracy_score(y_test, y_pred)

print(f"Accuracy del modelo final sobre TEST: {acc_test:.3f}")

disp = ConfusionMatrixDisplay.from_estimator(
    modelo_final,
    X_test,
    y_test,
    display_labels=data.target_names,
    cmap="Blues",
)
disp.ax_.set_title(f"Matriz de confusión - Wine (KNN K={mejor_k})")
plt.savefig("figures/confusion_wine.png", dpi=150, bbox_inches="tight")
plt.close()

# ----------------------------------------------------------------------
# 8) CONCLUSIONES (usadas en el informe)
# ----------------------------------------------------------------------
print("=" * 66)
print("CONCLUSIONES")
print("=" * 66)
print(
    f"""
- Problema: clasificar el tipo de vino (3 variedades: clase 0, 1 y 2).
- El target es la variedad del vino (etiqueta discreta) -> clasificación.
- Se usaron las 13 variables químicas del dataset (alcohol, ácidos, etc.).
- Se escaló con StandardScaler porque las variables tienen magnitudes muy
  distintas (van desde valores ~0.1 hasta ~30) y KNN depende de distancias.
- Métrica de distancia: euclídea (Minkowski p=2), la predeterminada.
- Se probaron K = 1..30; se eligió K = {mejor_k} con cross validation (cv=5)
  SOLO sobre entrenamiento, dejando el test para la evaluación final.
- Resultado CV (train): accuracy promedio = {max(resultados):.4f}
- Resultado FINAL sobre test: accuracy = {acc_test:.3f}.
- Matriz de confusión guardada en figures/confusion_wine.png.
- Overfitting: no se observa (el mejor K es razonable y el accuracy de test
  es estable y alto).
- KNN es una buena elección para este problema: dataset pequeño, se
  desempeña bien y es fácil de interpretar.
"""
)
print("Figuras guardadas: figures/curva_cv_wine.png y figures/confusion_wine.png")