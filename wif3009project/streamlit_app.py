import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load('HousePricing.pkl')

# Mapping dictionaries
property_type_dict = {
    "1-sty Terrace/Link House": 0,
    "1.5-sty Terrace/Link House": 1,
    "2-sty Terrace/Link House": 2,
    "2.5-sty Terrace/Link House": 3,
    "3-sty Terrace/Link House": 4,
    "3.5-sty Terrace/Link House": 5,
    "4-sty Terrace/Link House": 6,
    "4.5-sty Terrace/Link House": 7,
    "Apartment": 8,
    "Bungalow": 9,
    "Cluster House": 10,
    "Condominium": 11,
    "Flat": 12,
    "Residential Land": 13,
    "Semi-detached House": 14,
    "Serviced Residence": 15,
    "Townhouse": 16
}

location_dict = {
    "Ampang": 0,
    "Ampang Hilir": 1,
    "Bandar Damai Perdana": 2,
    "Bandar Menjalara": 3,
    "Bandar Tasik Selatan": 4,
    "Bangsar": 5,
    "Bangsar South": 6,
    "Batu Caves": 7,
    "Brickfields": 8,
    "Bukit Bintang": 9,
    "Bukit Jalil": 10,
    "Bukit Tunku (Kenny Hills)": 11,
    "Chan Sow Lin": 12,
    "Cheras": 13,
    "City Centre": 14,
    "Country Heights Damansara": 15,
    "Damansara": 16,
    "Damansara Heights": 17,
    "Desa Pandan": 18,
    "Desa ParkCity": 19,
    "Desa Petaling": 20,
    "Dutamas": 21,
    "Gombak": 22,
    "Jalan Ipoh": 23,
    "Jalan Klang Lama (Old Klang Road)": 24,
    "Jalan Kuching": 25,
    "Jalan Sultan Ismail": 26,
    "Jinjang": 27,
    "KL City": 28,
    "KL Eco City": 29,
    "KL Sentral": 30,
    "KLCC": 31,
    "Kepong": 32,
    "Keramat": 33,
    "Kuchai Lama": 34,
    "Mid Valley City": 35,
    "Mont Kiara": 36,
    "OUG": 37,
    "Pandan Indah": 38,
    "Pandan Jaya": 39,
    "Pandan Perdana": 40,
    "Pantai": 41,
    "Puchong": 42,
    "Rawang": 43,
    "Salak Selatan": 44,
    "Segambut": 45,
    "Sentul": 46,
    "Seputeh": 47,
    "Setapak": 48,
    "Setiawangsa": 49,
    "Sri Hartamas": 50,
    "Sri Petaling": 51,
    "Sungai Besi": 52,
    "Taman Desa": 53,
    "Taman Melawati": 54,
    "Taman Tun Dr Ismail": 55,
    "Titiwangsa": 56,
    "Wangsa Maju": 57,
    "taman cheras perdana": 58
}

furnishing_mapping = {
    'Fully Furnished': (1, 0, 0),
    'Partly Furnished': (0, 1, 0),
    'Unfurnished': (0, 0, 1)
}

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
)

# Streamlit app
st.title('House Price Prediction')

bedrooms = st.number_input('Enter the number of bedrooms', min_value=0.0, format='%f')
bathrooms = st.number_input('Enter the number of bathrooms', min_value=0.0, format='%f')
sqft = st.number_input('Enter the House Size in SqFT', min_value=0.0, format='%f')
furnishing = st.selectbox('Select Furnishing', list(furnishing_mapping.keys()))
price_per_sqft = st.number_input('Enter the Price per Sqft', min_value=0.0, format='%f')
property_type = st.selectbox('Select Property Type', list(property_type_dict.keys()))
car_parks = st.number_input('Enter the number of car parks', min_value=0.0, format='%f')
location = st.selectbox('Select Location', list(location_dict.keys()))

if st.button('Predict Price'):
    property_type_value = property_type_dict[property_type]
    location_value = location_dict[location]
    full_furnishing, part_furnishing, unfurnishing = furnishing_mapping[furnishing]

    X = np.array([[location_value, bedrooms, bathrooms, car_parks, property_type_value, sqft, full_furnishing, part_furnishing, unfurnishing, price_per_sqft]])
    price = model.predict(X)
    predicted_price = "{:,.2f}".format(price[0])

    st.write(f"The predicted house price is: RM {predicted_price}")
