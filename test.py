from docxtpl import DocxTemplate
 
 
def create_training_sheet(class_name, subject_name, tpl_name="tpl.docx", *marks):
    doc = DocxTemplate(tpl_name)
    marks = sorted(marks, key=lambda n: n[0])
    context = {'class_name': class_name,
               'subject_name': subject_name,
               'marks': [{'num': i + 1, 'fio': marks[i][0], 'mark': marks[i][1]} for i in range(len(marks))]}
    doc.render(context)
    doc.save("res.docx")


create_training_sheet("3И", "Математика", "tpl.docx",  
                      ("Петров Петр", "5"),  
                      ("Иванов Иван", "5"),  
                      ("Сергеев Сергей", "3"),  
                      ("Никитин Никита", "4"))