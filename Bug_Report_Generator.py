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
    all_bug.append([Bug_Id,Bug_Summary,Bug_Description, Severity,Priority, Environment, Bug_Label, steps])
    print("-"*40)



# now, after collection simple data we can display the output
print("="*40)
print("        Bug Report")
print("="*40)
for bug in all_bug:
    print("Bug ID: - ",bug[0])
    print("Bug summary: - ",bug[1])
    print("Bug Description: - ",bug[2])
    print("Severity: - ",bug[3])
    print("Priority: - ",bug[4])
    print("Environment: - ",bug[5]) 
    print("Bug Type: - ", bug[6])
    # print("Steps to reproduce: - ",no_of_step)
    print("Steps to reproduce: - \n")
    for step_num in bug[7]:
        print(step_num)
    # print(all_bug[bug_num]) #this display the list as it is which is not loooking good. 
    print("="*40)

# save the data in the text file 
file = open("Bug_report.txt","w")
file.write("="*40+"\n")
file.write("        Bug Report"+"\n")
file.write("="*40+"\n")
# now I want to write the same muultiple times
for bug in all_bug:
    file.write("Bug ID: - "+bug[0]+"\n")
    file.write("Bug summary: - "+bug[1]+"\n")
    file.write("Bug Description: - "+bug[2]+"\n")
    file.write("Severity: - "+bug[3]+"\n")
    file.write("Priority: - "+bug[4]+"\n")
    file.write("Environment: - "+ bug[5]+"\n")
    file.write("Bug Type: - "+ bug[6]+"\n")
    file.write("Steps to reproduce: - ")
    for step_num in bug[7]:
        file.write(step_num+"\n")
    file.write("="*40+"\n")
    
file.close()

# save the data in the excel file 

wb = openpyxl.Workbook()
ws = wb.active

ws.append(["Bug Report for project - Demo"])

ws.append(["Bug_Id","Bug_Summary","Bug_Description","Severity","Priority", "Environment","Bug_Label", "Step_to_reproduce"])
# to write in excel bug_count times
# for bug_num in range(bug_count):
#     ws.append([Bug_Id,Bug_Summary,Bug_Description, Severity,Priority, Environment, Bug_Label, steps])

for bug in all_bug:
    ws.append([
        bug[0],bug[1],bug[2],bug[3],bug[4],bug[5],bug[6],",".join(bug[7])
        ])
wb.save("Bug_report.xlsx")