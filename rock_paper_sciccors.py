import random

rock = "rock"
paper = "paper"
sciccors = "sciccors"
#i dont gotta do quatations now

bot_choices = [rock , paper , sciccors]
bots_pick = random.choice(bot_choices)
#bot picking
human_pick = rock
#change code above for your pick ^

rock_weak = paper
paper_weak = sciccors
sciccors_weak = rock
#honestly this was part of a different idea but i ended up scraping it(i wont remove it)
human_win = False
#win condition

if human_pick == paper :
    if bots_pick != sciccors:
        human_win = True
elif human_pick == rock :
     if bots_pick != paper :
       human_win = True
elif human_pick == sciccors :
     if bots_pick != rock :
        human_win = True
elif human_pick == bots_pick :
    human_win = "tie"
#elif right above this is useless and will never work but i dont wanna mess much up so im leaving it
# (turns out this part actually but another part did)
else :
    human_win = False

if bots_pick == human_pick :
    human_win = "Tie"
# checks for tie seperate from the main system because this is fucking stupid(im stupid)

hwin_speech = f"the human has won with {human_pick}"
bwin_speech = f"the bot has won with {bots_pick}"


print("----------------------------------------------------")
print("check to see bot and human choices correspond with winner")
print("----------------------------------------------------")
print(human_pick + bots_pick)
print("----------------------------------------------------")
print("additional checks because something is f-ed")
print("----------------------------------------------------")
print("----------------------------------------------------")
print(f"the human win var has {human_win} stored in it")
print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
print("██████╗░███████╗░██████╗██╗░░░██╗██╗░░░░░████████╗░██████╗")
print("██╔══██╗██╔════╝██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔════╝")
print("██████╔╝█████╗░░╚█████╗░██║░░░██║██║░░░░░░░░██║░░░╚█████╗░")
print("██╔══██╗██╔══╝░░░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░░╚═══██╗")
print("██║░░██║███████╗██████╔╝╚██████╔╝███████╗░░░██║░░░██████╔╝")
print("╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═════╝░")

print(":")

if human_win == True :
    print(hwin_speech)
elif human_win == "Tie" :
    print(f"it was a tie both bot and human picked {human_pick}")
else :
    print(bwin_speech)


