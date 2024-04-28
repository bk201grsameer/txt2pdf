from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib.styles import getSampleStyleSheet
import os

def txt_to_pdf(input_file, output_folder, output_file_name):
    # Define margins
    left_margin = 50
    right_margin = 50
    top_margin = 50
    bottom_margin = 50

    with open(input_file, "r") as txt_file:
        lines = txt_file.readlines()

    # If output folder is provided, generate output file in that folder
    if output_folder:
        output_path = os.path.join(output_folder, output_file_name)
    else:
        output_path = output_file_name

    # Add ".pdf" extension if not provided
    if not output_path.endswith('.pdf'):
        output_path += ".pdf"

    pdf = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    max_width = width - (
        left_margin + right_margin
    )  # Adjusted width after considering left and right margins

    # Set font style
    style = getSampleStyleSheet()["Normal"]
    pdf.setFont(style.fontName, style.fontSize)

    y = height - top_margin  # Starting y-coordinate
    for line in lines:
        # Word-wrap the line using simpleSplit
        wrapped_lines = simpleSplit(
            line.strip(), style.fontName, style.fontSize, max_width
        )
        # Draw each wrapped line
        for wrapped_line in wrapped_lines:
            pdf.drawString(left_margin, y, wrapped_line)
            y -= style.leading  # Move to the next line
        y -= style.leading  # Add extra spacing after each paragraph

    pdf.save()
    # After saving the PDF, let's also open the generated PDF for preview
    os.startfile(output_path)

# Example usage
input_file = input("Enter the path to the input text file: ")
output_folder = input("Enter the path to the output folder (leave blank for current folder): ").strip()
output_file_name = input("Enter the output file name (without extension, e.g., output): ")

if not output_folder:
    output_folder = None

txt_to_pdf(input_file, output_folder, output_file_name)
