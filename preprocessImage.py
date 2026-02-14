import cv2
import numpy as np


def preprocessImage(imagePath=None, imageArray=None):
    """
    Preprocess image for prediction or training.
    Accepts either imagePath or imageArray.
    """

    if imagePath is not None:
        image = cv2.imread(imagePath)
    elif imageArray is not None:
        image = imageArray
    else:
        raise ValueError("Either imagePath or imageArray must be provided.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize to fixed dimension (64x64)
    resized = cv2.resize(gray, (64, 64))

    # Normalize
    normalized = resized / 255.0

    # Flatten to 1D vector
    flattened = normalized.flatten()

    return flattened