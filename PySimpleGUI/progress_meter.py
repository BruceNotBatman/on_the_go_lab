import PySimpleGUI as sg

for i in range(1, 1000):
    sg.one_line_progress_meter("My Meter", i+1, 1000, 'key', 'Optional message')