Problem Statement  
In today’s fast-paced world, many individuals are unaware of their personal health risk levels due to lifestyle factors, body composition, and basic physiological parameters. Traditional health risk assessment requires clinical visits, lab tests, or complex questionnaires, which are time-consuming and often inaccessible. There is a clear need for an instant, intuitive, and educational tool that can provide immediate feedback on general health risk using only basic inputs such as height, weight, age, gender, and activity level — empowering users to make informed lifestyle decisions early.

Scope of the Project  
The **AI Health Risk Predictor** is a lightweight, offline desktop application that combines real-time BMI calculation with a machine learning model (Random Forest Classifier) to estimate an individual’s generalized health risk category (Low, Moderate, or High).  
In Scope:  
- Real-time calculation and display of Body Mass Index (BMI) with WHO-based categorization  
- Interactive GUI with sliders and dropdowns for easy input  
- Pre-trained ML model providing instant risk prediction  
- Color-coded visual feedback (Green → Orange → Red)  
- Pure Python implementation — no internet or external APIs required  

Out of Scope (Current Version):
- Diagnosis of specific diseases (e.g., diabetes, heart disease).  
- Integration with medical records or wearable devices.  
- Long-term health tracking or user accounts.
- Professional medical advice (this is an educational/awareness tool only).

Target Users  
- General public interested in health awareness.  
- Students and educators learning data science, machine learning, and GUI development. 
- Fitness enthusiasts and wellness beginners.  
- Health camps, schools, and community programs needing a quick screening demo tool. 

Age group: 15–80 years (slider range)

High-Level Features  
1.Real-Time BMI Calculation  
   Automatically computes BMI and displays category (Underweight, Normal, Overweight, Obese).  

2.AI-Powered Health Risk Prediction  
   Uses a trained Random Forest model to classify overall health risk into three levels based on height, weight, age, gender, and activity level.  

3.Interactive & User-Friendly Interface 
   - Smooth sliders for Height (140–200 cm), Weight (40–120 kg), and Age (15–80 years)  
   - Dropdown selection for Gender (Male/Female) and Activity Level (Low/Medium/High)  

4.Instant Visual Feedback 
   Color-coded result display (Green = Low Risk, Orange = Moderate Risk, Red = High Risk) with clear text.  

5.Lightweight & Portable 
   Runs offline, no installation beyond Python and two pip packages (numpy, scikit-learn).  

6.Educational Value 
   Demonstrates end-to-end ML pipeline + GUI integration in under 150 lines of clean, readable code.
