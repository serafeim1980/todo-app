import functions
import FreeSimpleGUI
# if i want to dont write FreeSimpleGui all over again i can just write import FreeSimpleGui as sg and replace the FreeSimpleGui below
label = FreeSimpleGUI.Text("Type in a To-Do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter a todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window('My To-Do App',
                              layout=[[label], [input_box, add_button]],
                              font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case FreeSimpleGUI.WIN_CLOSED:
            break


window.close()