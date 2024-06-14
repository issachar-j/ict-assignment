# word counter

import tkinter as tk
from tkinter import messagebox
from tkinter import *
import customtkinter
import string

def count_words():
    text = text_entry.get("1.0",  tk.END)
    
    par_test = text.split("\n")
    par = list(map(str.strip, par_test))
    par_count = len(par)
    for x in range(par_count) :
        try :
            par.remove('')
        except :
            pass

    sen_try = "".join(par)
    sen = sen_try.strip().split('.')
    for x in range(par_count) :
        try :
            sen.remove('')
        except :
            pass

    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    word_count = len(words)

    char_test = ''.join(par).split()
    char = ''.join(char_test)

    result_label.configure(text=f"Word Count: {word_count}")
    result_label_p.configure(text=f"paragraph Count: {len(par)}")
    result_label_s.configure(text=f"sentence Count: {len(sen)}")
    result_label_c.configure(text=f"character Count (with no space): {len(char)}")

root = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
root.resizable(False, False)
root.title("Word Counter")

text_entry =  tk.Text(master=root, wrap=tk.WORD, height=10, width=50)
text_entry.pack(padx=10, pady=10)

count_button =  customtkinter.CTkButton(master=root, text="Count", command=count_words)
count_button.pack(pady=5)

result_label_p =  customtkinter.CTkLabel(master=root, text="paragraph Count: 0", font=('Helvetica', 14))
result_label_p.pack(pady=5, padx=10, anchor=tk.W)
result_label_s =  customtkinter.CTkLabel(master=root, text="sentence Count: 0", font=('Helvetica', 14))
result_label_s.pack(pady=5, padx=10, anchor=tk.W)
result_label =  customtkinter.CTkLabel(master=root, text="Word Count: 0", font=('Helvetica', 14))
result_label.pack(pady=5, padx=10, anchor=tk.W)
result_label_c =  customtkinter.CTkLabel(master=root, text="character Count (with no space): 0", font=('Helvetica', 14))
result_label_c.pack(pady=10, padx=10, anchor=tk.W)

root.mainloop()