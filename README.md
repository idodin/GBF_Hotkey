# Status
In developement . **DO NOT USE THIS SCRIPT IF YOU DON'T EDIT IT FIRST ! See [Additional information](#additional-information).**  
[OK] Home, Reload, Back button  
[OK] Selection character + skills during fight (Only for MC)  
[OK] Resume, Retreat, Cancel button  
[OK] Party, Upgrade menu  
[OK] Kill script  

# Description
This is a little script write in python 3 (3.5.3) that bound keyboard's keys to buttons in-game. You have acces to home, reload, party(character or weapon or summon), upgrade(character or weapon or summon), attack, next, ok, cancel, retreat, resume, skills selection buttons and exit the script. 

# Requirement
 - Python 3 Enivronnement  
 - Pywinauto, pyautogui, colorama installed
 
 # How it works
 Launch the script and just press the key you want.  
 - Attack -> 1  
 - Next -> 2  
 - Ok -> 3  
 - Exit script -> 9  
 - Home -> h  
 - Reload -> g  
 - Back -> f  
 - Party menu -> $  
 - Upgrade menu -> -  
 - Cancel -> x  
 - Retreat -> c  
 - Resume -> v  
 - *Selection character + skill in fight -> o

*This option has hotkeys that are rebound just to select skills. You select your character, skills, then press back:  
- Skill 1 -> 1  
- Skill 2 -> 2  
- Skill 3 -> 3  
- Skill 4 -> 4  
- Back from skill menu -> *  

# Additional information
1. This script was write for my actual team (MC(Weapon-master), DJeanne, Lyria, Vira. All skybound). **THIS IS NOT GONNA WORK WITH A DIFFERENT TEAM !!!!** If you want to use this script with your own team, feel free to edit meshes + source code.   
3. Don't touch your mouse when script is launched and processing.   
4. Make sure that the chrome page (with GBF started) and the terminal (When script is launched) are on the same screen.  
5. Make sure that the terminal isn't over gbf interface. Always. Exemple: https://imgur.com/hIlkk4u  
5. When a menu ask for a number (when you want to go to party weapon or character or summon) input the correct number. If not can result in crash  
6.**Im new to python and even more to programming. Don't expect something well made, stable, dynamic or w/o bugs.**  

# Known bug 
[FIXED] Quest and cancel button wasn't detect by pyautogui. When using counter multiple time within a same function, second while loop doesn't work.  
[BUG] No control over user input which can result in crash if not following correctly the instruction or miss press a key.
