from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import os
import unidecode

face_cascade = cv2.CascadeClassifier('Resource/haarcascade_frontalface_alt.xml')
names = []
photos = []


def diacritics(path):

    for f in os.listdir(path):
        file_name, file_ext = os.path.splitext(f)
        names.append(file_name.replace('_', ' '))
        remove_diacs = (unidecode.unidecode(file_name)).replace('_', ' ')
        new_name = '{}{}'.format(remove_diacs, file_ext)

        os.rename(os.path.join(path, f), os.path.join(path, new_name))


def photoprep(path):

    for p in os.listdir(path):
        photo = cv2.imread(os.path.join(path, p), cv2.IMREAD_COLOR)
        photo_grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        card = cv2.imread('Resource/DOVISTA - User.jpg', cv2.IMREAD_COLOR)
        face_data = face_cascade.detectMultiScale(photo_grayscale, 1.1, 5)

        for (x, y, w, h,) in face_data:

            length = 50
            cord_x = cord_y = 10

            cv2.rectangle(photo_grayscale, (x-length, y-120), (x+w+length, y+h+length), (0, 0, 0))
            photo_crop = photo[y-140:y+h+length, x-length:x+w+length]
            photo_ready = cv2.resize(photo_crop, (480, 610))
            card[cord_y:cord_y+photo_ready.shape[0], cord_x:cord_x+photo_ready.shape[1]] = photo_ready
            card_rgb = cv2.cvtColor(card, cv2.COLOR_BGR2RGB)
            photos.append(card_rgb)


def adding_text():
    font = ImageFont.truetype('Resource/WorkSans-Medium.otf', 55)

    for i in range(0, len(names)):

        print(names[i])
        name, lastname = str(names[i]).split(' ')
        pil_card = Image.fromarray(photos[i])
        w, h = pil_card.size
        text_card = ImageDraw.Draw(pil_card)
        text_card.multiline_text(((w - 480), (h - 210)),
                                 '{}\n{}'.format(name, lastname),
                                 font=font,
                                 fill=(0, 0, 0, 0,),
                                 align='left',
                                 spacing=10)
        pil_card.save('Complete/{} {}.jpg'.format(name, lastname), 'JPEG')
