
# Password Strength Meter 🔐

**Password Strength Meter** is a simple web application built using **Streamlit** and **zxcvbn** for evaluating the strength of a password. The app checks the password’s strength, provides feedback, and offers suggestions for making the password more secure. It also displays visual feedback with emojis and tips for creating stronger passwords.

## Features

- **Password Strength Evaluation**: 🔍 The app evaluates the strength of a given password using the **zxcvbn** library, which provides a score from 0 (very weak) to 4 (very strong).
- **Suggestions for Improvement**: 💡 If the password is weak, the app will show suggestions on how to improve its strength.
- **Visual Feedback**: 🎨 The password strength is displayed using color-coded labels and emojis for better user understanding.
- **Password Tips**: 📝 The app provides general tips on creating strong passwords.

## How It Works

1. **Input Password**: ✍️ The user enters a password into the password field.
2. **Password Evaluation**: 📊 The app evaluates the password strength using the **zxcvbn** library.
3. **Feedback and Suggestions**: 📈 Based on the evaluation, the app shows the password's strength level, such as "Very Weak," "Weak," "Fair," "Strong," or "Very Strong."
4. **Improvement Tips**: 💪 If the password is weak or fair, the app suggests ways to improve it, such as increasing length, adding variety (upper/lowercase, numbers, symbols), and avoiding common phrases.
5. **Visual Indicators**: 🟢🟡🟠🔴 Emojis and color-coded text are used to make the feedback more interactive and user-friendly.

## Installation

To run this application locally, you need to install the required dependencies. Follow the steps below:

### Prerequisites

Make sure you have **Python 3.7+** installed on your machine. 🖥️

### Steps to Run

1. Clone or download the repository to your local machine. 📥

   ```bash
   git clone https://github.com/NarmeenAsghar/password-meter-streamlit.git
   ```

2. Navigate to the project directory. 📂

   ```bash
   cd password-strength-meter
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies using **pip**:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the app:

   ```bash
   streamlit run app.py
   ```

7. Open the application in your browser at `http://localhost:8501` 🌐.

## Usage

- **Enter a Password**: ✍️ Type or paste a password into the input box.
- **Evaluate Strength**: 🔒 The app will automatically evaluate the strength of your password.
- **Review Feedback**: 📝 The app will show you the strength level, along with helpful suggestions and tips for improvement.
- **Follow Tips**: 💡 Apply the suggestions to improve your password's strength.
