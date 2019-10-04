from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil
from os import path
import compare as cp

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.image_width = 360
        self.image_height = 360

        # Assign empty value to the image placeholders.
        self.master.firstImageDst = ""
        self.master.secondImageDst = ""

        load = Image.open("Images/Success Rule.jpeg")
        load = load.resize((self.image_width, self.image_height), Image.ANTIALIAS)
        initial_pic = ImageTk.PhotoImage(load)
        # self.pic_to_comp = PhotoImage(file="Images/upload_image.png")

        # First row containing label.
        self.welcome_label = Label(self.master, text="Welcome to Face Comparison", fg="black", width=111, height=3, bd=0, bg="#eee") \
            .grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        # Second row
        self.pic_vault = Label(self.master, text="Picture Defined", fg="black", width=30, height=37, bd=0, bg="#eee") \
            .grid(row=1, rowspan=3, column=0, padx=1, pady=1)
        self.real_img_label = Label(self.master, image=initial_pic)
        self.real_img_label.grid(row=1, column=1, padx=1, pady=1)
        self.compare_img_label = Label(self.master, image=initial_pic)
        self.compare_img_label.grid(row=1, column=2, padx=1, pady=1)
        # self.compare_img_label.image = initial_pic

        # Third row
        self.upload_firstImage_btn = Button(self.master, text="Upload Real Image", fg="black", width=40, height=7, bd=0, bg="#eee", cursor="hand2",
                                            command=lambda: self.upload_real_image()).grid(row=2, column=1, padx=1, pady=1)
        self.upload_SecondImage_btn = Button(self.master, text="Upload Image to Compare", fg="black", width=39, height=7, bd=0, bg="#eee", cursor="hand2",
                                             command=lambda: self.upload_comparison_image()).grid(row=2, column=2, padx=1, pady=1)
        self.compare_btn = Button(self.master, text="Compare Images", fg="black", width=39, height=7, bd=0,
                                             bg="#eee", cursor="hand2",
                                             command=lambda: self.compare_images()).grid(row=3, column=1, columnspan=2, padx=1, pady=1)

        # Fourth row
        self.result_display = Label(self.master, text="Result", fg="black", width=111, height=3, bd=0, bg="#eee") \
            .grid(row=4, column=0, columnspan=3, padx=1, pady=1)


    # Upload real image or first image.
    def upload_real_image(self):
        firstImageName = filedialog.askopenfilename(initialdir="Face_recognition/Images/lfw 2", title="Select file", filetypes=(("jpg files",
                    "*.jpg"), ("jpeg files", "*.jpeg"), ("png files", "*.png"), ("all files", "*.*")))
        print(firstImageName)
        src = path.realpath(firstImageName)

        # seperate the path from the filter
        head, tail = path.split(src)
        # print("path:" + head)
        print("file:" + tail)

        self.master.firstImageDst = "Images/" + tail
        shutil.copy(src, self.master.firstImageDst)
        print(self.master.firstImageDst)

        reload = Image.open(self.master.firstImageDst)
        reload = reload.resize((self.image_width, self.image_height), Image.ANTIALIAS)
        real_pic = ImageTk.PhotoImage(reload)
        self.real_img_label.config(image=real_pic)
        self.real_img_label.image = real_pic
        # self.pic_to_comp = PhotoImage(file=self.master.firstImageDst)

    # Upload the image to compare or second image.
    def upload_comparison_image(self):
        secondImageName = filedialog.askopenfilename(initialdir="Face_recognition/Images/lfw 2", title="Select file", filetypes=(("jpg files",
                    "*.jpg"), ("jpeg files", "*.jpeg"), ("png files", "*.png"), ("all files", "*.*")))
        print(secondImageName)
        src = path.realpath(secondImageName)

        # seperate the path from the filter
        head, tail = path.split(src)
        # print("path:" + head)
        print("file:" + tail)

        self.master.secondImageDst = "Images/" + tail
        shutil.copy(src, self.master.secondImageDst)
        print(self.master.secondImageDst)

        reload = Image.open(self.master.secondImageDst)
        reload = reload.resize((self.image_width, self.image_height), Image.ANTIALIAS)
        pic_to_comp = ImageTk.PhotoImage(reload)
        self.compare_img_label.config(image=pic_to_comp)
        self.compare_img_label.image = pic_to_comp
        # self.pic_to_comp = PhotoImage(file=self.master.secondImageDst)

    # This is the comparison function linking to the backend.
    def compare_images(self):
        print("Test for comparing these two images...")
        print(self.master.firstImageDst)
        print(self.master.secondImageDst)
        result = cp.main(cp.parse_arguments(["Model/20180402-114759",
                              self.master.firstImageDst,
                              self.master.secondImageDst]))
        positive_feedback = "These both images are similar."
        negative_feedback = "These both images are not similar."
        if result == True:
            self.result_display = Label(self.master, text=positive_feedback, fg="black", width=111, height=3, bd=0, bg="#eee") \
                .grid(row=4, column=0, columnspan=3, padx=1, pady=1)
            # self.result_display.config(text = positive_feedback)
            # self.result_display.text = positive_feedback
        else:
            self.result_display = Label(self.master, text=negative_feedback, fg="black", width=111, height=3, bd=0,
                                        bg="#eee") \
                .grid(row=4, column=0, columnspan=3, padx=1, pady=1)
            # self.result_display.config(text=negative_feedback)
            # self.result_display.text = negative_feedback



def main():
    print("Hello World")

    root = Tk()
    # Assigning the window's size.
    root.geometry("1000x750")
    # This prevents the window from resizing.
    root.resizable(0, 0)
    root.title("Face Recognition System")
    app = Window(root)
    app.mainloop()

if __name__ == "__main__":
    main()