import tkinter as tk
from tkinter import filedialog, messagebox
import os

def encrypt_decrypt_image(image_path, key, encrypt=True):
    try:
        fin = open(image_path, 'rb')
        image_data = fin.read()
        fin.close()

        image_data = bytearray(image_data)

        for index, value in enumerate(image_data):
            if encrypt:
                image_data[index] = value ^ key
            else:
                image_data[index] = value ^ key

        fin = open(image_path, 'wb')
        fin.write(image_data)
        fin.close()

        messagebox.showinfo("Success", "Encryption/Decryption done successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

class ImageEncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryption/Decryption Tool")

        # Increase window size
        master.geometry("400x200")

        self.key_label = tk.Label(master, text="Key:", font=("Times New Roman", 13, "bold"))
        self.key_label.grid(row=0, column=0, sticky="w")

        self.key_entry = tk.Entry(master)
        self.key_entry.grid(row=0, column=1)

        self.image_label = tk.Label(master, text="Image Path:", font=("Times New Roman", 13, "bold"))
        self.image_label.grid(row=1, column=0, sticky="w")

        self.image_entry = tk.Entry(master)
        self.image_entry.grid(row=1, column=1)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_image)
        self.browse_button.grid(row=1, column=2)

        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt_image, font=("Times New Roman", 13, "bold"))
        self.encrypt_button.grid(row=2, column=0)

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt_image, font=("Times New Roman", 13, "bold"))
        self.decrypt_button.grid(row=2, column=1)

    def browse_image(self):
        file_path = filedialog.askopenfilename()
        self.image_entry.delete(0, tk.END)
        self.image_entry.insert(0, file_path)

    def encrypt_image(self):
        key = self.key_entry.get()
        image_path = self.image_entry.get()
        try:
            key = int(key)
            encrypt_decrypt_image(image_path, key, encrypt=True)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer key.")

    def decrypt_image(self):
        key = self.key_entry.get()
        image_path = self.image_entry.get()
        try:
            key = int(key)
            encrypt_decrypt_image(image_path, key, encrypt=False)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer key.")

def main():
    root = tk.Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
