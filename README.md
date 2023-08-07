# WhatsApp Image Classifier


## Overview

The WhatsApp Image Classifier is a powerful neural network model designed to classify images shared on WhatsApp. This project leverages the vast amount of image data gathered from WhatsApp groups and conversations to train the model using transfer learning techniques. The goal is to accurately categorize images into different classes, making it easier for users to organize and search their media.


## How it Works

1. **Data Collection**: A large dataset of WhatsApp images is collected, annotated, and prepared for training the image classifier.

2. **Pre-processing**: The image data undergoes pre-processing steps such as resizing, normalization, and data augmentation to enhance the model's generalization capabilities.

3. **Transfer Learning**: The pre-trained deep learning model is loaded, and its weights are fine-tuned using the WhatsApp image dataset.

4. **Model Training**: The fine-tuned model is trained on the WhatsApp image dataset, optimizing for accuracy and minimizing loss.

5. **Model Evaluation**: The trained model is evaluated on a separate test dataset to measure its performance and identify potential areas of improvement.

6. **Deployment**: The trained model is integrated into the user-friendly interface, making it accessible to users for image classification.

## Requirements

- Python 3.x
- TensorFlow
- Keras
- NumPy
- OpenCV
- Flask (for the web interface)

## Usage

1. Clone the repository and navigate to the project directory.

2. Install the required dependencies using `pip`:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python flaskapp/flask_app.py
   ```

4. Access the web interface by navigating to `http://localhost:5000` in your web browser.

5. Upload a WhatsApp image or provide folder path containing the images using the interface and see the model accurately classify it into appropriate categories.

