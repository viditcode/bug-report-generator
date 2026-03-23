class ReportView:
    def print_report(self,bug):
        print("Bug ID: - ",bug.bug_id)
        print("Bug summary: - ",bug.summary)
        print("Bug Description: - ",bug.description)
        print("Severity: - ",bug.severity)
        print("Priority: - ",bug.priority)
        print("Environment: - ",bug.environment) 
        print("Bug Type: - ", bug.label)
        # print("Steps to reproduce: - ",no_of_step)
        print("Steps to reproduce: - \n")
        for step_num in bug.steps:
            print(step_num)
        # print(all_bug[bug_num]) #this display the list as it is which is not loooking good.
        print("Date and Time: - "+bug.timestamp+"\n") 
        print("="*40)