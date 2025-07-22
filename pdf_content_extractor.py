import fitz  # PyMuPDF
import json
import os

def extract_pdf_content(pdf_path, output_dir="extracted_content"):
    """
    Extracts text and images from a PDF and organizes them into a structured JSON file.

    Args:
        pdf_path (str): The path to the input PDF file.
        output_dir (str): The directory to save extracted images and the JSON file.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    structured_content = []

    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        # --- Text Extraction ---
        text = page.get_text("text")
        
        # --- Image Extraction ---
        image_list = page.get_images(full=True)
        
        image_paths = []
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Get the image extension
            image_ext = base_image["ext"]
            image_filename = f"page{page_num + 1}_image{image_index + 1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)
            
            # Save the image
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            image_paths.append(image_path)

        # Basic logic to associate text with images on the same page
        # This can be refined with more advanced layout analysis
        if text.strip() or image_paths:
            # A simple approach to structure the questions and options.
            # For the given sample, we can assume a pattern of one question image
            # followed by option images. This might need to be adjusted for
            # different PDF structures.
            
            question_text = ""
            lines = text.strip().split('\n')
            # A simple heuristic: assume the first significant line of text is the question
            for line in lines:
                if line.strip():
                    question_text = line.strip()
                    break

            question_image = ""
            option_images = []

            if image_paths:
                # Assuming the first image is related to the question
                question_image = image_paths[0]
                # Assuming the rest of the images are options
                option_images = image_paths[1:]

            structured_content.append({
                "question": question_text,
                "images": question_image,
                "option_images": option_images
            })

    # --- Structured Output ---
    json_output_path = os.path.join(output_dir, "extracted_content.json")
    with open(json_output_path, "w") as json_file:
        json.dump(structured_content, json_file, indent=4)
        
    print(f"Content extraction complete. Images and JSON file saved in '{output_dir}' directory.")
    print(f"JSON file created at: {json_output_path}")


# --- Execution ---
if __name__ == "__main__":
    # Ensure you have the PDF file in the same directory or provide the correct path
    pdf_file_path = "IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
    
    if os.path.exists(pdf_file_path):
        extract_pdf_content(pdf_file_path)
    else:
        print(f"Error: The file '{pdf_file_path}' was not found.")
        print("Please make sure the PDF file is in the same directory as the script or provide the full path.")