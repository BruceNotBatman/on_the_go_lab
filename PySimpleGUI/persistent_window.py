import PySimpleGUI as sg
#set the theme of the window
sg.theme('Dark Blue')

#set layout for the window
layout = [
    [sg.Text('Your typed chars appeare here: '), sg.Text(size=(12,1), key="-OUTPUT-")],
    [sg.Input(key='-IN-')],
    [sg.Button('Show'), sg.Button('Exit')]
]

window = sg.Window('Window Title', layout)

while True:
    event, values =window.read()
    print(event, values)
    if event==sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        window['-OUTPUT-'].update(values['-IN-'])

window.close()