from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from loadDataset import loadDataset
from modelUtils import saveModel


def trainModel():
    print("Loading dataset...")
    X, y = loadDataset()

    print("Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training Logistic Regression model...")
    model = LogisticRegression(
        multi_class="multinomial",
        solver="saga",
        max_iter=3000,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    saveModel(model)
    print("Model saved successfully!")

    return model