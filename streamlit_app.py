import streamlit as st
import requests

# Local FastAPI
API_URL = "https://myproject-639o.onrender.com"

st.set_page_config(
    page_title="AI Orchestration",
    page_icon="🤖"
)

st.title("🤖 AI Orchestration System")

st.write("FastAPI + Streamlit Demo")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question")

    else:

        try:

            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "question": question
                },
                timeout=30
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Response received")

                st.write(
                    result["answer"]
                )

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Cannot connect to FastAPI."
            )