# app.py
from flask import Flask, request, jsonify
import joblib
from utils import prepare_simple_input

app = Flask(__name__)
model = joblib.load('model/flight_model.pkl')
feature_columns = model.feature_names_in_.tolist()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    df = prepare_simple_input(
        date_str=data['date'],
        stops=data['stops'],
        airline=data['airline'],
        source=data['source'],
        dest=data['destination'],
        feature_columns=feature_columns
    )

    price = model.predict(df)[0]
    return jsonify({'predicted_price': round(price, 2)})

if __name__ == '__main__':
    app.run(debug=True)
