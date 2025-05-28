from tkinter import *


class MyApp:
    def __init__(self, parent):
        self.parent = parent

        self.main_frame = Frame(parent)
        self.main_frame.pack()

        self.button = Button(self.main_frame, text="Quit1", command=self.terminate_program)
        self.button.pack(side="left")
        self.button = Button(self.main_frame, text="Quit2", command=self.terminate_program)
        self.button.pack(side="left")

        self.bottomframe = Frame(self.main_frame)
        self.bottomframe.pack()

        self.button = Button(self.bottomframe, text="Quit3", command=self.terminate_program)
        self.button.pack(side="top")
        self.button = Button(self.bottomframe, text="Quit4", command=self.terminate_program)
        self.button.pack(side="left")

    def terminate_program(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()
