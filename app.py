import streamlit as st
from learning_coach import generate_learning_plan

st.set_page_config(
    page_title="AI Personalized Learning Coach",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Personalized Learning Coach")
st.write("Your personal AI assistant for smarter learning!")

with st.sidebar:
    st.header("👩‍🎓 Your Learning Profile")

    name = st.text_input("Your name")
    level = st.selectbox(
        "Your current level",
        ["Beginner", "Intermediate", "Advanced"]
    )
    topic = st.text_input("What do you want to learn?")
    goal = st.text_area("Your learning goal")
    hours = st.slider("Daily study hours", 1, 8, 2)

if st.button("🚀 Generate My Learning Plan"):
    if not topic.strip() or not goal.strip():
        st.warning("Please enter your topic and learning goal.")
    else:
        with st.spinner("Creating your personalized learning plan..."):
            plan = generate_learning_plan(
                topic, level, goal, hours
            )

        st.session_state["learning_plan"] = plan

if "learning_plan" in st.session_state:
    st.subheader("📚 Your Personalized Learning Plan")
    st.markdown(st.session_state["learning_plan"])

    st.download_button(
        "📥 Download Learning Plan",
        data=st.session_state["learning_plan"],
        file_name="learning_plan.md",
        mime="text/markdown"
    )

st.divider()
st.caption("Powered by Streamlit and Google Gemini AI")