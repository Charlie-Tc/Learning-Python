from pathlib import Path
#import os

game_over = False


def choose_category():
    base = Path(Path.cwd(),'Recetas')
    folders = ['Carnes','Ensaladas','Pastas','Postres']


    print('You have 4 categories to choose from')
    for folder in base.iterdir():
        if folder.is_dir():
            route = folder.parts[-1]
            print(f'Category of {route}')

    while True:
        insert = input('Choose a Category: ').title()
        if insert in folders:
            return base / insert
        else:
            print('Choose a category correct')


def display_recipes():
    pass






#pepe = display_recipes()
#print('esto es de pepe: ',pepe)







'''        if base.joinpath(base,'Carnes'):
            joins = Path.joinpath(base, 'Carnes')
            for files in joins.glob('*.txt'):
                last_words = files.parts[-1]
                nose.append(last_words)'''