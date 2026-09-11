import streamlit as st

# Page Configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Custom CSS for Animated Background and Glassmorphism UI
custom_css = """
<style>
/* 1. Animated Gradient Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #0f172a, #1e1b4b, #311042, #0f172a);
    background-size: 400% 400%;
    animation: gradientAnimation 12s ease infinite;
}

@keyframes gradientAnimation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Make Streamlit Header Transparent */
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

/* 2. Main Content Box (Glassmorphism Card) */
.main .block-container {
    background: rgba(255, 255, 255, 0.07);
    padding: 3rem 2.5rem;
    border-radius: 20px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    margin-top: 2rem;
}

/* Title & Text Styling */
h1 {
    color: #ffffff !important;
    text-align: center;
    font-weight: 700;
}

label {
    color: #e2e8f0 !important;
    font-weight: 500;
}

/* Custom Button Styling */
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    padding: 12px;
    border-radius: 10px;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(168, 85, 247, 0.4);
}
</style>
"""

# Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)

# App UI Content
st.title("⚖️ Health Metrics: BMI Calculator")

st.write("---")

# Input fields
weight = st.number_input("Oyage bara danna (kg):", min_value=1.0, step=0.1)
height_cm = st.number_input("Oyage usa danna (cm):", min_value=1.0, step=1.0)

st.write("")

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
        st.error("Usa 0 wenna ba mchan!!!")