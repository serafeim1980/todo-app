import FreeSimpleGUI as sg
import streamlit


sg.theme("Black")
layout = [
    [sg.Text("Ask me something:")],
    [sg.InputText(key="USER_INPUT")],
    [sg.Button("Send")],
    [sg.Text("", size=(40, 10), key="RESPONSE")]
]

window = sg.Window("Sera chatbot", layout)

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

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Send":
        user_input = values["USER_INPUT"]
        response, should_exit = get_response(user_input)
        window["RESPONSE"].update(f"Sera: {response}")

        window["USER_INPUT"].update("")

        if should_exit:
            sg.popup("Exiting chatbot. Goodbye!")
            break


window.close()





