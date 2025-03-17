import streamlit as st   # type: ignore
from currency_api import convert_currency, convert_gold  
from ai_model import detect_input  
from voice_input import voice_input   # type: ignore
from abjad_calculator import calculate_abjad  # type: ignore # ABJAD Module Import

st.title("🧠 AI-Powered Smart Unit Converter & ABJAD Calculator")  

# 🔹 Unit Converter Section  
st.header("🔄 Unit Converter")  
user_input = st.text_input("Enter value & unit (e.g., '10 KG'):")  

if st.button("Convert"):  
    try:  
        value, unit = user_input.split()  
        value = float(value)  

        if unit.upper() in ["USD", "PKR", "SAR"]:  
            result = convert_currency(value, unit.upper(), "PKR")  
        elif unit.lower() in ["tola", "gram"]:  
            result = convert_gold(value, unit.lower())  
        else:  
            result = "Invalid Unit"  

        st.write("### Converted Values:", result)  
    except:  
        st.write("Invalid Input! Please enter correctly.")  

if st.button("Use Voice Input"):  
    voice_text = voice_input()  
    st.write(f"You said: {voice_text}")  

# 🔹 ABJAD Calculator Section  
st.header("🔠 ABJAD Calculator")  
abjad_input = st.text_input("Enter Arabic text for ABJAD calculation:")  

if st.button("Calculate ABJAD"):  
    if abjad_input:  
        abjad_value = calculate_abjad(abjad_input)  
        st.write(f"ABJAD Numeric Value: {abjad_value}")  
    else:  
        st.write("Please enter Arabic text.")