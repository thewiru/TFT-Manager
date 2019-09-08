from Champion import Champion

#Assassins
khazix = Champion("Kha'zix", 1, ["Void", "Assassin"])
pyke = Champion("Pyke", 2, ["Pirate", "Assassin"])
zed = Champion("Zed", 2, ["Ninja","Assassin"])
evelynn = Champion("Evelynn", 3, ["Demon", "Assassin"])
katarina = Champion("Katarina", 3, ["Imperial", "Assassin"])
rengar = Champion("Rengar", 3, ["Wild", "Assassin"])
akali = Champion("Akali", 4, ["Ninja", "Assassin"])

#Blademasters
fiora = Champion("Fiora", 1, ["Noble", "Blademaster"])
camille = Champion("Camille", 1, ["Hextech", "Blademaster"])
shen = Champion("Shen", 2, ["Ninja", "Blademaster"])
aatrox = Champion("Aatrox", 3, ["Demon", "Blademaster"])
gangplank = Champion("Gangplank", 3, ["Pirate", "Blademaster", "Gunslinger"])
draven = Champion("Draven", 4, ["Imperial", "Blademaster"])
yasuo = Champion("Yasuo", 5, ["Exile", "Blademaster"])

#Brawlers
warwick = Champion("Warwick", 1, ["Wild", "Brawler"])
blitzcrank = Champion("Blitzcrank", 2, ["Robot", "Brawler"])
reksai = Champion("Rek'sai", 2, ["Void", "Brawler"])
volibear = Champion("Volibear", 3, ["Glacial", "Brawler"])
vi = Champion("Vi", 3, ["Hextech", "Brawler"])
chogath = Champion("Cho'gath", 4, ["Void", "Brawler"])

#Elementalists
lissandra = Champion("Lissandra", 2, ["Glacial", "Elementalist"])
kennen = Champion("Kennen", 3, ["Ninja", "Elementalist", "Yordle"])
brand = Champion("Brand", 4, ["Demon", "Elementalist"])
anivia = Champion("Anivia", 4, ["Glacial", "Elementalist"])

#Guardians
braum = Champion("Braum", 2, ["Glacial", "Guardian"])
leona = Champion("Leona", 4, ["Noble", "Guardian"])
pantheon = Champion("Pantheon", 5, ["Dragon", "Guardian"])

#Gunslingers
graves = Champion("Graves", 1, ["Pirate", "Gunslinger"])
tristana = Champion("Tristana", 1, ["Yordle", "Gunslinger"])
lucian = Champion("Lucian", 2, ["Noble", "Gunslinger"])
jinx = Champion("Jinx", 4, ["Hextech", "Gunslinger"])
miss_fortune = ("Miss Fortune", 5, ["Pirate", "Gunslinger"])

#Knights
darius = Champion("Darius", 1, ["Imperial", "Knight"])
garen = Champion("Garen", 1, ["Noble", "Knight"])
mordekaiser = Champion("Mordekaiser", 1, ["Phantom", "Knight"])
poppy = Champion("Poppy", 3, ["Yordle", "Knight"])
sejuani = Champion("Sejuani", 4, ["Glacial", "Knight"])
kayle = Champion("Kayle", 5, ["Noble", "Knight"])

#Rangers
vayne = Champion("Vayne", 1, ["Noble", "Ranger"])
varus = Champion("Varus", 2, ["Demon", "Ranger"])
ashe = Champion("Ashe", 3, ["Glacial", "Ranger"])
kindred = Champion("Kindred", 4, ["Phantom", "Ranger"])

#Shapeshifters
elise = Champion("Elise", 1, ["Demon", "Shapeshifter"])
nidalee = Champion("Nidalee", 1, ["Wild", "Shapeshifter"])
jayce = Champion("Jayce", 2, ["Hextech", "Shapeshifter"])
shyvana = Champion("Shyvana", 3, ["Dragon", "Shapeshifter"])
gnar = Champion("Gnar", 4, ["Wild", "Yordle", "Shapeshifter"])
swain = Champion("Swain", 5, ["Demon", "Imperial", "Shapeshifter"])

#Sorcerers
kassadin = Champion("Kassadin", 1, ["Void", "Sorcerer"])
ahri = Champion("Ahri", 2, ["Wild", "Sorcerer"])
lulu = Champion("Lulu", 2, ["Yordle","Sorcerer"])
twisted_fate = Champion("Twisted Fate", 2, ["Pirate", "Sorcerer"])
morgana = Champion("Morgana", 3, ["Demon", "Sorcerer"])
veigar = Champion("Veigar", 3, ["Yordle", "Sorcerer"])
aurelion_sol = Champion("Aurelion Sol", 4, ["Dragon", "Sorcerer"])
karthus = Champion("Karthus", 5, ["Phantom", "Sorcerer"])

#Default dictionary of every champion in the game
DEFAULT_CHAMPION_DICT = {'Aatrox':aatrox, 'Ahri':ahri, 'Akali':akali,
 'Anivia':anivia, 'Ashe':ashe, 'Aurelion Sol':aurelion_sol, 
 'Blitzcrank':blitzcrank, 'Brand':brand, 'Braum':braum, 'Camille':camille, 
 'Cho\'gath':chogath, 'Darius':darius, 'Draven':draven, 'Elise':elise, 
 'Evelynn':evelynn, 'Fiora':fiora, 'Gangplank':gangplank, 'Garen':garen, 
 'Gnar':gnar, 'Graves':graves, 'Jayce':jayce, 'Jinx':jinx, 'Karthus':karthus,
  'Kassadin':kassadin, 'Katarina':katarina, 'Kayle':kayle, 'Kennen':kennen, 
  'Kha\'zix':khazix, 'Kindred':kindred, 'Leona':leona, 'Lissandra':lissandra, 
  'Lucian':lucian, 'Lulu':lulu, 'Mordekaiser':mordekaiser, 'Morgana':morgana, 
  'Nidalee':nidalee, 'Pantheon':pantheon, 'Poppy':poppy, 'Pyke':pyke, 
  'Rek\'sai':reksai, 'Rengar':rengar, 'Sejuani':sejuani, 'Shen':shen, 
  'Shyvana':shyvana, 'Swain':swain, 'Tristana':tristana, 'Twisted Fate':twisted_fate, 
  'Varus':varus, 'Vayne':vayne, 'Veigar':veigar, 'Vi':vi, 'Volibear':volibear, 
  'Warwick':warwick, 'Yasuo':yasuo, 'Zed':zed}

DEFAULT_TRAIT_DICT = {'Assassin': 0, 'Blademaster': 0, 'Brawler': 0,
'Elementalist': 0, 'Guardian': 0, 'Gunslinger': 0, 'Knight': 0,
'Ranger': 0, 'Shapeshifter': 0, 'Sorcerer': 0, 'Demon': 0, 'Dragon': 0,
'Exile': 0, 'Glacial': 0, 'Hextech': 0, 'Imperial': 0, 'Ninja': 0,
'Noble': 0, 'Phantom': 0, 'Pirate': 0, 'Robot': 0, 'Void': 0, 'Wild': 0,
'Yordle': 0}

DEFAULT_CHAMPION_STACK = []

champion_dict = {'Aatrox':aatrox, 'Ahri':ahri, 'Akali':akali,
 'Anivia':anivia, 'Ashe':ashe, 'Aurelion Sol':aurelion_sol, 
 'Blitzcrank':blitzcrank, 'Brand':brand, 'Braum':braum, 'Camille':camille, 
 'Cho\'gath':chogath, 'Darius':darius, 'Draven':draven, 'Elise':elise, 
 'Evelynn':evelynn, 'Fiora':fiora, 'Gangplank':gangplank, 'Garen':garen, 
 'Gnar':gnar, 'Graves':graves, 'Jayce':jayce, 'Jinx':jinx, 'Karthus':karthus,
  'Kassadin':kassadin, 'Katarina':katarina, 'Kayle':kayle, 'Kennen':kennen, 
  'Kha\'zix':khazix, 'Kindred':kindred, 'Leona':leona, 'Lissandra':lissandra, 
  'Lucian':lucian, 'Lulu':lulu, 'Mordekaiser':mordekaiser, 'Morgana':morgana, 
  'Nidalee':nidalee, 'Pantheon':pantheon, 'Poppy':poppy, 'Pyke':pyke, 
  'Rek\'sai':reksai, 'Rengar':rengar, 'Sejuani':sejuani, 'Shen':shen, 
  'Shyvana':shyvana, 'Swain':swain, 'Tristana':tristana, 'Twisted Fate':twisted_fate, 
  'Varus':varus, 'Vayne':vayne, 'Veigar':veigar, 'Vi':vi, 'Volibear':volibear, 
  'Warwick':warwick, 'Yasuo':yasuo, 'Zed':zed}
trait_dict = {'Assassin': 0, 'Blademaster': 0, 'Brawler': 0,
'Elementalist': 0, 'Guardian': 0, 'Gunslinger': 0, 'Knight': 0,
'Ranger': 0, 'Shapeshifter': 0, 'Sorcerer': 0, 'Demon': 0, 'Dragon': 0,
'Exile': 0, 'Glacial': 0, 'Hextech': 0, 'Imperial': 0, 'Ninja': 0,
'Noble': 0, 'Phantom': 0, 'Pirate': 0, 'Robot': 0, 'Void': 0, 'Wild': 0,
'Yordle': 0}
champion_stack = []
champion_list = []
trait_list = []

is_champ = True
