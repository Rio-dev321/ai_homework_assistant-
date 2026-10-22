
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Homework Assistant",
    page_icon="📚"
)

st.title("📚 AI Homework Assistant")
st.write("Your personal AI study helper!")

topic = st.text_input("Enter your subject topic")

subject = st.selectbox(
    "Choose your subject",
    ["Biology", "Chemistry", "Physics", "English"]
)

language = st.selectbox(
    "Choose answer language",
    ["Easy English", "Roman Urdu", "Both English and Roman Urdu"]
)

if st.button("Generate Homework Help"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            with st.spinner("RIO is preparing your lesson..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are RIO, a helpful Class 10 tutor. "
                                "Explain topics with a definition, detailed "
                                "explanation, daily-life examples, key points, "
                                "and practice questions. Use simple language."
                            )
                        },
                        {
                            "role": "user",
                            "content": (
                                f"Subject: {subject}\n"
                                f"Topic: {topic}\n"
                                f"Answer language: {language}"
                            )
                        }
                    ],
                    temperature=0.5
                )

            st.subheader(f"{subject}: {topic}")
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            st.error("AI connection failed. Please check your API key and settings.")
            st.caption(str(e))
