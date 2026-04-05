student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}


for key in student_scores:
    score=student_scores[key]
    if 91< score<100:
        Grade="Outstanding"
    elif 81<score<90:
        Grade="Exceeds Expectations"
    elif 71<score<80:
        Grade="Acceptable"
    else:
        Grade = "Fail"
    
    student_grades[key]=Grade
    
print(student_grades)