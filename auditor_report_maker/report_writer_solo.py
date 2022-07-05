import PySimpleGUI as sg
from pathlib import Path
from docxtpl import DocxTemplate

# find the file sample.doc 
document_path = Path(__file__).parent/"ruben_solo.docx"
doc = DocxTemplate(document_path)


def edit():
    # create the layout for the window
    layout = [
        [sg.Text("Proprietor: "), sg.Input(key="PROPRIETOR", do_not_clear=False),],
        [sg.Text("Business Name: "), sg.Input(key="BUSINESS_NAME", do_not_clear=False)],
        [sg.Text("Address: "), sg.Input(key="ADDRESS", do_not_clear=False)],
        [sg.Text("Date: "), sg.Input(key="DATE", do_not_clear=False)],
        [sg.Button("Create Word File"), sg.Exit()],
    ]


    window = sg.Window("Single Proprietor: Auditor Ruben", layout)
    while True:
        event, values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event =="Create Word File":
            doc.render(values)
            output_path = Path(__file__).parent/f"{values['PROPRIETOR']}.docx"
            doc.save(output_path)
            sg.popup("File saved ", f"File have been saved here: {output_path}")
    window.close()
    


#fills up a solo proprietor auditor's report with necessary changes