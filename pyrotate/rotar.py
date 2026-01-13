from PIL import Image
import os

# Cargar la imagen
image_path = "tortuga44.bmp"
image = Image.open(image_path)

# Directorio para guardar las imágenes rotadas
output_dir = "rotado"
os.makedirs(output_dir, exist_ok=True)

# Rotar la imagen en incrementos de un grado
for angle in range(0, 46):
    rotated_image = image.rotate(angle, expand=True)
    rotated_image.save(os.path.join(output_dir, f"tortuga_{angle}.bmp"))

# Crear un archivo comprimido con todas las imágenes rotadas
#import shutil
#shutil.make_archive("/mnt/data/rotated_images", 'zip', output_dir)