import tkinter as tk
from tkinter import *
import pyttsx3
import threading


root = tk.Tk()
root.title("Proverbial Chatbot")
root.geometry("800x500")

var=None
result=None

#dictionary of proverbs
proverb_dict ={
    "As you sow": "so shall you reap.",
    "Make hay while": "the sun shines.",
    "Slow and steady": "wins the race.",
    "Actions speak louder": "than words.",
    "Don't put all": "your eggs in one basket.",
    "A bird in": "the hand is worth two in the bush."
} 

def reset():
    #resets the user_entry and bot_entry entry boxes, and proverb_label
    user_entry.delete(0, tk.END)
    user_entry.insert(0, "Enter first three words of a proverb, chatbot will complete i after click of 'Get Proverb' buttont.")
    bot_entry.delete(0, tk.END)
    proverb_label.config(text=" ")


def speak_text(text):
    #Function to handle text-to-speech in a separate thread
    try:
        # Stop any ongoing speech
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        del engine
    except Exception as e:
        print(f"TTS Error: {e}")


def get_result(var):
           #searches for var in proverb_dict and returns a result
           if var in proverb_dict:
              for key, value in proverb_dict.items():
                  if var == key:
                        bot_entry.delete(0, tk.END)
                        bot_entry.insert(0, value)
                        result= key + " " + value
                        return result 
           else:
                  bot_entry.delete(0, tk.END)
                  bot_entry.insert(0, " ")
                  result="Sorry, couldn't complete the proverb, Goodbye!"
           return result
    

def get_proverb():
           #get current value of entry box
           var = user_entry.get()
           
           #call function get_result that returns the proverb
           proverb=get_result(var)
           
           #displays proverb in the proverb_label
           proverb_label.config(text=proverb) 
           print(f"Speaking: {proverb}")
           
           # Use threading to prevent GUI blocking
           tts_thread = threading.Thread(target=speak_text, args=(proverb,))
           tts_thread.daemon = True  # Dies when main thread dies
           tts_thread.start()
           
                            
           
       
# Add frame for label for title
title_frame = Frame(master=root, width = 800, height=60, bg='grey')
title_frame.grid(row=0, column=0, columnspan=5, sticky="ew")
title_frame.grid_propagate(False)

#Add frame for chatbot labels and entry boxes
bot_frame = Frame(master=root, width=800, height=400, bg='light goldenrod')
bot_frame.grid(row=4, column=0, columnspan=5, sticky="ew")

       
# Add frame for button for reset function
reset_frame = Frame(master=root, width = 800, height=60, bg='grey')
reset_frame.grid(row=5, column=0, columnspan=5, sticky="ew")


#Add entry box for User input
user_entry = tk.Entry(bot_frame, width=80, font=("Times New Roman", 12))
user_entry.insert(0, "Enter first three words of a proverb, chatbot will complete it.")
user_entry.place(relx=0.15, rely=0.02, anchor="nw", width=600, height=40)

#Add entry box for Chatbot entry
bot_entry = tk.Entry(bot_frame, width=80, font=("Times New Roman", 12))
bot_entry.place(relx=0.15, rely=0.27, anchor="nw", width=600, height=40)

#Add label for title
title_label=Label(master=title_frame, text="Proverbial Chatbot", font=("Times New Roman", 20, "bold"), bg='grey')
title_label.place(relx=0.5, rely=0.5, anchor="center")

#Add label for User
user_label=Label(master=bot_frame, text="User", font=("Times New Roman", 20, "bold"), bg='white')
user_label.place(relx=0.02, rely=0.02, anchor="nw")

#Add label for Chatbot
bot_label=Label(master=bot_frame, text="Chatbot", font=("Times New Roman", 20, "bold"), bg='white')
bot_label.place(relx=0.0, rely=0.27, anchor="nw")

#Add label for resulting proverb
proverb_label=Label(master=bot_frame, text=" ", font=("Times New Roman", 20, "bold"), bg='white')
proverb_label.place(relx=0.50, rely=0.60, width=700, anchor="center")



#Configure root grid to center the frame
root.grid_columnconfigure(0, weight=1)

#Add button so that when clicked, executes function get_proverb()
btn1 = tk.Button(master=bot_frame, text="GET PROVERB", command=get_proverb)
btn1.place(relx=0.5, rely=1.0, width=100, height=30, anchor="s")

#Add button so that when clicked, executes function reset()
btn2 = tk.Button(master=reset_frame, text="Reset", bg="RosyBrown2", command=reset)
btn2.place(relx=0.5, rely=0.5, width=100, height=30, anchor="s")


#Run the application
root.mainloop()