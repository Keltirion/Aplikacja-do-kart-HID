from PIL import Image
import os

complete_cards = {}
number = 0

def companylogo():


    prompt1 = input('Czy chcesz dodać logo firmy zewnętrznej?(Yes/No)\n')

    if prompt1 == 'Yes' or 'yes':

        for file in os.listdir('Complete/'):

            file_name, file_ext = os.path.splitext(file)
            image = Image.open(os.path.join('Complete', file))
            complete_cards[number] = [file_name, image]
            number += 1

        for key, value in complete_cards.items():
            print(complete_cards)
            print('Nr {} - {}'.format(str(key), str(value[0])))



        prompt2 = int(input('Wybierz nr karty do której chcesz dodać logo: '))

        if prompt2 == 1:
            pass
        elif prompt2 == 2:
            pass
        elif prompt2 == 3:
            pass
        elif prompt2 == 4:
            pass
        elif prompt2 == 5:
            pass
        else:
            print('Nie wybrano firmy.')



    elif prompt1 == 'No' or 'no':
        pass


companylogo()
