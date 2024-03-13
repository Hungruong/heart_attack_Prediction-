# Heart Attack Prediction System
  This project is a graphical user interface (GUI) application developed using Python and the Tkinter library. The application is designed to predict the likelihood of a heart attack based on various patient data inputs. It utilizes a pre-trained machine learning model to make predictions.

## Features
  User-friendly GUI for data input and analysis
  Visualization of patient data through multiple plots
  Prediction of heart attack risk based on input parameters
  Clear display of prediction results
  Additional information about the dataset and its features
## Model
  The project uses a Logistic Regression model from the scikit-learn library for predicting heart disease. Logistic Regression is a linear model used for classification problems, where it predicts a binary output (0 or 1) based on one or more input features.

  In this case, the Logistic Regression model is trained on a heart disease dataset to predict whether a person has heart disease (1) or not (0) based on input features such as age, gender, cholesterol level, and other relevant medical data.

  The model is trained on a portion of the dataset, and its performance is evaluated using accuracy scores on both the training and testing data.
## Examples
  The example image shows the main window of the application, where users can input patient data, view visualizations, and obtain the prediction result.
  1. Patient has heart disease
     ![image](https://github.com/Hungruong/heart_attack_Prediction-/assets/112179739/3860f234-d0a5-407d-a2b5-2ead1def1016)
  2. Patient doesn't have heart disease
     ![image](https://github.com/Hungruong/heart_attack_Prediction-/assets/112179739/b1a48392-11f9-40a6-a8a2-59ccec40bc02)


## Prerequisites
  To run this application, you'll need the following dependencies installed:
  
    Python 3.x
    Tkinter (usually included with Python installations)
    NumPy
    Matplotlib
    Pillow (PIL)
    
  You can install the required Python packages using pip:
    
    pip install numpy matplotlib pillow

## Usage
  1. Clone this repository to your local machine:
    
    git clone https://github.com/Hungruong/heart_attack_Prediction-.git
  2. Navigate to the project directory:
    
    cd heart_attack_Prediction-
  3. Run the main Python script:

    python main.py
  4. The application GUI will open, allowing you to input patient data and analyze the heart attack risk.
     
## Dataset
  This project utilizes a heart disease dataset containing various features related to patient information and medical test results. The dataset is preprocessed and used to train a machine learning model for prediction purposes.

## Contributing
  Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
  
  Information related to the dataset:
    - `age` - age in years
    - `gender` - gender (1 = Male; 0 = Female)
    - `cp` - Chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3=asymptomatic)
    - `trestbps` - resting blood pressure (in mm Hg)
    - `cholesterol` - serum cholesterol in mg/dl
    - `fbs` - fasting blood sugar > 120mg/dl (1=true;0=false)
    - `restecg` - resting electrocardiographic results (0 = normal; 1 = ST-T; 2 = hypertrophy)
    - `thalach` - maximum heart rate
    - `exang` - exercise induced angina (1 = yes;0 = no)
    - `oldpeak` - ST depression induced by exercise
    - `slope` - the slope of the peak exercise ST segment (0 = upsloping; 1= flat; 2=downsloping)
    - `ca` - number of major vessels (0-3) colored by flourosopy
    - `thal` - 0 = normal; 1 = fixed defect; 2 = reversible defect
  Example data:
    age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
    52,1,0,125,212,0,1,168,0,1,2,2,3,0
    53,1,0,140,203,1,0,155,1,3.1,0,0,3,0

## License
    Copyright [2024] [Hung Truong]
