from tkinter import *


class Frontend:

    def sv(self, message):
        window = Tk()
        window.title('...')
        window.geometry('300x50')
        lbl = Label(window, text=message.getText() + ' ' + message.getSender())
        lbl.grid(column=0, row=0)
        btn = Button(window, text="Ok")
        btn.grid(column=1, row=1)
        # btn.pack(anchor=center)
        window.mainloop()


