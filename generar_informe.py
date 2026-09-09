"""
Programación 3 - Generador del informe Word de la actividad KNN
================================================================
Genera Informe_KNN.docx con:

    Parte 1: respuestas a las preguntas de las prácticas 2 a 7
    Parte 2: informe del mini proyecto (dataset Wine)

Los valores numéricos embebidos son los resultados REALES obtenidos
al ejecutar cada script (practica2_* ... mini_proyecto_wine.py).

Correr: python generar_informe.py  (requiere python-docx)
"""

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ----------------------------------------------------------------------
# RESULTADOS REALES DE LAS EJECUCIONES
# ----------------------------------------------------------------------
# Práctica 2 - Make Moons (train/test)
PRAC2 = [
    (1, 1.000, 0.956),
    (3, 0.948, 0.956),
    (5, 0.933, 0.944),
    (15, 0.924, 0.944),
    (50, 0.905, 0.922),
]

# Práctica 3 - Escalado
PRAC3_A = (0.933, 0.944)
PRAC3_B = (0.924, 0.944)

# Práctica 4 - CV para elegir K
PRAC4_MEJOR_K = 2
PRAC4_CV = 0.9190
PRAC4_TEST = 0.889

# Práctica 5 - Breast Cancer
PRAC5_TEST = 0.956

# Práctica 6 - K par/impar: (K, accuracy test, empates)
PRAC6 = [
    (3, 0.982, 0),
    (4, 0.947, 6),
    (5, 0.956, 0),
    (6, 0.956, 4),
    (7, 0.974, 0),
]

# Práctica 7 - Regresión (K, MAE)
PRAC7 = [(1, 0.151), (5, 0.138), (20, 0.342)]

# Mini proyecto - Wine
WINE_K = 17
WINE_CV = 0.9791
WINE_TEST = 1.000

doc = Document()

# ======================================================================
# PORTADA
# ======================================================================
titulo = doc.add_heading("K-Nearest Neighbors (KNN)", level=0)
titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph(
    "Informe de la actividad práctica - Programación 3\n"
    "Alumno: Juan Manuel Goncalves de Faria\n"
    "Instituto de Nivel Superior Comenio\n"
    "2° Cuatrimestre"
).alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_heading("Indice", level=1)
for item in [
    "1. Práctica 2 - Visualizando KNN con Make Moons",
    "2. Práctica 3 - ¿Importa escalar los datos?",
    "3. Práctica 4 - Encontrar el mejor K",
    "4. Práctica 5 - Dataset real: Breast Cancer Wisconsin",
    "5. Práctica 6 - K impar vs K par",
    "6. Práctica 7 - KNN Regression",
    "7. Práctica Final - Mini proyecto (Wine)",
]:
    doc.add_paragraph(item)

# ======================================================================
# PRÁCTICA 2
# ======================================================================
doc.add_heading("1. Práctica 2 - Visualizando KNN con Make Moons", level=1)
doc.add_paragraph(
    "Se entrenó KNN sobre make_moons (300 muestras, noise=0.25, random_state=42) "
    "con K = 1, 3, 5, 15 y 50. Resultados de accuracy:"
)

tabla = doc.add_table(rows=1, cols=3)
tabla.style = "Light Grid Accent 1"
celdas = tabla.rows[0].cells
celdas[0].text, celdas[1].text, celdas[2].text = "K", "Accuracy train", "Accuracy test"
for k, train, test in PRAC2:
    fila = tabla.add_row().cells
    fila[0].text = str(k)
    fila[1].text = f"{train:.3f}"
    fila[2].text = f"{test:.3f}"

doc.add_heading("Respuestas", level=2)
doc.add_paragraph(
    "¿Cuál modelo parece más flexible?\n"
    "K=1: la frontera se adapta punto por punto a los datos.\n\n"
    "¿Cuál parece tener mayor varianza?\n"
    "K=1: pequeños cambios en los datos producen grandes cambios en la frontera "
    "(frontera muy irregular, mayor varianza).\n\n"
    "¿Qué ocurre con K=1?\n"
    "Entrena con accuracy 1.000 (aprende el dataset de memoria) y genera una "
    "frontera muy irregular que abraza cada punto, incluyendo el ruido. Es el "
    "caso clásico de overfitting.\n\n"
    "¿Qué ocurre cuando K aumenta mucho?\n"
    "Con K=50 la frontera se vuelve muy suave y el accuracy baja (test 0.922). "
    "El modelo ignora detalles locales: underfitting.\n\n"
    "¿Dónde observamos overfitting?\n"
    "Con K=1 (y en general K pequeño): train muy alto respecto a test y frontera "
    "demasiado compleja.\n\n"
    "¿Dónde observamos underfitting?\n"
    "Con K=50: la frontera demasiado suave pierde capacidad de separar las dos "
    "lunas correctamente."
)

# ======================================================================
# PRÁCTICA 3
# ======================================================================
doc.add_heading("2. Práctica 3 - ¿Importa escalar los datos?", level=1)
doc.add_paragraph(
    f"Modelo A (sin escalado): train {PRAC3_A[0]:.3f} | test {PRAC3_A[1]:.3f}\n"
    f"Modelo B (con StandardScaler): train {PRAC3_B[0]:.3f} | test {PRAC3_B[1]:.3f}"
)
doc.add_heading("Respuestas", level=2)
doc.add_paragraph(
    "¿Los resultados son iguales?\n"
    "Sí, en este dataset casi idénticos (mismo accuracy de test: 0.944). "
    "Make Moons genera ambas variables en la misma escala.\n\n"
    "¿Por qué pueden cambiar?\n"
    "Porque KNN calcula distancias entre observaciones. Si una variable tiene "
    "magnitudes mucho mayores que otra, domina por completo la distancia.\n\n"
    "¿Qué efecto tiene la escala sobre la distancia?\n"
    "Regla: la diferencia de la variable con mayor rango opaca a las demás. "
    "Por ejemplo, una diferencia de 100.000 en ingresos tapa un cambio de 5 en edad.\n\n"
    "¿Qué modelo utilizarías?\n"
    "El modelo B (con escalado): es la práctica recomendada; siempre que las "
    "variables tengan escalas distintas conviene estandarizar (z = (x - media) / desviación)."
)

# ======================================================================
# PRÁCTICA 4
# ======================================================================
doc.add_heading("3. Práctica 4 - Encontrar el mejor K", level=1)
doc.add_paragraph(
    f"Se probó K = 1..30 con cross validation (cv=5) SOLO sobre train.\n"
    f"Mejor K según CV: K = {PRAC4_MEJOR_K} (accuracy promedio = {PRAC4_CV:.4f})\n"
    f"Evaluación final sobre test: {PRAC4_TEST:.3f}"
)
doc.add_heading("Respuestas", level=2)
doc.add_paragraph(
    "¿Qué K obtiene el mejor resultado?\n"
    f"K = {PRAC4_MEJOR_K}, con accuracy promedio de validación cruzada {PRAC4_CV:.4f}. "
    "K=1 y K=3 quedan muy cerca.\n\n"
    "¿La curva tiene un máximo claro?\n"
    "No: hay una meseta amplia entre K pequeños (K 1 a 7 rinden similares) y luego "
    "el rendimiento fluctúa alrededor de 0.89-0.90. No existe un pico único y marcado.\n\n"
    "¿Qué ocurre con K muy pequeño?\n"
    "K=1 sobreajusta: alta varianza, frontera irregular y peor accuracy de CV que "
    "valores intermedios.\n\n"
    "¿Qué ocurre con K muy grande?\n"
    "La predicción depende de una región enorme del espacio: mayor bias, frontera "
    "muy suave y accuracy CV que baja lentamente.\n\n"
    "¿El mejor K es necesariamente el más pequeño?\n"
    "No. Aquí el mejor resultó K=2; además, elegir K muy pequeño produce overfitting. "
    "Hay que buscar el equilibrio bias-varianza."
)

# ======================================================================
# PRÁCTICA 5
# ======================================================================
doc.add_heading("4. Práctica 5 - Dataset real: Breast Cancer Wisconsin", level=1)
doc.add_paragraph(
    "Dataset: 569 muestras, 30 variables. Clases: malignant (0) y benign (1).\n"
    f"Pipeline: StandardScaler + KNN (K=5). Accuracy sobre test: {PRAC5_TEST:.3f}.\n"
    "La matriz de confusión se guardó en figures/confusion_breast.png."
)
doc.add_heading("Respuestas", level=2)
doc.add_paragraph(
    f"¿Qué accuracy obtenemos?\n{PRAC5_TEST:.3f} (95.6% de las observaciones de test bien clasificadas).\n\n"
    "¿Por qué utilizamos StandardScaler?\n"
    "Las 30 variables tienen escalas muy distintas (radio, área, suavidad...). Como "
    "KNN usa distancias, sin escalar las variables de mayor magnitud dominarían.\n\n"
    "¿Qué sucede si quitamos el scaler?\n"
    "Conceptualmente el modelo pasa a depender de las variables con mayor rango, "
    "empeorando la precisión; por eso el escalado se aprende solo con train "
    "(evitando data leakage: el scaler se ajusta con fit_transform sobre X_train "
    "y solo transform sobre X_test).\n\n"
    "¿Qué ocurre con K=1?\n"
    "Clasifica según un único vecino: frontera extremadamente irregular y sensible "
    "al ruido (alta varianza).\n\n"
    "¿Qué ocurre con K=3?\n"
    "Muy buen rendimiento (ver práctica 6: 0.982 en test) y sin empates de votación.\n\n"
    "¿Qué ocurre con K=5?\n"
    "Rendimiento sólido y estable (0.956 en test).\n\n"
    "¿Qué ocurre con K=4?\n"
    "Al ser par, aparecen empates de votación (6 en test) que se desempatan de forma "
    "arbitraria; accuracy 0.947, levemente inferior.\n\n"
    "¿Qué ocurre si K es demasiado grande?\n"
    "La frontera se suaviza tanto que el modelo pierde detalle (underfitting).\n\n"
    "¿Qué K elegirías finalmente?\n"
    "K=3: mejor accuracy (0.982), K impar (sin empates) y validado con cross validation."
)

# ======================================================================
# PRÁCTICA 6
# ======================================================================
doc.add_heading("5. Práctica 6 - K impar vs K par", level=1)
tabla6 = doc.add_table(rows=1, cols=3)
tabla6.style = "Light Grid Accent 1"
celdas6 = tabla6.rows[0].cells
celdas6[0].text, celdas6[1].text, celdas6[2].text = "K", "Accuracy test", "Empates de votación"
for k, acc, emp in PRAC6:
    fila = tabla6.add_row().cells
    fila[0].text = str(k)
    fila[1].text = f"{acc:.3f}"
    fila[2].text = str(emp)

doc.add_heading("Respuestas", level=2)
doc.add_paragraph(
    "¿Elegirías siempre el mayor accuracy o existen otras razones para preferir un determinado K?\n"
    "No conviene elegir solo por accuracy. Otras razones:\n"
    "  1) Con K par y clasificación binaria hay empates (6 con K=4): el algoritmo "
    "desempata eligiendo la clase 0, lo cual es arbitrario.\n"
    "  2) K impar evita empates en problemas binarios (regla práctica, no obligatoria).\n"
    "  3) El K elegido debe ser estable bajo cross validation, no ajustado al test.\n"
    "Aquí el mejor accuracy lo da K=3 (0.982, impar y sin empates), que además es "
    "consistente con la elección por CV."
)

# ======================================================================
# PRÁCTICA 7
# ======================================================================
doc.add_heading("6. Práctica 7 - KNN Regression", level=1)
tabla7 = doc.add_table(rows=1, cols=2)
tabla7.style = "Light Grid Accent 1"
celdas7 = tabla7.rows[0].cells
celdas7[0].text, celdas7[1].text = "K", "MAE sobre test"
for k, mae in PRAC7:
    fila = tabla7.add_row().cells
    fila[0].text = str(k)
    fila[1].text = f"{mae:.3f}"

doc.add_heading("Respuestas", level=2)
doc.add_paragraph(
    "¿Qué ocurre con K=1?\n"
    "La curva de predicción copia el ruido punto a punto: sobreajuste (overfitting). "
    "MAE bajo pero la forma general es 'serrucho'.\n\n"
    "¿Qué ocurre con K=5?\n"
    "Equilibrio: sigue la forma del seno con suavizado razonable. MAE mínimo de los tres (0.138).\n\n"
    "¿Qué ocurre con K=20?\n"
    "La curva se suaviza demasiado y pierde la forma del seno en los bordes: "
    "underfitting. MAE 0.342, el peor.\n\n"
    "¿Cómo cambia la curva de predicción?\n"
    "Con K creciente la predicción deja de ser el valor de un único vecino y pasa a ser "
    "el promedio de una región más grande: la curva se suaviza.\n\n"
    "¿Dónde aparece el overfitting?\n"
    "Con K=1 (la curva ajusta hasta el ruido individual).\n\n"
    "¿Dónde aparece el underfitting?\n"
    "Con K=20 (la curva es demasiado simple para capturar la forma del seno)."
)

# ======================================================================
# PRÁCTICA FINAL - MINI PROYECTO
# ======================================================================
doc.add_heading("7. Práctica Final - Mini proyecto: Wine", level=1)
doc.add_paragraph(
    "Para el mini proyecto se eligió el dataset Wine (NO utilizado en la explicación). "
    "Pipeline completo: Exploración → X/y → Train/Test split → StandardScaler → KNN → "
    "Cross Validation → selección de K → modelo final → test → métricas → conclusiones."
)

doc.add_heading("Respuestas del informe", level=2)
doc.add_paragraph(
    "¿Qué problema estamos resolviendo?\n"
    "Clasificar la variedad de un vino a partir de su composición química.\n\n"
    "¿Qué representa el target?\n"
    "La variedad del vino (clase 0, 1 o 2) → problema de clasificación multiclase.\n\n"
    "¿Qué variables utilizamos?\n"
    "Las 13 variables químicas del dataset: alcohol, ácido málico, cenizas, "
    "alcalinidad, magnesio, fenoles, flavonoides, etc.\n\n"
    "¿Por qué necesitamos escalar?\n"
    "Las magnitudes van desde 0.13 hasta 1680 (prolina). KNN basa todo en distancias, "
    "así que sin escalar la variable dominante sería 'prolina'.\n\n"
    "¿Qué métrica de distancia utilizamos?\n"
    "Euclídea (Minkowski con p=2), la predeterminada de KNeighborsClassifier.\n\n"
    "¿Qué valores de K probamos?\n"
    "Todos los K de 1 a 30 mediante cross validation (cv=5).\n\n"
    "¿Cómo elegimos K?\n"
    "Con cross validation SOLO sobre entrenamiento, para no usar el test en la decisión."
    f" Resultó K = {WINE_K} (accuracy promedio CV = {WINE_CV:.4f}).\n\n"
    "¿Utilizamos K impar? ¿Por qué?\n"
    "El mejor K por CV fue impar (17). La regla de K impar es una buena práctica para "
    "evitar empates en clasificación binaria; con 3 clases también pueden existir "
    "empates, pero K impar sigue siendo una buena referencia.\n\n"
    f"¿Cuál fue el resultado de Cross Validation?\n"
    f"Accuracy promedio de {WINE_CV:.4f} para K = {WINE_K} (sobre entrenamiento).\n\n"
    f"¿Cuál fue el resultado final sobre test?\n"
    f"Accuracy = {WINE_TEST:.3f} (100% de aciertos sobre el 20% de datos reservados).\n\n"
    "¿Qué muestra la matriz de confusión?\n"
    "Todas las observaciones de test quedaron en la diagonal (ningún error). Se guardó "
    "en figures/confusion_wine.png.\n\n"
    "¿Existe evidencia de overfitting?\n"
    "No: el mejor K es intermedio (17), el accuracy de test es alto y estable, y la "
    "diferencia entre CV y test es mínima (0.979 vs 1.000).\n\n"
    "¿Es KNN una buena elección para este problema?\n"
    "Sí: el dataset es chico (178 muestras, 13 features), las clases están balanceadas "
    "y KNN alcanzó un rendimiento excelente de forma simple e interpretable."
)

doc.save("Informe_KNN.docx")
print("Informe_KNN.docx generado correctamente.")