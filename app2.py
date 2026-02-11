import streamlit as st
import pickle
import numpy as np
import os
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))


st.title("Market Price Prediction App")
st.write("Predict price per kg based on market conditions")

# Real categories (ziwe sawa na dataset yako)
commodities = ["Beans", "Rice", "Tomatoes", "Potatoes"]
markets = ["Dar es Salaam", "Arusha", "Mwanza"]
seasons = ["Dry", "Rainy"]
supply_levels = ["Low", "Medium", "High"]

# User Inputs (REAL VALUES)
commodity = st.selectbox("Select Commodity", commodities)
market = st.selectbox("Select Market", markets)
month = st.slider("Select Month", 1, 12)
season = st.selectbox("Select Season", seasons)
supply_level = st.selectbox("Select Supply Level", supply_levels)

# Encoding manually (simple mapping)
commodity_map = {name: i for i, name in enumerate(commodities)}
market_map = {name: i for i, name in enumerate(markets)}
season_map = {name: i for i, name in enumerate(seasons)}
supply_map = {name: i for i, name in enumerate(supply_levels)}

if st.button("Predict Price"):

    input_data = np.array([[
        commodity_map[commodity],
        market_map[market],
        month,
        season_map[season],
        supply_map[supply_level]
    ]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Price per Kg: {prediction[0]:,.2f} TZS")

