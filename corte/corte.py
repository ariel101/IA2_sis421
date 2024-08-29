import os
from PIL import Image

def recortar_imagenes_en_directorio(input_dir, output_dir, ancho=600, alto=800):
    # Crear el directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterar sobre cada archivo en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            try:
                # Abre la imagen
                imagen = Image.open(input_path)

                # Calcula las coordenadas del recorte (centrado)
                ancho_actual, alto_actual = imagen.size
                izquierda = (ancho_actual - ancho) / 2
                superior = (alto_actual - alto) / 2
                derecha = (ancho_actual + ancho) / 2
                inferior = (alto_actual + alto) / 2

                # Recorta la imagen
                imagen_recortada = imagen.crop((izquierda, superior, derecha, inferior))

                # Guarda la imagen recortada
                imagen_recortada.save(output_path)
                print(f'Imagen recortada guardada como {output_path}')
            except Exception as e:
                print(f"Error al procesar la imagen {filename}: {e}")

# Rutas de directorio
input_dir = 'F:\VIDEO_DATASET\plantaPae4'  # Reemplaza con la ruta de tu directorio de imágenes
output_dir = 'F:\DATASET_RECORTE\PLANTA_PAE'  # Reemplaza con la ruta donde quieres guardar las imágenes recortadas

# Ejecutar la función
recortar_imagenes_en_directorio(input_dir, output_dir)
