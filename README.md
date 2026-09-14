#import
import tkinter as tk
import random
from stringprep import b1_set

#innitialise
root = tk.Tk()
root.geometry("530x621")
root.title("TF2 Bingo")
seed = ""
BTNheight = 6
BTNwidth = 12

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
           "Go to 2Fort",
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
           ]
NTRYseed = tk.StringVar(root)
SCLstep = tk.DoubleVar()
font  = ("fixedsys")
#7755024343407313
#def
def sort(x):
    global seed, bingers
    if str(NTRYseed.get()).isdigit() == True:
        seed = "0."+NTRYseed.get()
        print(seed)
    else:
        seed = random.random()
    return seed

def gen_seed():
    global bingers
    bingers = sorted(bingers, key=sort)
    b1["text"] = bingers[0]
    b2["text"] = bingers[1]
    b3["text"] = bingers[2]
    b4["text"] = bingers[3]
    b5["text"] = bingers[4]
    b6["text"] = bingers[5]
    b7["text"] = bingers[6]
    b8["text"] = bingers[7]
    b9["text"] = bingers[8]
    b10["text"] = bingers[9]
    b11["text"] = bingers[10]
    b12["text"] = bingers[11]
    b13["text"] = "Death by random crit (free space)"
    b14["text"] = bingers[13]
    b15["text"] = bingers[14]
    b16["text"] = bingers[15]
    b17["text"] = bingers[16]
    b18["text"] = bingers[17]
    b19["text"] = bingers[18]
    b20["text"] = bingers[19]
    b21["text"] = bingers[20]
    b22["text"] = bingers[21]
    b23["text"] = bingers[22]
    b24["text"] = bingers[23]
    b25["text"] = bingers[24]




    
def copy_seed():
    global seed
    root.clipboard_clear()
    try:
        root.clipboard_append(int(seed*10000000000000000))
    except:
        pass

def toggle1():
    if b1["bg"]=="limegreen":
        b1["bg"] = "lightgrey"
    else:
        b1["bg"]="limegreen"
def toggle2():
    if b2["bg"]=="limegreen":
        b2["bg"] = "lightgrey"
    else:
        b2["bg"]="limegreen"
def toggle3():
    if b3["bg"]=="limegreen":
        b3["bg"] = "lightgrey"
    else:
        b3["bg"]="limegreen"
def toggle4():
    if b4["bg"]=="limegreen":
        b4["bg"] = "lightgrey"
    else:
        b4["bg"]="limegreen"
def toggle5():
    if b5["bg"]=="limegreen":
        b5["bg"] = "lightgrey"
    else:
        b5["bg"]="limegreen"
def toggle6():
    if b6["bg"]=="limegreen":
        b6["bg"] = "lightgrey"
    else:
        b6["bg"]="limegreen"
def toggle7():
    if b7["bg"]=="limegreen":
        b7["bg"] = "lightgrey"
    else:
        b7["bg"]="limegreen"
def toggle8():
    if b8["bg"]=="limegreen":
        b8["bg"] = "lightgrey"
    else:
        b8["bg"]="limegreen"
def toggle9():
    if b9["bg"]=="limegreen":
        b9["bg"] = "lightgrey"
    else:
        b9["bg"]="limegreen"
def toggle10():
    if b10["bg"]=="limegreen":
        b10["bg"] = "lightgrey"
    else:
        b10["bg"]="limegreen"
def toggle11():
    if b11["bg"]=="limegreen":
        b11["bg"] = "lightgrey"
    else:
        b11["bg"]="limegreen"
def toggle12():
    if b12["bg"]=="limegreen":
        b12["bg"] = "lightgrey"
    else:
        b12["bg"]="limegreen"
def toggle13():
    if b13["bg"]=="limegreen":
        b13["bg"] = "lightgrey"
    else:
        b13["bg"]="limegreen"
def toggle14():
    if b14["bg"]=="limegreen":
        b14["bg"] = "lightgrey"
    else:
        b14["bg"]="limegreen"
def toggle15():
    if b15["bg"]=="limegreen":
        b15["bg"] = "lightgrey"
    else:
        b15["bg"]="limegreen"
def toggle16():
    if b16["bg"]=="limegreen":
        b16["bg"] = "lightgrey"
    else:
        b16["bg"]="limegreen"
def toggle17():
    if b17["bg"]=="limegreen":
        b17["bg"] = "lightgrey"
    else:
        b17["bg"]="limegreen"
def toggle18():
    if b18["bg"]=="limegreen":
        b18["bg"] = "lightgrey"
    else:
        b18["bg"]="limegreen"
def toggle19():
    if b19["bg"]=="limegreen":
        b19["bg"] = "lightgrey"
    else:
        b19["bg"]="limegreen"
def toggle20():
    if b20["bg"]=="limegreen":
        b20["bg"] = "lightgrey"
    else:
        b20["bg"]="limegreen"
def toggle21():
    if b21["bg"]=="limegreen":
        b21["bg"] = "lightgrey"
    else:
        b21["bg"]="limegreen"
def toggle22():
    if b22["bg"]=="limegreen":
        b22["bg"] = "lightgrey"
    else:
        b22["bg"]="limegreen"
def toggle23():
    if b23["bg"]=="limegreen":
        b23["bg"] = "lightgrey"
    else:
        b23["bg"]="limegreen"
def toggle24():
    if b24["bg"]=="limegreen":
        b24["bg"] = "lightgrey"
    else:
        b24["bg"]="limegreen"
def toggle25():
    if b25["bg"]=="limegreen":
        b25["bg"] = "lightgrey"
    else:
        b25["bg"]="limegreen"

        
#format
genseedBTN = tk.Button(root, text="Generate Seed", command=gen_seed, font=font, width=25, height=7).grid(row=5, column=0, columnspan=2, sticky=tk.W)
addseedNTRY = tk.Entry(root, textvariable = NTRYseed).grid(row=5, column=4, sticky=tk.W)
copyseedBTN = tk.Button(root, text="Copy Seed", command=copy_seed, font=font, width=25, height=7).grid(row=5, column=2, columnspan=2)

b1=tk.Button(text="", font=font, command=toggle1, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b1.grid(row=0, column=0)
b2=tk.Button(text="", font=font, command=toggle2, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b2.grid(row=1, column=0)
b3=tk.Button(text="", font=font, command=toggle3, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b3.grid(row=2, column=0)
b4=tk.Button(text="", font=font, command=toggle4, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b4.grid(row=3, column=0)
b5=tk.Button(text="", font=font, command=toggle5, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b5.grid(row=4, column=0)
b6=tk.Button(text="", font=font, command=toggle6, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b6.grid(row=0, column=1)
b7=tk.Button(text="", font=font, command=toggle7, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b7.grid(row=1, column=1)
b8=tk.Button(text="", font=font, command=toggle8, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b8.grid(row=2, column=1)
b9=tk.Button(text="", font=font, command=toggle9, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b9.grid(row=3, column=1)
b10=tk.Button(text="", font=font, command=toggle10, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b10.grid(row=4, column=1)
b11=tk.Button(text="", font=font, command=toggle11, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b11.grid(row=0, column=2)
b12=tk.Button(text="", font=font, command=toggle12, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b12.grid(row=1, column=2)
b13=tk.Button(text="", font=font, command=toggle13, height=BTNheight, width=BTNwidth, wraplength=110, bg="limegreen", state=tk.DISABLED)
b13.grid(row=2, column=2)
b14=tk.Button(text="", font=font, command=toggle14, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b14.grid(row=3, column=2)
b15=tk.Button(text="", font=font, command=toggle15, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b15.grid(row=4, column=2)
b16=tk.Button(text="", font=font, command=toggle16, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b16.grid(row=0, column=3)
b17=tk.Button(text="", font=font, command=toggle17, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b17.grid(row=1, column=3)
b18=tk.Button(text="", font=font, command=toggle18, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b18.grid(row=2, column=3)
b19=tk.Button(text="", font=font, command=toggle19, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b19.grid(row=3, column=3)
b20=tk.Button(text="", font=font, command=toggle20, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b20.grid(row=4, column=3)
b21=tk.Button(text="", font=font, command=toggle21, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b21.grid(row=0, column=4, sticky=tk.W)
b22=tk.Button(text="", font=font, command=toggle22, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b22.grid(row=1, column=4, sticky=tk.W)
b23=tk.Button(text="", font=font, command=toggle23, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b23.grid(row=2, column=4, sticky=tk.W)
b24=tk.Button(text="", font=font, command=toggle24, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b24.grid(row=3, column=4, sticky=tk.W)
b25=tk.Button(text="", font=font, command=toggle25, height=BTNheight, width=BTNwidth, wraplength=110, bg="lightgrey")
b25.grid(row=4, column=4, sticky=tk.W)



#mainloop
root.mainloop()
