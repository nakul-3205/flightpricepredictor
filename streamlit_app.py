# streamlit_app.py
import streamlit as st
import joblib
from utils import prepare_simple_input

st.set_page_config(page_title="Flight Fare Predictor", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'> Flight Price Predictor</h1>", unsafe_allow_html=True)

model = joblib.load('model/flight_model.pkl')
feature_columns = model.feature_names_in_.tolist()



st.markdown("##  Enter your flight details below")

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(" Source", ["Delhi", "Mumbai", "Kolkata", "Chennai", "Banglore"])
    stops = st.selectbox(" Stops", ["0 stop", "1 stop", "2 stops", "3 stops"])
    date = st.date_input(" Journey Date")

with col2:
    dest = st.selectbox(" Destination", ["Cochin", "Delhi", "Banglore", "Hyderabad", "Kolkata", "New Delhi"])
    airline = st.selectbox(" Airline", [
        "IndiGo", "Air India", "SpiceJet", "GoAir", "Vistara", "Jet Airways", "Air Asia"
    ])

if st.button(" Predict Price"):
    formatted_date = date.strftime("%d %B %Y")

    input_df = prepare_simple_input(
        date_str=formatted_date,
        stops=stops,
        airline=airline,
        source=source,
        dest=dest,
        feature_columns=feature_columns
    )

    price = model.predict(input_df)[0]
    st.success(f" Estimated Flight Price: Rs{round(price, 2)}")
