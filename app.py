import streamlit as st
import os
import pandas as pd
from model.bug import Bug
from services.file_services import FileServices
from view.report_view import ReportView
from utils.validator import valid_priority, valid_severity  


page = st.sidebar.radio("Bug Report Generator", ["Report a Bug", "View Bug Report", "Summary"])
st.sidebar.write("v5
.0.0")

if page == "Report a Bug":
    st.title("Report a Bug")

    summary = st.text_input("Bug Summary")
    description = st.text_area("Bug Description")
    severity = st.selectbox("Severity", valid_severity)
    priority = st.selectbox("Priority", valid_priority)
    environment = st.text_area("Environment")
    label = st.text_input("Bug Label")
    
    st.subheader("Steps to Reproduce")
    no_of_steps = st.number_input("Number of Steps", min_value=1, step=1)

    steps = []
    for step_num in range(no_of_steps):
        step = st.text_input(f"Step {step_num + 1}")
        steps.append(step)

    if st.button("Submit Bug Report"):
        if summary.strip() == "":
            st.error("Please fill in the summary.")
        elif description.strip() == "":
            st.error("Please fill in the description.")
        elif environment.strip() == "":
            st.error("Please fill in the environment.")
        elif label.strip() == "":
            st.error("Please fill in the bug label.")
        else:
            service = FileServices()
            bug_number = service.get_bug_number()
            bug = Bug(bug_number, summary, description, severity, priority, environment, label, steps)
            service.save_to_txt(bug)
            service.save_to_excel(bug)
            service.close()
            st.success(f"Bug {bug.bug_id} report submitted successfully!")
elif page == "View Bug Report":
    st.title("View Bug Report")
    if os.path.exists("Bug_report.xlsx"):
        df = pd.read_excel("Bug_report.xlsx")

        col1, col2, col3, col4 =st.columns(4)
        col1.metric("Total Bugs", len(df))
        col2.metric("Critical Bugs", len(df[df["Severity"] == "Critical"]))
        col3.metric("Minor Bugs", len(df[df["Severity"] == "Minor"]))
        col4.metric("Major Bugs", len(df[df["Severity"] == "Major"]))
        df.index = range(1, len(df) + 1)
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            with open ("Bug_report.txt", "rb") as file:
                st.download_button("Download Bug Report", file, file_name="Bug_report.txt")
        with col2:
            with open ("Bug_report.xlsx", "rb") as excel_file:
                st.download_button("Download Excel Report", excel_file, file_name="Bug_report.xlsx")
    else:
        st.info("No bug reports found. Please submit a bug first.")

elif page == "Summary":
    st.title("Latest Bug Summary")

    if os.path.exists("Bug_report.xlsx"):
        df = pd.read_excel("Bug_report.xlsx")

        if len(df)>0:
            last_bug = df.iloc[-1]
            st.subheader(f"Bug ID: {last_bug['Bug_Id']}")
            st.write(f"**Summary:** {last_bug['Bug_Summary']}")
            st.write(f"**Description:** {last_bug['Bug_Description']}")
            col1, col2 = st.columns(2)
            with col1: 
                st.write(f"**Severity:** {last_bug['Severity']}")
                st.write(f"**Priority:** {last_bug['Priority']}")
            with col2:
                st.write(f"**Environment:** {last_bug['Environment']}")
                st.write(f"**Label:** {last_bug['Bug_Label']}")
                st.write(f"**Reported At:** {last_bug['Date and Time']}")
                
            steps = last_bug['Step_to_reproduce'].split(",")
            st.subheader("Steps to Reproduce")
            for i, step in enumerate(steps, 1):
                st.write(f"{i}. {step}")

            col1, col2 = st.columns(2)
            with col1:
                with open ("Bug_report.txt", "rb") as file:
                    st.download_button("Download Bug Report", file, file_name="Bug_report.txt")
            with col2:
                with open ("Bug_report.xlsx", "rb") as excel_file:
                    st.download_button("Download Excel Report", excel_file, file_name="Bug_report.xlsx")
        else:
            st.info("No bug reports found. Please submit a bug first.")
    else:
        st.info("No bug reports found. Please submit a bug first.")