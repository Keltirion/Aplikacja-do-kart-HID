import cv2
import os
import unicodedata

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


def diacritics(path):

    for f in os.listdir(path):

        file_name, file_ext = os.path.splitext(f)
        remove_diacs = unicodedata.normalize('NFD', file_name).encode('ascii', 'ignore')
        decode = remove_diacs.decode('UTF-8')
        new_name = '{}{}'.format(decode, file_ext)

        os.rename(os.path.join(path, f), os.path.join(path, new_name))

def photoprep(path):

    for p in os.listdir(path):
        photo = cv2.imread(os.path.join(path, p), cv2.IMREAD_COLOR)
        photo_grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

        face_data = face_cascade.detectMultiScale(photo_grayscale, 1.3, 5)
        for (x, y, w, h,) in face_data:
            length = 40
            cv2.rectangle(photo_grayscale, (x-length, y-120), (x+w+length, y+h+length), (0,0,0))
            photo_crop = photo[y-120:y+h+length, x-length:x+w+length]
            photo_ready = cv2.resize(photo_crop, None, fx=0.5, fy=0.5)

            cv2.imshow('Test', photo_ready)
            cv2.waitKey(0)
            cv2.imwrite(p, photo_ready)
            cv2.destroyAllWindows()