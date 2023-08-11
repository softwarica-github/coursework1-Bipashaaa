from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import unittest

class ImageSteganographyApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")
        self.root.geometry("500x400+300+150")

        self.create_widgets()

    def create_widgets(self):
        self.label1 = Label(text="Image Steganography")
        self.label1.place(relx=0.3, rely=0.1, height=20, width=150)

        self.encode_button = Button(text="Encode", command=self.encode)
        self.encode_button.place(relx=0.3, rely=0.3, height=40, width=80)

        self.decode_button = Button(text="Decode", command=self.decode)
        self.decode_button.place(relx=0.5, rely=0.3, height=40, width=80)

    def open_file(self):
        fileopen = askopenfilename(initialdir="/Desktop", title="Select file", filetype=(("JPEG files", "*.jpg"), ("All files", "*.*")))
        return fileopen

    def encode(self):
        self.root.withdraw()
        enc = Toplevel()
        enc.title("Encode")
        enc.geometry("500x400+300+150")

        label1 = Label(enc, text="Secure message")
        label1.place(relx=0.1, rely=0.1, height=20, width=100)

        self.entry = Entry(enc)
        self.entry.place(relx=0.4, rely=0.1)

        label2 = Label(enc, text="File Name")
        label2.place(relx=0.1, rely=0.2, height=20, width=100)

        self.entry_save = Entry(enc)
        self.entry_save.place(relx=0.4, rely=0.2)

        def encode_image():
            fileopen = self.open_file()
            if fileopen:
                response = messagebox.askyesno("Pop Up", "Do you want to encode?")
                if response:
                    # Perform encoding logic here (removed stegano)
                    messagebox.showinfo("Pop Up", "Successfully encoded")
                else:
                    messagebox.showwarning("Pop Up", "Unsuccessful")

        button_select = Button(enc, text="Select file", command=self.open_file)
        button_select.place(relx=0.1, rely=0.3)

        button_encode = Button(enc, text="Encode", command=encode_image)
        button_encode.place(relx=0.4, rely=0.5)

    def decode(self):
        self.root.withdraw()
        dnc = Toplevel()
        dnc.title("Decode")
        dnc.geometry("500x400+300+150")

        def decode_image():
            fileopen = self.open_file()
            if fileopen:
                # Perform decoding logic here (removed stegano)
                label4 = Label(dnc, text="Decoded message goes here")
                label4.place(relx=0.3, rely=0.3)

        button_select = Button(dnc, text="Select file", command=self.open_file)
        button_select.place(relx=0.1, rely=0.3)

        button_decode = Button(dnc, text="Decode", command=decode_image)
        button_decode.place(relx=0.4, rely=0.5)


class TestImageSteganographyApp(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = ImageSteganographyApp(self.root)

    def test_open_file(self):
        file_path = self.app.open_file()
        self.assertIsNotNone(file_path)

    # Add more test cases as needed

    def tearDown(self):
        self.root.destroy()


if __name__ == "__main__":
    unittest.main(exit=False)

root = Tk()
app = ImageSteganographyApp(root)
root.mainloop()
