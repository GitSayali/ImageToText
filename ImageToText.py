import time
import logging
import traceback

import pytesseract
from PIL import Image

_LOGGER = logging.getLogger(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_text_from_image(img, read_type=0):     
    """
    Reads text from an image using Tesseract OCR.

    :param img: Input image as a NumPy array
    :param read_type: OCR mode (0: normal, 1: numbers only, 2: words only, 3: dense text)
    :return: Extracted text as a list
    """
    
    # Define the Tesseract configuration based on read_type
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
        return []  # Return an empty list instead of proceeding
    
    text_output = []
    
    try:
        #Load image from file path instead of assuming a NumPy array
        img = Image.open(img)


        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(img, config=text_config)
        
        text_output.append(text)
        
    except Exception as e:
        _LOGGER.error(f'There was an error reading the image: {str(e)}')

    return text_output
	
output = read_text_from_image("example.png")
print(output)