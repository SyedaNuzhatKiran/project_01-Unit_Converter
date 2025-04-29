import streamlit as st

# Unit categories and their conversion rates relative to base units
unit_data = {
    "Length": {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    },
    "Mass": {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄")
    st.title("🔄 Google-Style Unit Converter")

    category = st.selectbox("Select Unit Category", list(unit_data.keys()))

    if category != "Temperature":
        units = list(unit_data[category].keys())
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", units)
        value = st.number_input(f"Enter value in {from_unit}", step=0.1)

        if st.button("Convert"):
            base_value = value * unit_data[category][from_unit]
            converted_value = base_value / unit_data[category][to_unit]
            st.success(f"{value} {from_unit} = {converted_value:.4f} {to_unit}")
    else:
        units = list(unit_data["Temperature"].keys())
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", units)
        value = st.number_input(f"Enter temperature in {from_unit}", step=0.1)

        if st.button("Convert"):
            converted_value = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")

    st.markdown("---")
    st.caption("Created by Nuzhat Kiran — Inspired by Google Converter")

if __name__ == "__main__":
    main()
