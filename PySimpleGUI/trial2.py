import PySimpleGUI as sg


def read():
    layout =[
        [sg.Text("You are now in another window!")],
        [sg.Button('Next'), sg.Button('Exit')]
    ]

    window = sg.Window("Window 2", layout)
    while True:
        event, values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Next':
            print('We go back to another window')
            window.close()
            #trial1.read1()

#look at trail1 for the explenation program
