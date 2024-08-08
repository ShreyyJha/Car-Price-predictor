import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
from streamlit.web.cli import main
import base64

model = pk.load(open('model.pkl','rb'))
st.header('Car Price Predictor')

path = r"C:\Users\Asus\Downloads\Cardetails.csv"
cars_data = pd.read_csv(path)

def get_first_word(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip(' ')
    
cars_data['name'] = cars_data['name'].apply(get_first_word)

name = st.selectbox('Car Brand',cars_data['name'].unique())
year = st.slider('Car manufacture year',1990,2024)
km_driven = st.slider('No of kms Driven',0,200000)
fuel = st.selectbox('Fuel Type',cars_data['fuel'].unique())
seller_type = st.selectbox('Seller Type',cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission Type',cars_data['transmission'].unique())
owner = st.selectbox('Owner',cars_data['owner'].unique())
mileage = st.slider('Car Mileage',10,40)
engine = st.slider('Engine cc',700,5000)
max_power = st.slider('Max Power (bhp)',0,200)
seats = st.slider('No of Seats',4,10)

if st.button("Predict Price"):
    input_data_model = pd.DataFrame(
    [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]],
    columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
)

    input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],inplace=True)
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4],inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2],inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3],inplace=True)
    input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner','Fourth & Above Owner', 'Test Drive Car'],[1,2,3,4,5],inplace=True)

    car_price = model.predict(input_data_model)
    st.markdown('The price of the car is going to be '+str(car_price[0].round(2))+' INR')

def add_background(image_path):
    with open(r"C:\Users\Asus\Desktop\cars.jpeg", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
          f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_image});
            align-items: flex-end;
            background-position: 40px;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
image_path = r"C:\Users\Asus\Desktop\cars.jpeg"  # Change the path as needed
add_background(image_path)