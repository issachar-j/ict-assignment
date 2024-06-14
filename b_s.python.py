# Algorithm implementation
# Our team have chosen binary search

import tkinter as tk
from tkinter import messagebox
from tkinter import *
import customtkinter

def binary_search(arr, target):
   low = 0
   high = len(arr) - 1
   while low <= high:
       mid = (low + high) // 2
       if arr[mid] == target:
           return mid
       elif arr[mid] < target:
           low = mid + 1
       else:
           high = mid - 1
   return -1


def search():
   try:
       target = int(entry_target.get())
       numbers = list(map(int, entry_numbers.get().split()))
       numbers.sort()
       index = binary_search(numbers, target)
       if index != -1:
           sorted_d.configure(text=f"Sorted list : {", ".join(list(map(str, numbers)))}")
           result_label.configure(text=f"Target found at index {index} of the sorted list.", text_color="green")
       else:
           result_label.configure(text="Target not found.", text_color="red")
   except ValueError:
       messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")


# GUI
root = customtkinter.CTk()
root.title("Flood-Binary Search Algorithm")
customtkinter.set_appearance_mode("dark")
root.geometry("600x350")
root.resizable(False, False)



label_numbers = customtkinter.CTkLabel(master=root, text="Enter sorted numbers (separated by space):", font=('Helvetica', 14))
label_numbers.pack(padx=10, pady=10, anchor=tk.W)


entry_numbers = customtkinter.CTkEntry(master=root, placeholder_text="Enter data here...", width=250, height=25, font=('Helvetica', 12))
entry_numbers.pack(padx=10, pady=10, anchor=tk.W)

label_target = customtkinter.CTkLabel(master=root, text="Enter target number:", font=('Helvetica', 14))
label_target.pack(padx=10, pady=10, anchor=tk.W)


entry_target = customtkinter.CTkEntry(master=root, placeholder_text="Find...", width=70, height=25, font=('Helvetica', 12))
entry_target.pack(padx=10, pady=10, anchor=tk.W)


sorted_d = customtkinter.CTkLabel(master=root, text="Sorted list:", font=('Helvetica', 15))
sorted_d.pack(padx=10, pady=10, anchor=tk.W)


search_button = customtkinter.CTkButton(master=root, text="Search", command=search, font=('Helvetica', 14))
search_button.pack(padx=10, pady=10, anchor=tk.CENTER)


result_label = customtkinter.CTkLabel(master=root, text="", font=('Helvetica', 14))
result_label.pack(padx=10, pady=10, anchor=tk.CENTER)


root.mainloop()