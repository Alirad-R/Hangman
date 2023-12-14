import PySimpleGUI as sg

sg.theme('AmberDark')

layout = [[sg.Text("This is the first row")],
          [sg.Text("Enter your name: "), sg.InputText()],
          [sg.Button("OK"), sg.Button("Cancel")]]

window = sg.Window("Hangman", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break;
    print(values[0])
    
window.close()