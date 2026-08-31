"""
Programa 3 - Por que NO se entrena y se prueba con el mismo set
================================================================
Demuestra tu idea: si entrenamos y probamos con el mismo dataset,
el modelo "se saca 10 siempre" porque MEMORIZO las respuestas,
no porque realmente entienda. A eso se le llama SOBREAJUSTE (overfitting).

Comparacion:
    CASO A (TRAMPOSO):    entreno + pruebo con los 150 datos iguales.
    CASO B (CORRECTO):    divido con train_test_split y pruebo con
                          datos que el modelo nunca vio.

Correr: .\\venv\\Scripts\\python.exe split_vs_overfit.py
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data        # [150, 4]
y = iris.target      # [150]

# ----------------------------------------------------------------------
# CASO A (TRAMPOSO): mismo set para entrenar y probar
# ----------------------------------------------------------------------
modelo_tramposo = LogisticRegression(max_iter=200)
modelo_tramposo.fit(X, y)            # aprendo con TODO
pred_tramposo = modelo_tramposo.predict(X)  # y pruebo con TODO
prec_tramposo = accuracy_score(y, pred_tramposo)
print(f"CASO A (mismo set para entrenar y probar):   {prec_tramposo:.1%}")

# ----------------------------------------------------------------------
# CASO B (CORRECTO): separo con train_test_split
# ----------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y,
)

modelo_correcto = LogisticRegression(max_iter=200)
modelo_correcto.fit(X_train, y_train)        # aprendo con training
pred_correcto = modelo_correcto.predict(X_test)  # pruebo con testing (nunca vistos)
prec_correcto = accuracy_score(y_test, pred_correcto)
print(f"CASO B (separado con train_test_split):      {prec_correcto:.1%}")

print()
print("Conclusion: el CASO A parece 'perfecto' pero es una mentira,")
print("solo significa que el modelo memorizo. El CASO B es la medicion")
print("honesta: predice flores que NUNCA vio.")
