import cv2
from PIL import Image
import os

def capturar_fotogramas(video_path, output_dir, intervalo_frames, ancho=600, alto=800):
    # Crear el directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Abrir el video
    video = cv2.VideoCapture(video_path)

    # Verificar si el video se abrió correctamente
    if not video.isOpened():
        print("Error al abrir el video")
        return

    # Inicializar el contador de fotogramas
    contador_fotogramas = 0
    contador_guardados = 0

    while True:
        # Leer el siguiente fotograma
        ret, frame = video.read()

        if not ret:
            break

        # Si el contador de fotogramas es múltiplo del intervalo, guardar la imagen
        if contador_fotogramas % intervalo_frames == 0:
            # Convertir el fotograma a una imagen de PIL
            imagen = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Redimensionar la imagen a 600x800 píxeles
            imagen = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

            # Guardar la imagen
            output_path = os.path.join(output_dir, f"dolar11-{contador_guardados:05d}.jpg")
            imagen.save(output_path)
            print(f"Fotograma guardado como {output_path}")
            contador_guardados += 1

        contador_fotogramas += 1

    # Liberar el video
    video.release()
    print("Proceso completado.")

# Parámetros del script
video_path = r'F:\VIDEO_DATASET\dolar11.mp4'  # Reemplaza con la ruta de tu video
output_dir = r'F:\VIDEO_DATASET\DOLAR'  # Reemplaza con la ruta del directorio donde se guardarán las imágenes
intervalo_frames = 5  # Capturar un fotograma cada 10 fotogramas

# Ejecutar la función
capturar_fotogramas(video_path, output_dir, intervalo_frames)
