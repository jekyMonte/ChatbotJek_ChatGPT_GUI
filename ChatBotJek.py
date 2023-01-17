import customtkinter as CTK
import openai
from api_key import API_KEY


openai.api_key = API_KEY
CTK.set_appearance_mode("Dark")
CTK.set_default_color_theme("green")

root = CTK.CTk()
root.wm_title("ChatbotJek")
root.geometry("600x450")

def send_message():
    textbot.configure(state="normal")
    text = chat.get()
    print(text)
    try:
        completions = openai.Completion.create(engine="text-davinci-003", prompt=text, max_tokens=1024, n=1,stop=None,temperature=0.5)
        message = completions.choices[0].text
    except ValueError as e:
        print(e)
        message = "Error ="+e
    
    textbot.insert("1.0", "BotJek:"+message+"\n\n")
    print("Sending message")
    textbot.configure(state="disabled")
    chat.delete(0, 1000)

def enter(text):
    textbot.configure(state="normal")
    text = chat.get()
    print(text)
    try:
        completions = openai.Completion.create(engine="text-davinci-003", prompt=text, max_tokens=1024, n=1,stop=None,temperature=0.5)
        message = completions.choices[0].text
    except ValueError as e:
        print(e)
        message = "Error ="+e
        
    textbot.insert("1.0", "BotJek:"+message+"\n\n")
    print("Sending message")
    
    textbot.configure(state="disabled")
    chat.delete(0, 1000)

root.wm_iconbitmap("icon.ico")
frame = CTK.CTkFrame(root)
frame.pack(fill="both", expand=True)

labelu = CTK.CTkLabel(frame, text="ChatbotJek", font=("Roboto", 24))
labelu.pack(pady=12, padx=10)

textbot = CTK.CTkTextbox(frame, state='disabled')
textbot.configure(height=300, width=500)
textbot.pack()

chat = CTK.CTkEntry(frame, placeholder_text="Click Enter to Send")
chat.bind("<Return>", enter)
chat.configure(height=30, width=350)
chat.pack(pady=5, padx=10)

send = CTK.CTkButton(frame, text="Send", command=send_message)
send.pack()

root.mainloop()