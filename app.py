import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ Health Metrics: BMI Calculator")

# Input fields
weight = st.number_input("Oyaage bara danna (kg):", min_value=1.0, step=0.1)


height_cm = st.number_input("Oyaage usa danna (cm):", min_value=1.0, step=1.0)

if st.button("Calculate BMI"):
    if height_cm > 0:
        
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        
        st.subheader(f"Oyaage BMI eka: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("Bara madi (Underweight)")
        elif 18.5 <= bmi < 25:
            st.success("Bara hari (Healthy)")
        else:
            st.error("Bara wadi (Overweight)")
    else:
        st.error("Usa 0 wenna ba mchan!")