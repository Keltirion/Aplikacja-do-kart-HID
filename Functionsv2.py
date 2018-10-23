from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import os
import unidecode

# XML do wykrywania twarzy dla OpenCV, czcionka do karty hid, lista imion.
face_cascade = cv2.CascadeClassifier('Resource/haarcascade_frontalface_alt.xml')
font = ImageFont.truetype('Resource/WorkSans-Medium.otf', 55)
names = []


def renamefiles(path):

    for file in os.listdir(path):
        file_name, file_ext = os.path.splitext(file)
        names.append(file_name.replace('_', ' '))
        file_nodiacs = (unidecode.unidecode(file_name)).replace('_', ' ')
        os.rename(os.path.join(path, file), os.path.join(path, file_nodiacs, file_ext))


def createhid(path):

    for file in os.listdir(path):

        photo = cv2.imread(os.path.join(path, file), cv2.IMREAD_COLOR)
        photo_grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        card = cv2.imread('Resource/DOVISTA - User.jpg', cv2.IMREAD_COLOR)
        face_data = face_cascade.detectMultiScale(photo_grayscale, 1.05, 8, minSize=(50, 50))

        for (x, y, w, h,) in face_data:
            size = 50
            cord_x = cord_y = 10
            print('Znaleziono ' + str(face_data.shape[0]) + ' twarzy')
            cv2.rectangle((photo_grayscale), (x-size, y-120), (x+w+size, y+h+size), (0, 0, 0))
            photo_crop = photo[y-140:y+h+size, x-size:x+w+size]
            photo_ready = cv2.resize(photo_crop, (480,610))
            card[cord_y:cord_y+photo_ready.shape[0], cord_x:cord_x+photo_ready.shape[1]] = photo_ready
            card_rgb = cv2.cvtColor(card, cv2.COLOR_BGR2RGB)

            pil_card = Image.fromarray(card_rgb)
            w, h = pil_card.size
            text_card =  ImageDraw.Draw(pil_card)
            lastname, name = str(names[0]).split(' ')
            print('To jest imie ' + name)
            print('To jest nazwisko ' + lastname)
            text_card.multiline_text(((w - 480), (h - 210)),
                                 '{}\n{}'.format(name, lastname),
                                 font=font,
                                 fill=(0, 0, 0, 0,),
                                 align='left',
                                 spacing=10)
            del names[0]
            pil_card.save('Complete/{} {}.jpg'.format(name, lastname), 'JPEG')