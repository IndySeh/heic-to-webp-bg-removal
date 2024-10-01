# HEIC to WebP Converter with Background Removal

This Python script allows you to convert `.heic` (or `.HEIC`) image files to `.webp` format while removing the background. It automates the process of batch conversion for all `.heic` files in a folder and saves them in a new folder in compressed `.webp` format.

## Features

- **HEIC to WEBP conversion**: Converts `.heic` images to `.webp` format.
- **Background removal**: Removes the background of the images using the `rembg` package.
- **Image optimization**: Compresses and optimizes the `.webp` images for better quality.

## Requirements

- Python 3.x
- Install the following Python libraries:
  ```bash
  pip install pyheif Pillow rembg
  ```

## How to Use

1. Clone the repository or download the script.
2. Place all your `.heic` images in the root folder where the script is located.
3. Run the script:
   ```bash
   python convert_heic_to_webp.py
   ```
4. The converted and optimized `.webp` images will be saved in the `./webp-files` folder.

## Example

If you have a `.heic` image like `image1.heic`, after running the script, you will get an optimized `image1.webp` file with the background removed.

## Folder Structure

- **Input folder**: The folder where your `.heic` images are stored.
- **Output folder**: The `./webp-files` folder where the converted `.webp` images will be saved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
