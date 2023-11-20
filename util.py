import json
import pickle
import numpy as np
import pickle

__result = None
model = None

# Load the trained model from the pickle file
with open('nalasha.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to get user input and make predictions
def predict_user_input(input1, input2, input3):
    try:
        input_data = np.array([input1, input2, input3]).reshape(1, -1)

        # Make prediction using the loaded model
        prediction = model.predict(input_data)

        prediction_int = int(prediction[0])

        # Display the prediction
        print(f"The predicted target variable is: {prediction_int}")

        return prediction_int
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to get user input and make predictions
# predict_user_input(2, 1, 1)

