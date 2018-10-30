from Functions import *


folder = 'C:/Users/lel.dva/Documents/Python/Aplikacja do kart HID/Photos/'


print('Wykryto {} plików.'.format(len(os.listdir(folder))))

renamefiles(folder)

createhid(folder)

print('Done!')

