import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Ruta de la imagen
image_path = "MapaMetroLyon.png"

# Cargar la imagen
img = mpimg.imread(image_path)

# Invertir el eje y para que coincida con el estándar del eje cartesiano
img = img[::-1, :]

# Crear una figura y ejes
fig, ax = plt.subplots()

# Mostrar la imagen en los ejes
ax.imshow(img)

# Configurar límites del eje x e y según sea necesario
ax.set_xlim(0, img.shape[1])  # Ancho de la imagen
ax.set_ylim(0, img.shape[0])  # Altura de la imagen

# Configuración adicional
ax.set_title('Imagen sobre plano cartesiano')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

# Función para manejar clics en la imagen
def onclick(event):
    # Obtener las coordenadas del clic en la imagen
    x, y = event.xdata, event.ydata
    print(f"Coordenadas del clic en la imagen: X={x}, Y={y}")

# Conectar la función de clic al evento de clic en la figura
fig.canvas.mpl_connect('button_press_event', onclick)

# Mostrar la figura
plt.show()