from datetime import datetime
class Bug:
    def __init__(self, bug_id, summary, description, severity, priority, environment, label, steps):
        self.bug_id = "Bug - "+str(bug_id)
        self.summary = summary
        self.description = description
        self.severity = severity
        self.priority = priority
        self.environment = environment
        self.label = label
        self.steps = steps    
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  