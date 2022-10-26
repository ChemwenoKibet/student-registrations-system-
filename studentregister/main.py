from fastapi import fastapi


app = fastapi()


@app.get('/Students')
def create_student_details(studentname:str, admissionnum:int,finalyear:int ):
    return{studentname, admissionnum, finalyear}

@app.update('/Students/update')
def update_student_details(studentname:str, admissionnum:int,finalyear:int):
    return {studentname, admissionnum, finalyear}
