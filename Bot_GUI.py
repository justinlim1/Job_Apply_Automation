from tkinter import *
from tkinter.font import Font
from tkinter.filedialog import askopenfilename
import os



#from https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter



class GUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.fCounter = 0
        self.title_font = Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.subtitle_font = Font(family='Helvetica', size=12, weight="bold", slant="italic")

        container = Frame(self)
        container.grid(row=10)
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
        self.passwordEntry.grid(row=1, column=1, sticky=E)
        button = Button(self, text="Next", command=self.next)
        button.grid(row=15, column=1, sticky=E,pady=30)

    def next(self):
        self.email = self.emailEntry.get()
        self.password = self.passwordEntry.get()
        self.controller.show_frame("ResumeFrame")


class ResumeFrame(Page):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.resumePath = None
        chooseResume = Button(self, text="Choose Resume", bg="red", foreground="blue", command=self.chooseFramePath)
        chooseResume.grid(row=0,column=0)

        button = Button(self, text="Next", command=lambda: controller.show_frame("SearchFrame"))
        button.grid(row=10, column=2,sticky=E,pady=65)
        back = Button(self, text="Back", command=self.back)
        back.grid(row=10,  column=1,sticky=E,pady=65,padx=(73,0))

    def chooseFramePath(self):
        self.resumePath = askopenfilename()

        self.pathName = Label(self,text=os.path.basename(self.resumePath))

        self.pathName.grid(row=0, column=1)
        self.update()
    def back(self):
        if self.resumePath:
            self.pathName.grid_forget()
        self.controller.show_frame("LoginFrame")


class SearchFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.keywordsLabel = Label(self, text="Keywords:")
        self.locationLabel = Label(self, text="Location:")
        self.keywordsEntry = Entry(self)
        self.locationEntry = Entry(self)
        self.buttonFrame = Frame(self)


        self.keywordsLabel.grid(row=0, column=0, sticky=E)
        self.locationLabel.grid(row=1, column=0, sticky=E)
        self.keywordsEntry.grid(row=0, column=1)
        self.locationEntry.grid(row=1, column=1)

        self.buttonFrame.grid(row=2, column=1)
        button = Button(self.buttonFrame, text="Apply", command=self.apply)
        button.grid(column=2,row=1,pady=30)
        back = Button(self.buttonFrame, text="Back", command=self.back)
        back.grid(column=1,row=1,pady=30,padx=(90,0))

    def back(self):
        self.controller.show_frame("ResumeFrame")

    def apply(self):

        self.keywords = self.keywordsEntry.get()
        self.location = self.locationEntry.get()
        self.controller.destroy()
        self.destroy()

