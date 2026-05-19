def report_dict(name, backend, frontend, design, average, grade):
   
    return {  "name": name,  "Backend": backend,  "Frontend": frontend,  "Design": design, "average": int(average),  "grade": grade }


def generate_report(name, backend, frontend, design):
  
    average = (backend + frontend + design) / 3

    if average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'E'
    
   
    return report_dict(name, backend, frontend, design, average, grade)

name = input("Enter student name: ")
backend = int(input("Enter Backend marks: "))
frontend = int(input("Enter Frontend marks: "))
design = int(input("Enter Design marks: "))


report = generate_report(name, backend, frontend, design)



print(report)
        

