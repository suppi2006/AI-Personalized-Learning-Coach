import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

def generate_learning_plan(topic, level, goal, hours):
    if not api_key:
        return "Please configure GEMINI_API_KEY in your .env file."

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
        Act as a personalized AI learning coach.

        Topic: {topic}
        Student level: {level}
        Learning goal: {goal}
        Daily study time: {hours} hours

        Create a personalized learning plan with:
        1. Learning objectives
        2. Daily study schedule
        3. Beginner-friendly explanations
        4. Practice exercises
        5. Quiz questions with answers
        6. Progress tracking suggestions

        Use clear, simple language.
        """

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text or "No response generated."

    except Exception as e:
        return f"Error generating plan: {e}"