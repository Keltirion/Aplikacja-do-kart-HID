# Modules required for the program to run successfully.
from Functions import *
import time

# User's manual in a .txt file printed on the screen.
file = open('Resource/Tekst.txt', 'r')
print(file.read())
# Waiting for user input. "Press Enter"
input('')




# Information about the number of files in the "Photos" folder.
folder = 'Photos/'
lista = os.listdir(folder)
print('Wykryto {} plików.'.format(len(os.listdir(folder))))

# The start of the function
createhid(folder)

# Termination of programs, terminal displayed by min.
print('Gotowe!')

time.sleep(60)