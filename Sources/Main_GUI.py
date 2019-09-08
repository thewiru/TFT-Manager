from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import os
import math
import MainFunctions as MF
import Default_Champion_List as DCF
import GUIFunctions as GF


root = Tk()
root.title("TFT Manager v1.1 by Sky Sumisu")
root['bg'] = "#353C51"
root.iconbitmap(os.getcwd()+'\\Images\\icon.ico')
root.geometry("690x750+800+30")
root.resizable(False, False)



fr = Frame(root, height=34)
fr['bg'] = "#353C51"
fr.grid(row=0, column=0, columnspan = 2, sticky=N, pady=(20,0), padx=(20,10))
fr2 = Frame(root, height=34)
fr2.grid(row=0, column=2, columnspan = 2, sticky=N, pady=(20,0), padx=(40,10))
fr3 = Frame(root)
fr3['bg'] = "#353C51"
fr3.grid(row=1, column=0, columnspan = 5, sticky= N+E+W+S)
fr4 = Frame(fr3)
fr4['bg'] = "#353C51"
fr4.grid(row=0, column= 0, sticky = N+E+W+S)

fr_cost_1 = Frame(root, height=34)
fr_cost_2 = Frame(root, height=34)
fr_cost_3 = Frame(root, height=34)
fr_cost_4 = Frame(root, height=34)
fr_cost_5 = Frame(root, height=34)

frame_list = [fr, fr_cost_1, fr_cost_2, fr_cost_3, fr_cost_4, fr_cost_5]

def remove_frames():
  for frame in frame_list:
    frame.grid_remove()

cost_group = StringVar(root)
cost_group.set(GF.cost_options[0])
cost_menu = ttk.Combobox(fr4, values=GF.cost_options)
cost_menu.set(cost_group.get())
cost_menu.grid(row=0, column =0, pady=(30,10), padx=(40,30))

text_area = Listbox(fr2, width = 28, height= 34, state = 'normal')
text_area.grid(row=0, column=0, rowspan=20)
MF.refresh(text_area)

x=0
for champ in DCF.champion_list:

  GF.images.append(ImageTk.PhotoImage(Image.open(champ.image).resize((59,59)), Image.ANTIALIAS))

  b = Button(fr, image = GF.images[-1], command= lambda x=champ: MF.increment(x, text_area), highlightthickness = 0, bd = 0)
  b.grid(row=math.floor(x/5), column=x%5)
  x+=1
fr.grid_remove()
for frame in frame_list:
  i=0
  x=0
  if frame == fr:
    continue
  for champ in DCF.champion_list:
    if champ.cost == frame_list.index(frame):
      b = Button(frame, image = GF.images[i], command= lambda x=champ: MF.increment(x, text_area), highlightthickness = 0, bd = 0)
      b.grid(row=math.floor(x/5), column=x%5)
      x+=1
    i+=1
  frame.grid(row=0, column=0, columnspan = 2, sticky=N, pady=(20,0), padx=(20,10))
  frame['bg'] = "#353C51"
  frame.grid_remove()
fr.grid()


MF.refresh(text_area)

sb = Scrollbar(fr2)
sb.grid(column=1, row=0, sticky=N+S, rowspan=25)
text_area.config(font = ("Courier New", 12), yscrollcommand = sb.set)
sb.config(command=text_area.yview)

search_by_cost = Button(fr4, text = "Filter by cost", command = 
  lambda : [remove_frames(), frame_list[int(cost_menu.get())].grid()]
  if cost_menu.get() is not "#" else [remove_frames(), fr.grid()])
search_by_cost.grid(row=0, column = 1, pady=(30,10), padx=(0,40))

undo_button = Button(fr3, text = "Undo", command = lambda: MF.undo(text_area), width=10, height=2)
undo_button.grid(row=0, column=2, columnspan=1, pady=(20,10), padx=(0,10))

reset_button = Button(fr3, text = "Reset", command = lambda: GF.are_you_sure(text_area), width=10, height=2)
reset_button.grid(row=0, column=1, columnspan=1, pady=(20,10), padx=(56,10))

context_changer = Button(fr3, text = "Traits", command = lambda: GF.change_context(context_changer, text_area), width=10, height=2)
context_changer.grid(row=0, column=3, columnspan=1, pady=(20,10), padx=(0,10))

root.mainloop()
