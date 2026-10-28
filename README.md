# 🎓 AI Personalized Learning Coach

An AI-powered learning assistant that generates personalized study plans based on a student's learning level, topic of interest, learning goals, and available daily study hours.

## ✨ Features

- 👤 Enter your name and learning profile.
- 📚 Choose your current learning level.
- 🎯 Specify the topic you want to learn and your learning goal.
- ⏰ Set your daily study hours.
- 🤖 Generate a personalized learning plan using Google Gemini AI.
- 📥 Download the generated learning plan.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv

## 📋 Prerequisites

- Python 3.10 or later
- A Google Gemini API key

## ⚙️ Installation and Setup

1. Clone this repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Open the project folder:

   ```bash
   cd YOUR_PROJECT_FOLDER
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. Run the application:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL displayed in your terminal.

## 🚀 How to Use

1. Enter your name.
2. Select your current learning level.
3. Enter the topic you want to learn.
4. Describe your learning goal.
5. Set your daily study hours.
6. Click **Generate My Learning Plan**.
7. Review and download your personalized plan.

## 🔐 Security

- Store API keys in environment variables.
- Never upload your `.env` file or expose your API key in a public repository.
- Keep `.env` listed in `.gitignore`.

## 🎯 Project Objective

The goal of this project is to make learning more personalized and structured by using generative AI to help students organize their study time and learning goals.

## 👩‍💻 Author

Supriya

## 📄 License

This project was developed as part of an AI internship project.
