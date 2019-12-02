import keyboard #to screenshot
import time #to pause
from PIL import Image #to crop
from fpdf import FPDF #to create the PDF
from tqdm import tqdm_notebook #to get some progress insights

print("What do you want to do?\nEnter 1 for screenshot\nEnter 2 for cropping")

choice = input()

if choice == 1:

    print("Hi there! How many pages do you want to screenshot?")
    n = input()

    print("Ok! We'll start as soon as you'll press 'S'")

    keyboard.wait('S')

    for i in range(0,int(n),1) :
        keyboard.press_and_release('print_screen')
        time.sleep(2) # to be sure that we're in the next page
        keyboard.press_and_release('right arrow')
        time.sleep(2) # to be sure that we're in the next page
        
elif choice == 2 :
    
    print("Hi there! How many pages do you want to crop?")
    n = input()

    # You might want to crop the image
    
    print("x1")
    x1 = input()
    print("y1")
    y1 = input()
    print("x2")
    x2 = input()
    print("y2")
    y2 = input()

    for i in range(0,int(n),1):
        links = str(i) + ".png"
        images = Image.open(links)
        cropped_images = images.crop((x1,y1,x2,y2)) #left, top, right, bottom
        cropped_images.save(str(i)+".png")
    

print("All done duddy :)")
