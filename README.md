# Read Text from Image Using Tesseract OCR

This project provides a Python function to extract text from an image using Tesseract OCR. The function supports different reading modes for normal text, numbers only, and words only.

## Requirements

Make sure you have the following dependencies installed before running the script:

```bash
pip install pillow pytesseract opencv-python numpy
```

Additionally, you need to have **Tesseract-OCR** installed on your system:

- **Windows**: [Download here](https://github.com/UB-Mannheim/tesseract/wiki)
- **Linux/macOS**: Install via package manager:
  ```bash
  sudo apt install tesseract-ocr  # Ubuntu/Debian
  brew install tesseract  # macOS
  ```

## Usage

### Function Definition
```python
from PIL import Image
import pytesseract
import numpy as np
import logging

def read_text_from_image(img, read_type=0):
    """
    Reads text from an image using Tesseract OCR.

    :param img: Image file path (string) or a NumPy array
    :param read_type: OCR mode (0: normal, 1: numbers only, 2: words only, 3: dense text)
    :return: Extracted text as a list
    """
    logging.basicConfig(level=logging.ERROR)
    _LOGGER = logging.getLogger(__name__)
    
    text_config = ''
    if read_type == 0:
        text_config = '--psm 6'
    elif read_type == 1:
        text_config = '--psm 6 -c tessedit_char_whitelist=0123456789'
    elif read_type == 2:
        text_config = "--psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz"
    elif read_type == 3:
        text_config = '--psm 5'
    else:
        _LOGGER.error('Invalid input, Please input correct read_type: 0, 1, 2, or 3')
        return []

    text_output = []
    try:
        if isinstance(img, str):
            img = Image.open(img)
        elif isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        
        text = pytesseract.image_to_string(img, config=text_config)
        text_output.append(text)
    except Exception as e:
        _LOGGER.error(f'There was an error reading the image: {str(e)}')
    
    return text_output
```
## Output
[MAKE TEXT\nSTAND OUT FROM\n) BACKGROUNDS ]

### Example Usage

#### 1️⃣ Reading Text from an Image File
```python
text = read_text_from_image("sample_image.png", read_type=0)
print(text)
```

#### 2️⃣ Reading Text from a NumPy Image Array
```python
import cv2
img = cv2.imread("sample_image.png")  # Load image using OpenCV
text = read_text_from_image(img, read_type=0)
print(text)
```

## Read Type Options
| Value | Description |
|-------|-------------|
| `0`   | Normal text mode (default) |
| `1`   | Numbers only |
| `2`   | Words only (lowercase) |
| `3`   | Dense text mode |

## Troubleshooting

- **Tesseract-OCR Not Found?** Set the Tesseract path manually:
  ```python
  pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
  ```
- **Poor Text Extraction?** Try adjusting the `--psm` value or preprocessing the image (e.g., converting to grayscale).

## License
This project is open-source and available for personal and commercial use.

---
✅ **Now you're ready to extract text from images using Tesseract OCR!** 🚀

