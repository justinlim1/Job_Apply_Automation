from tkinter import *
from tkinter.filedialog import askopenfilename


# from https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

class GUI(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.fCounter = 0

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginFrame, ResumeFrame, SearchFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class LoginFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.emailLabel = Label(self, text="Email:")
        self.passwordLabel = Label(self, text="Password:")
        self.emailEntry = Entry(self)
        self.passwordEntry = Entry(self)

        self.emailLabel.grid(row=0, column=0, sticky=E)
        self.passwordLabel.grid(row=1, column=0, sticky=E)
        self.emailEntry.grid(row=0, column=1)
        self.passwordEntry.grid(row=1, column=1)
        button = Button(self, text="Next", command=self.next)
        button.grid()

    def next(self):
        self.email = self.emailEntry.get()
        self.password = self.passwordEntry.get()
        self.controller.show_frame("ResumeFrame")


class ResumeFrame(Page):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        chooseResume = Button(self, text="Choose Resume", bg="red", foreground="blue", command=self.chooseFramePath)
        chooseResume.grid()
        button = Button(self, text="Next", command=lambda: controller.show_frame("SearchFrame"))
        button.grid()
        back = Button(self, text="Back", command=self.back)
        back.grid()

    def chooseFramePath(self):
        self.resumePath = askopenfilename()

        self.pathName = Label(text=self.resumePath)

        self.pathName.grid()

    def back(self):
        self.pathName.grid_forget()
        self.controller.show_frame("LoginFrame")


class SearchFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))


if __name__ == "__main__":
    root = Tk()
    main = GUI(root)
    root.title("Linkedin Easy Apply")
    main.grid()
    root.wm_geometry("300x130")
    root.mainloop()
