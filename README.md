# Implementacion de Modelos de Regresion con Django REST Framework

Este repositorio contiene dos proyectos web independientes que implementan modelos de machine learning.

## Proyectos

### ACT XI: Implementacion en una Web del Modelo Entrenado de Regresion Lineal Simple
Aplicacion web que implementa un modelo de regresion lineal simple.

### ACT XII: Implementacion Modelo de Regresion Logistica
Aplicacion web que implementa un modelo de regresion logistica para predecir compras basado en edad y salario.

## Requisitos

- Python 3.8 o superior
- pip

## Instalacion

1. Instalar las dependencias:

```
pip install -r requirements.txt
```

## ACT XI: Regresion Lineal Simple

### Generar el modelo

```
cd ACT_XI_RegresionLineal
python crear_modelo.py
```

### Ejecutar el servidor

```
python manage.py runserver 8000
```

### Acceder a la aplicacion

Abrir el navegador en: http://localhost:8000

## ACT XII: Regresion Logistica

### Generar el modelo

```
cd ACT_XII_RegresionLogistica
python crear_modelo.py
```

### Ejecutar el servidor

```
python manage.py runserver 8001
```

### Acceder a la aplicacion

Abrir el navegador en: http://localhost:8001

## Estructura del Proyecto

```
RegresionLogistica/
├── ACT_XI_RegresionLineal/
│   ├── api/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── serializers.py
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── manage.py
│   └── crear_modelo.py
├── ACT_XII_RegresionLogistica/
│   ├── api/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── serializers.py
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── manage.py
│   └── crear_modelo.py
├── Datos/
│   ├── UserData.csv
│   └── Lab04_9B_LogisticRegression (1).ipynb
└── requirements.txt
```

## Notas

- Ambos servidores pueden ejecutarse simultaneamente en puertos diferentes.
- Los modelos deben generarse antes de ejecutar los servidores.
- Los archivos .pkl generados se almacenan en la carpeta api de cada proyecto.
