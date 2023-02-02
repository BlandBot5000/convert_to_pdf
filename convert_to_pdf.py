import os
from os import path
import argparse
from PIL import Image


def arg_parser():
    parser = argparse.ArgumentParser(description="Convert a folder of images into a pdf.")
    parser.add_argument("-p", "--path", type=str, help="Folder path", required=True)
    args = parser.parse_args();
    return args

def open_folder(folder_path: str):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def convert_to_pdf(folder_path):
    pdf = []
    images = os.listdir(folder_path)
    images.sort()

    for i in images:
        image_path = path.join(folder_path, i)
        print(image_path)
        try: pdf.append(Image.open(image_path).convert('RGBA').convert('RGB'))
        except Image.UnidentifiedImageError: continue 

    cover_page = pdf[0]
    pdf.remove(cover_page)
    
    pdf_name = path.join(os.path.dirname(folder_path), os.path.basename(folder_path))
    cover_page.save(pdf_name + '.pdf', save_all=True, append_images=pdf)

if __name__ == "__main__":
    #Start program
    print("[ Convert to PDF ]\n")

    args = arg_parser()
    convert_to_pdf(args.path)
    
    print("\n---Program End---")

