
import time
import random

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to the game of The Majestic Scrolls")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

time.sleep(3)

print("You are in a Mystical Palace. Infront of you are 2 doors.")
time.sleep(2.5)
print("Taking one of these doors will lead you to a. the next set of doors, or b. a mini adventure.")
time.sleep(2.5)
print("You must find 5 scrolls to leave this dreadful palace.")
s1 = (input("Make your choice wisely, left or right?"))
if s1 in ['l', 'L', 'left', 'Left', 'LEFT']:
   print ("You walk through the door on the left and you're greeted by a cave. It's very dark, but you can feel a stick on the floor.")

   #STICK IN INVENTORY
   ss1 = (input("Do you wish to pick it up?"))
   if ss1 in ['y', 'Y', 'YES', 'Yes', 'yes']:
      print ("You pick up a stick and start to sharpen it. You hastily carry on.")
      time.sleep(2)
      stick = 1

   #STICK NOT IN INVENTORY
   else:
         print ("You leave the stick on the floor and decide to carry on.")
         stick = 0

   #APPROACHING THE RHINO
   ss2 = (input("As you are walking through the cave, you see a small shiny object. Do you wish to approach it?"))
   if ss2 in ['y', 'YES', 'Y', 'Yes', 'yes']:
      print ("You approach the object as slowly as possible...")
      time.sleep(2)
      print ("As you go closer, you start to make out that the object is a horn!")
      time.sleep(3)
      print ("The horn amongst you is the horn of a rhino!")
      ss3 = (input("Do you want to fight it?"))

      #FIGHTING THE RHINO
      if ss3 in ['y', 'Y', 'YES', 'Yes', 'yes']:

      #WITH STICK IN INVENTORY
         if stick == 1:
            print ("You have a sharp stick in your inventory. You take it out to fight the rhino.")
            time.sleep(1.5)
            print ("You rapidly stab the rhino in it's eye and you gain an advantage!")
            time.sleep(1.5)
            print ("As you stab the rhino, you see something stuck on the rhino's back.")
            time.sleep(1.5)
            print ("It's a scroll!")
            time.sleep(2)
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("                    Player1 is fighting!                        ")
            print ("       You must hit something above a 6 to kill the rhino!      ")
            print ("Be careful though, if the rhino hits higher than you, you'll die")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(2)
            import random
            pdmg1 = (random.randint(4,10))
            edmg1 = (random.randint(3,6))
            print ("You hit a", pdmg1)
            time.sleep(4)
            print ("The rhino hits a", edmg1)
            time.sleep(2)


            if edmg1 > pdmg1:
                  print ("The rhino has dealt more damage than you!")
                  print ("GAME OVER")
                  scrolls = 0

            elif pdmg1 < 5:
                  print ("You didn't do enough damage to kill the rhino, but you manage to escape")
                  scrolls = 0

            else:
                  print ("You killed the rhino and took the scroll off it's back.")
                  scrolls = 1
      #WITHOUT STICK IN INVENTORY
         else:
            print ("You have nothing in your inventory to gain an advantage!")
            time.sleep(1.5)
            print ("Shoulda picked up the stick.")
            time.sleep(1.5)
            print ("But stuck on the rhino's back is a scroll!")
            time.sleep(2)
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("                    Player1 is fighting!                        ")
            print ("       You must hit something above a 6 to kill the rhino!      ")
            print ("Be careful though, if the rhino hits higher than you, you'll die")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(2)
            time.sleep(2)
            import random
            pdmg1 = (random.randint(1,10))
            edmg1 = (random.randint(3,6))
            print ("You hit a", pdmg1)
            time.sleep(4)
            print ("The rhino hits a", edmg1)
            time.sleep(2)
   

            if edmg1 > pdmg1:
                  print ("The rhino has dealt more damage than you!")
                  print ("GAME OVER")
                  scrolls = 0
            elif pdmg1 < 4:
                  print ("You didn't do enough damage to kill the rhino, but you manage to escape.")
                  scrolls = 0

            else:
                  print ("You killed the rhino and take the scroll off its back.")
                  scrolls = 1

      #RUNNING FROM THE RHINO
      else:
         print("You start to move on but the rhino wakes up from its slumber!")
         time.sleep(2)
         print("You run as fast as you can but the rhino is faster!")
         time.sleep(2)
         print("The rhino is big so you quickly turn a corner into an alley.")
         time.sleep(2)
         print("The rhino tries to come in but is too big!")
         scrolls = 0


         
        
      
