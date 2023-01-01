
#Step 8: Import all the necessary libraries
import pickle
import streamlit as st

pickle_in = open('classifier', 'rb')                        #Open our classifier binary file in read mode
classifier = pickle.load(pickle_in)

@st.cache()

# Define the function which will make the prediction using data
# inputs from users
def prediction(age, sex,
               non_anginal_pain, max_heart_rate, exercise_induced_angina):
    
    # Make predictions
    prediction = classifier.predict(
        [[age,sex, non_anginal_pain,max_heart_rate, exercise_induced_angina]])
    
    if prediction == 0:
        pred = 'You probably do not suffer from heart disease'
    else:
        pred = 'PLEASE SEE A DOCTOR!  You might are suffering from heart disease'
    return pred

# This is the main function in which we define our webpage
def main():
    
    # Create input fields
    age = st.number_input("age",
                                  min_value=30,
                                  max_value=100,
                                  value=34,
                                  step=1,
                                 )
    
    sex = st.number_input("sex -(0-1)",
                                  min_value=0,
                                  max_value=1,
                                  value=1,
                                 )
    non_anginal_pain = st.number_input("non_anginal_pain -(0-1)",
                          min_value=0,
                          max_value=1,
                          value=1,
                         )

    max_heart_rate = st.number_input("max_heart_rate",
                          min_value=50,
                          max_value=210,
                          value=55,
                          step=1
                         )
   
    exercise_induced_angina = st.number_input("exercise_induced_angina -(0-1)",
                          min_value=0,
                          max_value=1,
                          value=1,
                         )

    result = ""
    
    # When 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(age,sex,non_anginal_pain, max_heart_rate, exercise_induced_angina)
        st.success(result)
        
if __name__=='__main__':
    main()
    
