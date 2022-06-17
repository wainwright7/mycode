#!/usr/bin/python3
"""Driving a simple text based game of navigation with
   dictionary objects | by Jay Patel """

# Replace RPG starter project with this code when new instructions are live
#Imports
import os
import time
import sys
#welcome message with instructions
def showInstructions():  
    """Show the game instructions when called"""
    print('''
    __        __     _                               
    \ \      / /___ | |  ___  ___   _ __ ___    ___  
     \ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \ 
      \ V  V /|  __/| || (__| (_) || | | | | ||  __/ 
       \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___| 

    RPG Game
    ========
    You start in the Hall of this house. 
    Go in each room, get all the items you can get. 
    Watch out for a monster, kill it or DIE!
    Go to the garden to Win the game.
          
    Commands:
          
    go   [directions - east, west, north, south]
    get  [item]
    map  [to see your current postion and MAP]
          
    ''')
    
#shows status of the player 
def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Your Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


#an inventory, which is initially empty
inventory = []
#player's health and monster's health
player = {"health":50}
monster = {"health":40, "attack":15}
#spells to kill the monster
spells = {"Expecto Petroleum":40, "Covid":10, "Flu":5}
#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'descr' : 'You are in a Hall of this house. \nSouth to Hall is a Kitchen.\nEast to Hall is a Dinning Room.\n'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east'  : 'Bed Room' ,
                  'creature' : 'monster',
                  'descr' : 'You are in a Kitchen.\nNorth to the Kitchen is a Hall.\nEast to the Kitchen is a Bedroom.\n'
            },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south' : 'Bed Room' ,
                  'item' : 'potion',
                  'descr': 'You are in the Dining Room.\nWest to the Dining Room is a Hall.\nSouth to the Dinning Room is a Bed Room.\n'
               },
            'Bed Room'  :  {
                  'north' : 'Dining Room' ,
                  'east' : 'Garden' ,
                  'west' : 'Kitchen' ,
                  'item' : 'wand',
                  'descr': 'You are in the Bed Room now.\nWest to the Bed Room is a Kitchen.\nNorth to the Bed Room is a Dinning Room.\nEast to the Bed Room is a Garden.\n'
                           
            },
            'Garden' : {
                  'west' : 'Bed Room',
                  'descr': 'You are in the garden.\nWest to garden is a Bedroom.'
            }
         }

#fight with monster in the kitchen
def fight_monster():  
  for spell in spells:
    print("- ", spell) #prints all spells
    
#player dies and Game over
  while True:
    if player["health"] <= 0:
        print('''
          ____                            ___                     
         / ___|  __ _  _ __ ___    ___   / _ \ __   __ ___  _ __  
        | |  _  / _` || '_ ` _ \  / _ \ | | | |\ \ / // _ \| '__| 
        | |_| || (_| || | | | | ||  __/ | |_| | \ V /|  __/| |    
         \____| \__,_||_| |_| |_| \___|  \___/   \_/  \___||_|                                                
        ''')    
        print("\n--------------You died, looser!--------------\n") #you died, Game over
        sys.exit()
      
    if monster["health"] <= 0:
      del rooms[currentRoom]['creature']   #removes monster from the kitchen
      print("\nYou killed the monster, You are a real monster, move on now!\n")      
      break

    #asks for spell to attack  
    attack_choice = input("\nWhich spell you want to use?\n>").title()
    
    if attack_choice == "Expecto Petroleum":
        print("Magical gas is poured over the monster and set on fire")
        monster["health"] = monster["health"] - spells["Expecto Petroleum"]
        print("The monster is attacking you!")
        print("The monster's health is now", monster["health"])
        time.sleep(1)        
        player["health"] = player["health"] - monster["attack"]     
        print("Your health is now ", player["health"])
      
    elif attack_choice == "Covid":
        print("You attacked the monster with Covid!")
        monster["health"] = monster["health"] - spells["Covid"]
        print("The monster is attacking you!")
        print("The monster's health is now ", monster["health"])
        time.sleep(1)        
        player["health"] = player["health"] - monster["attack"]
        print("Your health is now ", player["health"])
      
    elif attack_choice == "Flu":
        print("You attacked the monster with Flu!")
        monster["health"] = monster["health"] - spells["Flu"]
        print("The monster is attacking you! ")
        print("The monster's health is now ", monster["health"])
        time.sleep(1)        
        player["health"] = player["health"] - monster["attack"]
        print("Your's health is now ", player["health"])
      
    else:
        print("Sorry. Please type correct option.") #if player doesn't type correct spell

      
#loop forever
while True:
    if currentRoom == 'Hall':
      print("---------------------------")
      print(rooms['Hall']['descr'])
    showStatus()
    #when player enters kitchen
    if currentRoom == 'Kitchen':      
      if "creature" in rooms[currentRoom]:
        print('''
     __  __                     _               
    |  \/  |  ___   _ __   ___ | |_  ___  _ __  
    | |\/| | / _ \ | '_ \ / __|| __|/ _ \| '__| 
    | |  | || (_) || | | |\__ \| |_|  __/| |    
    |_|  |_| \___/ |_| |_||___/ \__|\___||_|    
    
    You are faced with a monster. 
    Fight with monster using following spells.\n''')
        fight_monster()
              
      
    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:    
    move = ''
    while move == '':  
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    os.system('clear') #to clear the screen    
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            #there is no door (link) to the new room
            if 'descr' in rooms[currentRoom]:
              print(rooms[currentRoom]['descr'])
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('\nYou got ' + move[1] + '!\n')
            #delete the item from the room
            del rooms[currentRoom]['item']
            #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
         
    #prints map and description of current location
    if move[0] == 'map' :
        print('''
        _____________   _____________
        |           |   |           |           ^
        |           |   |           |           N
        |   Hall    |   |  Dinning  |
        |           |   |   Room    |
        |___________|   |___________|

        _____________   _____________   _______________
        |           |   |           |    * * * * * *  |
        |           |   |           |               * |
        |  Kitchen  |   |  Bedroom  |      Garden   * |
        |           |   |           |    * * * * * *  |
        |___________|   |___________|   ______________|     

      ''')
        print(rooms[currentRoom]['descr']) #print currentroom's description
          
    # Winning situation
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'wand' in inventory:
        print('''
  ____       _        _                  _                              
 / ___| ___ | |  ___ | |__   _ __  __ _ | |_  ___    _   _   ___   _   _ 
| |    / _ \| | / _ \| '_ \ | '__|/ _` || __|/ _ \  | | | | / _ \ | | | |
| |___|  __/| ||  __/| |_) || |  | (_| || |_|  __/  | |_| || (_) || |_| |
 \____|\___||_| \___||_.__/ |_|   \__,_| \__|\___|   \__, | \___/  \__,_|
                                                     |___/               
 __  __                     _               
|  \/  |  ___   _ __   ___ | |_  ___  _ __  
| |\/| | / _ \ | '_ \ / __|| __|/ _ \| '__| 
| |  | || (_) || | | |\__ \| |_|  __/| |    
|_|  |_| \___/ |_| |_||___/ \__|\___||_| 
        ''')
        print('You escaped the house with the rare key and magic potion and magical wand... YOU WON!\n')
        break
    #player is in the garden but without all items necessory to win the game
    if currentRoom == 'Garden' and 'key' and 'potion' and 'wand' not in inventory:
        print('You need to get Gate Key, healthy potion and Magic wand to Win this game.\nGo Check other rooms.')
    elif currentRoom == 'Garden' and 'potion' not in inventory:
        print('You need to get Gate Key, healthy potion and Magic wand to Win this game.\nGo Check other rooms.')
    elif currentRoom == 'Garden' and 'wand' not in inventory:
        print('You need to get Gate Key, healthy potion and Magic wand to Win this game.\nGo Check other rooms.')
    elif currentRoom == 'Garden' and 'key' not in inventory:
        print('You need to get Gate Key, healthy potion and Magic wand to Win this game.\nGo Check other rooms.')
    
