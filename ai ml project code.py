import tkinter as tk
from tkinter import ttk
import numpy as np
from sklearn.ensemble import RandomForestClassifier

X_train = np.array([
    [160, 50, 25, 0, 2],
    [165, 55, 22, 1, 2],
    [170, 70, 30, 0, 1],
    [160, 80, 35, 1, 0],
    [175, 90, 40, 0, 0],
    [155, 45, 20, 1, 2],
    [180, 100, 50, 0, 0],
    [165, 65, 28, 1, 1],
    [170, 85, 45, 0, 0],
    [160, 60, 33, 1, 1],
])
y_train = np.array([0,0,1,1,2,0,2,1,2,1])
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)
risk_labels = ["Low Risk", "Moderate Risk", "High Risk"]
risk_colors = ["green", "orange", "red"]

root = tk.Tk()
root.title("AI Health Risk Predictor")
root.geometry("500x650")
root.configure(bg="#f0f0f0")

title = tk.Label(root, text="AI Health Risk Predictor", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=15)

tk.Label(root, text="Height (cm)", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
height_scale = tk.Scale(root, from_=140, to=200, orient=tk.HORIZONTAL, length=400)
height_scale.set(165)
height_scale.pack()

tk.Label(root, text="Weight (kg)", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
weight_scale = tk.Scale(root, from_=40, to=120, orient=tk.HORIZONTAL, length=400)
weight_scale.set(70)
weight_scale.pack()

tk.Label(root, text="Age (years)", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
age_scale = tk.Scale(root, from_=15, to=80, orient=tk.HORIZONTAL, length=400)
age_scale.set(30)
age_scale.pack()

tk.Label(root, text="Gender", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
gender_var = tk.StringVar(value="Male")
gender_menu = ttk.Combobox(root, textvariable=gender_var, values=["Male","Female"], font=("Arial",12), state="readonly")
gender_menu.pack(pady=5)

tk.Label(root, text="Activity Level", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
activity_var = tk.StringVar(value="Medium")
activity_menu = ttk.Combobox(root, textvariable=activity_var, values=["Low","Medium","High"], font=("Arial",12), state="readonly")
activity_menu.pack(pady=5)

bmi_label = tk.Label(root, text="BMI: --", font=("Arial",16,"bold"), bg="#f0f0f0")
bmi_label.pack(pady=10)
result_label = tk.Label(root, text="Predicted Health Risk: --", font=("Arial",16,"bold"), bg="#f0f0f0")
result_label.pack(pady=10)

def update_risk(event=None):
    try:
        # Get slider values
        height = float(height_scale.get())
        weight = float(weight_scale.get())
        age = int(age_scale.get())

        # Check values
        if height <= 0 or weight <= 0 or age <= 0:
            raise ValueError

        # Gender & Activity mapping
        gender = 0 if gender_var.get() == "Male" else 1
        activity_map = {"Low":0, "Medium":1, "High":2}
        activity = activity_map.get(activity_var.get(), 1)  # default Medium

        # BMI calculation
        bmi = weight / ((height/100)**2)
        bmi_label.config(text=f"BMI: {bmi:.1f}")

        # AI Prediction
        X_new = np.array([[height, weight, age, gender, activity]])
        pred = model.predict(X_new)[0]

        # Update result
        result_label.config(
            text=f"Predicted Health Risk: {risk_labels[pred]}",
            fg=risk_colors[pred]
        )

    except:
        bmi_label.config(text="BMI: --")
        result_label.config(text="Predicted Health Risk: --", fg="black")

height_scale.bind("<Motion>", update_risk)
weight_scale.bind("<Motion>", update_risk)
age_scale.bind("<Motion>", update_risk)
gender_menu.bind("<<ComboboxSelected>>", update_risk)
activity_menu.bind("<<ComboboxSelected>>", update_risk)

# Initialize with default prediction
update_risk()

root.mainloop()