# 🚇 Metro de Lyon – Sistema inteligente de rutas óptimas

## 🧩 Descripción general
Proyecto desarrollado en **Python** dentro de la asignatura de **Inteligencia Artificial (ETSIINF-UPM)**.  
Consiste en la implementación de un **sistema de búsqueda de rutas óptimas en el metro de Lyon**, aplicando el **algoritmo A\*** para calcular el camino más corto entre dos estaciones considerando **distancia, transbordos y línea de metro**.

El proyecto combina **inteligencia artificial, modelado de grafos y visualización interactiva**, mostrando los trayectos sobre un **mapa real del metro de Lyon** mediante **Tkinter y Matplotlib**.

---

## 🎯 Objetivos principales
- Implementar el algoritmo **A\*** para el cálculo de rutas óptimas en grafos.  
- Modelar el **mapa del metro** con estaciones, líneas y distancias reales.  
- Representar gráficamente los trayectos y transbordos entre estaciones.  
- Diseñar una interfaz visual sencilla e intuitiva para el usuario.  
- Integrar la lógica de IA con una capa de visualización dinámica.  

---

## ⚙️ Tecnologías utilizadas
- **Lenguaje:** Python 3  
- **Bibliotecas:** Tkinter, Matplotlib, NumPy  
- **Paradigma:** Programación orientada a objetos  
- **Algoritmo principal:** A\* (A-Star Search)  
- **Entorno:** Visual Studio Code / Anaconda  

---

## 🧱 Estructura del proyecto
| Archivo / Módulo | Descripción |
|------------------|-------------|
| **`Main.py`** | Control principal del programa. Inicia el proceso de búsqueda y comunicación entre la lógica y la interfaz. |
| **`app.py`** | Interfaz gráfica desarrollada con Tkinter y Matplotlib. Permite seleccionar origen/destino y muestra el camino óptimo en el mapa. |
| **`estacion.py`** | Clase `estacion`: modela cada estación del metro (nombre, coordenadas, transbordos, conexiones). |
| **`arista.py`** | Clase `arista`: representa las conexiones entre estaciones, con distancia y línea asociada. |
| **`Ejes.py`** | Conversión de coordenadas y escalado del mapa para representar gráficamente las rutas. |
| **`MapaMetroLyon.png` / `lyon_vacio.jpg`** | Mapa base del metro utilizado para renderizar el recorrido. |

---

## 🧮 Funcionamiento general
1. El usuario selecciona una estación **de origen** y otra **de destino** en la interfaz.  
2. El sistema genera un **grafo de estaciones y conexiones**, donde cada arista tiene un coste según la distancia y la penalización por transbordo.  
3. Se aplica el **algoritmo A\*** para encontrar el **camino más corto** (minimizando distancia total y cambios de línea).  
4. El resultado se muestra:
   - 📍 En texto (lista de estaciones visitadas).  
   - 🗺️ En el mapa (trayecto dibujado con líneas de colores según el metro real).  

---

## 🧠 Algoritmo y modelado
El algoritmo A\* evalúa cada estación usando la función: f(n) = g(n) + h(n)
donde:  
- `g(n)` = coste acumulado desde el origen.  
- `h(n)` = distancia heurística al destino (medida euclídea en coordenadas X, Y).  

Para cada **transbordo de línea**, se aplica una penalización adicional en `g(n)` para reflejar el tiempo perdido al cambiar de línea.

---

## ▶️ Ejecución del proyecto
Desde el directorio raíz del proyecto:

1. Ejecutar el archivo principal en una terminal dentro de la carpeta del proyecto /metro-lyon: **python app.py**
2. Seleccionar un origen
3. Seleccionar un destino
4. Observar la ruta trazada (lista de paradas y grafo con trasbordos en el mapa)


