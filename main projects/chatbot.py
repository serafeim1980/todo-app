import streamlit as st

def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "bye":
        return "Goodbye! Have a nice day gtxs!", True

    elif user_input in ["hello", "hi"]:
        return "Kalos ta arxidia mas!", False

    elif user_input == "how are you":
        return "I'm just code, but thanks for asking!", False

    elif user_input == "what's your name":
        return "I'm a simple Python chatbot. Ti de katalavaineis?", False

    else:
        return "Niko?", False

st.title("Sera Chatbot")

if 'exit' not in st.session_state:
    st.session_state.exit = False

user_input = st.text_input("Ask me something:")

if user_input and not st.session_state.exit:
    response, should_exit = get_response(user_input)
    st.write("Sera: ", response)

    if should_exit:
        st.session_state.exit = True
        st.write("Exiting chatbot. Goodbye!")


