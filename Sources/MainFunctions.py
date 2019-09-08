import Default_Champion_List as DCL
import GUIFunctions as GF


def refresh(listbox):
  DCL.champion_list = DCL.champion_dict.values()
  DCL.trait_list = DCL.trait_dict.items()
  DCL.champion_list= sorted(DCL.champion_list, key= lambda x: x.appeared, reverse=True)
  DCL.trait_list= sorted(DCL.trait_list, key= lambda x: x[1], reverse=True)
  GF.update_text(listbox)
  


def increment(champ, listbox):
  DCL.champion_dict[champ.name].appeared+=1
  for trait in DCL.champion_dict[champ.name].traits:
    DCL.trait_dict[trait]+=1
  DCL.champion_stack.append(champ)
  refresh(listbox)

def undo(listbox):
  if len(DCL.champion_stack) > 0:
   tmp = DCL.champion_stack.pop()
   DCL.champion_dict[tmp.name].appeared-=1
   for trait in DCL.champion_dict[tmp.name].traits:
     DCL.trait_dict[trait]-=1
  refresh(listbox)

def reset(listbox):
  
  for champ in DCL.champion_dict:
    DCL.champion_dict[champ].appeared=0
  for trait in DCL.trait_dict:
    DCL.trait_dict[trait]=0
  DCL.champion_stack = DCL.DEFAULT_CHAMPION_STACK

  refresh(listbox)



