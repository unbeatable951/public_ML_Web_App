# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:43:14 2025

@author: SACHIN
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))


#sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction Sysytem',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           
                            icons =['activity','heart'],
                            
                            default_index=0)
#Diabetes Prediction Page
if(selected=='Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction Using ML')
    
    #getting the input from the user
    #columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number Of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    
    with col2:
        Insulin = st.text_input('Insulin')
        
    with col3:
        BMI = st.text_input('BMI')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
        
    with col2:
        Age = st.text_input('Age')
    
    
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button for Prediction
    if st.button('Diabetes test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction, Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The Person Is Diabetic'
        else:
            diab_diagnosis='The Person Is Not Diabetic'
    st.success(diab_diagnosis)      
    
    
    
    
    
    
    
    
    
if(selected=='Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction Using ML')
        
        #getting the input from the user
        #columns for input fields
    col1,col2,col3 = st.columns(3)
        
    with col1:
        age = st.text_input('Age')
            
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain Type')
            
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
            
    with col3:
        fbs = st.text_input('Fasting Blood Suger > 120mg/dl')
            
    with col1:
        restecg = st.text_input('Resting Electrocardiographic result')
            
    with col2:
        thalach = st.text_input('Maximum Heart rate Achieved')
            
    with col3:
        exang = st.text_input('Exercise Induced Angina')
            
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
            
    with col2:
        slope= st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colores by flouroscopy')
            
    with col1:
        thal = st.text_input('thal:0=normal;1=fixed defect;2=reversable defect')
            
            
         #code for prediction
    heart_diagnosis =''
         
         #creating a button for Prediction
    if st.button('Heart Disease test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, ca, thal]])
             
        if(heart_prediction[0]==1):
           heart_diagnosis = 'The Person Is Having Heart Disease'
        else:
            heart_diagnosis='The Person Is Not  Having Heart Disease'
                 
                 
    st.success(heart_diagnosis)       
         
     
        
        
      
            
    
    
    
    
    
    
    
    
    
    
    
    
    