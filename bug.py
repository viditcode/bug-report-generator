class Bug:
    def __init__(self, bug_id, summary, description, severity, priority, environment, label, steps):
        self.bug_id = bug_id
        self.summary = summary
        self.description = description
        self.severity = severity
        self.priority = priority
        self.environment = environment
        self.label = label
        self.steps = steps        

    def print_report(self):
        print("Bug ID: - ",self.bug_id)
        print("Bug summary: - ",self.summary)
        print("Bug Description: - ",self.description)
        print("Severity: - ",self.severity)
        print("Priority: - ",self.priority)
        print("Environment: - ",self.environment) 
        print("Bug Type: - ", self.label)
        # print("Steps to reproduce: - ",no_of_step)
        print("Steps to reproduce: - \n")
        for step_num in self.steps:
            print(step_num)
        # print(all_bug[bug_num]) #this display the list as it is which is not loooking good. 
        print("="*40)
    
    def save_to_txt(self,file):
        file.write("Bug ID: - "+self.bug_id+"\n")
        file.write("Bug summary: - "+self.summary+"\n")
        file.write("Bug Description: - "+self.description+"\n")
        file.write("Severity: - "+self.severity+"\n")
        file.write("Priority: - "+self.priority+"\n")
        file.write("Environment: - "+self.environment+"\n")
        file.write("Bug Type: - "+ self.label+"\n")
        file.write("Steps to reproduce: - \n")
        for step_num in self.steps:
            file.write(step_num+"\n")
        file.write("="*40+"\n")
    
    def save_to_excel(self,ws):
        ws.append([
            self.bug_id,self.summary,self.description,self.severity,self.priority,self.environment,self.label,",".join(self.steps)
            ])