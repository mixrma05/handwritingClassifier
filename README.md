# Handwriting Classifier
This project is a multi-class Machine Learning (ML) system that classifies handwritten uppercase and lowercase English alphabets (A-Z and a-z) using Logistic Regression on a custom self-handwritten dataset.

## Python Libraries Used
1. NumPy (numpy): NumPy is used for efficient numerical array operations and to represent image pixel data as feature vectors.
2. OpenCV (cv2): OpenCV is used for image preprocessing operations such as grayscale conversion, resizing, and decoding uploaded images.
3. Scikit-learn (sklearn): Scikit-learn is used to implement multinomial Logistic Regression for 52-class classification and to evaluate model accuracy.
4. Joblib (joblib): Joblib is used for model persistence so that the trained model is saved and reused without retraining.
5. Streamlit (streamlit): Streamlit is used to build a lightweight graphical interface for uploading images and displaying predictions.
6. OS (os): The OS module is used for directory traversal and file management operations.

## About Logistic Regression
Logistic Regression is a discriminative model that learns weight parameters to separate classes by maximizing the likelihood of correct class labels. In this project, multinomial Logistic Regression is used to classify flattened image feature vectors into 52 alphabet classes.

## Instructions For This Repository
Once all the contents of this repository are downloaded (In the .zip format in most cases), the first step is to add a folder named **dataset/** within the main project directory. This is where all of the user's handwritten alphabets will be stored. Now, there are several rules concerning the alphabets. They are as follows:
1. There will be 30 samples of each alphabet (A-Z and a-z). Meaning, 1560 samples (30 samples * (26 alphabets * 2 sets)).
2. These alphabets must be written on a CLEAR white sheet of paper (Preferably A4 size) with a CLEAR, SMUDGE-FREE black pen (Preferably; Any other colour can also be used but darker colours yield best results).
3. Clear images of each alphabet must be taken SEPARATELY (Both uppercase and lowercase). The user must make sure to crop the final image of each alphabet in such a way that the alphabet is right in the centre of the image. This level of accuracy is a must because that will make it easier for the model after training to recognise the alphabet and output the result accordingly.
4. No shadows must be present in the final cropped image. The pictures must be taken in bright-lighted environments.

After following these steps, once the 30 images of each uppercase and lowercase alphabet are ready, they must be added in the **dataset/** folder mentioned earlier. The structure of the **dataset/** folder must be as follows:

<img width="801" height="661" alt="2026-02-14_17-39-18" src="https://github.com/user-attachments/assets/a52797a3-06a3-4ff3-8405-86d5b8d6f81e" />

*Note:* It is preferred to follow the naming convention for the image files and folders as specified above.

Once all of this is done, head back to the main project directory and create a new folder named **savedModels/**. Leave it empty and do not add anything in it as this is the location of the training model file which will be saved here (In the .pkl format) once the model is trained with the aforementioned dataset.

## Running This Project
After following all of the above steps, it's finally time to run this project.<br/>
Open the main project directory in a terminal and run the command ```streamlit run main.py --server.address 127.0.0.1```. This will open the project in your web browser.

*Note 1:* For the first time, the site will take some time as the model needs to be trained. But the model will be trained only once, and once it is done, the training model file will be saved in the **savedModels/** folder as mentioned above. This model does not need to be trained repeatedly, and starting from the second time onward, the user will be able to directly upload the pictures of their handwritten uppercase/lowercase alphabets for the model to predict and output.

*Note 2:* On running the aforementioned command in the terminal, if the project does not open in the browser, it's mostly due to the browser not permitting http:// sites to load. To overcome this setback, the user must enable http:// websites to load, the settings for which can be found in the **Privacy**, **Security** or **Advanced Options** menus in the browser settings (Varies from browser to browser).
