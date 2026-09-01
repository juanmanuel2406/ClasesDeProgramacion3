"""
Programa 3 - Ejercicio de REGRESION
===================================
Regresion = prediccion de un valor CONTINUO (un numero),
a diferencia de la clasificacion que predice una categoria.

Situacion (ejemplo real de negocio):
    Queremos predecir el PRECIO de una casa a partir de sus
    datos (features). El target es continuo: el precio en dolares.

Dataset: "california housing" (incluido en scikit-learn)
    - ~20.000 samples (casas)
    - 8 features  (anios de la zona, ingresos, habitantes, etc.)
    - target      = precio medio de la casa (continuo)

Ideas clave que ya vimos y que aplican aca:
    - X = features  [n_samples, n_features]
    - y = target    [n_samples]
    - train_test_split (NO usar el mismo set para entrenar y probar)
    - fit -> entrenar, predict -> predecir datos nuevos
    - El Error Medio Absoluto (MAE) mide cuan lejos anduvimos.

Correr: .\\venv\\Scripts\\python.exe regresion.py
"""

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# ----------------------------------------------------------------------
# 1) CARGAR DATASET
# ----------------------------------------------------------------------
print("Descargando/leyendo dataset...")
datos = fetch_california_housing()
X = datos.data        # features
y = datos.target      # target: precio de la casa (en decenas de miles USD)
print("Features (X):", X.shape)
print("Target (y):", y.shape)
print("Nombres de features:", datos.feature_names, "\n")

# ----------------------------------------------------------------------
# 2) SEPARAR TRAINING / TESTING
# ----------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,        # 20% para testing
    random_state=42,
)

print("Training:", X_train.shape)
print("Testing:", X_test.shape, "\n")

# ----------------------------------------------------------------------
# 3) MODELO (regresion lineal) + TRAINING + PREDICCION
# ----------------------------------------------------------------------
modelo = LinearRegression()
modelo.fit(X_train, y_train)          # aprende del pasado (etiquetado)

predicciones = modelo.predict(X_test) # predice precios de casas NUEVAS

# ----------------------------------------------------------------------
# 4) EVALUACION (errores: mientas mas chicos, mejor)
# ----------------------------------------------------------------------
mae = mean_absolute_error(y_test, predicciones)   # error medio absoluto
mse = mean_squared_error(y_test, predicciones)    # error cuadratico medio

print(f"Error Medio Absoluto (MAE):  {mae:.4f}  (en decenas de miles de USD)")
print(f"Error Cuadratico Medio (MSE): {mse:.4f}")

# Convertimos a dolares para que sea mas entendible
print(f"\nEn dolares: el modelo se equivoca en promedio por ~${mae*10000:,.0f}")
print(f"Precio promedio real de una casa: ~${y.mean()*10000:,.0f}\n")

# ----------------------------------------------------------------------
# 5) Mostrar algunas predicciones vs el precio real
# ----------------------------------------------------------------------
print("Primeros 5 del testing (precio real vs predicho):")
for real, pred in zip(y_test[:5], predicciones[:5]):
    print(f"  Real ${real*10000:>10,.0f}  |  Predicho ${pred*10000:>10,.0f}")

# ----------------------------------------------------------------------
# 6) Comparar: regresion NO es clasificacion.
#    La "precision" no aplica igual; usamos la distancia del error.
#    R^2 (coeficiente de determinacion): 1 = perfecto, 0 = promedio.
# ----------------------------------------------------------------------
r2 = modelo.score(X_test, y_test)
print(f"\nR^2 (que tan bien explica el modelo la variacion): {r2:.2f}")
