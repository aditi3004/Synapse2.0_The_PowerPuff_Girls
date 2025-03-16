import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel

# Initialize Vertex AI
vertexai.init(project="cummins123", location="us-central1")
model = GenerativeModel("gemini-2.0-flash-001")

def generate_content_from_prompt(user_prompt):
    """Generate allergy predictions & dietary alternatives from user input."""
    try:
        modified_prompt = (f"{user_prompt} \n\nThe system predicts possible allergies from symptoms, "
                           "identifies potential allergens in food products, and provides safe dietary alternatives.")
        response = model.generate_content(modified_prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

# Streamlit UI
st.set_page_config(page_title="Allergy & Diet Assistant", page_icon="🥗", layout="centered")

# Title & Description
st.title("🥗 Smart Allergy & Diet Assistant")
st.markdown("Enter food details or symptoms to detect allergens and get safe dietary recommendations.")

# User Input
user_prompt = st.text_area("🔍 Enter symptoms or food concerns:", height=100, 
                           placeholder="Example: I feel itchy after eating peanuts.")

# Submit Button
if st.button("🔍 Analyze Allergy & Get Alternatives"):
    if user_prompt.strip():
        response = generate_content_from_prompt(user_prompt)
        st.subheader("🛑 **Detected Allergens & Recommendations:**")
        st.markdown(f"<div style='background-color:#ffe6e6; padding:15px; border-radius:10px; font-size:16px;'>"
                    f"{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text.")
