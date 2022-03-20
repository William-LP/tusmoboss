from tkinter import *
from tkinter import ttk
from data_manipulation import *


stats = {}  
data = load_data('data.txt')
if not stats :
    stats = load_stats(data)
    

# Main windows
root = Tk()
root.resizable(False, False)
root.title("TUSMO BOSS")

# Word / letters to work on
word_box = Text(root, height=5,width=50, font=("Helvetica", 16))
size_box = Text(root, height=5, width=5)

# Call function 
red_button = Button(root,background="red",padx=50, pady=50,text="valider lettre rouges",foreground="white")
yellow_button = Button(root,background="yellow",padx=50, pady=50,text="valider lettre jaunes",foreground="black")
delete_button = Button(root,background="grey",padx=50, pady=50,text="supprimer des lettres",foreground="white")

word_size_button = Button(root,background="blue",padx=15, pady=15,text="Filtrer nombre lettres",foreground="white")
reset_button = Button(root,background="green",padx=15, pady=15,text="reset",foreground="white")

# List words in data
listbox = Listbox(root)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = BOTH)
listbox.config(yscrollcommand = scrollbar.set)
for values in data[:100]:
    listbox.insert(END, values)
scrollbar.config(command = listbox.yview)

# Render elements
word_box.pack(side=TOP)
listbox.pack(side = LEFT, fill = BOTH)
red_button.pack(side=LEFT)
yellow_button.pack(side=LEFT)
delete_button.pack(side=LEFT)
reset_button.pack(side=RIGHT)
word_size_button.pack(side=RIGHT)
size_box.pack(side=RIGHT)   

root.mainloop()