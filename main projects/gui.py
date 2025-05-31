import functions
import FreeSimpleGUI
# if i want to dont write FreeSimpleGui all over again i can just write import FreeSimpleGui as sg and replace the FreeSimpleGui below


label = FreeSimpleGUI.Text("Type in a To-Do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter a todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()