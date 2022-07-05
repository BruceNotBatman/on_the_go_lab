import PySimpleGUI as sg
#set color for the window
sg.theme('Dark Grey')
#create the layout, each bracket is a line for a GUI
layout=[
    [sg.Text('Filename:')],
    [sg.Input(), sg.FileBrowse()],
    [sg.OK(), sg.Cancel()]
]
#create the window with layout variables 
window = sg.Window('Retrieve a File', layout)

event, values = window.read()
window.close()