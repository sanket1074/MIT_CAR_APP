import streamlit as st
import pickle
import pandas as pd
from datetime import datetime

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open('final_model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

# ---------------- TITLE ---------------- #
st.title('🚗 Car Price Prediction')

# ---------------- INPUTS ---------------- #

insurance_validity = st.selectbox(
    'Insurance validity:',
    ['Comprehensive', 'Third Party insurance', 'Zero Dep', 'Not Available']
)

fuel_type = st.selectbox(
    'Fuel Type:',
    ['Petrol', 'Diesel', 'CNG']
)

ownership = st.selectbox(
    'Ownership:',
    ['First Owner', 'Second Owner', 'Third Owner', 'Fourth Owner']
)

transmission = st.selectbox(
    'Transmission Type:',
    ['Manual', 'Automatic']
)

kms_driven = st.number_input('KMs Driven:', min_value=0)

seats = st.number_input('Number of Seats:', min_value=2, max_value=10, value=5)

mileage = st.number_input('Mileage (kmpl):')

engine = st.number_input('Engine (cc):')

max_power = st.number_input('Max Power (bhp):')

torque = st.number_input('Torque (Nm):')

manufacturing_year = st.number_input('Manufacturing Year:', min_value=1990, max_value=2026)

# ---------------- PREDICT ---------------- #

if st.button('Predict Price'):

    try:
        # Feature engineering
        current_year = datetime.now().year
        car_age = current_year - manufacturing_year

        # Input dictionary
        input_dict = {
            'kms_driven': kms_driven,
            'seats': seats,
            'mileage(kmpl)': mileage,
            'engine(cc)': engine,
            'max_power(bhp)': max_power,
            'torque(Nm)': torque,
            'car_age': car_age,
            'insurance_validity': insurance_validity,
            'fuel_type': fuel_type,
            'ownership': ownership,
            'transmission': transmission
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_dict])

        # Convert categorical to dummies
        input_df = pd.get_dummies(input_df)

        # Match training columns
        input_df = input_df.reindex(columns=columns, fill_value=0)

        # Prediction
        prediction = model.predict(input_df)[0]

        price_rs = int(prediction * 100000)

        st.success(f'💰 Predicted Price: ₹ {price_rs:,} ({prediction:.2f} Lakhs)')

    except Exception as e:
        st.error("⚠️ Something went wrong. Check inputs or model files.")
        st.write(e)