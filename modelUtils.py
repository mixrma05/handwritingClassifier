import os
import joblib


MODEL_PATH = "savedModels/logisticModel.pkl"


def saveModel(model):
    os.makedirs("savedModels", exist_ok=True)
    joblib.dump(model, MODEL_PATH)


def loadModel():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None