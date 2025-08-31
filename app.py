from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form (convert to float to handle decimals like CGPA = 6.61)
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]

    # Make prediction
    prediction = model.predict(final_features)
    output = 'Placed' if prediction[0] == 1 else 'Not Placed'

    return render_template('home.html', prediction_text=f'Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)
