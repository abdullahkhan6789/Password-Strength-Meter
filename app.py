import re
import streamlit as st

# Page styling with modern and fancy designs
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# Custom CSS for design enhancements
st.markdown("""
            <style>
            body {
                background: linear-gradient(45deg, #6a11cb, #2575fc);
                font-family: 'Arial', sans-serif;
                color: #fff;
                margin: 0;
                padding: 0;
            }

            .main {
                text-align: center;
                padding: 50px;
            }

            .stTextInput {
                width: 70% !important;
                margin: 20px auto;
                padding: 15px;
                font-size: 18px;
                border-radius: 12px;
                border: 2px solid #fff;
                background-color: rgba(255, 255, 255, 0.8);
                color: #333;
            }

            .stTextInput:focus {
                border-color: #6a11cb;
                background-color: rgba(255, 255, 255, 1);
            }

            .stButton button {
                width: 60%;
                background-color: #6a11cb;
                color: white;
                font-size: 20px;
                padding: 15px;
                border-radius: 12px;
                border: none;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
                cursor: pointer;
                transition: all 0.3s ease-in-out;
            }

            .stButton button:hover {
                background-color: #2575fc;
                transform: scale(1.05);
            }

            .stSuccess, .stError, .stInfo {
                font-size: 20px;
                padding: 20px;
                border-radius: 12px;
                margin-top: 20px;
                width: 80%;
                margin-left: auto;
                margin-right: auto;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
                text-align: center;
            }

            .stSuccess {
                background-color: #28a745;
                color: white;
            }

            .stError {
                background-color: #dc3545;
                color: white;
            }

            .stInfo {
                background-color: #ffc107;
                color: white;
            }

            .stExpanderHeader {
                background-color: #f1f1f1;
                color: #333;
                font-size: 20px;
                font-weight: bold;
                padding: 10px;
            }

            .stExpanderContent {
                background-color: #fff;
                padding: 10px;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
                border-radius: 12px;
            }

            /* Custom Icon Styling */
            .icon {
                font-size: 36px;
                margin-right: 8px;
            }

            .stExpander {
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            }
            </style>
            """, unsafe_allow_html=True)

# Page title and description with icon
st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its security level and get sugession to improve it 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check (at least 12 characters for a stronger password)
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 12 characters long** for better security.")

    # Uppercase and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase [A-Z] and lowercase [a-z] letters**.")

    # Digit Check (at least 2 digits)
    if len(re.findall(r"\d", password)) >= 2:
        score += 1
    else:
        feedback.append("❌ Password should include **at least two digits (0-9)**.")

    # Special Character Check (must have at least one of !@#$%^&*)
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**.")

    # Password should not contain common patterns or repeated characters
    if re.search(r"(.)\1\1", password):  # Checks for 3 or more repeated characters
        feedback.append("❌ Password should not contain repeated characters (e.g., 'aaa').")

    # Display password strength results
    if score == 5:
        st.success("✔️ **Strong Password**. Your password is secure. 💪")
    elif score == 4:
        st.info("⚠️ **Moderate Password**. Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password**. Follow the suggestions below to strength it.")

    # Provide feedback
    if feedback:
        with st.expander("**Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Input field for password (right-aligned, more modern look)
password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔐")

# Button to check password strength 
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first! 🚫")  # Show warning if password is empty
