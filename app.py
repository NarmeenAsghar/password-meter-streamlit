import streamlit as st
import re

# Function to evaluate password strength
def evaluate_password_strength(password):
    # Check password length
    length_score = len(password) >= 12
    
    # Check for the presence of different character types
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'[0-9]', password) is not None
    has_special = re.search(r'[^A-Za-z0-9]', password) is not None
    
    # Evaluate strength based on conditions
    if length_score and has_upper and has_lower and has_digit and has_special:
        strength = "Very Strong"
        feedback = []
    elif length_score and has_upper and has_lower and has_digit:
        strength = "Strong"
        feedback = ["Add a special character for extra security."]
    elif length_score and (has_upper or has_lower) and has_digit:
        strength = "Fair"
        feedback = ["Consider using more diverse characters like special symbols."]
    elif length_score or (has_upper and has_lower):
        strength = "Weak"
        feedback = ["Password is too simple. Try adding more variety."]
    else:
        strength = "Very Weak"
        feedback = ["Password is too short or too simple. Please add more characters and variety."]
    
    return strength, feedback

# Streamlit App Interface
st.title("Password Strength Meter 🔐")
st.markdown("## Check your password strength and improve security! 🛡️")

# Create an input field for the password
password = st.text_input("Enter your password:", type='password')

# Container for the requirements and feedback that will appear below
with st.container():
    # If a password is entered, evaluate and show strength
    if password:
        # Call the function to evaluate the password strength
        strength, feedback = evaluate_password_strength(password)
        
        # Display password strength
        st.write(f"### Password strength: **{strength}**")
        
        # If password strength is not strong, show feedback suggestions
        if strength != "Very Strong":
            st.write("### Suggestions to improve your password: 💡")
            for suggestion in feedback:
                st.write(f"- {suggestion}")
        else:
            st.write("Your password is very strong! 🎉 No further changes are needed.")
        
        # Show visual feedback using colored text (optional)
        if strength == "Very Weak":
            st.markdown('<span style="color:red">🚨 Very Weak Password! Please improve it immediately! 🚨</span>', unsafe_allow_html=True)
        elif strength == "Weak":
            st.markdown('<span style="color:orange">⚠️ Weak Password. Consider improving it. ⚠️</span>', unsafe_allow_html=True)
        elif strength == "Fair":
            st.markdown('<span style="color:yellow">⚠️ Fair Strength. Some improvement is needed. ⚠️</span>', unsafe_allow_html=True)
        elif strength == "Strong":
            st.markdown('<span style="color:green">✅ Strong Password! Well done! ✅</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="color:blue">🎉 Very Strong Password! Keep it up! 🎉</span>', unsafe_allow_html=True)
    
    # Optionally, add some extra help/information at the bottom
    st.markdown("---")
    st.markdown("### Tips to make your password stronger 💪")
    st.markdown(""" 
    - **Length**: Make your password at least 12 characters long. 📝
    - **Variety**: Use a mix of uppercase, lowercase, numbers, and special characters. 🔠
    - **Avoid**: Using common words or phrases that are easy to guess. 🚫
    - **Use a password manager**: To store and generate strong passwords securely. 🔒
    """)
