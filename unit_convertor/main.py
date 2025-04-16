import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
        "seconds_minutes": lambda s: s / 60,
        "minutes_seconds": lambda m: m * 60,
        "hours_minutes": lambda h: h * 60,
        "minutes_hours": lambda m: m / 60
    }
    
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return "Conversion not supported"

# --- Streamlit UI ---
st.set_page_config(page_title="Smart Unit Converter", page_icon="📏", layout="centered")
st.title("\U0001F4CF Smart Unit Converter")

# Tabs for different unit types
tab1, tab2, tab3, tab4 = st.tabs(["Length", "Weight", "Temperature", "Time"])

with tab1:
    st.subheader("Length Conversion")
    value = st.number_input("Enter the value:", min_value=0.0, format="%.2f", key="length_value")
    unit_from = st.selectbox("Convert from:", ["meter", "kilometer"], key="length_from")
    unit_to = st.selectbox("Convert to:", ["meter", "kilometer"], key="length_to")
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result:.2f}" if isinstance(result, (int, float)) else f"Error: {result}")

with tab2:
    st.subheader("Weight Conversion")
    value = st.number_input("Enter the value:", min_value=0.0, format="%.2f", key="weight_value")
    unit_from = st.selectbox("Convert from:", ["gram", "kilogram"], key="weight_from")
    unit_to = st.selectbox("Convert to:", ["gram", "kilogram"], key="weight_to")
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result:.2f}" if isinstance(result, (int, float)) else f"Error: {result}")

with tab3:
    st.subheader("Temperature Conversion")
    value = st.number_input("Enter the temperature:", format="%.2f", key="temp_value")
    unit_from = st.selectbox("Convert from:", ["celsius", "fahrenheit"], key="temp_from")
    unit_to = st.selectbox("Convert to:", ["celsius", "fahrenheit"], key="temp_to")
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result:.2f} {unit_to}" if isinstance(result, (int, float)) else f"Error: {result}")

with tab4:
    st.subheader("Time Conversion")
    value = st.number_input("Enter the time:", min_value=0.0, format="%.2f", key="time_value")
    unit_from = st.selectbox("Convert from:", ["seconds", "minutes", "hours"], key="time_from")
    unit_to = st.selectbox("Convert to:", ["seconds", "minutes", "hours"], key="time_to")
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result:.2f} {unit_to}" if isinstance(result, (int, float)) else f"Error: {result}")
