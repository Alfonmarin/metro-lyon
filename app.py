import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.image as mpimg #import para la imagen de fondo
from Main import a_estrella, estacion_a, estacion_b, estacion_c, estacion_d, obtExtremo #imports de las estrucutras de datos de las estaciones

class App:

    COLORES_LINEA = {'A': 'red', 'B': 'blue', 'C': 'orange', 'D': 'green'}

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Ruta Metro Lyon")


        # esto establece el tamanio inicial de la ventana
        self.root.geometry("800x600") 

        # variables para almacenar las estaciones de origen y destino
        self.origen_var = tk.StringVar()
        self.destino_var = tk.StringVar()

        # esto son las etiquetas y menus desplegables
        ttk.Label(root, text="Estación de Origen:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.menu_origen = ttk.Combobox(root, textvariable=self.origen_var, state="readonly")
        self.menu_origen.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(root, text="Estación de Destino:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.menu_destino = ttk.Combobox(root, textvariable=self.destino_var, state="readonly")
        self.menu_destino.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # boton para calcular la ruta
        ttk.Button(root, text="Calcular Ruta", command=self.calcular_ruta).grid(row=2, column=0, columnspan=2, pady=10)

        # cuadro de texto para mostrar la ruta
        self.ruta_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
        self.ruta_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # crea el grafico de matplotlib
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # oculta los ejes del grafico
        self.ax.axis('off')

        # esto carga la imagen de fondo
        self.background_img = mpimg.imread('lyon_vacio.jpg')
        self.ax.imshow(self.background_img, extent=[0, 600, 0, 600]) 


        # canvas de matplotlib para integrar en la interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


        # esto es para redimensionar la ventana al maximizar
        self.configurar_redimensionamiento()

        # rellena los menus desplegables con las estaciones
        self.llenar_menus_desplegables()


    def calcular_ruta(self):
        origen = self.origen_var.get()
        destino = self.destino_var.get()

        # llamada a la funcion A* con las estaciones de origen y destino
        ruta = a_estrella(obtener_estacion_por_nombre(origen), obtener_estacion_por_nombre(destino))

        # muestra la ruta en el cuadro de texto
        self.ruta_text.config(state=tk.NORMAL)
        self.ruta_text.delete("1.0", tk.END)
        for estacion in ruta:
            self.ruta_text.insert(tk.END, estacion + "\n")
        self.ruta_text.config(state=tk.DISABLED)

        # Dibuja la ruta en el grafico
        self.dibujar_ruta(ruta)


    def dibujar_ruta(self, ruta):
        # limpia el grafico
        self.ax.clear()

        # obtiene  las coordenadas de las estaciones en la ruta
        coordenadas_x = [obtener_estacion_por_nombre(estacion).x for estacion in ruta]
        coordenadas_y = [obtener_estacion_por_nombre(estacion).y for estacion in ruta]

        # Dibuja la ruta utilizando el color de la línea de cada arista
        for i in range(len(ruta) - 1):
            estacion_actual = obtener_estacion_por_nombre(ruta[i])
            estacion_siguiente = obtener_estacion_por_nombre(ruta[i + 1])

            for arista in estacion_actual.vecinos:
                if obtExtremo(estacion_actual, arista) == estacion_siguiente:
                    color = self.COLORES_LINEA.get(arista.linea, 'black')  # Negro por defecto si no se encuentra el color
                    break

            # dibuja la linea entre las estaciones
            self.ax.plot([estacion_actual.x, estacion_siguiente.x],
                        [estacion_actual.y, estacion_siguiente.y],
                        marker='o', linestyle='-', color=color)


            # aniade etiqueta para cada estacion
            self.ax.annotate(estacion_actual.nombre,
                         xy=(estacion_actual.x, estacion_actual.y),
                         xytext=(5, 5),
                         textcoords='offset points',
                         ha='center',
                         va='center',
                         color='black',  
                         fontsize=7)  

            # Añadir etiqueta para la última estación (destino)
            if i == len(ruta) - 2:
                self.ax.annotate(estacion_siguiente.nombre,
                             xy=(estacion_siguiente.x, estacion_siguiente.y),
                             xytext=(5, 5),
                             textcoords='offset points',
                             ha='center',
                             va='center',
                             color='black',  
                             fontsize=7)  


        # Dibuja la imagen de fondo
        self.ax.imshow(self.background_img, extent=[0, 600, 0, 600], alpha=0.5)
        
        
        # Oculta los ejes tras pulsar el boton de calcular ruta
        self.ax.axis('off')

        # Agrega la siguiente linea para actualizar el lienzo
        self.canvas.draw()



    def configurar_redimensionamiento(self):
    # Configura opciones de redimensionamiento para todas las filas y columnas
        for i in range(5):  
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):  
            self.root.grid_columnconfigure(i, weight=1)

        # Establece propiedades de redimensionamiento para el lienzo
        self.canvas_widget.grid(row=0, column=2, rowspan=5, padx=5, pady=5, sticky='nsew') 

        # Ajusta el cuadro superior
        ttk.Label(self.root, text="Estación de Origen:").grid(row=0, column=0, padx=(10, 5), pady=5, sticky='w')  
        self.menu_origen.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(self.root, text="Estación de Destino:").grid(row=1, column=0, padx=(10, 5), pady=5, sticky='w')  
        self.menu_destino.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Mueve el cuadro de la lista hacia la izquierda
        self.ruta_text.grid(row=2, column=0, rowspan=3, padx=(10, 5), pady=5, sticky='w')  

    def llenar_menus_desplegables(self):
        # lista de todas las estaciones de todas las lineas
        estaciones_todas = estacion_a + estacion_b + estacion_c + estacion_d

        # Ordena las estaciones alfabeticamente
        estaciones_todas.sort(key=lambda estacion: estacion.nombre)

        # Rellena los menus desplegables con las estaciones
        valores_origen = [estacion.nombre for estacion in estaciones_todas]
        self.menu_origen['values'] = valores_origen

        valores_destino = [estacion.nombre for estacion in estaciones_todas]
        self.menu_destino['values'] = valores_destino

def obtener_estacion_por_nombre(nombre):
    for estacion in estacion_a + estacion_b + estacion_c + estacion_d:
        if(nombre == estacion.nombre):
            return estacion

# Crea la aplicacion
root = tk.Tk()
app = App(root)

# Ejecuta la aplicacion
root.mainloop()
