import tkinter
from tkinter import *
from bot_functions import response
from voice import talk,take_command
from ml_part import respond
def send():
    voice_data=take_command()
    if 'can you help me' in voice_data or 'hey help me' in voice_data:
        talk('How can I help you? :')
        msg=take_command()
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        res = response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
        talk(res)
    elif 'hey you there' in voice_data or 'hey lets chat':
        talk('hey lets have a chat')
        msg=take_command()
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        res = response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
        talk(res)
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)

base = Tk()
base.title("Hello")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
photo = PhotoImage(file="mic.png")

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window

scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, image=photo,border=0, command= send )

#Place all components on the screen
SendButton.pack(side=BOTTOM, padx=15, pady=10)
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
base.mainloop()