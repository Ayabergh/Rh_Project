from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_evaluation_report(evaluation):
    # Create the filename with employee name and evaluation date
    filename = f"evaluation_report_{evaluation.employee.name}_{evaluation.date}.pdf"
    
    # Create the canvas for the PDF
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Set title and introductory information
    c.drawString(100, 750, f"Evaluation Report for {evaluation.employee.name}")
    c.drawString(100, 735, f"Date: {evaluation.date.strftime('%Y-%m-%d')}")
    
    # Display additional evaluation details
    c.drawString(100, 705, f"Evaluation Type: {evaluation.get_evaluation_type_display()}")  # Annual/Semi-Annual
    c.drawString(100, 690, f"Performance Rating: {evaluation.performance_rating}")
    c.drawString(100, 675, f"Skills Developed: {evaluation.skills_developed}")
    c.drawString(100, 660, f"Manager Comments: {evaluation.comments}")
    
    # Display objectives (or other fields based on your data model)
    if evaluation.criteria:
        c.drawString(100, 645, f"Custom Criteria:")
        y_position = 630
        for key, value in evaluation.criteria.items():
            c.drawString(100, y_position, f"{key}: {value}")
            y_position -= 15
    
    # Save the PDF
    c.save()
    
    return filename
