import os
from PIL import Image

# Rutas de las carpetas
carpeta_entrada = "F:\DATASET_RECORTE\DOLAR"
carpeta_salida = "F:\DATASET_RECORTE\REDUCCION\DOLAR"

# Asegúrate de que la carpeta de salida exista
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# Recorrer todas las imágenes en la carpeta de entrada
for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(('.jpg', '.jpeg', '.png')):  # Filtra solo los formatos de imagen que te interesan
        # Ruta completa de la imagen
        ruta_imagen = os.path.join(carpeta_entrada, archivo)
        
        # Cargar la imagen
        imagen_original = Image.open(ruta_imagen)
        
        # Redimensionar la imagen a 300x300
        imagen_redimensionada = imagen_original.resize((300, 300))
        
        # Guardar la imagen redimensionada en la carpeta de salida
        ruta_salida = os.path.join(carpeta_salida, archivo)
        imagen_redimensionada.save(ruta_salida)
        
        print(f"Imagen {archivo} redimensionada y guardada en {ruta_salida}")

print("Todas las imágenes han sido redimensionadas y guardadas.")
