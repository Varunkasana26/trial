import streamlit as st

# A mock database to store user data (loan taken and amount)
users_db = {}

# Function to show home page or user loan details
def display_homepage(user_name):
    if user_name in users_db:
        user_data = users_db[user_name]
        if user_data["loan_taken"]:
            st.title(f"Welcome, {user_data['name']}!")
            st.write(f"Loan Amount Taken: ${user_data['loan_amount']}")
            st.write(f"Loan Interest: ${user_data['interest_amount']}")
            st.write(f"Repayment Status: {'Paid' if user_data['loan_paid'] else 'Pending'}")
        else:
            st.title(f"Welcome, {user_data['name']}!")
            st.write(f"You have not taken a loan yet.")
            show_loan_application(user_name)
    else:
        st.title("Welcome!")
        st.write("Please enter your name to proceed.")
        st.sidebar.write("Enter your name to view loan status.")

# Function to handle loan application
def show_loan_application(user_name):
    st.subheader("Apply for a Loan")
    loan_amount = st.number_input("Enter loan amount:", min_value=100, step=100)
    
    if loan_amount > 0:
        interest_rate = 5.0  # Fixed interest rate (can be dynamic)
        interest_amount = (loan_amount * interest_rate) / 100
        total_repayment = loan_amount + interest_amount
        
        st.write(f"Interest Rate: {interest_rate}%")
        st.write(f"Interest Amount: ${interest_amount}")
        st.write(f"Total Repayment Amount: ${total_repayment}")
        
        # Submit loan application
        apply_button = st.button("Apply for Loan")
        if apply_button:
            users_db[user_name] = {
                "name": user_name,
                "loan_taken": True,
                "loan_amount": loan_amount,
                "interest_amount": interest_amount,
                "loan_paid": False
            }
            st.success(f"Loan application successful! You have applied for ${loan_amount}.")
    else:
        st.write("Please enter a valid loan amount.")

# Function to handle loan repayment
def show_loan_repayment(user_name):
    if user_name in users_db:
        user_data = users_db[user_name]
        if user_data["loan_taken"] and not user_data["loan_paid"]:
            st.subheader("Repay your Loan")
            repayment_amount = st.number_input("Enter repayment amount:", min_value=100)
            if repayment_amount >= user_data["loan_amount"] + user_data["interest_amount"]:
                if st.button("Repay Loan"):
                    users_db[user_name]["loan_paid"] = True
                    st.success("Loan repaid successfully!")
            else:
                st.warning(f"Amount should be greater than or equal to ${user_data['loan_amount'] + user_data['interest_amount']}")
        elif user_data["loan_paid"]:
            st.write("Your loan is already paid!")
        else:
            st.write("You don't have an active loan.")

# Sidebar for user login
st.sidebar.title("Loan Lending App")
user_name = st.sidebar.text_input("Enter your name", "")

# Display homepage content based on user input
if user_name:
    display_homepage(user_name)
    show_loan_repayment(user_name)
else:
    st.sidebar.write("Please enter your name to view loan details and apply for loans.")
