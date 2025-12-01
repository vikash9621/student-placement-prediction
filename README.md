# Student Placement Prediction

A machine learning web application that predicts student placement outcomes based on academic and personal attributes.

## Features

- **ML-Powered Predictions**: Uses a trained model to predict placement probability
- **Web Interface**: Clean, responsive form for data input
- **Real-time Results**: Instant prediction display
- **Multiple Factors**: Considers 8 key student attributes

## Input Parameters

The model evaluates students based on:

- **IQ**: Intelligence quotient score
- **Previous Semester Result**: Academic performance in last semester
- **CGPA**: Cumulative Grade Point Average
- **Academic Performance**: Overall academic rating
- **Internship Experience**: Binary (0/1) for internship completion
- **Extra Curricular Score**: Rating for non-academic activities
- **Communication Skills**: Communication ability score
- **Projects Completed**: Number of projects finished

## Quick Start

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd student-placement-prediction-main
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Fill in all required fields in the web form
2. Click "Predict" to get placement prediction
3. View result: "Placed" or "Not Placed"


## Project Structure

```
├── app.py              # Flask web application
├── model.pkl           # Trained ML model
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment config
└── templates/
    └── home.html      # Web interface
```

## Technology Stack

- **Backend**: Flask (Python)
- **ML**: scikit-learn, NumPy
- **Frontend**: HTML, CSS
- **Deployment**: Render

## Model Information

The application uses a pre-trained machine learning model (`model.pkl`) that has been trained on student placement data to predict outcomes based on the input features.
