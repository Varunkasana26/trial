import streamlit as st
import streamlit_authenticator as stauth
from datetime import datetime

# Styling for white and light blue theme
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    .stButton button {
        background-color: #ADD8E6;
    }
    .stTitle {
        color: #4682B4;
    }
    .stTextInput input {
        border-radius: 5px;
        border: 1px solid #ADD8E6;
        padding: 10px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to handle login and Google authentication
def login_page():
    st.title("Welcome to Credify")
    st.subheader("Please log in to continue")

    # Creating a simple login form (for demonstration purposes, not Google OAuth yet)
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if username == "user" and password == "password":
            # Set session state for login status
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.experimental_rerun()  # Reload to home page
        else:
            st.error("Incorrect username or password. Please try again.")

# Function for the home page
def home_page():
    st.title(f"Welcome back, {st.session_state.username}")
    
    # Simulate loan details
    loan_taken = st.selectbox("Have you taken a loan?", ("Yes", "No"))
    
    if loan_taken == "Yes":
        loan_amount = st.number_input("Enter your loan amount ($)", min_value=0, value=1000)
        loan_duration = st.selectbox("Select loan duration (years)", [1, 2, 3, 4, 5])
        interest_rate = 5.0  # Fixed interest rate for demonstration
        total_amount = loan_amount * (1 + (interest_rate / 100) * loan_duration)
        
        st.subheader(f"Loan Details")
        st.write(f"Loan Amount: ${loan_amount}")
        st.write(f"Duration: {loan_duration} years")
        st.write(f"Interest Rate: {interest_rate}%")
        st.write(f"Total Amount to be Repaid: ${total_amount:.2f}")
    else:
        st.subheader("Interest Rates for Loan")
        st.write("We offer loans with an interest rate of **5% per year** for 1-5 years.")
        st.write("Please contact us for further details.")
    
    if st.button("Sign Up"):
        st.write("Signing you up...")
        # Here you can add the actual signup process for the user
        st.session_state.signed_up = True
        st.success("You have successfully signed up!")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# Main function to handle page flow
def main():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        login_page()
    else:
        home_page()

# Run the app
if __name__ == "__main__":
    main()
