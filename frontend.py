import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import aspose.slides as slides
import aspose.pydrawing as drawing
from gesture import detection

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()

def convert_ppt_to_img(): 
    ppt_path = file_path
    
    ppt_name = os.path.basename(ppt_path)
    img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PPT_IMG')
    os.makedirs(img_dir, exist_ok=True)
    
    # Open PowerPoint application
    pres = slides.Presentation(ppt_path)
    thumbnail_size = drawing.Size(1024, 768)
    for index in range(pres.slides.length):
        # Get reference of slide
        slide = pres.slides[index]

        # Save as JPG
        slide.get_thumbnail(thumbnail_size).save(os.path.join(img_dir, f'slide_{index}.jpg'), drawing.imaging.ImageFormat.jpeg)


    print('Images saved successfully in', img_dir)
    # Open navigation window
    quit_window()
    detection('PPT_IMG')
    # detection("PPT")


# Create GUI for selecting PPT file
root = Tk()
root.title('PPT Image Converter')
root.geometry('400x200')

browse_button = Button(root, text="Browse PPT file", command=browse_file)
browse_button.pack(pady=10)

convert_button = Button(root, text="Convert to Images", command=convert_ppt_to_img)
convert_button.pack(pady=10)

def quit_window():
    root.destroy()


root.mainloop()
