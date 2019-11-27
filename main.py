// TODO vefore executing this code : 1. open the file containing the subject of interest 2. put in full screen (if hard/impossible, open it with chrome and press F11) 3. Press the key S 4. It will automatically do a screenshot (should be saved in OneDrive) and move to the next page
// PS : you might want to customize this code a little bit (mostly if it doesn't go to the next page with ->)

import keyboard
import pause

print("how many pages do you want to screenshot?")

n = input()

for i in n:
  keyboard.press_and_release('print_screen')
  keyboard.press_and_release('right arrow')
  pause(5) // to be sure that we're in the next page
  
print("We're done here :)")
