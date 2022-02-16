print("Welcome to Text Monster Game. In this game, There are 3 floors and 5 rooms on each floor. There is a prize to win the game in one of the rooms. There are also 2 monsters and a boss monster that can catch you by surprise in these rooms, so be careful! You can look around and find magic stones and 4 swords, you only have two hands and one pocket to store 3 items, so choose wisely. Your task is to get through all of the rooms to find the prize and defeat the monsters if you run into one. In order to play the game you will have to type 'left', 'right', 'up', 'down', 'fight', or 'grab' when prompted. I wish you the best!" )

floor1 = ['monster', 'sword', 'upstairs', 'sword', 'nothing']
floor2 = ['sword', 'magic stones', 'sword', 'upstairs', 'monster']
floor3 = ['prize', 'boss monster', 'sword', 'monster', 'downstairs']

userRoom = 4
userFloor = floor1
gameState = False
inventory = []
lastInput = ""

while (gameState == False): 
  userInput = (input("What would you like to do next? ").lower())

  if userInput == "left":
    if userRoom == 0:
      print("There are no more rooms to the left.")
    elif userFloor[userRoom] == "monster" and lastInput == "left" :
      print("Sorry you lost.")
      gameState = True
    else:
      userRoom = userRoom - 1
      
  elif userInput == "right":
    if userRoom == 4:
      print("There are no more rooms to the right.")
    elif userFloor[userRoom] == "monster" and lastInput == "right" :
      print("Sorry, you lost.")
      gameState = True 
    else:
      userRoom = userRoom + 1 

  elif userInput == "up":
    if userFloor[userRoom] == "upstairs":
      if userFloor == floor1:
        userFloor = floor2
      else:
        userFloor = floor3 
    else:
      print("There is no staircase to go up.")

  elif userInput == "down":
    if userFloor[userRoom] == "downstairs":
      if userFloor == floor3:
        userFloor = floor2
      else: 
        userFloor = floor1
    else:
      print("There is no staircase to go down.")

  elif userInput == "grab":
    if len(inventory) < 3:
      if userFloor[userRoom] == "sword" or userFloor[userRoom] == "magic stones":
        inventory.append(userFloor[userRoom])
        userFloor[userRoom] = "nothing."
      elif userFloor[userRoom] == "prize":
        print("You found the prize! Congratulations you won the game!")
        userFloor[userRoom] = "A WINNER!"
        gameState = True
      else:
        print("You can't grab.")
    else:
      print("You can't grab more than 3 items.")

  elif userInput == "fight":
    if userFloor[userRoom] == "monster":
      if "sword" in inventory:
        userFloor[userRoom] = "nothing."
        inventory.remove("sword")
      else: 
        print("Sorry you lost.")
        gameState = True 
    if userFloor[userRoom] == "boss monster":
      if "sword" in inventory and "magic stones" in inventory:
        userFloor[userRoom] = "nothing."
        inventory.remove("sword")
        inventory.remove("magic stones")
      else: 
        print("Sorry, you lost.")
        gameState = True 
      
  print ("This room has: " + userFloor[userRoom])
  lastInput = userInput 
  