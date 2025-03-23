import streamlit as st
from groq import Groq

# Set Streamlit page config
st.set_page_config(page_title="GenAI Project", layout="centered")

# Load API key securely
api_key = st.secrets["API_KEY"]

# Initialize Groq API client
client = Groq(api_key=api_key)

def generate_response(text: str, model_name="llama-3.3-70b-versatile"):
    """Generate response from the model using streaming."""
    try:
        stream = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ],
            model=model_name,
            stream=True
        )
        for chunk in stream:
            response = chunk.choices[0].delta.content
            if response:
                yield response
    except Exception as e:
        yield f"Error: {str(e)}"

# Apply Custom CSS for beautification
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stApp {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stTextArea textarea {
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 10px;
            font-size: 16px;
        }
        .stButton button {
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
        }
        .stButton button:hover {
            background-color: #45a049 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("Llama 3.3 Chatbot")
st.subheader("Powered by Groq API")

# User input
user_input = st.text_area("Ask any question:", placeholder="Type your query here...")

# Generate response on button click
if st.button("Generate", type="primary"):
    if user_input.strip():
        st.subheader("Model Response")
        st.write_stream(generate_response(user_input))
    else:
        st.warning("Please enter a question before clicking Generate.")
