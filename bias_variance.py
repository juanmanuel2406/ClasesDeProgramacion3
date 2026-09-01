"""
Programa 3 - Bias-Variance Tradeoff
===================================
Muestra el tradeoff entre SESGO (bias) y VARIANZA.

- Modelo demasiado SIMPLE  (polinomio grado 1 = recta)  -> ALTO SESGO -> SUBJUSTA
- Modelo demasiado COMPLEJO (polinomio grado 20)        -> ALTA VARIANZA -> SOBREAJUSTA

El ejemplo es el del Python Data Science Handbook (seccion 05.03).

Correr: .\\venv\\Scripts\\python.exe bias_variance.py
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Datos con patron real + ruido (igual que el libro)
# ----------------------------------------------------------------------
def make_data(N=30, err=0.8, rseed=1):
    rng = np.random.RandomState(rseed)
    X = rng.rand(N, 1)
    y = 10 * X ** 3 + 3 * X + 2 + err * rng.randn(N)
    return X, y

# ----------------------------------------------------------------------
# Regresion polinomial usando scikit-learn
# ----------------------------------------------------------------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def PolynomialRegression(degree):
    return make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression(),
    )

X, y = make_data()

# ----------------------------------------------------------------------
# Entrenar dos modelos: uno muy simple y otro muy complejo
# ----------------------------------------------------------------------
xfit = np.linspace(-0.1, 1.0, 1000)[:, None]

model1 = PolynomialRegression(1).fit(X, y)     # recta        -> ALTO SESGO
model20 = PolynomialRegression(20).fit(X, y)   # polinomio 20 -> ALTA VARIANZA

# ----------------------------------------------------------------------
# Graficar ambos
# ----------------------------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

ax[0].scatter(X.ravel(), y, s=40)
ax[0].plot(xfit.ravel(), model1.predict(xfit), color='gray')
ax[0].axis([-0.1, 1.0, -2, 14])
ax[0].set_title('High-bias model: Underfits the data', size=14)

ax[1].scatter(X.ravel(), y, s=40)
ax[1].plot(xfit.ravel(), model20.predict(xfit), color='gray')
ax[1].axis([-0.1, 1.0, -2, 14])
ax[1].set_title('High-variance model: Overfits the data', size=14)

plt.show()
print("Grafico mostrado. (Si no aparece, instala con:",
      ".\\venv\\Scripts\\python.exe -m pip install matplotlib)")
