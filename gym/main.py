import streamlit as st
from models.chatGemini import get_llm_response
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="IronAI - Smart Fitness",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CUSTOM CSS (Animation + Glassmorphism)
# ==========================================
st.markdown("""
    <style>
    /* 1. ANIMATED BACKGROUND */
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    .stApp {
        background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #141414);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }

    /* 2. GLASSMORPHISM FORM CONTAINER */
    /* We target the specific block where form usually resides if needed, 
       but here we style the inputs to float nicely. */
    
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        color: white;
    }

    /* 3. INPUT FIELD STYLING */
    /* Remove default borders and add modern dark feel */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-testid="stMarkdownContainer"] {
        color: white !important;
    }
    
label { color: #FFFFFF !important; }
    
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: rgba(0, 0, 0, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        color: white;
    }

    /* 4. TITLE STYLING */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 0px;
        text-shadow: 0 0 20px rgba(0,0,0,0.5);
    }
    .highlight {
        background: -webkit-linear-gradient(45deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.7);
        font-size: 14px;
        margin-bottom: 30px;
    }

    /* 5. BUTTON STYLING */
    div.stButton > button {
        background: rgb(10 7 7)
      
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: bold;
        letter-spacing: 1px;
        width: 100%;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(0, 198, 255, 0.6);
        color: white; /* Keep text white on hover */
    }
    
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HELPER FUNCTIONS
# ==========================================
# def get_llm_response(user_data):
#     time.sleep(1.5) # Simulate AI thinking
#     return f"""
#     ### ⚡ MISSION: {user_data['goal'].upper()}
    
#     **🔥 Calories:** 2,600 kcal | **💧 Water:** 3.5L
    
#     #### 🍽️ {user_data['diet']} Meal Plan
#     * **Pre-Workout:** Banana & Espresso
#     * **Post-Workout:** Whey Protein + 5g Creatine
#     * **Dinner:** Tofu stir-fry with Szechuan sauce
    
#     #### 🏋️‍♂️ Protocol
#     * **Compound Lift:** Deadlifts (3x5)
#     * **Accessory:** Lat Pulldowns (4x12)
#     * **Cardio:** 15min HIIT Sprints
#     """

# ==========================================
# 4. MAIN UI
# ==========================================

# CUSTOM HTML TITLE (Fixes the <span> issue)
st.markdown("<h1>IRON<span class='highlight'>AI</span> FITNESS</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>GENERATE YOUR ELITE PHYSIQUE PROTOCOL</p>", unsafe_allow_html=True)

# THE FORM
with st.form("fitness_form"):
    
    # Row 1
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        age = st.number_input("Age", 16, 90, 25)
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
    with col2:
        goal = st.selectbox("Goal", ["Muscle Gain", "Fat Loss", "Recomp", "Endurance"])
        height = st.number_input("Height (cm)", 100, 250, 175)
        diet = st.selectbox("Diet", ["Vegetarian", "Vegan", "Omnivore", "Keto"])

    # Spacer
    st.markdown("###")
    
    # Submit Button
    submitted = st.form_submit_button("🚀 INITIATE ANALYSIS")

# ==========================================
# 5. OUTPUT
# ==========================================
if submitted:
    user_data = {
        "gender": gender, "age": age, "weight": weight, 
        "height": height, "diet": diet, "goal": goal
    }
    
    with st.spinner("🔄 SYNCING WITH NEURAL NET..."):
        result = get_llm_response(user_data)
    
    # Result Card
    st.markdown(f"""
    <div style="
        background-color: rgba(0,0,0,0.6); 
        border: 1px solid #00c6ff; 
        border-radius: 15px; 
        padding: 20px; 
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 198, 255, 0.2);">
        {result}
    </div>
    """, unsafe_allow_html=True)