from tkinter import *

class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.current_page = 0
        
        self.pages = [
            ("Hello, Everyone!", "This is the widgets of Tkinter:"),
            ("Frame Widget", "A container for organizing other widgets."),
            ("Label Widget", "Displays text in your GUI."),
            ("Button Widget", "Triggers actions when clicked."),
            ("Checkbutton Widget", "Enables a check when clicked")
        ]
        
        self.main_frame = Frame(parent)
        self.main_frame.pack(expand=True)
        
        self.label1 = Label(self.main_frame, text=self.pages[0][0], font=("Arial", 16))
        self.label1.pack()
        
        self.label2 = Label(self.main_frame, text=self.pages[0][1], font=("Arial", 13))
        self.label2.pack()

        self.button_test = Button(self.main_frame, text="Button", font=("Arial", 14), bg="yellow")
        self.check_button = Checkbutton(self.main_frame, text="Checkbutton", font=("Arial", 14), bg="yellow")
        
        self.button_next = Button(self.main_frame, text="Next", font=("Arial", 14), padx=10, pady=5, command=self.next_slide)
        self.button_prev = Button(self.main_frame, text="Previous", font=("Arial", 14), padx=10, pady=5, command=self.previous_slide)
        self.button_next.pack(pady=10)
        self.button_prev.pack(pady=10)

    def next_slide(self):
        self.current_page += 1
        if self.current_page < len(self.pages):
            self.label1.config(text=self.pages[self.current_page][0])
            self.label2.config(text=self.pages[self.current_page][1])

            if self.current_page == 3:
                self.button_test.pack(pady=10, before=self.button_next)
            else:
                self.button_test.pack_forget()

            if self.current_page == 4:
                self.check_button.pack(pady=10, before=self.button_next)
            else:
                self.check_button.pack_forget()
    
        else:
            self.current_page = 0
    
    def previous_slide(self):
        self.current_page -= 1
        if self.current_page < len(self.pages):
            self.label1.config(text=self.pages[self.current_page][0])
            self.label2.config(text=self.pages[self.current_page][1])

            if self.current_page == 3:
                self.button_test.pack(pady=10, before=self.button_next)
            else:
                self.button_test.pack_forget()

            if self.current_page == 4:
                    self.check_button.pack(pady=10, before=self.button_next)
            else:
                self.check_button.pack_forget()
            
        else:
            self.current_page = len(self.pages) - 1

if __name__ == "__main__":
    root = Tk()
    root.state("zoomed")
    myapp = MyApp(root)
    root.mainloop()
