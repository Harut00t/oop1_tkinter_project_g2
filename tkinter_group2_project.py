from tkinter import *


class MyApp:
    def __init__(self, parent):
        self.parent = parent

        self.main_frame = Frame(parent)
        self.main_frame.pack(expand=True)

        label = Label(self.main_frame, text="Hello, Everyone!", font=("Arial", 16))
        label.pack()
        label = Label(self.main_frame, text="This is the widgets of Tkinter:", font=("Arial", 13))
        label.pack()

        self.button = Button(self.main_frame, text="Frame", font=("Arial", 20), padx=20, pady=10, command=self.open_frame)
        self.button.pack(side="left", pady=10)
        self.button = Button(self.main_frame, text="Label", font=("Arial", 20), padx=20, pady=10)
        self.button.pack(side="left", pady=10)
        self.button = Button(self.main_frame, text="Button", font=("Arial", 20), padx=20, pady=10)
        self.button.pack(side="left", pady=10)
        self.button = Button(self.main_frame, text="Button checker", font=("Arial", 20), padx=20, pady=10)
        self.button.pack(side="left", pady=10)

    def open_frame(self):
        new_window = Frame(self.parent)
        new_window.title("Frame")
        new_window.pack(expand=True)

        label = Label(new_window, text="This is the new screen!", font=("Arial", 16))
        label.pack(pady=20)

        close_button = Button(new_window, text="Close", font=("Arial", 14), command=new_window.destroy)
        close_button.pack()


if __name__ == "__main__":
    root = Tk()
    root.state("zoomed")
    myapp = MyApp(root)
    root.mainloop()
