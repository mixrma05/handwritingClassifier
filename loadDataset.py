import os
import numpy as np
from preprocessImage import preprocessImage


def loadDataset(datasetPath="dataset"):
    X = []
    y = []

    for folderName in os.listdir(datasetPath):
        folderPath = os.path.join(datasetPath, folderName)

        if not os.path.isdir(folderPath):
            continue

        # Extract proper label
        if folderName.lower().startswith("uppercase"):
            label = folderName[-1].upper()
        elif folderName.lower().startswith("lowercase"):
            label = folderName[-1].lower()
        else:
            continue

        for imageName in os.listdir(folderPath):
            imagePath = os.path.join(folderPath, imageName)

            features = preprocessImage(imagePath=imagePath)
            X.append(features)
            y.append(label)

    return np.array(X), np.array(y)