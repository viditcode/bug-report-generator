# to create a bug report generator, I need to have to take input from user for every fields.
# there are muliple things which enter in this tools
'''
1 - Bug_Id,
2 - Bug_Summary
3 - Bug_Description
4 - Severity
5 - Priority
6 - Step
7 - Environment
8 - Bug_Label 
9 - POT file
'''

# import libraries
import openpyxl
from bug import Bug

# take the value from user
bug_count = int(input("Enter the count of Bugs: - "))

# create a storage 
all_bug = []


# now ask user to enter the bug details bug count times.
for bug_num in range(bug_count):
    steps =[]
    print("-"*40)
    print("Please Enter Bug number: -"+str(bug_num+1))
    Bug_Id = input("Enter the Bug_Id: ")
    Bug_Summary = input("Enter the Bug_Summary: ")
    Bug_Description = input("Enter the Bug_Description:  ")
    Severity = input("Enter the Severity:  ")
    Priority = input("Enter the Priority:  ")
    Environment = input("Enter the Environment:  ")
    Bug_Label = input("Enter the Bug_Label:  ")
    no_of_step = int(input("Enter the number of Step:  "))
    for step_num in range(no_of_step):
        step_to_reproduce = input("Enter the step number: "+str(step_num+1)+" ")
        steps.append(step_to_reproduce)
    bug = Bug(Bug_Id,Bug_Summary,Bug_Description, Severity,Priority, Environment, Bug_Label, steps)
    all_bug.append(bug)
    print("-"*40)

# now, after collection simple data we can display the output
print("="*40)
print("        Bug Report")
print("="*40)



# save the data in the text file 
file = open("Bug_report.txt","w")
file.write("="*40+"\n")
file.write("        Bug Report"+"\n")
file.write("="*40+"\n")
    

# save the data in the excel file 

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Bug Report for project - Demo"])
ws.append(["Bug_Id","Bug_Summary","Bug_Description","Severity","Priority", "Environment","Bug_Label", "Step_to_reproduce"])

for bug in all_bug:
    bug.print_report()
    bug.save_to_txt(file)
    bug.save_to_excel(ws)
wb.save("Bug_report.xlsx")
file.close()
