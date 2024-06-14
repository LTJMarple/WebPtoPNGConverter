import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image

class ImageConverter:
    def __init__(self, master):
        self.master = master
        master.title("Image Converter")

        self.label = Label(master, text="Choose your conversion option:")
        self.label.pack(pady=20)

        self.convert_webp_to_png_button = Button(master, text="Convert WebP to PNG", command=self.convert_webp_to_png)
        self.convert_webp_to_png_button.pack(pady=10)

        self.convert_png_to_ico_button = Button(master, text="Convert PNG to ICO", command=self.convert_png_to_ico)
        self.convert_png_to_ico_button.pack(pady=10)

    def convert_webp_to_png(self):
        file_paths = filedialog.askopenfilenames(title="Select WebP Files", filetypes=[("WebP files", "*.webp")])
        if file_paths:
            for file_path in file_paths:
                self.convert_file(file_path, 'PNG')

    def convert_png_to_ico(self):
        file_paths = filedialog.askopenfilenames(title="Select PNG Files", filetypes=[("PNG files", "*.png")])
        if file_paths:
            for file_path in file_paths:
                self.convert_file(file_path, 'ICO')

    def convert_file(self, file_path, format):
        file_dir, file_name = os.path.split(file_path)
        file_base, _ = os.path.splitext(file_name)
        output_path = os.path.join(file_dir, f"{file_base}.{format.lower()}")

        with Image.open(file_path) as img:
            if format == 'ICO':
                img.save(output_path, format, sizes=[(256, 256)])
            else:
                img.save(output_path, format)
        print(f"Converted {file_path} to {output_path}")

if __name__ == "__main__":
    root = Tk()
    converter = ImageConverter(root)
    root.geometry("400x200")
    root.mainloop()
