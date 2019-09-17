from tkinter import *
from tkinter.filedialog import askopenfilename

class GUI(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.fCounter = 0
        f1 = LoginFrame(self)
        f2 = ResumeFrame(self)
        f3 = SearchFrame(self)
        self.frames=[]
        self.frames.append(f1)
        self.frames.append(f2)
        self.frames.append(f3)


        container = Frame(self)
        buttonFrame = Frame(self)

        container.pack(side="top", fill="both", expand=True)
        buttonFrame.pack(side="bottom", fill=X, expand=False)


        f1.place(in_=container, x=0, y=0, relwidth=1, relheight=0.5)
        f2.place(in_=container, x=0, y=0, relwidth=1, relheight=0.5)
        f3.place(in_=container, x=0, y=0, relwidth=1, relheight=0.5)


        self.backB = Button(buttonFrame, text="Back", command=self.back)
        nextB = Button(buttonFrame, text="Next", command=self.show)
        nextB.pack(side="right")






        f1.lift()
    def show(self):
        self.fCounter += 1
        nextF = self.frames[self.fCounter]
        if self.fCounter == 1:
            self.backB.pack(side="right")

        nextF.lift()
    def back(self):
        self.fCounter -= 1
        nextF = self.frames[self.fCounter]
        if self.fCounter == 0:
            self.backB.pack_forget()
        nextF.lift()



class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class LoginFrame(Page):
    def __init__(self,*args, **kwargs):

        Page.__init__(self, *args, **kwargs)
        self.emailLabel = Label(self,text="Email:")
        self.passwordLabel = Label(self,text="Password:")
        self.emailEntry = Entry(self)
        self.passwordEntry = Entry(self)

        self.emailLabel.grid(row=0, column=0,sticky=E)
        self.passwordLabel.grid(row=1, column=0, sticky=E)
        self.emailEntry.grid(row=0, column=1)
        self.passwordEntry.grid(row=1, column=1)

    def next(self):
        self.email = self.emailEntry.get()
        self.password = self.password.get()


class ResumeFrame(Page):
    def __init__(self,*args, **kwargs):
        Page.__init__(self, *args, **kwargs)


        chooseResume = Button(self,text="Choose Resume",bg= "red",foreground = "blue", command=self.chooseFramePath)
        chooseResume.pack()


    def chooseFramePath(self):
        self.resumePath = askopenfilename()


        pathName = Label(text=self.resumePath)
        pathName.pack()


class SearchFrame(Page):
    def __init__(self,*args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    root = Tk()
    main = GUI(root)
    root.title("Linkedin Easy Apply")
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("300x130")
    root.mainloop()