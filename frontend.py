
# frontend.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import backend

class EAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI E-Waste Detection Assistant")
        self.root.geometry("500x600")

        self.label = tk.Label(root, text="Upload E-Waste Image", font=("Arial", 14))
        self.label.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.collect_btn = tk.Button(root, text="Schedule Collection", command=self.schedule, state=tk.DISABLED)
        self.collect_btn.pack(pady=10)

        self.image_path = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if file_path:
            self.image_path = file_path
            img = Image.open(file_path).resize((300, 300))
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo

            is_e = backend.is_e_waste(file_path)
            if is_e:
                self.result_label.config(text="✅ E-Waste Detected", fg="green")
                self.collect_btn.config(state=tk.NORMAL)
            else:
                self.result_label.config(text="❌ Not E-Waste", fg="red")
                self.collect_btn.config(state=tk.DISABLED)

    def schedule(self):
        msg = backend.schedule_collection()
        messagebox.showinfo("Collection", msg)
        self.result_label.config(text="")
        self.collect_btn.config(state=tk.DISABLED)
        self.image_label.config(image="")