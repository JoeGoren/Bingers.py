#import
import tkinter as tk
import tkinter.font as tkFont
import random

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
bingers = ["Get a random crit kill",
           "Be an MVP at the end of a round",
           "Get revenge on a player",
           "Die to a random crit",
           "Win without the opposition capping any points",
           "Get backstabbed by a kunai Spy",
           "Get to 1hp",
           "Get accused of cheating",
           "Kill an enemy with afterburn",
           "Get an achievement",
           "End a round in a stalemate",
           "Get 5 kills without dying",
           "Survive humiliation time on the loosing team",
           "Get a taunt kill witht the pootis pow",
           "Find a T-poser",
           "Someone talks in voice chat",
           "Someone plays music in voice chat",
           "Doctor Sex or Nate H is in the lobby",
           "Get gifted a sandvich",
           "Someone says a slur",
           "Get a weapon / case drop",
           "Kill someone who's in the discord VC",
           "Get autobalanced",
           "Get another player to killbind after you do",
           "Go to Upward",
           "Go to Dustbowl",
           "Cap a point",
           "Partner taunt with the opposite team",
           "Get a 2+:1 K:D at the end of a round",
           "Get a kill with a mini-crit",
           "Kill a demonight",
           "'Befriend' someone in Pyroland",
           "Get a pickaxe kamikaze kill on soldier",
           "Touch grass (in game)",
           "Get huntsman taunt kill",
           "Someone complains in discord VC",
           "Kill 3 enemies as Scout in one life, only using melees",
           "Die to a sentry as Scout",
           "Kill a scout, only using the pistol (assists count)",
           "Airshot an enemy as Soldier",
           "Use a banner twice in one life",
           "Destroy a dispenser as Soldier",
           "Kill a Blu Soldier as a Red Demo, or vice versa (assists count)",
           "Destroy a sentry as Pyro",
           "Kill using an airblast deflection",
           "Get an environmental kill as Pyro",
           "Kill a Pyro as Demoknight",
           "Get two kills with single mouse input",
           "Collide with a map's invisible ceiling",
           "Get oneshot as Heavy",
           "Get 5 kills as shotgun Heavy (no minigun)",
           "Recreate Meet the Medic (get ubered as Heavy)",
           "Place a lvl 3 sentry outside the opposition's spawn doors",
           "Get 5 kills on one sentry",
           "Kill a Spy with a wrench",
           "Kill a sentry with a sentry",
           "Uber a Sniper",
           "Get 3 kills as battle Medic (no healing)",
           "Die of afterburn",
           "Have your heal patient kill another Medic and their patient",
           "Heal an enemy Spy",
           "Get 3 kills with the SMG in a single life",
           "Headshot another sniper",
           "Extingish a teammate with jarate",
           "Pin a ragdoll to the wall with the huntsman",
           "Get a stock revolver kill on a Heavy",
           "Get 5 kills as Gunspy (no stabbing)",
           "Telefrag a player",
           "Die to a dead player",
           "Stop an enemy from a winning cap",
           "Tank a headshot as a class with >150 health",
           "Someone else joins VC"
           ]
font  = tkFont.Font(family="small fonts", size=8, weight="bold")
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
    rerollBTN['text'] = f"Rerolls: {rerolls}"
    rerollBTN['state'] = "normal"
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
    if rootsize != "45x43":
        rootsize = "45x43"
        root.geometry(rootsize)
        root.wm_attributes("-alpha", 0.4)
        minmaxBTN["bg"] = "black"
        minmaxBTN["fg"] = "white"
        minmaxBTN["text"] = "Open Board"
        minmaxBTN["height"], minmaxBTN["width"] = 3, 5

    else:
        rootsize = "456x525"
        root.geometry(rootsize)
        root.wm_attributes("-alpha", 1)
        minmaxBTN["bg"] = "lightgrey"
        minmaxBTN["text"] = "Minimise"
        minmaxBTN["fg"] = "black"
        minmaxBTN["height"], minmaxBTN["width"] = 6, 10
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
minmaxBTN.grid(row=0, column=0, columnspan=1, sticky=tk.NW)
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
