# HEIF to PNG Converter

This Python script converts all `.heif` and `.heic` image files in a specified input folder to `.png` format. All other file formats are automatically ignored. The converted PNGs are saved in an `output` folder.

---

## 📁 Folder Structure

```
project-directory/
├── input/              # Place your .heif or .heic files here
├── output/             # Converted .png files will be saved here
├── convert_heif_to_png.py
├── README.md
```

---

## 🚀 How to Use

### 1. 🔧 Requirements

Install required libraries using pip:

```bash
pip install pillow pillow-heif
```

### 2. 👥 Add Your Images

Place your `.heif` or `.heic` image files in the `input/` directory.

### 3. ▶️ Run the Script

```bash
python main.py
```

### 4. 📄 Get Your PNGs

After execution, converted `.png` files will be available in the `output/` directory.

---

## 🛠️ Script Behavior

* Only `.heif` and `.heic` files are processed.
* Files are skipped if:

  * They are not image files
  * They are in unsupported formats
* Errors during image conversion are caught and logged without halting the script.

---

## 🧠 Tech Stack

* [Python](https://www.python.org/)
* [Pillow](https://python-pillow.org/)
* [pillow-heif](https://github.com/strukturag/pillow-heif)

---

## 📌 Notes

* This script does **not** overwrite existing files in the output directory.
* You can customize the folder paths by modifying `input_folder` and `output_folder` in the script.

---

## ✅ License

This project is released under the MIT License. Feel free to use and adapt it for your own needs.
