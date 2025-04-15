import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set page config
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .title {
        text-align: center;
        color: #2a9d8f;
        font-size: 2.5em;
    }
    .description {
        text-align: center;
        color: #264653;
        font-size: 1.1em;
        margin-bottom: 2em;
    }
    .bmi-result {
        font-size: 1.8em;
        text-align: center;
        margin: 1em 0;
        padding: 0.5em;
        border-radius: 10px;
    }
    .underweight {
        background-color: #ffd166;
    }
    .normal {
        background-color: #06d6a0;
    }
    .overweight {
        background-color: #ef476f;
    }
    .obese {
        background-color: #d62839;
    }
    .stButton>button {
        width: 100%;
        background-color: #2a9d8f;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #21867a;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<h1 class="title">BMI Calculator</h1>', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2345/2345270.png", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### About BMI")
    st.markdown("""
    Body Mass Index (BMI) is a measure of body fat based on height and weight.
    
    **Categories:**
    - Underweight: < 18.5
    - Normal weight: 18.5 - 24.9
    - Overweight: 25 - 29.9
    - Obese: ≥ 30
    """)

# Main content
st.markdown('<h1 class="title">BMI Calculator</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Enter your weight and height to calculate your Body Mass Index</p>', 
            unsafe_allow_html=True)

# Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Measurement system selection
    measurement_system = st.radio(
        "Select measurement system:",
        ["Metric (kg & cm)", "Imperial (lbs & ft/in)"],
        horizontal=True
    )
    
    # Input fields based on measurement system
    if measurement_system == "Metric (kg & cm)":
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, step=0.1)
        height_m = height / 100
    else:
        weight_lbs = st.number_input("Weight (lbs)", min_value=2.2, max_value=660.0, step=0.1)
        weight = weight_lbs / 2.205
        feet = st.number_input("Height (feet)", min_value=1, max_value=8, step=1)
        inches = st.number_input("Height (inches)", min_value=0, max_value=11, step=1)
        height_m = (feet * 12 + inches) * 0.0254
    
    # Calculate BMI
    if st.button("Calculate BMI"):
        if weight > 0 and height_m > 0:
            bmi = weight / (height_m ** 2)
            bmi_rounded = round(bmi, 1)
            
            # Determine category and color
            if bmi < 18.5:
                category = "Underweight"
                color_class = "underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
                color_class = "normal"
            elif 25 <= bmi < 30:
                category = "Overweight"
                color_class = "overweight"
            else:
                category = "Obese"
                color_class = "obese"
            
            # Display results
            st.markdown(
                f'<div class="bmi-result {color_class}">'
                f'<strong>Your BMI:</strong> {bmi_rounded}<br>'
                f'<strong>Category:</strong> {category}'
                '</div>', 
                unsafe_allow_html=True
            )
            
            # BMI chart visualization
            fig, ax = plt.subplots(figsize=(8, 2))
            categories = ["Underweight", "Normal", "Overweight", "Obese"]
            ranges = [(0, 18.5), (18.5, 25), (25, 30), (30, 50)]
            colors = ['#ffd166', '#06d6a0', '#ef476f', '#d62839']
            
            for i, (start, end) in enumerate(ranges):
                ax.barh(0, end-start, left=start, color=colors[i], height=0.5)
            
            ax.axvline(x=bmi, color='black', linestyle='--', linewidth=2)
            ax.text(bmi+0.5, 0.25, f'You: {bmi_rounded}', va='center')
            ax.set_xlim(0, 50)
            ax.set_xticks(np.arange(0, 51, 5))
            ax.set_yticks([])
            ax.set_title('BMI Categories')
            st.pyplot(fig)
            
            # Health recommendations
            with st.expander("Health Recommendations"):
                if category == "Underweight":
                    st.markdown("""
                    - Consider consulting a nutritionist to develop a healthy weight gain plan
                    - Focus on nutrient-dense foods
                    - Incorporate strength training to build muscle mass
                    """)
                elif category == "Normal weight":
                    st.markdown("""
                    - Maintain your current healthy habits
                    - Continue regular physical activity
                    - Eat a balanced diet
                    """)
                elif category == "Overweight":
                    st.markdown("""
                    - Aim for gradual weight loss (0.5-1kg per week)
                    - Increase physical activity
                    - Reduce processed foods and sugary drinks
                    """)
                else:  # Obese
                    st.markdown("""
                    - Consult with a healthcare professional
                    - Consider a medically supervised weight loss program
                    - Focus on sustainable lifestyle changes
                    """)
        else:
            st.error("Please enter valid weight and height values.")