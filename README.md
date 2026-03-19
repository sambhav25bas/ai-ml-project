#AI HEALTH RISK PREDICTOR

##Overview of the Project

The AI Health Risk Predictor is a lightweight, user-friendly desktop application that uses a trained Random Forest Classifier to predict an individual's health risk level (Low, Moderate, or High) based on basic physiological and lifestyle inputs.
It combines real-time BMI calculation with an AI model to provide instant, color-coded health risk feedback which is perfect for health awareness apps, educational demos, or medical prototyping.
This project demonstrates the integration of AI with a graphical user interface (GUI) in pure Python and it requires no web framework required.

##Features

•	Real-time BMI calculation with category display.
•	Interactive sliders for Height, Weight, and Age.
•	Gender and Activity Level selection via dropdown.
•	Pre-trained Random Forest model for health risk prediction.
•	Instant visual feedback with color-coded results.
•	Smooth and responsive GUI built with Tkinter.
•	Lightweight and runs offline.

##Technologies / Tools Used

TECHNOLOGY	PURPOSE
PYTHON 3.X	Core programming language
TKINTER	GUI framework (built-in with Python)
NUMPY	Numerical operations & data handling
SCIKIT-LEARN	Random Forest Classifier (ML model)
TTK (TKINTER)	Modern-styled widgets (Combobox, etc)

##Steps to Install & Run the Project

Prerequisites
•	Python 3.6 or higher
•	pip (Python package manager)
Installation Steps (for libraries):
•	pip install numpy scikit-learn (in cmd).
•	Now just copy the code from github and run.
##Instructions for Testing
1.	Run the code and You’ll see default values and initial prediction.
2.	Move the Height, Weight, and Age sliders and Watch BMI and risk update in real-time
