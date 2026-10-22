
import streamlit as st

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

if st.button("Generate Homework Help"):
    if topic.strip():
        st.info("Your topic: " + topic)
        st.write("Subject:", subject)
        st.write("AI generation will be connected in the next step.")
    else:
        st.warning("Please enter a topic first.")
