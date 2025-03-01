from dotenv import load_dotenv
import  os
import google.generativeai as genai
import streamlit as st


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_response(question):
    model=genai.GenerativeModel("gemini-1.5-pro-latest")
    response=model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q & A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")


# When submit is clicked
if submit:
    if input.strip():  # Check if input is not empty
        response = get_gemini_response(input)
        st.subheader("The response is")
        st.write(response)
    else:
        st.error("Please enter a question.")  # Show error if input is empty