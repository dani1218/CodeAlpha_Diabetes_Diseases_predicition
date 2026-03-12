# CodeAlpha_Diabetes_Diseases_predicition
# Disease Prediction (Diabetes) — Machine Learning Web App (Flask)

A simple end-to-end **Disease Prediction** project (Diabetes) built using **Machine Learning** and deployed as a **Flask web application**.  
The app takes patient medical inputs and predicts whether the patient is likely to have diabetes (**Outcome: 0 / 1**), along with an optional risk probability (if the model supports `predict_proba`).

## Project Objective
Predict the possibility of a disease from structured medical data using classification algorithms.  
This project demonstrates the full workflow:
- data handling and feature selection
- model training and saving (pickle)
- web deployment using Flask + HTML/CSS UI

## Dataset / Features
This project uses the well-known diabetes dataset (Pima Indians Diabetes style).

**Input features:**
- Pregnancies  
- Glucose  
- BloodPressure  
- SkinThickness  
- Insulin  
- BMI  
- DiabetesPedigreeFunction  
- Age  

**Target label:**
- Outcome (0 = Negative, 1 = Positive)

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn (ML model)
- Flask (web backend)
- HTML + CSS (frontend UI)
- Pickle (`.pkl`) for saved model

## How to Run Locally
1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Install dependencies:
   ```bash
   pip install flask numpy scikit-learn pandas
   ```

3. Make sure these files exist:
   - `app.py`
   - `diabetes_model.pkl` (your trained model)
   - `templates/index.html`

4. Start the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser:
   - http://127.0.0.1:5000/

## Output
The web app displays:
- **Prediction:** Positive / Negative
- **Risk Probability:** shown if model provides `predict_proba`

## Notes
- This project is for educational purposes and demonstrates ML deployment.
- Predictions depend on the dataset and model training.
- This is **not a medical diagnosis**—consult a healthcare professional for clinical decisions.

## Future Improvements
- Add input validation and realistic range hints per feature
- Use a full preprocessing pipeline (imputer + scaler + model) saved as one `.pkl`
- Add model evaluation page (Accuracy, F1, ROC-AUC, Confusion Matrix)
- Deploy online (Render / Railway / PythonAnywhere)

---
**Author:** (your name)  
**Task:** Disease Prediction from Medical Data (Classification)
