import streamlit as st

# Function to display the login page
def login_page():
    st.title("Welcome to Credify")
    st.subheader("Please log in to continue")

    # Create login form
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if username == "user" and password == "password":
            # If the login is successful, set a session state to indicate the user is logged in
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.experimental_rerun()  # Reload the app to show the home page
        else:
            st.error("Incorrect username or password. Please try again.")

# Function to display the home page
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

# Main function to handle the app flow
def main():
    # Check if the user is logged in
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        login_page()
    else:
        home_page()

# Run the app
if __name__ == "__main__":
    main()

