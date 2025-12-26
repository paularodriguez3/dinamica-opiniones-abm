# Consenso y polarización en la dinámica espacial de opiniones

Este repositorio acompaña al trabajo **“Consenso y polarización en la dinámica espacial de opiniones bajo confianza acotada”**.

El objetivo del estudio es analizar cómo resultados colectivos macroscópicos, como el **consenso global** o la **polarización persistente**, pueden emerger a partir de **interacciones sociales locales** entre individuos, combinando dinámicas de opinión bajo confianza acotada con mecanismos de **relocalización espacial inspirados en el modelo de segregación de Schelling**.

---

## Documento principal

El artículo completo del trabajo se encuentra en:

- `paper/Paper_1_CI_Paula_Rosa.pdf`

En él se describen:
- El contexto teórico y el estado del arte.
- El diseño del modelo basado en agentes.
- La metodología experimental.
- Los resultados de simulación.
- La discusión y conclusiones.

---

## Estructura del repositorio

```text
OPINION_MODEL
├── data/
│   └── Opinion_variance.csv
│
├── models/
│   └── paper1.nlogox
│
├── paper/
│   └── Paper_1_CI_Paula_Rosa.pdf
│
├── results/
│   ├── plots/
│   │   ├── variance_unimodal.png
│   │   └── variance_bimodal.png
│   │
│   └── snapshots/
│       ├── initial_state_uni.png
│       ├── intermediate_state_uni.png
│       ├── final_state_uni.png
│       ├── initial_state_bi.png
│       ├── intermediate_state_bi.png
│       └── final_state_bi.png
│
├── src/
│   └── graph.py
│
└── README.md
````

---

## Descripción del modelo

El modelo implementa un **modelo de dinámica de opiniones espacial basado en agentes** en la plataforma NetLogo.
Cada agente representa un individuo ubicado en un espacio bidimensional y caracterizado por una **opinión continua** en el intervalo ([0,1]).

Los principales mecanismos del modelo son:

* **Interacción social bajo confianza acotada (modelo de Deffuant)**:
  Los agentes solo interactúan con vecinos cuyas opiniones difieren menos que un umbral de tolerancia.

* **Actualización gradual de opiniones** mediante una tasa de aprendizaje.

* **Relocalización espacial tipo Schelling**:
  Cuando la fracción de vecinos socialmente compatibles cae por debajo de un umbral de satisfacción, el agente puede reubicarse en una posición vacía del espacio.

El tiempo evoluciona en pasos discretos (*ticks*), siguiendo un esquema de actualización secuencial.

---

## Modelos NetLogo

* `models/paper1.nlogox`
  Archivo de NetLogo con la configuración de **BehaviorSpace** utilizada para ejecutar los experimentos de simulación bajo diferentes condiciones iniciales (unimodales y bimodales).

---

## Datos

El directorio `data/` contiene los archivos CSV exportados desde NetLogo, que recogen métricas agregadas del sistema, en particular:

* `Opinion_variance.csv`
  Evolución temporal de la **varianza global de opiniones**, utilizada para cuantificar el grado de consenso o polarización.

---

## Resultados

### Gráficas agregadas

* `results/plots/`
  Curvas de la varianza de opiniones a lo largo del tiempo:

  * `variance_unimodal.png`: condiciones iniciales unimodales (consenso).
  * `variance_bimodal.png`: condiciones iniciales bimodales (polarización persistente).

### Estados espaciales

* `results/snapshots/`
  Capturas del estado espacial del sistema en distintos momentos de la simulación:

  * Estado inicial.
  * Estado intermedio.
  * Estado final.

Estas imágenes ilustran la emergencia de consenso o la formación de clústeres polarizados y segregados espacialmente.

---

## Análisis y visualización

El script `src/graph.py` procesa los archivos CSV generados por NetLogo y reproduce las gráficas de varianza de opiniones incluidas en el directorio `results/plots/`.

### Requisitos

* Python 3.x
* matplotlib
* csv (librería estándar)

---

## Reproducibilidad

1. Ejecutar el modelo en NetLogo utilizando el archivo `paper1.nlogox`.
2. Exportar los resultados de las simulaciones en formato CSV.
3. Guardar los archivos en el directorio `data/`.
4. Ejecutar el script `graph.py` para generar las figuras agregadas.

---

## Autora

**Paula Rosa Rodríguez Morales**
