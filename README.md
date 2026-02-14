# handwritingClassifier
Handwriting Classifier that recognises uppercase and lowercase alphabets using Logistic Regression

Once the code is downloaded, the user is expected to create a dataset/ folder within this project. The structure of this dataset folder/ must be as follows:

<img width="803" height="670" alt="image" src="https://github.com/user-attachments/assets/d15f03d5-b317-49b5-8531-862ff5663618" />

The images that will be uploaded (Which will be used as dataset for training the model), make it a point that the alphabets (Both uppercase and lowercase) are written on a CLEAR WHITE SHEET of paper (Preferably A4) with a CLEAR, SMUDGE-FREE black ink pen. The alphabet must be centred in image (Which is a must for making sure that the model is trained on perfect data). After doing this, navigate back to the main project folder and create a new subfolder named savedModels/ and just leave it empty. That will be used for saving the model on which the dataset will be trained.

Once everything is ready, DO NOT run the 'python main.py' command. Instead, run the 'streamlit run main.py --server.address 127.0.0.1' command. If the user's web browser prevents http:// sites from loading, then it is requested for them to enable loading http:// websites, the setting of which can be found within the 'Privacy', 'Security' or 'Advanced Settings' menus within the browser settings.
