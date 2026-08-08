# Data Science — Pipeline de Análisis

## Estructura del Proyecto

```
project/
├── data/
│   ├── raw/                # Datos sin procesar
│   ├── processed/          # Datos limpios
│   └── models/             # Modelos entrenados (.pkl)
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_evaluation.ipynb
├── src/
│   ├── data/               # Scripts de carga/limpieza
│   ├── features/           # Feature engineering
│   ├── models/             # Entrenamiento y predicción
│   └── visualization/      # Gráficos y dashboards
├── tests/
├── requirements.txt
└── README.md
```

## Pipeline Estándar

### 1. Exploración (EDA)
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("data/raw/dataset.csv")

# Overview
df.info()
df.describe()
df.isnull().sum()

# Distribuciones
df.hist(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True)
```

### 2. Preprocesamiento
```python
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Manejo de nulos
df.fillna(df.median(), inplace=True)

# Encoding
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### 3. Modelado
```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

# Entrenar múltiples modelos
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(),
}

for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"{name}: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### 4. Evaluación
```python
from sklearn.metrics import classification_report, confusion_matrix

# Predicciones
y_pred = best_model.predict(X_test)

# Métricas
print(classification_report(y_test, y_pred))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
```

## Reglas de Calidad para Data Science

- SIEMPRE separar train/test ANTES de preprocesar (evitar data leakage)
- NUNCA usar accuracy sola (usar F1, precision, recall según contexto)
- SIEMPRE versionar datos Y modelos (DVC o MLflow)
- Documentar TODAS las decisiones (¿por qué eliminaste esa feature?)
- Cross-validation (nunca evaluar solo con un split)
- Reproducibilidad: random_state fijo, requirements.txt con versiones
