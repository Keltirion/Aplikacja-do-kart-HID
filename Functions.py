# Modules required for the program to run successfully.
from PIL import ImageFont, ImageDraw, Image
import numpy
import cv2
import os
import unidecode

# XML for face detection for OpenCV containing the values required for facial identification,
# font for the hid card and empty list for storing names.
face_cascade = cv2.CascadeClassifier('Resource/haarcascade_frontalface_alt.xml')
font = ImageFont.truetype('Resource/WorkSans-Medium.otf', 55)
names = []

# A function that detects the face and builds card formats.
def createhid(path):
# A loop passing through all files in the folder.
    for file in os.listdir(path):
        # Extracting names and surnames from file names,
        # omitting the file "Thumbs.db" appearing in the folders on win7.
        # Separate the file extension.
        # Replacing Polish diacritical signs with ASCII, removing "_" and creating a new file name.
        if file != 'Thumbs.db':
            file_name, file_ext = os.path.splitext(file)
            names.append(file_name.replace('_', ' '))
            file_nodiacs = (unidecode.unidecode(file_name)).replace('_', ' ')
            os.rename(os.path.join(path, file), os.path.join(path, file_nodiacs + file_ext))
            # Reading photos, converting to gray scale in order to get a single-layer photo.
            photo = cv2.imread(os.path.join(path, file_nodiacs + file_ext), cv2.IMREAD_COLOR)
            photo_grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
            card = cv2.imread('Resource/DOVISTA - User.jpg', cv2.IMREAD_COLOR)
            # A file containing patterns for face detection.
            face_data = face_cascade.detectMultiScale(photo_grayscale, 1.05, 8, minSize=(300, 350))
            # A function that tries to find a face, in the absence of a face, skipping a photo.
            try:
                if face_data.all():
                    # Confirmation of face detection with first and last name printed on the screen.
                    print('Wykryto Twarz dla: ' + str(names[0]))
                    # Face detection and notch from the photo. Change the size of the cut image.
                    for (x, y, w, h,) in face_data:
                        size = 50
                        cord_x = cord_y = 10
                        cv2.rectangle(photo_grayscale, (x - size, y - 120), (x + w + size, y + h + size), (0, 0, 0))
                        photo_crop = photo[y - 140:y + h + size, x - size:x + w + size]
                        img_for_show = cv2.resize(photo_crop, (800, 800))
                        # Display detected face for confirmation by the user.
                        cv2.imshow(names[0], img_for_show)
                        # "Enter" for confirmation.
                        # "Space" for skip.
                        # "ESC" for exit from the program.
                        while 1:
                            # Waiting for user input to confirm with key stroke the correctness of detection.
                            key = cv2.waitKey(0)
                            # "Enter" for confirmation.
                            if key == 13:
                                # Closing the window. Resizing the photo to fit card template.
                                cv2.destroyAllWindows()
                                photo_ready = cv2.resize(photo_crop, (480, 610))
                                card[cord_y:cord_y + photo_ready.shape[0],
                                cord_x:cord_x + photo_ready.shape[1]] = photo_ready
                                # Converting to color.
                                card_rgb = cv2.cvtColor(card, cv2.COLOR_BGR2RGB)
                                pil_card = Image.fromarray(card_rgb)
                                w, h = pil_card.size
                                # Drawing the name of the user on card. Name and lastname are from the list.
                                text_card = ImageDraw.Draw(pil_card)
                                name, lastname = str(names[0]).split(' ')
                                # Formating the text.
                                text_card.multiline_text(((w - 480), (h - 210)),
                                                         '{}\n{}'.format(name, lastname),
                                                         font=font,
                                                         fill=(0, 0, 0, 0,),
                                                         align='left',
                                                         spacing=10)
                                # Deleting the name from the list.
                                del names[0]
                                # Saving the complete card in to folder as .jpg image. Ready for print.
                                pil_card.save('Complete/{} {}.jpg'.format(name, lastname), 'JPEG')
                                # Exiting the loop.
                                break
                            # "Space" for skip.
                            elif key == 32:
                                print('Pomijam użytkownika: ' + str(names[0]))
                                del names[0]
                                # Closing all windows.
                                cv2.destroyAllWindows()
                                break
                            # "ESC" for exit from the program.
                            elif key == 27:
                                exit(0)
            # If face is not detected, error is printed and program moves along to next file.
            except AttributeError:
                print('Błąd, nie wykryto twarzy dla: ' + str(names[0]))
                del names[0]
