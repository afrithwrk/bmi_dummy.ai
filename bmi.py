import streamlit as st 
import google.generativeai as genai 
import pandas as pd 
import os
from dotenv import load_dotenv
load_dotenv()

# configure the api key
key_variable  = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key_variable)

# set up our page

st.title('HEALTH ASSISTANT FOR FITNESS🚀')
st.subheader('This page will help you to get information for fitness using BMI values📝')


st.sidebar.subheader('Height')

height = st.sidebar.text_input('Enter the height in meters : ')

st.sidebar.subheader('Weight')
weight = st.sidebar.text_input('Enter the weight in KGs : ')

# Calculating BMi values

try:
    height = pd.to_numeric(height)
    weight = pd.to_numeric(weight)
    if height > 0 and weight > 0:
        bmi = weight/(height**2)
        st.sidebar.success(f'BMI value is : {bmi:.2f} ')
    else:
        st.write('Please Enter positive values')
except:
    st.sidebar.info('Please enter positive values')
    
input = st.text_input('Ask your question here 🔍')

submit = st.button('Click here 🎯')
    
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_result(bmi,input):    
    if input is not None:
        
        prompt = f'''
        You are a health assistant now so you need to get results based on the fitness or other health related question.
        Use the BMI {bmi:.2f} for suggestions.
        You can suggest some diet to be followed and also some fitness exercises to the user.
        If any medication or medicine related question are asked always mention that 'check with the nearby doctors for the medications'
        '''
        
        result = model.generate_content(input+prompt)
        
    return result.text
    
if submit:
    with st.spinner('Result is loading......'):
        response = generate_result(bmi,input)
        st.markdown(':green[Result]')
        st.write(response)