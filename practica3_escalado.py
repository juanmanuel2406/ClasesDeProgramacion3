"""
Programación 3 - PRÁCTICA 3: ¿Importa escalar los datos?
========================================================
Comparamos dos modelos sobre el mismo dataset (make_moons):

    Modelo A: KNN sin escalado
    Modelo B: KNN con StandardScaler (dentro de un Pipeline)

Preguntas:
    ¿Los resultados son iguales?
    ¿Por qué pueden cambiar?
    ¿Qué efecto tiene la escala sobre la distancia?
    ¿Qué modelo utilizarías?

Correr: python practica3_escalado.py
"""

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# ----------------------------------------------------------------------
# 1) DATOS (make_moons: ambas características en la misma escala)
# ----------------------------------------------------------------------
X, y = make_moons(n_samples=300, noise=0.25, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# ----------------------------------------------------------------------
# 2) MODELO A - SIN ESCALADO
# ----------------------------------------------------------------------
modelo_a = KNeighborsClassifier(n_neighbors=5)
modelo_a.fit(X_train, y_train)

# ----------------------------------------------------------------------
# 3) MODELO B - CON ESCALADO (PIPELINE)
# ----------------------------------------------------------------------
modelo_b = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5),
)
modelo_b.fit(X_train, y_train)

# ----------------------------------------------------------------------
# 4) COMPARACIÓN
# ----------------------------------------------------------------------
acc_a_train = modelo_a.score(X_train, y_train)
acc_a_test = modelo_a.score(X_test, y_test)
acc_b_train = modelo_b.score(X_train, y_train)
acc_b_test = modelo_b.score(X_test, y_test)

print("=" * 56)
print("Modelo A (sin escalado):")
print(f"  accuracy train = {acc_a_train:.3f}")
print(f"  accuracy test  = {acc_a_test:.3f}")
print("Modelo B (con escalado):")
print(f"  accuracy train = {acc_b_train:.3f}")
print(f"  accuracy test  = {acc_b_test:.3f}")
print("=" * 56)

print(
    "\nAnalisis:\n"
    "  - En make_moons ambas variables (X1, X2) ya nacen en la misma escala,\n"
    "    por eso ambos modelos rinden practicamente igual.\n"
    "  - El escalado se vuelve CRITICO cuando las variables tienen magnitudes\n"
    "    muy distintas (ej.: edad 18-80 vs ingresos 20.000-5.000.000): sin\n"
    "    escalar, la variable de mayor magnitud domina por completo la\n"
    "    distancia euclidea (regla: z = (x - media) / desviacion)."
)