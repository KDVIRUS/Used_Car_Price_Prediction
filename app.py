import streamlit as st
import pickle
import pandas as pd

pipe_gbr = pickle.load(open('pipe_gbr.pkl', 'rb'))

st.title('Used Cars Price Predictor')

fuel_types = ['Petrol', 'CNG', 'Diesel']
seller_types = ['Dealer', 'Individual']
transmission_types = ['Automatic', 'Manual']

fuel_type = st.selectbox('Fuel Type',sorted(fuel_types))
seller_type = st.selectbox('Seller Type',sorted(seller_types))
transmission_type = st.selectbox('Transmission',sorted(transmission_types))

col3, col4, col5, col6 = st.columns(4)

with col3:
    kms_driven = st.number_input('KMS Driven')
with col4:
    past_owners = st.number_input('Number Of Past Owners: ')
with col5:
    age = 2024 - st.number_input('Year Of Manufacture')
with col6:
    present_price = st.number_input('Current Price of Car')

if st.button('Predict Price'):

    input_df = pd.DataFrame(
     {'Present_Price(lacs)' : [present_price], 'Kms_Driven' : [kms_driven], 'Fuel_Type' : [fuel_type], 'Seller_Type': [seller_type], 'Transmission': [transmission_type], 'Past_Owners': [past_owners], 'Age': [age]}
     )
    
    result = pipe_gbr.predict(input_df)
    
    st.header("Predicted Price for your car is: " + str(int(result[0])))
    

