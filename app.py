import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ Health Metrics: BMI Calculator")
st.write("Docker & CI/CD igena ganna hadapu simple project ekak.")

# Input fields
weight = st.number_input("Oyaage bara danna (kg):", min_value=1.0, step=0.1)
height = st.number_input("Oyaage usa danna (meters):", min_value=0.1, step=0.01)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.subheader(f"Oyaage BMI eka: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("Bara madi (Underweight)")
        elif 18.5 <= bmi < 25:
            st.success("Bara hari (Healthy)")
        else:
            st.error("Bara wadi (Overweight)")
    else:
        st.error("Usa 0 wenna ba mchan!")