

'''from random import choice

print('Bienvenido al juego ahorcado')

print(f'Adivina una palabra introduciendo letra por letra  \n \tTienes 6 ❤ restantes\n ')

pc = ['gatos', 'perros', 'conejo']
letters_corrects = []
letter_incorrects = []
lives = 6
success = 0
game_over = False

def choose_words(list_words):
    choosen_word = choice(list_words)
    letters_unique = len(set(choosen_word))
    return choosen_word, letters_unique

def request_a_letter():
    choosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'

    while not is_valid:
        choosen_letter = input('Enter a letter: ')
        if choosen_letter in alphabet and len(choosen_letter) == 1:
            is_valid = True
        else:
            print('You have not chosen a correct letter')
    return choosen_letter

def display_new_board(choose_letter):
    list_hidden = []

    for l in choose_letter:
        if l in letters_corrects:
            list_hidden.append(l)
        else:
            list_hidden.append('-')

    print(' '.join(list_hidden))

def check_letter(choosen_letter, word_hidden, lives, coincidenses):
    end = False

    if choosen_letter in word_hidden:
        letters_corrects.append(choosen_letter)
        coincidenses += 1
    else:
        letter_incorrects.append(choosen_letter)
        lives -= 1

    if lives == 0:
        end = lose()
    elif coincidenses == letters_unique:
        end = gain(word_hidden)

    return lives, end, coincidenses

def lose():
    print('You have run out of lives')
    print('The hidden word was ' + word)

    return True

def gain(word_descovered):
    display_new_board(word_descovered)
    print('Felicitaciones, has encontrado la palabra!!!')

    return True

word, letters_unique = choose_words(pc)

while not game_over:
    print('*' * 20)
    display_new_board(word)
    print('Letter incorrects: ' + '-'.join(letter_incorrects))
    print(f'lives: {lives}')
    print('*' * 20)
    letter = request_a_letter()

    lives, finished, success = check_letter(letter, word, lives, success)
    game_over = finished
'''
def enter_word(word):
    my_word = word
    word_reversed = my_word[::-1]
    return word_reversed

my_word = enter_word('pepe como estas!')
print(my_word)

def calculate_area(radius):
    valor_pi = 3.14159 * (radius ** 2)
    return valor_pi

area = calculate_area(2)
print(area)

def count_vocals(vocals):
    quantity = 0
    five_vocals = 'aeiouAEIOU'
    for character in vocals:
        if character in five_vocals:
            quantity += 1

    return quantity

quatity = count_vocals('pepe')
print(quatity)

def calculate_average(*args):
    sum_numbers = sum(args)
    result = sum_numbers / len(args)
    return result

suma = calculate_average(2,3,3,5,7,10)
print(suma)

def is_palindromo(word):
    words = word
    if words == word[::-1]:
        return True
    else:
        return False

print(is_palindromo('rapar'))




def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list

print(fibonacci(4))
