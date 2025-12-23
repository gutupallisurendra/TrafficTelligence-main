from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and preprocessors
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
le_holiday = pickle.load(open('encoder_holiday.pkl', 'rb'))
le_weather = pickle.load(open('encoder_weather.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs
        holiday = request.form['holiday']
        weather = request.form['weather']
        temp = float(request.form['temp'])
        rain = float(request.form['rain'])
        snow = float(request.form['snow'])
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        hours = int(request.form['hours'])
        minutes = int(request.form['minutes'])
        seconds = int(request.form['seconds'])

        # Encode categorical inputs
        holiday_encoded = le_holiday.transform([holiday])[0]
        weather_encoded = le_weather.transform([weather])[0]

        # Arrange features in correct order (matching training)
        features = np.array([[holiday_encoded, weather_encoded, temp, rain, snow, year, month, day, hours, minutes, seconds]])

        # Apply scaler
        features_scaled = scaler.transform(features)

        # Make prediction
        prediction = model.predict(features_scaled)[0]

        return render_template('index.html', prediction_text=f'Estimated Traffic Volume is: {prediction:.2f}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {e}')

if __name__ == "__main__":
    app.run(debug=True)
