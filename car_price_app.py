# import streamlit as st
# import pandas as pd
# import pickle

# # Load the trained pipeline (Random Forest with preprocessing inside)
# with open('car_price_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# # Streamlit App Title
# st.title("🚗 Car Price Prediction App")

# st.write(
#     """
#     This app predicts the **estimated price** of a used car.
    
#     Fill out the details below:
#     """
# )

# # Input fields for user
# company = st.text_input("Enter Company Name")
# name = st.text_input("Enter Car Model Name")
# year = st.number_input("Enter Year of Purchase", min_value=1990, max_value=2025, step=1)
# kms_driven = st.number_input("Enter Kilometers Driven", min_value=0, step=500)
# fuel_type = st.selectbox("Select Fuel Type", ["Petrol", "Diesel", "LPG"])

# # Prediction Button
# if st.button("Predict Price"):
#     # Create input DataFrame with correct column order
#     input_data = pd.DataFrame(
#         [[company, name, year, kms_driven, fuel_type]],
#         columns=["company", "name", "year", "kms_driven", "fuel_type"]
#     )

#     # Predict using the loaded model
#     predicted_price = model.predict(input_data)[0]

#     # Show result
#     st.success(f"Estimated Car Price: ₹ {int(predicted_price):,}")

import streamlit as st
import pandas as pd
import pickle

# Load model
with open('car_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Sample dropdown options (you can expand based on your dataset)
company_options = ["Maruti", "Hyundai", "Honda", "Toyota", "Ford", "Mahindra", "Tata", "Chevrolet", "BMW"]
model_options = {
    "Maruti": ["Swift", "Wagon R", "Baleno"],
    "Hyundai": ["i20", "Creta", "Verna"],
    "Honda": ["City", "Civic", "Jazz"],
    "Toyota": ["Fortuner", "Innova", "Etios"],
    "Ford": ["EcoSport", "Figo", "Endeavour"],
    "Mahindra": ["XUV500", "Scorpio", "Bolero"],
    "Tata": ["Nexon", "Altroz", "Harrier"],
    "Chevrolet": ["Beat", "Cruze", "Sail"],
    "BMW": ["3 Series", "X1", "5 Series"]
}

# --- Page Setup ---
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")

# --- Logo and Banner ---
st.markdown("""
    <div style="display: flex; align-items: center;">
        <img src="https://cdn-icons-png.flaticon.com/512/743/743007.png" width="50" style="margin-right:10px;">
        <h1 style="margin: 0; padding: 0;">Car Price Prediction</h1>
    </div>
""", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1200&q=80", use_column_width=True)

st.markdown("### 🚘 Enter the car details below to estimate its price:")

# --- Form with Tooltips and Dropdowns ---
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        company = st.selectbox(
            "🔹 Select Company",
            company_options,
            help="Choose the car manufacturer"
        )

        model_name = st.selectbox(
            "🚙 Select Car Model",
            model_options[company],
            help="Select a model based on the chosen company"
        )

    with col2:
        year = st.number_input(
            "📅 Year of Purchase",
            min_value=1990,
            max_value=2025,
            step=1,
            help="Year when the car was purchased"
        )

        kms_driven = st.number_input(
            "🛣️ Kilometers Driven",
            min_value=0,
            step=500,
            help="Total kilometers the car has been driven"
        )

    fuel_type = st.selectbox(
        "⛽ Fuel Type",
        ["Petrol", "Diesel", "LPG"],
        help="Fuel type the car uses"
    )

    submitted = st.form_submit_button("🔍 Predict Price")

# --- Prediction ---
if submitted:
    input_df = pd.DataFrame(
        [[company, model_name, year, kms_driven, fuel_type]],
        columns=["company", "name", "year", "kms_driven", "fuel_type"]
    )

    predicted_price = model.predict(input_df)[0]
    formatted_price = f"₹ {int(predicted_price):,}"

    st.markdown("---")
    st.success(f"🎯 Estimated Car Price: {formatted_price}")

    # Animation: Balloons for affordable cars, snow for luxury
    if predicted_price < 300000:
        st.balloons()
    elif predicted_price > 1000000:
        st.snow()

    st.info("This is an estimated price based on historical data. Actual market prices may vary.")

# --- Footer ---
st.markdown("""
    <hr style="border-top: 1px solid #bbb;">
    <center>
        Made with ❤️ using Streamlit<br>
        <small>© 2025 CarPredict Inc.</small>
    </center>
""", unsafe_allow_html=True)







