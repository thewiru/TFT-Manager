from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
import math
import MainFunctions as MF
import Default_Champion_List as DCF
import GUIFunctions as GF


root = Tk()
root.title("TFT Manager v1.0 by Sky Sumisu")
root['bg'] = "#353C51"
root.iconbitmap(os.getcwd()+'\\Images\\icon.ico')
root.geometry("690x750+800+30")
root.resizable(False, False)

images = []
buttons = []

fr = Frame(root)
fr['bg'] = "#353C51"
fr.grid(row=0, column=0, sticky=N, pady=(20,0))
fr2 = Frame(root, height=34)
fr2.grid(row=0, column=1, sticky=N, pady=(20,0))
fr3 = Frame(root)
fr3['bg'] = "#353C51"
fr3.grid(row=1, column=0, columnspan=2, sticky= N+E+W+S)

text_area = Listbox(fr2, width = 28, height= 34, state = 'normal')
text_area.grid(row=0, column=0, rowspan=20)
MF.refresh(text_area)

x=0
for champ in DCF.champion_list:

  images.append(ImageTk.PhotoImage(Image.open(champ.image).resize((59,59)), Image.ANTIALIAS))

  b = Button(fr, image = images[-1], command= lambda x=champ: MF.increment(x, text_area), highlightthickness = 0, bd = 0)
  #b.config(height = 40, width= 40)
  buttons.append(b)
  b.grid(row=math.floor(x/5), column=x%5)
  x+=1

MF.refresh(text_area)

sb = Scrollbar(fr2)
sb.grid(column=1, row=0, sticky=N+S, rowspan=25)
text_area.config(font = ("Courier New", 12), yscrollcommand = sb.set)
sb.config(command=text_area.yview)

undo_button = Button(fr3, text = "Undo", command = lambda: MF.undo(text_area), width=10, height=2)
undo_button.grid(row=0, column=0, columnspan=1, pady=(20,10), padx=(75,75))

reset_button = Button(fr3, text = "Reset", command = lambda: GF.are_you_sure(text_area), width=10, height=2)
reset_button.grid(row=0, column=1, columnspan=1, pady=(20,10), padx=(75,75))

context_changer = Button(fr3, text = "Traits", command = lambda: GF.change_context(context_changer, text_area), width=10, height=2)
context_changer.grid(row=0, column=2, columnspan=1, pady=(20,10), padx=(75,75))

root.mainloop()
