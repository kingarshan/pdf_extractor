import fitz  
import json
import os

def extract_pdf_content(pdf_path, output_dir="extracted_content"):

    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_document = fitz.open(pdf_path)
    
    structured_content = []

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        text = page.get_text("text")
        
        image_list = page.get_images(full=True)
        
        image_paths = []
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            
            image_ext = base_image["ext"]
            image_filename = f"page{page_num + 1}_image{image_index + 1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)
            
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            image_paths.append(image_path)

        if text.strip() or image_paths:
            
            
            question_text = ""
            lines = text.strip().split('\n')
            for line in lines:
                if line.strip():
                    question_text = line.strip()
                    break

            question_image = ""
            option_images = []

            if image_paths:
                question_image = image_paths[0]
                option_images = image_paths[1:]

            structured_content.append({
                "question": question_text,
                "images": question_image,
                "option_images": option_images
            })

    json_output_path = os.path.join(output_dir, "extracted_content.json")
    with open(json_output_path, "w") as json_file:
        json.dump(structured_content, json_file, indent=4)
        
    print(f"Content extraction complete. Images and JSON file saved in '{output_dir}' directory.")
    print(f"JSON file created at: {json_output_path}")


if __name__ == "__main__":
    pdf_file_path = "IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
    
    if os.path.exists(pdf_file_path):
        extract_pdf_content(pdf_file_path)
    else:
        print(f"Error: The file '{pdf_file_path}' was not found.")
        print("Please make sure the PDF file is in the same directory as the script or provide the full path.")
