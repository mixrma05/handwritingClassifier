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

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    resized = cv2.resize(gray, (64, 64))

    normalized = resized / 255.0

    flattened = normalized.flatten()

    return flattened
