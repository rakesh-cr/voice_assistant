import tkinter
from tkinter import *
from tkinter import messagebox
from main import chat
from main import exit

root = tkinter.Tk()
root.geometry("400x500")
#root.attributes('-alpha', 0.8)
photo = PhotoImage(file="mic.png")
photo2= PhotoImage(file="e10.png")
btn = Button(
    root,
    image=photo,
    command=chat,
    border=1
    )
exit_btn=Button(
    root,
    image=photo2,
    command=exit,
    border=0
)
exit_btn.pack(side=TOP, padx=15, pady=5,anchor=E)
btn.pack(side=BOTTOM, padx=15, pady=10)


#Create Chat window
ChatLog = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(root, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

ChatLog.config(state=NORMAL)
ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

res = chat()
ChatLog.insert(END, "Bot: " + res + '\n\n')

ChatLog.config(state=DISABLED)
ChatLog.yview(END)
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)

root.mainloop()