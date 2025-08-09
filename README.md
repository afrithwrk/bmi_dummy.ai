# bmi_dummy.ai

Health Assistant for fitness based on bmi
  * An AI-powered fitness and health assistant built with Streamlit and Google Generative AI.
  * This app calculates BMI and provides personalized diet, exercise, and health recommendations based on user inputs.

Features :
  * BMI Calculator – Enter height & weight to get your BMI instantly.
  * AI-Powered Recommendations – Diet, exercise, and general fitness tips generated using Google Generative AI (Gemini).
  * Safe Medical Guidance – If medical advice is requested, the app recommends consulting a doctor.
  * Interactive UI – Built with Streamlit for a smooth, user-friendly experience.

Tech Stack :
  * Python
  * Streamlit
  * Google Generative AI API (Gemini)
  * Pandas
  * dotenv for environment variable management

Installation & Setup :
1️,Clone the Repository
   *   git clone https://github.com/yourusername/health-assistant-fitness.git
   *   cd health-assistant-fitness

2 ,Create Virtual Environment & Install Dependencies
   * python -m venv venv
   * source venv/bin/activate   # On Mac/Linux
   * venv\Scripts\activate      # On Windows
   * pip install -r requirements.txt

3 ,Set Up API Key
  * Create a .env file in the project root.
  * Add your Google Generative AI API key:

4 ,Run the App
  * streamlit run bmi.py

Screenshots :
  * BMI Calculator Sidebar
  * AI-Powered Recommendations

Example Prompt :
  * Height: 1.75 m
  * Weight: 68 kg
  * BMI: 22.20
  * Question: "Suggest a weekly workout plan"

AI Response :
  * Monday: Cardio (30 min) + Strength training (upper body)
  * Wednesday: Yoga (45 min) + Core exercises
  * Friday: Cardio (20 min) + Strength training (lower body)
  * ... and more diet suggestions.

Disclaimer :
  * This app is not a substitute for professional medical advice.
  * For any health concerns or medication advice, consult a certified healthcare professional.

Contributing :
  * Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

License :
  * This project is licensed under the MIT License.

