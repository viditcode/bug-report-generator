from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
class AIService:
    def __init__(self):
        self.api_key = os.getenv("AI_API_KEY")
        if not self.api_key:
            raise ValueError("AI API key is not set. Please set the AI_API_KEY environment variable.")  
        
        self.client = genai.Client(api_key= self.api_key)
        if not self.client:
            raise ValueError("Failed to initialize the AI model. Please check your API key and configuration.")\
        
        
    
    def analysis_bug(self, bug):
        prompt = f"""
        You are a senior QA engineer with 10 years of experience
        in software testing and bug analysis.
        Your job is to analyse bug reports and provide
        clear, technical, actionable insights.
        Analyse this bug report and provide:
        1. Bug Type (Bug, improvement) = type of bug/improvement in (UI, Backend, Performance, Security, etc.)
        2. one line summary of the bug
        3. possible root cause of the bug
        4. suggest fix for the bug
        5. Severity assissment of bug 

        6. some edge cases to test after fixing the bug

        bug deatils :
        Bug summary: - {bug.summary}
        Bug Description: - {bug.description}
        Severity: - {bug.severity}  
        Priority: - {bug.priority}
        Environment: - {bug.environment}
        Steps to reproduce: - {",".join(bug.steps)}

        keep the response concise and to the point.
        """
        response = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt)
        return response.text