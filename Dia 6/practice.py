from pathlib import Path
import shutil
from os import system
#import os

game_over = False

def choose_optios():
    system('cls')

    print('\t\t \033[1mHello Welcome to the Game\033[0m')

    print(f'the folder \033[1mRecipes\033[0m is in {Path.cwd()}\n')

    print(''' you have \033[1m6\033[0m options to choose:
    [1] Read Recipes
    [2] Create Recipes
    [3] Create Category
    [4] Delete Recipes
    [5] Delete Category
    [6] End Program
    ''')


def choose_category():
    base = Path(Path.cwd(),'Recetas')
    folders = [folder.parts[-1] for folder in base.iterdir() if folder.is_dir()]


    print('You have the following categories to choose from')
    for category in folders:
        print(f'Category of {category}')

    while True:
        insert = input('Choose a Category: ').title()
        if insert in folders:
            return base / insert
        else:
            print('Choose a category correct')


# It is a function that validates if the specified path in the parameter exists, and if so, it iterates through the path prints all the files.
def display_recipes(selected_route):

    recipes = False

    if selected_route.is_dir():
        for file in selected_route.iterdir():
            if file.is_file():
                print(file.name)
                recipes = True

    if not recipes:
        print('No recipes found in the selected category.')


def choose_recipe():
    selected_route = choose_category()
    display_recipes(selected_route)

    while True:
        recipe_name = input('Choose a Recipe: ').lower()
        recipe_path = selected_route / recipe_name

        if recipe_path.is_file():
            print(f"You selected the recipe: {recipe_name}")
            break
        else:
            print("Invalid recipe. Please choose a valid recipe.")

    return recipe_path


def display_content():
    recipe_choose = choose_recipe()
    options = ['open','exit']

    while True:
        print('you have 2 options to choose: OPEN and EXIT')
        user_choose = input('Choose a option: ').lower()
        if user_choose == 'exit' and user_choose in options:
            print(f'you choosen exit')
            break
        elif user_choose == 'open' and user_choose in options:
            open_file = open(recipe_choose, 'r', encoding="utf-8")
            content_display = open_file.read()
            print(content_display)
            break
        else:
            print('Choose a valid option')


def delete_category():
    category = choose_category()

    if category.is_dir():
        shutil.rmtree(category)
        print('the chosen category has been removed')
    else:
        print('the directory does not exist')


def delete_recipes():
    recipes = choose_recipe()

    if recipes.is_file():
        recipes.unlink()
        print('The chose recipe has been removed')
    else:
        print('The recipe does not exist')


def create_category():
    new_name_category = input('Enter the name of the category to create: ').title()
    base = Path.cwd() / 'Recetas' / new_name_category
    if new_name_category.isalpha():
        base.mkdir(exist_ok= True, parents= True)
        print('The directory was created successfully')
    else:
        print('Enter a directory valid')


def create_recipes():
    selected_cate = choose_category()

    new_name_category = input('Enter the name of the recipes to create: ') + '.txt'
    new_recipes = Path.cwd() / selected_cate / new_name_category
    if selected_cate:
        new_recipes.touch(exist_ok= True)
        print('The recipes was created successfully')


def finaliting_program():
    game_over = True
    print('Program Finished')
    return True


while True:
    choose_optios()

    enter_option = int(input('Enter a option: '))

    if enter_option == 1:
        display_content()
    elif enter_option == 2:
        create_recipes()
    elif enter_option == 3:
        create_category()
    elif enter_option == 4:
        delete_recipes()
    elif enter_option == 5:
        delete_category()
    elif enter_option == 6:
        finaliting_program()
        break

    else:
        print('Enter a option valid')






