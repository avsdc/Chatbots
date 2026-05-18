# Description - Proverbial Chatbot
App uses Python, Tkinter, pyttsx3 and threading. 
User has to enter the first three words of a well-known proverb 
in the User entry box, and upon clicking of the button 'Get Proverb' remaining words of the proverb are entered 
in the chatbot entry box if found. The complete proverb is then displayed in the label. Text to speech conversion 
also occurs. First, when the first three words of the proverb are entered in the User entry box, text is converted to
speech, next when the remaining words of the proverb are entered in the chatbot entry box this text is also converted
to speech. Finally, the completed proverb that appears in the label is also coverted to speech. After the first three
words of the proverb are entered in the User entry box, if the reamining words are not found, a message appears in the 
label, that the proverb couldn't be completed. Reset button should be then clicked, and the original message to enter 
three words in the User entry box will reappear. The Chatbot entry box, and label will be blank. App also uses threading
to create a separate thread for text to speech, so that GUI is not blocked.

## How to use:
Enter the command python app.py at your project directory prompt. In the Tkinter GUI that appears, delete the placeholder
message that is displayed at first, and then enter the first three words of a famous proverb. Click the 'Get Proverb' button. 
The rest of the proverb appears in the Chatbot entry box, and complete proverb in the label if found. Other proverbs can also
be tried, by deleting the three words of the previously entered proverb in the User entry box, entering three words of a new
proverb, and pressing the 'Get Proverb' button. Again, the remaining words of the proverb will appear in the Chatbot entry box, 
and the complete proverb in the label. Upon entering the first three words of a proverb that cannot be found by the app, a 
message will appear in the label, that the proverb couldn't be found. Entering the reset button, will clear the chatbot entry
box and label, and the original message will appear in the User entry box.
