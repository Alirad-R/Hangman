import PySimpleGUI as sg

sg.theme('DarkBlue14')

layout = [[sg.Text("This is the first row")],
          [sg.Text("Enter your name: "), sg.InputText()],
          [sg.Button("OK"), sg.Button("Cancel")],
          [sg.Button("Submit", visible=False, bind_return_key=True)]]

window = sg.Window("Hangman", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break;
    elif event == "Submit" or event == "OK":
        print(values[0])
    
window.close()