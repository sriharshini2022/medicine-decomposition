import streamlit as st
import google.generativeai as genai
import os

# Set Google API Key
GOOGLE_API_KEY = "sgdf"  # Replace with your actual Google API key
genai.configure(api_key=GOOGLE_API_KEY)

# Streamlit App Config
st.set_page_config(page_title="Eco Disposal Advisor", layout="centered")
st.title("🌿 Eco-Friendly Medicine Disposal Advisor")
st.markdown("Enter any medicine name. We'll use AI to suggest how to dispose of it responsibly.")

# Medicine Input
medicine = st.text_input("💊 Medicine Name")

# Generate Prompt for AI
def generate_disposal_prompt(medicine_name):
    return f"""
You are an environmental pharmacist assistant. A user has a medicine named '{medicine_name}'.

First, identify the common active ingredients in this medicine.

Then, provide a clear, environmentally responsible disposal method for this medicine, following this format:

**Ingredients:** <list them here>  
**Disposal Method:** <give a safe, environmentally friendly method — do NOT flush unless absolutely necessary>

Make sure your advice is easy for a non-expert to follow.
"""

# Call Google Gemini API to get disposal advice
def get_disposal_advice_gemini(medicine_name):
    prompt = generate_disposal_prompt(medicine_name)
    
    # Use a valid model for text generation (based on the available list)
    model = genai.GenerativeModel('models/gemini-1.5-pro-001')  # Use this model from the available list
    response = model.generate_content(prompt)
    
    return response.text.strip()

# Main Action
if st.button("♻️ Get Disposal Advice"):
    if not medicine:
        st.warning("Please enter a medicine name.")
    else:
        with st.spinner("Thinking..."):
            try:
                # Call the AI model for disposal advice
                advice = get_disposal_advice_gemini(medicine)
                st.success("Here's the disposal recommendation:")
                st.markdown(advice)
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("Powered by Google Gemini • For educational and environmental awareness purposes only.")

