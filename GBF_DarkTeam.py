"""
Autor: Nexius74
Version: 1.0.0
Details: Usage of keyboard input to manipulate GBF. Cause im a lazy ass that don't wanna move his hand over mouse
Update: 06.03.2018
"""
import msvcrt
from colorama import Fore
import pywinauto
import sys, time, os
import pyautogui as pyat

DateTime = time.asctime()

# Button in fight
Attack_btn = "meshes\\buttons\\Attack_btn.PNG"
Next_btn = "meshes\\buttons\\Next_btn.PNG"
# OK Button cause semi-transparancy makes them different
Ok_btn = "meshes\\buttons\\Ok_btn.PNG"
Ok_btn_2 = "meshes\\buttons\\Ok_btn_2.PNG"
Ok_btn_3 = "meshes\\buttons\\Ok_quest_btn_3.PNG"
Ok_btn_4 = "meshes\\buttons\\Ok_btn_4.PNG"
# Cancel button
Cancel_btn = "meshes\\buttons\\Cancel_btn.PNG"
Cancel_btn_2 = "meshes\\buttons\\Cancel_btn_2.PNG"
# Retreat and resume button
Retreat_btn = "meshes\\buttons\\Retreat_btn.PNG"
Retreat_btn_2 = "meshes\\buttons\\Retreat_btn_2.PNG"
Resume_btn = "meshes\\buttons\\Resume_btn.PNG"
# Home button
Home_btn = "meshes\\buttons\\Home_btn.PNG"
Reload_btn = "meshes\\buttons\\Reload_btn.PNG"
Back_btn = "meshes\\buttons\\Back_btn.PNG"
Back_skill_btn = "meshes\\skills\\Back_skills.PNG"
# Submenu buttons
Party_btn = "meshes\\buttons\\Party_btn.PNG"
Upgrade_btn = "meshes\\buttons\\Upgrade_btn.PNG"
Weapon_btn = "meshes\\buttons\\Weapon_btn.PNG"
Character_btn = "meshes\\buttons\\Character_btn.PNG"
Summon_btn = "meshes\\buttons\\Summon_btn.PNG"
# Skill bar
Mc_skillbar = "meshes\\skills\\MC_skillbar.PNG"
# MC skill number
MC_skill_1 = "meshes\\skills\\mc_skills\\Skill_1.PNG"
MC_skill_2 = "meshes\\skills\\mc_skills\\Skill_2.PNG"
MC_skill_3 = "meshes\\skills\\mc_skills\\Skill_3.PNG"
MC_skill_4 = "meshes\\skills\\mc_skills\\Skill_4.PNG"

# Function
"""HotKey Function"""
def __kbfunc():
    x = msvcrt.kbhit()
    if x:
        ret = msvcrt.getch()
    else:
        ret = False
    return ret

def __focusterminal():
    # We instance the application that handle control over window
    # And we connect it to the running app
    # Instead of connect we can use start to launch an app
    app = pywinauto.application.Application().connect(title="C:\\Python\\python.exe")
    # .window_ search for the window with the same title. Same as .findbestmatch
    w_handle = app.window_(title="C:\\Python\\python.exe")
    # We minize the window that was found
    w_handle.Minimize()
    # And we restore it to it's precedent state but in the front of all program and active
    w_handle.Restore()
"""End HotKey Function"""


"""Menu Section"""
# Submenu caracter selection for skills. Work in progress
def __selectioncaracter():
    # Once enter this, keys are rebound to skill instead of attack, next, ok button
    print("\n 1.MC \n 2.DJeanne \n 3.Lyria \n 4.Vira \n 5.Sub_1 \n 6.Sub_2 \n")
    ask = input("Which caracter: ")
    if ask == "1":
        __detectMC()
    elif ask == "2":
        __detectMain1()
    elif ask == "3":
        __detectMain2()
    elif ask == "4":
        __detectMain3()
    elif ask == "5":
        __detectSub1()
    elif ask == "6":
        __detectSub2()

# Submenu to choose if we wanna go into party and which type (weapon,chara,summon)
def __partymenu():
    print("|INFO|" + DateTime + "|" + " Starting party menu selection ...")
    print("\n 1.Characters \n 2.Weapons \n 3.Summons \n")
    ask = input("Where do you want to go (choose a number): ")
    __home()
    time.sleep(3)
    temp = pyat.locateCenterOnScreen(Party_btn)
    counter = 1
    btn_found = False
    try:
        while counter < 20:
            if temp is None:
                print("|INFO|" + DateTime + "|" + " Searching the party button ...")
                counter += 1
            else:
                pyat.click(temp)
                btn_found = True
                temp = ""
                time.sleep(0.5)
                __focusterminal()
                break
        if ask == "1":
            print("|INFO|" + DateTime + "|" + " You enter the character menu")
        elif ask == "2":
            while btn_found:
                temp = pyat.locateCenterOnScreen(Weapon_btn)
                if temp is None:
                    print("|INFO|" + DateTime + "|" + " Searching the weapon button ...")
                else:
                    pyat.click(temp)
                    btn_found = False
                    __focusterminal()
                    print("|INFO|" + DateTime + "|" + " You enter the weapon menu")
                    break
        elif ask == "3":
            while btn_found:
                temp = pyat.locateCenterOnScreen(Summon_btn)
                if temp is None:
                    print("|INFO|" + DateTime + "|" + " Searching the summon button ...")
                else:
                    pyat.click(temp)
                    btn_found = False
                    __focusterminal()
                    print("|INFO|" + DateTime + "|" + " You enter the summon menu")
                    break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Submenu to choose what to upgrade (weapon,chara,summon)
def __upgrademenu():
        print("|INFO|" + DateTime + "|" + " Starting upgrade menu selection ...")
        print("\n 1.Characters \n 2.Weapons \n 3.Summons \n")
        ask = input("Where do you want to go (choose a number): ")
        __home()
        time.sleep(3)
        temp = pyat.locateCenterOnScreen(Upgrade_btn)
        counter = 1
        btn_found = False
        try:
            while counter < 20:
                if temp is None:
                    print("|INFO|" + DateTime + "|" + " Searching the upgrade button ...")
                    counter += 1
                else:
                    pyat.click(temp)
                    btn_found = True
                    temp = ""
                    time.sleep(0.5)
                    __focusterminal()
                    break
            if ask == "1":
                while btn_found:
                    temp = pyat.locateCenterOnScreen(Character_btn)
                    if temp is None:
                        print("|INFO|" + DateTime + "|" + " Searching the character button ...")
                    else:
                        pyat.click(temp)
                        btn_found = False
                        __focusterminal()
                        print("|INFO|" + DateTime + "|" + " You enter the character menu")
                        break
            elif ask == "2":
                print("|INFO|" + DateTime + "|" + " You enter the weapon menu")
            elif ask == "3":
                while btn_found:
                    temp = pyat.locateCenterOnScreen(Summon_btn)
                    if temp is None:
                        print("|INFO|" + DateTime + "|" + " Searching the summon button ...")
                    else:
                        pyat.click(temp)
                        btn_found = False
                        __focusterminal()
                        print("|INFO|" + DateTime + "|" + " You enter the summon menu")
                        break
        except OSError:
            print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
            print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
            __exit()
"""End Menu Section"""

"""Skill selection Section"""
# Back button after entering skill menu
def __backskill():
    try:
        counter = 1
        while counter < 20:
            temp = pyat.locateCenterOnScreen(Back_skill_btn)
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                print("|INFO|" + DateTime + "|" + " Rollback")
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Detect Main character
def __detectMC():
    try:
        print("|INFO|" + DateTime + "|" + " Searching for MC ...")
        temp = pyat.locateCenterOnScreen(Mc_skillbar)
        counter = 1
        break_stat = False
        # Search for MC skill bar
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break_stat = True
                print("|INFO|" + DateTime + "|" + " MC was found !")
                print("|INFO|" + DateTime + "|" + " Selection skill in progress ...")
                __skillMC(break_stat)
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()
    return break_stat

# Skill selection MC
def __skillMC(break_stat):
    # Change hotkey to make 1 = skill 1, etc ...
    try:
        while break_stat:
            x = __kbfunc()
            if x != False and x.decode() == "1":
                counter = 1
                temp = pyat.locateCenterOnScreen(MC_skill_1)
                while counter < 20:
                    if temp is None:
                        counter += 1
                    else:
                        pyat.click(temp)
                        time.sleep(0.5)
                        __focusterminal()
                        break
            elif x != False and x.decode() == "2":
                temp = pyat.locateCenterOnScreen(MC_skill_2)
                counter = 1
                while counter < 20:
                    if temp is None:
                        counter += 1
                    else:
                        pyat.click(temp)
                        time.sleep(0.5)
                        __focusterminal()
                        break
            elif x != False and x.decode() == "3":
                temp = pyat.locateCenterOnScreen(MC_skill_3)
                counter = 1
                while counter < 20:
                    if temp is None:
                        counter += 1
                    else:
                        pyat.click(temp)
                        time.sleep(0.5)
                        __focusterminal()
                        break
            elif x != False and x.decode() == "4":
                temp = pyat.locateCenterOnScreen(MC_skill_4)
                counter = 1
                while counter < 20:
                    if temp is None:
                        counter += 1
                    else:
                        pyat.click(temp)
                        time.sleep(0.5)
                        __focusterminal()
                        break
            elif x != False and x.decode() == "*":
                break_stat = False
                __backskill()
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()
"""End skill selection Section"""

"""Button Section"""
# Attack button during fight
def __attack():
    print("|INFO|" + DateTime + "|" + " You attack the ennemy")
    try:
        temp = pyat.locateCenterOnScreen(Attack_btn)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Next button during fight
def __next():
    log = print("|INFO|" + DateTime + "|" + " You move to next area")
    try:
        temp = pyat.locateCenterOnScreen(Next_btn)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Ok button. Same as quest button (when just finish a quest)
def __ok():
    log = print("|INFO|" + DateTime + "|" + " You choose to OK/Quest")
    try:
        temp = pyat.locateCenterOnScreen(Ok_btn)
        temp2 = pyat.locateCenterOnScreen(Ok_btn_2)
        temp3 = pyat.locateCenterOnScreen(Ok_btn_3)
        temp4 = pyat.locateCenterOnScreen(Ok_btn_4)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
        while counter < 21:
            if temp2 is None:
                counter += 1
            else:
                pyat.click(temp2)
                time.sleep(0.5)
                __focusterminal()
                break
        while counter < 22:
            if temp3 is None:
                counter += 1
            else:
                pyat.click(temp3)
                time.sleep(0.5)
                __focusterminal()
                break
        while counter < 23:
            if temp4 is None:
                counter += 1
            else:
                pyat.click(temp4)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Cancel button when don't want to add people or cancel a quest
def __cancel():
    log = print("|INFO|" + DateTime + "|" + " You choose to cancel your action")
    try:
        temp = pyat.locateCenterOnScreen(Cancel_btn)
        temp2 = pyat.locateCenterOnScreen(Cancel_btn_2)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
        while counter < 21:
            if temp2 is None:
                counter += 1
            else:
                pyat.click(temp2)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Retreat button when quit during quest stage
def __retreat():
    log = print("|INFO|" + DateTime + "|" + " You choose to retreat from the quest")
    try:
        temp = pyat.locateCenterOnScreen(Retreat_btn)
        temp2 = pyat.locateCenterOnScreen(Retreat_btn_2)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
        while counter < 21:
            if temp2 is None:
                counter += 1
            else:
                pyat.click(temp2)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Resume button when you have quit a quest stage
def __resume():
    log = print("|INFO|" + DateTime + "|" + " You choose to resume the quest")
    try:
        temp = pyat.locateCenterOnScreen(Resume_btn)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Home button even when in fight
def __home():
    log = print("|INFO|" + DateTime + "|" + " Going back home ...")
    try:
        temp = pyat.locateCenterOnScreen(Home_btn)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Reload button
def __reload():
    log = print("|INFO|" + DateTime + "|" + " Reloading the game ...")
    try:
        temp = pyat.locateCenterOnScreen(Reload_btn)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()

# Back button
def __back():
    log = print("|INFO|" + DateTime + "|" + " Going back ...")
    try:
        temp = pyat.locateCenterOnScreen(Back_btn)
        counter = 1
        while counter < 20:
            if temp is None:
                counter += 1
            else:
                pyat.click(temp)
                time.sleep(0.5)
                __focusterminal()
                break
    except OSError:
        print(Fore.RED + "|ERROR|" + DateTime + "|" + " Something's wrong with meshes files ...")
        print(Fore.RED + "|INFO|" + DateTime + "|" + " Exiting the script ...")
        __exit()
"""End Button Section"""


"""Break the script"""
def __exit():
    log = print("|INFO|" + DateTime + "|" + " Script closed succesfully")
    sys.exit()
"""End break the script"""

# Start the program
print("Welcome to GBF-hotkey !")
print(
"""
Autor: Nexius74
Version: 1.0.0
Last Update: 06.03.2018
More information: https://github.com/Nexius74/GBF_Simplify_Fight/blob/master/README.md
"""
)
while True:
    x = __kbfunc()
    if x != False and x.decode() == '1': # Attack
        __attack()
    elif x != False and x.decode() == '2': # Next
        __next()
    elif x != False and x.decode() == '3': # Ok
        __ok()
    elif x != False and x.decode() == '9': # Exit script
        __exit()
    elif x != False and x.decode() == 'h': # Home
        __home()
    elif x != False and x.decode() == 'g': # Reload
        __reload()
    elif x != False and x.decode() == 'f': # Back
        __back()
    elif x != False and x.decode() == '$': # Party menu
        __partymenu()
    elif x != False and x.decode() == '-': # Upgrade menu
        __upgrademenu()
    elif x != False and x.decode() == 'x': # Cancel
        __cancel()
    elif x!= False and x.decode() == 'c': # Retreat
        __retreat()
    elif x != False and x.decode() == 'v': # Resume
        __resume()
    elif x != False and x.decode() == 'o': # Skill character selection
        __selectioncaracter()
