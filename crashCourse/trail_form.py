from pathlib import Path
from docxtpl import DocxTemplate

document_path = Path(__file__).parent/"sample2.docx" 
doc = DocxTemplate(document_path)

context = {"THIS": "NEW WORD"}
doc.render(context)
doc.save(Path(__file__).parent/"output.docx")
