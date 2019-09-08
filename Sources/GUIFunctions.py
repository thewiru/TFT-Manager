from tkinter import *
import Default_Champion_List as DCL
import MainFunctions as MF
from PIL import Image
from PIL import ImageTk
import math

images = []

def update_text(listbox):
  listbox.delete(0, END)
  get_list(listbox)

def get_list(listbox):
  if DCL.is_champ:
    for item in DCL.champion_list:
      s = "  "
      s+=item.name
      for dot in range (24 - len(item.name)):
        s+='.'
      s+=str(item.appeared)
      listbox.insert(END, s)
  else:
    for trait in DCL.trait_list:
      s = "  "
      s+=trait[0]
      for dot in range (24 - len(trait[0])):
        s+='.'
      s+=str(trait[1])
      listbox.insert(END, s)

def change_context(button, listbox):
  DCL.is_champ= not DCL.is_champ
  button.config(text = 'Traits' if DCL.is_champ else "Champions")
  MF.refresh(listbox)

def are_you_sure(listbox):
  popup = Toplevel()
  popup.title('AYS?')
  popup.geometry("200x80+1050+350")
  popup.resizable(False, False)
  label1 = Label(popup, text= "Are you sure you want to reset?")
  cancel_button = Button(popup, text="Cancel", command= lambda: popup.destroy(), width=5)
  reset_ok = Button(popup, text= "Reset", command= lambda: [MF.reset(listbox), popup.destroy()], width=5)
  label1.grid(row=0, column=0, columnspan= 5, padx=(12,0), pady=(7,5))
  cancel_button.grid(row=2, column=1, padx=(12,6), pady=(5,5))
  reset_ok.grid(row=2, column=3, padx=(12,0), pady=(5,5))
  popup.grab_set()
  popup.mainloop()


cost_options = ("#", 1, 2, 3, 4, 5)


  
