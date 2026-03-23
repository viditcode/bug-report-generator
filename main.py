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

from model.bug import Bug
from services.file_services import FileServices
from view.report_view import ReportView
from utils.validator import get_from_list, get_non_empty, get_valid_number
from utils.validator import valid_priority, valid_severity


service = FileServices()

# take the value from user
bug_count = get_valid_number("Enter the count of Bugs: - ")

# create a storage 
all_bug = []

starting_number = service.get_bug_number()
# now ask user to enter the bug details bug count times.
for bug_num in range(bug_count):
    steps =[]
    print("-"*40)
    print("Please Enter Bug number: -"+str(bug_num+1))
    
    Bug_Summary = get_non_empty("Enter the Bug_Summary: ")
    Bug_Description = get_non_empty("Enter the Bug_Description:  ")
    Severity = get_from_list("Enter the Severity:  ", valid_severity)
    Priority = get_from_list("Enter the Priority:  ", valid_priority)
    Environment = get_non_empty("Enter the Environment:  ")
    Bug_Label = get_non_empty("Enter the Bug_Label:  ")
    no_of_step = get_valid_number("Enter the number of Step:  ")
    for step_num in range(no_of_step):
        step_to_reproduce = get_non_empty("Enter the step number: "+str(step_num+1)+" ")
        steps.append(step_to_reproduce)
    bug = Bug(starting_number+bug_num,Bug_Summary,Bug_Description, Severity,Priority, Environment, Bug_Label, steps)
    all_bug.append(bug)
    print("-"*40)



# now, after collection simple data we can display the output
print("="*40)
print("        Bug Report")
print("="*40)


view = ReportView()

# save the data in the text file 

for bug in all_bug:
    view.print_report(bug)
    service.save_to_txt(bug)
    service.save_to_excel(bug)

service.close()
print("File saved successfully")