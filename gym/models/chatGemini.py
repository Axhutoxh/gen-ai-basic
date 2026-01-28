import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

def get_llm_response(user_data):
    # 1. Initialize Gemini Flash Model
 
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=st.secrets["GOOGLE_API_KEY"],
        temperature=0.7
    )

    # 2. Define the Prompt Template
    # This maps the input variables to the prompt string automatically
    template = """
    Act as an elite fitness coach.
    Create a personalized diet and workout routine for the following user:
    
    - **Age:** {age}
    - **Gender:** {gender}
    - **Weight:** {weight} kg
    - **Height:** {height} cm
    - **Goal:** {goal}
    - **Diet Preference:** {diet}
    
    Please provide:
    1. A daily calorie and macro target.
    2. A sample daily meal plan based on their diet preference.
    3. A concise workout split (days of the week).
    
    Format the response in clean Markdown.
    """
    
    prompt = PromptTemplate.from_template(template)

    # 3. Create the Chain (LCEL Syntax)
    # prompt | llm -> pipes the prompt output directly into the model
    chain = prompt | llm

    # 4. Run the Chain
    # We pass 'user_data' directly because its keys (age, gender, etc.) 
    # match the variables defined in the template above.
    response = chain.invoke(user_data)

    return response.content