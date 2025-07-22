PDF Content Analysis and Question GenerationIntroductionThis project is a Python-based tool designed to analyze PDF documents, specifically educational materials like math olympiad sample papers. The primary goal is to extract all meaningful content—text and images—and structure it in a machine-readable format (JSON). This serves as the foundation for a larger AI-powered system that can generate questions based on the extracted visual and textual information.This repository contains Part 1 of the assignment, focusing on content extraction.FeaturesText Extraction: Extracts all textual content from each page of the PDF.Image Extraction: Identifies and saves all images from the PDF as separate files (.png, .jpg, etc.).Structured JSON Output: Organizes the extracted content by page, associating text with the corresponding images and structuring them into a question/options format.RequirementsPython 3.6+PyMuPDFPillowInstallationClone the repository (or download the script):git clone <repository-url>
cd <repository-directory>
Install the required Python libraries using pip:pip install PyMuPDF Pillow
UsagePlace the PDF file you want to analyze in the same directory as the Python script (pdf_content_extractor.py). By default, the script looks for a file named IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf.Run the script from your terminal:python pdf_content_extractor.py
If your PDF has a different name, you can modify the pdf_file_path variable within the script:# In pdf_content_extractor.py
pdf_file_path = "your_pdf_file_name.pdf"
OutputThe script will create a new directory named extracted_content/ in the same location. This directory will contain:Extracted Images: All images from the PDF, saved with filenames like page1_image1.png, page2_image1.png, etc.JSON File: A file named extracted_content.json that contains the structured data.Example JSON StructureThe extracted_content.json file will have a structure similar to this:[
    {
        "question": "1. Which of the following is the heaviest?",
        "images": "extracted_content/page1_image1.png",
        "option_images": [
            "extracted_content/page1_image2.png",
            "extracted_content/page1_image3.png",
            "extracted_content/page1_image4.png",
            "extracted_content/page1_image5.png"
        ]
    },
    {
        "question": "2. Find the value of",
        "images": "extracted_content/page2_image1.png",
        "option_images": [
            "extracted_content/page2_image2.png",
            "extracted_content/page2_image3.png",
            "extracted_content/page2_image4.png",
            "extracted_content/page2_image5.png"
        ]
    }
]
Libraries UsedPyMuPDF (fitz): For parsing the PDF file, extracting text, and identifying image objects.Pillow (PIL): Used for handling and saving the extracted image data, though PyMuPDF handles most of the direct extraction.os: For handling file paths and creating directories.json: For creating and writing the final JSON output file.