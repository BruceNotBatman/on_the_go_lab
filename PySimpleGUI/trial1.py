import PySimpleGUI as sg
import trial2

def read():
    layout =[
        [sg.Text("Experimenting with functions!")],
        [sg.Button('Next'), sg.Button('Exit')]
    ]

    window = sg.Window("Window 1", layout)
    while True:
        event, values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Next':
            print('We move to another window')
            #window.close()
            trial2.read()
    window.close()
read()

#this experimental program is my trial form that allows me to go to another form then go back here