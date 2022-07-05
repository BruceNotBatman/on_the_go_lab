import PySimpleGUI as sg
import report_writer_solo
import report_writer_corp

choices =['solo','corp']

layout =[
    [sg.Text('Pick a Form: '), sg.Combo(choices, key='input')],
    [sg.Button('Fill up Form'), sg.Button('Exit')]
]

window = sg.Window('Trying Combo Boxes', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Fill up Form':
        if values == {'input':'solo'}:
            report_writer_solo.edit()
        if values == {'input':'corp'}:
            report_writer_corp.edit()
window.close()

#this is the main file