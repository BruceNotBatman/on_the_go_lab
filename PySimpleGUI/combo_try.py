import PySimpleGUI as sg

choices =[1,2,3]

layout =[
    [sg.Text('Pick a Number: '), sg.Combo(choices, key='input')],
    [sg.Button('Reveal Number'), sg.Button('Exit')]
]

window = sg.Window('Trying Combo Boxes', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event =='Reveal Number':
        print(values)

window.close()