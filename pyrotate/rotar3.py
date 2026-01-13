from PIL import Image
import os

# Cargar la imagen
image_path = "tortuga32.bmp"
image = Image.open(image_path)

# Directorio para guardar las imágenes rotadas y redimensionadas
output_dir = "rotado32"
os.makedirs(output_dir, exist_ok=True)

# Rotar la imagen en incrementos de un grado y redimensionar a 64x64 píxeles
target_size = (32, 32)
for angle in range(0, 361):
    rotated_image = image.rotate(angle, expand=True)
    resized_image = rotated_image.resize(target_size)
    resized_image.save(os.path.join(output_dir, f"tortuga_{angle}.bmp"))