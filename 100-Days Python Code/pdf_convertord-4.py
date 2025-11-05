# 📄 PDF Converter in Python
# Features: Text → PDF, Image → PDF

from fpdf import FPDF
from PIL import Image
import os

def text_to_pdf():
    text_file = input("Enter text file path (e.g., notes.txt): ")
    output_file = input("Enter output PDF name (e.g., notes.pdf): ")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    try:
        with open(text_file, "r", encoding="utf-8") as f:
            for line in f:
                pdf.multi_cell(0, 10, line.strip())
        pdf.output(output_file)
        print(f"✅ Text converted to PDF: {output_file}")
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")

def image_to_pdf():
    image_file = input("Enter image file path (e.g., photo.jpg): ")
    output_file = input("Enter output PDF name (e.g., photo.pdf): ")

    try:
        image = Image.open(image_file)
        rgb_image = image.convert("RGB")
        rgb_image.save(output_file)
        print(f"✅ Image converted to PDF: {output_file}")
    except FileNotFoundError:
        print("❌ Image not found. Please check the path.")

def main():
    while True:
        print("\n===== PDF Converter =====")
        print("1. Convert Text to PDF")
        print("2. Convert Image to PDF")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            text_to_pdf()
        elif choice == "2":
            image_to_pdf()
        elif choice == "3":
            print("Exiting PDF Converter. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
