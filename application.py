import streamlit as st
import pandas as pd
import sys
from src.exception import CustomException
from src.pipeline.predict_pipeline import PredictPipeline

# Load the pre-trained model
@st.cache_data
def load_predict_pipeline():
    return PredictPipeline()

# Create a Streamlit app
def main():
    try:
        predict_pipeline = load_predict_pipeline()

        st.sidebar.title('Input Features')
        gender = st.sidebar.selectbox('Gender', ['male', 'female'])
        race_ethnicity = st.sidebar.selectbox('Race/Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
        parental_education = st.sidebar.selectbox('Parental Level of Education', ['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree', 'master\'s degree'])
        lunch = st.sidebar.selectbox('Lunch', ['standard', 'free/reduced'])
        test_preparation_course = st.sidebar.selectbox('Test Preparation Course', ['none', 'completed'])
        reading_score = st.sidebar.slider('Reading Score', 0, 100, 50)
        writing_score = st.sidebar.slider('Writing Score', 0, 100, 50)

        # Create DataFrame with specified data types
        input_data = pd.DataFrame({
            'gender': [gender],
            'race_ethnicity': [race_ethnicity],
            'parental_level_of_education': [parental_education],
            'lunch': [lunch],
            'test_preparation_course': [test_preparation_course],
            'reading_score': [reading_score],
            'writing_score': [writing_score]
        }, index=[0])  # Specify data types
        input_data['reading_score'] = input_data['reading_score'].astype('int32')
        input_data['writing_score'] = input_data['writing_score'].astype('int32')

        if st.button('Predict'):
            predictions = predict_pipeline.predict(input_data)

            st.title('Your ML Model App')
            st.write('Prediction:', predictions[0])

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == '__main__':
    main()
