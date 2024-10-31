"""Deji Shodunke
   Module_2_Lab-Case_Study_Report_Card
   This app will ask the user for the students last name, first name and GPA.  
   The app will then calculate and report if the students grades qualify for the Deans'list,
   Honor Roll, or neither."""
   
def reportCard():
    while True:
        
        lastName = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if lastName.upper() == 'ZZZ':
            print("Exit")
            break
        
        firstName = input("Enter the student's first name: ")
        

        gpa = float(input("Enter the student's GPA: "))

        if gpa >= 3.5:
            print(f"{firstName} {lastName} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{firstName} {lastName} has made the Honor Roll.")
        else:
            print(f"{firstName} {lastName} did not qualify for the Dean's List or Honor Roll.")

reportCard()