# 🚦 TrafficTelligence - Traffic Volume Prediction using Machine Learning

TrafficTelligence is a web application that predicts traffic volume based on various weather, date, and time parameters using a trained machine learning model (Random Forest Regressor).

---

## 📊 Features
- Predict traffic volume using inputs like temperature, rain, snow, weather conditions, and date-time features.
- Preprocessing includes label encoding and feature scaling.
- Trained with Random Forest Regressor for high accuracy.
- Built using Flask for backend and HTML+CSS for frontend.

---

## 🧠 Technologies Used
- Python
- Pandas, NumPy, Seaborn, Matplotlib
- Scikit-learn
- Flask
- HTML/CSS
- Git & GitHub

---

## 📂 Project Structure

TrafficTelligence/
│
├── Flask/
│ ├── app.py # Flask backend
│ ├── templates/
│ │ └── index.html # Frontend page
│ ├── model.pkl # Trained Random Forest model
│ ├── encoder_holiday.pkl # Holiday label encoder
│ ├── encoder_weather.pkl # Weather label encoder
│ ├── scaler.pkl # Feature scaler
│
├── traffic volume.csv # Original dataset
├── data_exploration.ipynb # Jupyter notebook for analysis
├── Requirements.txt # List of dependencies
└── README.md # Project documentation


---

## 🚀 How to Run the Project

1. **Clone the repo**:
   ```bash
   git clone https://github.com/YourUsername/TrafficTelligence.git
   cd TrafficTelligence



