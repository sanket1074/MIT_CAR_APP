import streamlit as st
import pickle

d1={'Comprehensive': 0,'Third Party insurance': 1,'Zero Dep': 2,'Not Available': 3,'Third Party': 1}
d2={'Petrol': 0, 'Diesel': 1, 'CNG': 2}
d3={'Manual': 0, 'Automatic': 1}
d4={'First Owner': 1,'Second Owner': 2,'Third Owner': 3,'Fourth Owner': 4,'Fifth Owner': 5}

final_model = pickle.load(open('final_model.pkl','rb'))

st.title('Car Price Prediction')

insurance_validity = st.selectbox('Insurance validity:', list(d1.keys()))
fuel_type = st.selectbox('Fuel Type:', list(d2.keys()))
kms_driven = st.text_input('KMs Driven:')
ownership = st.selectbox('Ownership:', list(d4.keys()))
transmission = st.selectbox('Transmission Type:', list(d3.keys()))

if st.button('Predict'):
    try:
        kms_driven = int(kms_driven)
    except:
        st.error("Enter valid KMs Driven")
        st.stop()

    insurance_validity = int(d1[insurance_validity])
    fuel_type = int(d2[fuel_type])
    ownership = int(d4[ownership])
    transmission = int(d3[transmission])

    test = [[insurance_validity, fuel_type, kms_driven, ownership, transmission]]

    yp = final_model.predict(test)[0]

    price_rs = int(yp * 100000)

    st.success(f'💰 Predicted Price: ₹ {price_rs:,} ({yp:.2f} Lakhs)')