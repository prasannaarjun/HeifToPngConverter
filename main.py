from pathlib import Path
from PIL import Image
import pillow_heif

# Input and output folder paths
input_folder = Path("input/tour pics")  # Replace with your actual folder path
output_folder = Path("output")

# Create output folder if it doesn't exist
output_folder.mkdir(parents=True, exist_ok=True)

# Register HEIF/HEIC plugin
pillow_heif.register_heif_opener()

# Loop through all files in the input folder
for file in input_folder.iterdir():
    if file.is_file() and file.suffix.lower() in [".heif", ".heic"]:
        try:
            # Open and convert to PNG
            img = Image.open(file)
            output_path = output_folder / (file.stem + ".png")
            img.save(output_path, format="PNG")
            print(f"Converted: {file.name} -> {output_path.name}")
        except Exception as e:
            print(f"Failed to convert {file.name}: {e}")
    else:
        print(f"Skipped: {file.name}")
