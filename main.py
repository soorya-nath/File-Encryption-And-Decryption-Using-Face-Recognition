import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import os
from match_checker import get_locs,check
from cryp import enc,dec

class WebcamApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas = tk.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()
        self.btn_encrypt = tk.Button(window, text="Encrypt File", width=25, height=2, command=self.encrypt_file)
        self.btn_encrypt.pack(pady=5)
        self.btn_decrypt = tk.Button(window, text="Decrypt File", width=25, height=2, command=self.decrypt_file)
        self.btn_decrypt.pack(pady=5)
        self.btn_decrypt = tk.Button(window, text="exit", width=25,height=2, command=self.exit)
        self.btn_decrypt.pack(pady=5)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.update_video()

    def exit(self):
        exit(0)

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Choose a file to encrypt")
        print(file_path)
        return file_path 
    
    def update_video(self):
        ret, frame = self.vid.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = self.face_cascade.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(rgb_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            pil_img = Image.fromarray(rgb_frame)
            self.img = ImageTk.PhotoImage(image=pil_img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.window.after(10, self.update_video)
    

    def capture_image(self):
        ret, frame = self.vid.read()
        if ret:
            faces = self.face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                image_name = f"{len(os.listdir('captured_images')) + 1}.jpg"
                image_path = os.path.join('captured_images', image_name)
                cv2.imwrite(image_path, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                return image_name                
            else:
                messagebox.showwarning("No Face Detected", "No face detected in the image. Try again.")


    def encrypt_file(self):
        img = self.capture_image()
        if img:
            file = self.choose_file() 
            images = os.listdir(".\\captured_images")
            hit = 0
            a = 0
            for image in images:
                if image!=img:
                    a = check(".\\captured_images\\"+image,".\\captured_images\\"+img)
                    if a:
                        hit = 1
                        msg = enc(file,get_locs(".\\captured_images\\"+image))
                        if msg:
                            messagebox.showinfo("file successfully encrytped","file succesfully secured!!")
                            os.remove(file)
                        else:
                            messagebox.showerror("encryption failed","error in encryption")
                        os.remove("./captured_images/"+img)
                        break
            if not hit:
                msg = enc(file,get_locs(".\\captured_images\\"+img))
                if msg:
                    messagebox.showinfo("file successfully encrytped","file is secured")
                else:
                    messagebox.showerror("encryption failed","error in encryption")


    def decrypt_file(self):
        img = self.capture_image()
        if img:
            file = self.choose_file() 
            images = os.listdir(".\\captured_images")
            print(images)
            hit = 0
            a = 0
            for image in images:
                if image!=img:
                    a = check(".\\captured_images\\"+image,".\\captured_images\\"+img)
                    if a:
                        hit = 1
                        os.remove("./captured_images/"+img)
                        msg = dec(file,get_locs(".\\captured_images\\"+image))
                        if msg:
                            messagebox.showinfo("file successfully decrypted","you can access it now")
                            os.remove(file)
                        else:
                            messagebox.showerror("decryption failed","error in decryption!! unauthorized acces")
                        break
            if not a:
                messagebox.showerror("decryption failed","unauthorized access")
            if not hit: os.remove("./captured_images/"+img)


window = tk.Tk()
window.title("Webcam Video Capture & Image Capture with Face Detection")

os.makedirs('captured_images', exist_ok=True)
app = WebcamApp(window, "Webcam Video Capture & Image Capture with Face Detection")
window.mainloop()