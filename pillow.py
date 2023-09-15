from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_images_to_pdf(input_folder, output_pdf):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(tuple(image_extensions))]
    image_files.sort()

    if not image_files:
        print("No image files found in the specified folder.")
        return

    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)

        try:
            img = Image.open(image_path)
            img_width, img_height = img.size
            c.setPageSize((img_width, img_height))
            c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
            c.showPage()
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    c.save()
    print(f"Images have been successfully converted to {output_pdf}")

if __name__ == "__main__":
    input_folder = r'C:\Users\khali\Documents\books'
    output_pdf = r'C:\Users\khali\Documents\books\output.pdf'

    convert_images_to_pdf(input_folder, output_pdf)