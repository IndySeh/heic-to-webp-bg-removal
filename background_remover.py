import pyheif
import os
from PIL import Image
from rembg import remove


def convert_heic_to_webp(input_path: str, output_path: str) -> None:
    heif_file = pyheif.read(input_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    # Remove Background
    image = remove(image)

    # Be careful while using quality parameter below.
    image.save(output_path, "WEBP", quality=85, optimize=True)


input_folder = "input_path"
output_folder = "output_path"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".heic") or filename.endswith(".HEIC"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(
            output_folder, f"{os.path.splitext(filename)[0]}.webp"
        )

        # Convert HEIC to WebP and compress
        convert_heic_to_webp(input_path, output_path)
        print(f"Processed {filename}")
