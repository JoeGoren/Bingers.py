#import
import tkinter as tk
import tkinter.font as tkFont
import random
from stringprep import b1_set

#innitialise
root = tk.Tk()
rootsize="456x525"
root.geometry(rootsize+"+0+0")
root.title("TF2 Bingo")
gridsize = 5
id=1
root.attributes("-topmost", True)
root.overrideredirect(True)
#var
bingers = ["Be an MVP at the end of a round",
           "Dominate another player",
           "Die to a random crit",
           "Win without the opposition capping any points",
           "Get votekicked",
           "Get backstabbed by a kunai sweat",
           "Survive a fight on less than 5 HP",
           "Get accused of cheating",
           "Get an achievement",
           "End a round in a stalemate",
           "Win a round without dying",
           "Survive humiliation time on the loosing team",
           "Get a taunt kill",
           "Find a T-poser",
           "Someone speaks in voice chat",
           "Doctor Sex is in the lobby",
           "Get gifted a sandvich",
           "Someone says a slur",
           "Get a weapon / case drop",
           "Kill someone who's in discord VC",
           "Get autobalanced",
           "Get another player to killbind after you do",
           "Get sent to Brazil",
           "Go to Upward",
           "Go to Dustbowl",
           "Actually manage to cap on CTF",
           "Partner taunt with the opposite team",
           "Get a 5+:1 K:D (assists don't count)",
           "Kill 3 enemies as Scout in one life, only using the stock bat",
           "Steal a health pack from a burning teamate as Scout",
           "Die to a mini sentry as Scout",
           "Airshot an enemy as Soldier",
           "Use a banner twice in one life",
           "Destroy an Engie nest as Soldier",
           "Destroy a sentry as Pyro",
           "Kill using an airblast deflection",
           "Get an environmental kill as Pyro",
           "Get oneshot as Heavy",
           "Play shotgun Heavy for a round (no minigun allowed)",
           "Recreate Meet the Medic (get ubered as Heavy)",
           "Place a lvl 3 sentry outside the opposition's spawn doors",
           "Get 10 kills on one sentry",
           "win as Engineer without placing a single building",
           "Uber a Spy",
           "Play battle Medic for a round (no mediguns)",
           "Watch a teammate die to afterburn that you could of healed",
           "Have your heal patient kill another Medic and their patient",
           "Get 3 kills with the SMG in a single life",
           "Headshot another sniper",
           "Extingish a teammate with jarate",
           "Get a stock revolver kill on a Heavy",
           "Play Gunspy (no stabbing)",
           "Telefrag another player",
           "Kill and die to another player at the same time",
           "Stop an enemy from a winning cap",
           "Dodge a Sniper by standing still",
           "Someone else joins VC"
           ]
font  = tk.font.Font(family="small fonts", size=8, weight="bold")
rerollflag = False
pickfrom = 27
rerolls = 1
#def
def sort(x):
    seed = random.random()
    return seed

def gen_seed():
    global bingers, rerollflag, rerolls
    rerollflag = False
    rerolls = 1
    bingers = sorted(bingers, key=sort)
    for i in range(1,26):
        globals()["buttons"+str(i)].BTN["text"] = bingers[i-1]
        globals()["buttons" + str(i)].BTN["bg"] = "lightgrey"
        globals()["buttons" + str(i)].BTN["state"] = "normal"
    globals()["buttons"+"13"].BTN["text"] = "Go to 2Fort (free space)"
    globals()["buttons" + "13"].BTN["bg"] = "#548090"
    globals()["buttons" + "13"].BTN["state"] = "disabled"

def minmax():
    global rootsize
    if rootsize != "90x85":
        rootsize = "90x85"
        root.geometry(rootsize)
        root.wm_attributes("-alpha", 0.4)
        minmaxBTN["bg"] = "black"
        minmaxBTN["fg"] = "white"
        minmaxBTN["text"] = "Open board"

    else:
        rootsize = "456x525"
        root.geometry(rootsize)
        root.wm_attributes("-alpha", 1)
        minmaxBTN["bg"] = "lightgrey"
        minmaxBTN["text"] = "Minimise"
        minmaxBTN["fg"] = "black"

def close_window():
    root.destroy()

def reroll():
    global rerollflag, rerolls
    if rerollflag == False and rerolls > 0:
        rerollflag = True
        for i in range(1,26):
            if globals()["buttons"+str(i)].BTN["bg"] == "lightgrey":
                globals()["buttons"+str(i)].BTN["bg"] = "#a8574a"
            else:
                globals()["buttons"+str(i)].BTN["state"] = "disabled"
    else:
        rerollflag = False
        for i in range(1,26):
            if globals()["buttons"+str(i)].BTN["bg"] == "#a8574a":
                globals()["buttons"+str(i)].BTN["bg"] = "lightgrey"
            else:
                globals()["buttons"+str(i)].BTN["state"] = "normal"
                globals()["buttons" + "13"].BTN["state"] = "disabled"

#format
genseedBTN = tk.Button(root, text="Generate Seed", command=gen_seed, font=font, bg="lightgray", height=6, width=22)
genseedBTN.grid(row=0, column=1, columnspan=2, sticky=tk.W)
minmaxBTN = tk.Button(root, text="Minimise", command=minmax, font=font, bg="lightgrey", height=6, width=10, wraplength=60)
minmaxBTN.grid(row=0, column=0, columnspan=1, sticky=tk.W)
closeBTN = tk.Button(root, text="Close Tab", command=close_window, font=font, bg="lightgray", height=6, width=10)
closeBTN.grid(row=0, column=4, columnspan=1, sticky=tk.W)
rerollBTN = tk.Button(root, text=f"Reroll: {rerolls}", command=reroll, font=font, bg="lightgray", height=6, width=10)
rerollBTN.grid(row=0, column=3, columnspan=1, sticky=tk.W)

class bingersBTN:
    def __init__(self, row, column):
        self.BTN = tk.Button(text="", font=font, command=self.toggle, height=6, width=10, wraplength=85, bg="lightgrey", fg="black")
        self.BTN.grid(row=row, column=column, sticky=tk.NSEW)

    def toggle(self):
        global bingers, rerollflag, pickfrom, rerolls
        if rerollflag == True and self.BTN["bg"] == "#a8574a":
            self.BTN["text"] = bingers[pickfrom]
            pickfrom+=1
            rerollflag = False
            rerolls-=1
            rerollBTN['text'] = f"Rerolls: {rerolls}"
            if rerolls == 0:
                rerollBTN['state'] = "disabled"
            else:
                rerollBTN['state'] = "normal"
            for i in range(1,26):
                if  globals()["buttons"+str(i)].BTN["bg"] == "#a8574a":
                    globals()["buttons" + str(i)].BTN["bg"] = "lightgrey"
                else:
                    globals()["buttons" + str(i)].BTN["state"] = "normal"
                    globals()["buttons" + "13"].BTN["state"] = "disabled"
        elif rerollflag == False:
            if self.BTN["bg"] == "#548090":
                if rerolls > 0:
                    self.BTN["bg"] = "lightgrey"
                    rerolls-=1
                    rerollBTN['text'] = f"Rerolls: {rerolls}"
                    if rerolls == 0:
                        rerollBTN['state'] = "disabled"
            else:
                self.BTN["bg"] = "#548090"
                rerolls += 1
                rerollBTN['state'] = "normal"
                rerollBTN['text'] = f"Rerolls: {rerolls}"

for row in range(0,gridsize):
    for column in range(0, gridsize):
        globals()["buttons"+str(id)] = bingersBTN(row+1, column)
        id+=1
gen_seed()

#mainloop
root.mainloop()
