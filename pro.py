# 📦 IMPORTING THE NECESSARY LIBRARIES
import streamlit as st                         # For building the web interface
from together import Together                 # For accessing Together AI's language models
import os

# 🔐 SETTING THE API KEY FOR TOGETHER AI
# Method 1: Set as environment variable (recommended)
os.environ["TOGETHER_API_KEY"] = "8181e1cbb4d7aa4ec2b6edb89ab98521c7d63fb7ba0814780062fc78fcae8a75"
client = Together()

# Method 2: Alternative - pass as keyword argument (if supported)
# client = Together(api_key="your_api_key_here")

# 🧠 CHOOSING THE MODEL
model_name = "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo"  # Updated model name

# 🧑 DEFINING USER ROLE FOR THE CHAT FORMAT
userrole = "user"                              # Role is set as 'user' for chat input

# 📚 PRE-DEFINED PROMPT TO GUIDE THE MODEL
pre_prompt = "Teach me the following concept: " # Pre-prompt for teaching

# 📝 VARIABLE TO STORE RESPONSE
response = ""                                  # Empty response placeholder

# 🎓 STREAMLIT USER INTERFACE
st.title("PROFESSOR_GPT APP")                  # Main title of the app (fixed typo)
st.divider()                                   # Horizontal line for UI separation

# ✍️ TEXT INPUT FIELD FOR USER QUERY
prompt = st.text_input("What do you want to learn?") # User inputs the topic

# 🔘 BUTTON TO TRIGGER GPT RESPONSE
gptbutton = st.button("Teach me")              # Button to start the process

# 💡 SMALL CAPTION TO GUIDE USERS
st.caption("ProfessorGPT will work when you press the button")
st.divider()                                   # Another UI divider

# ▶️ IF BUTTON IS PRESSED, PROCESS THE REQUEST
if gptbutton and prompt:  # Added check to ensure prompt is not empty
    with st.spinner("I am preparing your lecture"): # Show a loading spinner while processing
        try:
            response = client.chat.completions.create(     # Call Together AI Chat Completion API
                model=model_name,
                messages=[
                    {"role": userrole, "content": pre_prompt + prompt} # Combine pre_prompt with user input
                ]
            )
            
            st.snow()                                        # Nice snow effect on completion
            st.write(response.choices[0].message.content)    # Display the AI-generated response
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please check your API key and internet connection.")

elif gptbutton and not prompt:
    st.warning("Please enter a topic you want to learn about!")