import PySimpleGUI as sg
from pathlib import Path
from docxtpl import DocxTemplate

# find the file sample.doc 
document_path = Path(__file__).parent/"ruben_corp.docx"
doc = DocxTemplate(document_path)


def edit():
    # create the layout for the window
    layout = [
        [sg.Text("Company Name: "), sg.Input(key="COMPANY_NAME", do_not_clear=False),],
        [sg.Text("Company Address: "), sg.Input(key="COMPANY_ADDRESS", do_not_clear=False)],
        [sg.Text("Date: "), sg.Input(key="Date", do_not_clear=False)],
        [sg.Text("Number of Stockholders: "), sg.Input(key="Number_Stockholders", do_not_clear=False)],
        [sg.Text("President/Chairman of the Board: "), sg.Input(key="PRESIDENT", do_not_clear=False)],
        [sg.Text("Treasurer/Chief Financial Officer: "), sg.Input(key="TREASURER", do_not_clear=False)],
        [sg.Button("Create Word File"), sg.Exit()]
    ]


    window = sg.Window("Corporation: Auditor Ruben", layout)
    while True:
        event, values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event =="Create Word File":
            doc.render(values)
            output_path = Path(__file__).parent/f"{values['COMPANY_NAME']}.docx"
            doc.save(output_path)
            sg.popup("File saved ", f"File have been saved here: {output_path}")
    window.close()
            
    


#fills up a corporation's auditor's report with necessary changes