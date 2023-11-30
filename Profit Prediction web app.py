# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:11:36 2023

@author: aditi
"""

import numpy as np
import pickle
import streamlit as st

st.set_page_config(layout="wide")

# loading the saved model
loaded_model = pickle.load(open("C:/Users/aditi/OneDrive/Desktop/data science internship/profit_model.sav", 'rb'))

#creating a function for prediction
def profit_prediction(input_data):
    
    #Ensure input_data is a list or array
    if not isinstance(input_data, (list, np.ndarray)):
        raise ValueError("Input data should be a list or numpy array")
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)
    
    # Return the prediction as a string
    return prediction[0]

  
def main():
    
    # giving a title
    st.title('Profit Prediction Web APP')
    
    # getting the input data from the user
    RnDSpend=st.text_input('R&D Spend')
    Administration=st.text_input('Administration')
    MarketingSpend=st.text_input('Marketing Spend')
    
    
    # code for Prediction
    profit = ''
    
    # creating a button for Prediction
    if st.button("Profit Prediction Result"):
        input_data = [float(RnDSpend),float(Administration),float(MarketingSpend)]
        profit = profit_prediction(input_data)
    
    st.success(f'The profit is: {profit}')
    
if __name__ == '__main__':
    main()
    