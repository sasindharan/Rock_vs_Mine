import numpy as np
import pickle
import streamlit as st

# Load the pre-trained model
loaded_model = pickle.load(open('C:/Users/sasin/Downloads/machine learning projects/trained_model.sav', 'rb'))

def rock_vs_mine(input_data):
    # Convert input data to numpy array
    input_data_as_numpy = np.asarray(input_data)
    # Reshape input data
    input_reshape = input_data_as_numpy.reshape(1, -1)
    # Make prediction
    prediction = loaded_model.predict(input_reshape)
    return prediction[0]

def main():
    st.title("Rock vs Mine Prediction")

    # Create input fields for each feature
    input_features = []
    for feature_label in range(65, 91):  # ASCII code for 'A' to 'Z'
        feature_value = st.text_input(f"Feature {chr(feature_label)}")
        input_features.append(feature_value)

    # Predict when button is clicked
    if st.button("Predict"):
        prediction = rock_vs_mine(input_features)
        if prediction == 'R':
            st.success("The object is a rock.")
        else:
            st.success("The object is a mine.")

if __name__ == "__main__":
    main()
