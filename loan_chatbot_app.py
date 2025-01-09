import streamlit as st
from transformers import pipeline

# Load pre-trained model and tokenizer
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Create function to generate responses
def generate_response(user_input):
    response = chatbot(user_input)
    return response[0]['generated_text']

# Chatbot interface
def chatbot_interface():
    st.title("Loan Lending Chatbot")
    
    # Start a conversation
    if 'conversation' not in st.session_state:
        st.session_state.conversation = ""
    
    user_input = st.text_input("You:", "")
    
    if user_input:
        # Append user input to conversation history
        st.session_state.conversation += f"You: {user_input}\n"
        
        # Generate bot response
        bot_response = generate_response(user_input)
        
        # Append bot response to conversation history
        st.session_state.conversation += f"Bot: {bot_response}\n"
    
    # Display conversation
    st.text_area("Conversation", value=st.session_state.conversation, height=300, max_chars=None)

# Main function to run the app
def main():
    chatbot_interface()

# Run the app
if __name__ == "__main__":
    main()
