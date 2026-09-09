"""
Programación 3 - PRÁCTICA 6: K impar vs K par
==============================================
Sobre el dataset Breast Cancer Wisconsin comparamos K = 3, 4, 5, 6 y 7.

Además del accuracy, contamos cuántos EMPATES de votación se producen
en las predicciones sobre test. Con K par y clasificación binaria,
la votación puede quedar igualada (ej.: 2 votos - 2 votos). En ese caso
scikit-learn desempata eligiendo la clase de índice menor (clase 0).

Correr: python practica6_k_par_impar.py
"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# ----------------------------------------------------------------------
# 1) DATOS
# ----------------------------------------------------------------------
data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print("=" * 70)
print(f"{'K':>4} | {'Acc test':>9} | {'Empates en votación':>19}")
print("-" * 70)


def contar_empates(pipeline, X_test):
    """Cuenta cuántas observaciones de test terminan con votación empatada."""
    scaler = pipeline.named_steps["standardscaler"]
    knn = pipeline.named_steps["kneighborsclassifier"]

    _, indices = knn.kneighbors(scaler.transform(X_test))

    empates = 0
    for fila in indices:
        # votos por clase (ej.: [3, 0] -> 3 votos para 0, 0 votos para 1)
        votos = np.bincount(y_train[fila], minlength=2)
        # empate <=> todas las clases reciben la misma cantidad de votos
        if len(set(votos)) == 1:
            empates += 1
    return empates


for k in [3, 4, 5, 6, 7]:
    pipeline = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=k),
    )
    pipeline.fit(X_train, y_train)

    acc_test = pipeline.score(X_test, y_test)
    empates = contar_empates(pipeline, X_test)

    print(f"{k:>4} | {acc_test:>9.3f} | {empates:>19}")

print("=" * 70)
print(
    "\nAnalisis:\n"
    "  - Con K par la votacion puede quedar 2-2 (o 3-3) y el resultado se\n"
    "    desempata de forma arbitraria (scikit-learn elige la clase 0).\n"
    "  - Con K impar en clasificacion binaria nunca hay empate.\n"
    "  - El mejor K depende del problema: siempre hay que comparar K impar\n"
    "    y K par y elegir con cross validation (recuerda: no usar el test)."
)