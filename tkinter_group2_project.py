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
        self.button = Button(self.main_frame, text="Label", font=("Arial", 20), padx=20, pady=10, command=self.open_label)
        self.button.pack(side="left", pady=10)
        self.button = Button(self.main_frame, text="Button", font=("Arial", 20), padx=20, pady=10, command=self.open_button)
        self.button.pack(side="left", pady=10)
        self.button = Button(self.main_frame, text="Button checker", font=("Arial", 20), padx=20, pady=10, command=self.open_button_checker)
        self.button.pack(side="left", pady=10)

    def open_frame(self):
        new_window = Toplevel(self.parent)
        new_window.title("Frame")
        new_window.geometry("500x300")

        frame = Frame(new_window, bg="lightgray")  
        frame.pack(fill="both", expand=True)

    def open_label(self):
        new_window = Toplevel(self.parent)
        new_window.title("Frame")
        new_window.geometry("500x300")

        frame = Frame(new_window, bg="lightgray")  
        frame.pack(fill="both", expand=True)

        label = Label(frame, text="This is a label", font=("Arial", 16), bg="lightgray")
        label.pack(pady=20)
    
    def open_button(self):
        new_window = Toplevel(self.parent)
        new_window.title("Frame")
        new_window.geometry("500x300")

        frame = Frame(new_window, bg="lightgray")  
        frame.pack(fill="both", expand=True)

        label = Label(frame, text="This is a label", font=("Arial", 16), bg="lightgray")
        label.pack(pady=20)

        self.button = Button(new_window, text="This is a button", font=("Arial", 20), bg="lightgray", padx=20, pady=10, command=self.destruct)
        self.button.pack(side="top", pady=10)

        label = Label(frame, text="Click it to close all of the tabs", font=("Arial", 12), bg="lightgray")
        label.pack(pady=20)

    def open_button_checker(self):
        new_window = Toplevel(self.parent)
        new_window.title("Button Checker")
        new_window.geometry("500x300")

        frame = Frame(new_window, bg="lightgray")  
        frame.pack(fill="both", expand=True)

        label = Label(frame, text="This is a frame", font=("Arial", 16), bg="lightgray")
        label.pack(pady=20)

        self.check_var = IntVar()

        self.result_label = Label(frame, text="", font=("Arial", 14), bg="lightgray")
        self.result_label.pack(pady=10)

        def toggle_label():
            if self.check_var.get() == 1:
                self.result_label.config(text="Checkbutton is ON")
            else:
                self.result_label.config(text="Checkbutton is OFF")

        self.check_button = Checkbutton(frame, text="Toggle Label", font=("Arial", 14), bg="lightgray", variable=self.check_var, command=toggle_label)
        self.check_button.pack(pady=10)

        self.button = Button(frame, text="Close", font=("Arial", 14), bg="gray", padx=20, pady=10, command=new_window.destroy)
        self.button.pack(pady=10)

    def destruct(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    root.state("zoomed")
    myapp = MyApp(root)
    root.mainloop()
