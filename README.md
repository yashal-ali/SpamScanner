

# SMS Spam Classifier using Streamlit

This project implements a simple SMS (Short Message Service) spam classifier using Streamlit, a popular Python library for creating web applications with minimal effort. The classifier uses Natural Language Processing (NLP) techniques to preprocess text data and a machine learning model trained on SMS messages to predict whether a given message is spam or not.

![image](https://github.com/yashal-ali/SpamScanner/assets/96627139/d558ebe9-4b70-4c3b-86b4-595e4055dfa2)


## Project Structure

- `app.py`: The main Streamlit application file containing the classifier logic.
- `vectorizer.pkl`: Pickled file containing the fitted TF-IDF vectorizer used for text preprocessing.
- `model.pkl`: Pickled file containing the trained machine learning model (e.g., Naive Bayes) for classification.
- `requirements.txt`: List of Python dependencies required to run the application.
- `README.md`: This file, providing project overview and instructions.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system.
- Git installed on your system.
- Heroku CLI installed on your system (for deployment).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sms-spam-classifier.git
   cd sms-spam-classifier
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App Locally

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501` to view and interact with the app.

### Usage

- Enter a message in the text area provided and click on the "Predict" button.
- The app will classify the message as "Spam" or "Not Spam" based on the trained model.



## Credits

- This project uses the `streamlit` library for building the web application.
- The SMS spam classifier model is trained using `scikit-learn`.
- Natural Language Processing (NLP) techniques are implemented using `nltk`.



