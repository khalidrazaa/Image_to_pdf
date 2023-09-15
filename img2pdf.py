import img2pdf
import os

def convert_images_to_pdf(input_folder, output_pdf):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(tuple(image_extensions))]
    image_files.sort()

    if not image_files:
        print("No image files found in the specified folder.")
        return

    pdf_bytes = img2pdf.convert([os.path.join(input_folder, image_file) for image_file in image_files])

    with open(output_pdf, "wb") as pdf_file:
        pdf_file.write(pdf_bytes)

    print(f"Images have been successfully converted to {output_pdf}")

if __name__ == "__main__":
    input_folder = r'C:\Users\khali\Documents\books'
    output_pdf = r'C:\Users\khali\Documents\books\active_math.pdf'

    convert_images_to_pdf(input_folder, output_pdf)