import tkinter as tk
from tkinter import messagebox
from tkinter import *
import customtkinter
import string

def count_words():
    text = text_entry.get("1.0",  tk.END)
    
    #count paragraph
    par_test = text.split("\n")
    par = list(map(str.strip, par_test))
    par_count = len(par)
    for x in range(par_count) :
        try :
            par.remove('')
        except :
            pass

    #count sentence
    sen_try = "".join(par)
    sen = sen_try.strip().split('.')
    for x in range(par_count) :
        try :
            sen.remove('')
        except :
            pass

    #count word
    # Remove punctuation from the text first
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    word_count = len(words)

    #count character
    char_test = ''.join(par).split()
    char = ''.join(char_test)

    result_label.configure(text=f"Word Count: {word_count}")
    result_label_p.configure(text=f"paragraph Count: {len(par)}")
    result_label_s.configure(text=f"sentence Count: {len(sen)}")
    result_label_c.configure(text=f"character Count (with no space): {len(char)}")

# Create the main application window
root = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
root.resizable(False, False)
root.title("Word Counter")

# Create a master=root for better layout
# Create a text widget for text input
text_entry =  tk.Text(master=root, wrap=tk.WORD, height=10, width=50)
text_entry.pack(padx=10, pady=10)

# Create a button to count words
count_button =  customtkinter.CTkButton(master=root, text="Count", command=count_words)
count_button.pack(pady=5)

# Create a label to display the result
result_label_p =  customtkinter.CTkLabel(master=root, text="paragraph Count: 0", font=('Helvetica', 14))
result_label_p.pack(pady=5)
result_label_s =  customtkinter.CTkLabel(master=root, text="sentence Count: 0", font=('Helvetica', 14))
result_label_s.pack(pady=5)
result_label =  customtkinter.CTkLabel(master=root, text="Word Count: 0", font=('Helvetica', 14))
result_label.pack(pady=5)
result_label_c =  customtkinter.CTkLabel(master=root, text="character Count (with no space): 0", font=('Helvetica', 14))
result_label_c.pack(pady=5)

# Run the application
root.mainloop()
