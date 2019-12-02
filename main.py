import keyboard #to screenshot
import time #to pause
from PIL import Image #to crop
from fpdf import FPDF #to create the PDF
from tqdm import tqdm_notebook #to get some progress insights

print("Hi there! How many pages do you want to screenshot?")
n = input()

print("Ok! We'll start as soon as you'll press 'S'")

keyboard.wait('S')

for i in range(1,int(n),1) :
    keyboard.press_and_release('print_screen')
    time.sleep(3) # to be sure that we're in the next page
    keyboard.press_and_release('right arrow')
    time.sleep(3) # to be sure that we're in the next page

# You might want to crop the image

links = "C:\\Users\\BarackObama\\BidenAndIPictures\\img" # You need to customize that bro

for i in range(0,n,1):
    links = "C:\\Users\\User\\OneDrive\\3 Old\\Autres\\Images\\Captures d’écran\\2019-11-28 (" + str(i) + ").png"
    images = Image.open(links)
    cropped_images = images.crop((530,0,1722,1504)) #left, top, right, bottom
    cropped_images.save(str(i)+".png")
    
# You might want to convert the png to jpeg


# You might want to create a pdf from the list of png

pdf = FPDF()
for i in tqdm_notebook(range(0,n,1)):
    pdf.add_page()
    pdf.image(str(i)+".png",0,0,210)
pdf.output("EM-endoc15.pdf", "F")

print("All done duddy :)")
