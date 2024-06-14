import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image

class WebPtoPNGConverter:
    def __init__(self, master):
        self.master = master
        master.title("WebP to PNG Converter")

        self.label = Label(master, text="Drop your WebP files here")
        self.label.pack(pady=20)

        self.convert_button = Button(master, text="Convert Files", command=self.convert_files)
        self.convert_button.pack(pady=20)

    def convert_files(self):
        file_paths = filedialog.askopenfilenames(title="Select WebP Files", filetypes=[("WebP files", "*.webp")])
        if file_paths:
            for file_path in file_paths:
                self.convert_file(file_path)

    def convert_file(self, file_path):
        file_dir, file_name = os.path.split(file_path)
        file_base, _ = os.path.splitext(file_name)
        output_path = os.path.join(file_dir, f"{file_base}.png")

        with Image.open(file_path) as img:
            img.save(output_path, "PNG")
        print(f"Converted {file_path} to {output_path}")

if __name__ == "__main__":
    root = Tk()
    converter = WebPtoPNGConverter(root)
    root.geometry("400x200")
    root.mainloop()
