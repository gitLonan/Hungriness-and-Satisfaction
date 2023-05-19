import sys
from rich.console import Console
import random
import time
import datetime
from rich import print
from rich.console import Group
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn,RenderableColumn, track
from rich.padding import Padding
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich.live import Live
from rich.prompt import Confirm
from rich.progress import track
import json
########################my folder imports
####  map layouts  ####
from maps_layout import main_city_layout
from maps_layout import zemun_layout
from maps_layout import novi_beograd_layout
from maps_layout import vracar_layout
from maps_layout import zvezdara_layout
from maps_layout import vozdovac_layout
from maps_layout import grocka_layout
####  shops  ##########
from Belgrade_shops_and_Char_tags import shop_menu
console = Console()
layout = Layout()
#progress = Progress(auto_refresh=False)
#Hunger & Satisfaction
#python -m rich.live
############# CHARACTER PREFRENCE ###########################################33
BOGDAN ={'fitness': "7/10", "sweets": "loves them", "favorite_food": "palačinka", "irritability": "low", 'color': 'bright_blue'}
MARKO ={'fitness': "9/10", "sweets": "no information", "favorite_food": "sausage", "irritability": "high", 'color': 'bright_yellow'}
TEODORA ={'fitness': "6/10", "sweets": "not a fan", "favorite_food": "vegan salads", "irritability": "high", 'color': 'bright_magenta'}
VELJKO ={'fitness': "2/10", "sweets": "preferes them", "favorite_food": "burek", "irritability": "no information", 'color': 'bright_black'}
ANA ={'fitness': "4/10", "sweets": "not a fan", "favorite_food": "pasta", "irritability": "low", 'color': 'bright_green'}



place = '' #This is used in main(), more explaination down there


#they are needed to score the in the game and are called in adding_goal_progress() line 439
hungriness_points = 0
satisfaction_points = 0

difficulty = {'Hard': 1100, 'Normal':1900, 'Easy': 2700} #1100,1900,2700
dif = 'Normal' #sets difficulty in func choosing_difficulty, because if you dont choose its set to Normal


####ZA igrace mogu da napravim tagove i sto vise neka hrana ima tagove koji se poklapaju sa tom hranom
#ono daje vise score-a
############# ZEMUN ###############
zemun_kiklop = [{'hrana': 'Gyros 700g' ,            'cena': 800 , 'koeficijent': 1.9, 'tags': ['meat','big', 'tortilla','grilled']},
                {'hrana': 'Kiklop hamburger 300g' , 'cena': 590 , 'koeficijent': 1.4, 'tags': ['meat', 'flatbread', 'low','grilled']},
                {'hrana': 'Kebab rolls 225g' ,      'cena': 550, 'koeficijent': 1.3, 'tags': ['meat', 'kebab', 'bun', 'low','grilled']},
                {'hrana': 'Pancakes' ,              'cena': 390 , 'koeficijent': 1.2, 'tags': ['sweet', 'eurocrem', 'bananas', 'medium']}
                ]
############# NOVI BEOGRAD ###############
novi_bg_food_fact = [{'hrana': 'Smoked sausage 200g' ,        'cena': 300 , 'koeficijent': 0.9, 'tags': ['meat', 'smoked','low','bun']},
                     {'hrana': 'Leskovac burger 300g' ,       'cena': 350 , 'koeficijent': 1, 'tags': ['meat','low','bun','grilled']},
                     {'hrana': 'Toasted sesame white 300g' ,  'cena': 350, 'koeficijent': 1.1, 'tags': ['sesam','meat','flatbread','medium']},
                     {'hrana': 'Sirloin sandwich' ,           'cena': 170 , 'koeficijent': 0.8, 'tags': ['sandwich', 'low','meat', 'vegetable']}
                     ]
############# VRACAR ###############
vracar_mara = [{'hrana': 'Omelette Mara',                       'cena': 500, 'koeficijent': 1.2, 'tags': ['eggs', 'vegetable', 'big']},
                     {'hrana': 'Tortilla stuffed shish kebab',  'cena': 430, 'koeficijent': 1.5, 'tags': ['meat', 'tortilla','kebab','medium','bacon','grilled']},
                     {'hrana': 'Vegetarian tortilla' ,          'cena': 310, 'koeficijent': 1.5, 'tags': ['vegetable','tortilla','medium',]},
                     {'hrana': 'Salad with chicken' ,           'cena': 440 , 'koeficijent': 1.3, 'tags': ['meat', 'vegetable','flatbread','smoked','big']}
            ]
############# ZVEZDARA ###############
zvezdara_gusar = [{'hrana': 'Gourmet hamburger 280g', 'cena': 350, 'koeficijent': 1.2, 'tags':['meat', 'bun', 'low']},
                     {'hrana': 'White Hanger 200g',   'cena': 300, 'koeficijent': 1.2, 'tags': ['meat','low']},
                     {'hrana': 'Kinder pancakes' ,    'cena': 250, 'koeficijent': 0.9, 'tags': ['sweet','kinder','vanilla','eurocrem','medium']},
                     {'hrana': 'Pancake Pirate' ,     'cena': 300 , 'koeficijent': 1, 'tags': ['sweet','nutella','bananas']}
                ]
############# VOZDOVAC ###############
vozdovac_vajat = [{'hrana': 'Vienna schnitzel 200g',  'cena': 300, 'koeficijent': 1.7, 'tags': ['meat', 'schnitzel','bun','medium','kajmak']},
                     {'hrana': 'Bun with cream 220g', 'cena': 150, 'koeficijent': 0.5, 'tags': ['kajmak','bun','low']},
                     {'hrana': 'French fries 200g',  'cena': 180, 'koeficijent': 0.6, 'tags': ['french fries','toasted']},
                     {'hrana': 'sweet pies',          'cena': 400, 'koeficijent': 1.3, 'tags': ['sweet','vanilla','pies', 'big']}
                ]
############# GROCKA ###############
grocka_panter = [{'hrana': 'Bacon in a flatbread 150g', 'cena': 330, 'koeficijent': 1.1, 'tags': ['meat', 'bacon','flatbread','low']},
                     {'hrana': 'Burger hot 160g',       'cena': 150, 'koeficijent': 0.6, 'tags': ['meat','bun','low','grilled']},
                     {'hrana': 'Gourmet burger 230g' ,  'cena': 420, 'koeficijent': 1.3, 'tags': ['meat','grilled','medium']},
                     {'hrana': 'Kebabs on cream 400g' , 'cena': 740, 'koeficijent': 1.8, 'tags': ['meat','kebab','kajmak','big','bun']}
                ]
#Needed in the main()
dict_of_shops = {'Zemun': zemun_kiklop,
                'Novi Beograd': novi_bg_food_fact,
                'Vracar': vracar_mara,
                'Zvezdara': zvezdara_gusar,
                'Vozdovac': vozdovac_vajat,
                'Grocka': grocka_panter,}
#Needed in the main()
#

#Creation of a character Table and Panel, you need to create a table soo you have more control over information than "fill" the Panel with that Table
#soo that you can use that same Panel and update the Layout, only renderables are put in Panel
##################################   Classes  ###################################################3333333



class Character():
    def __init__(self, name, fit, sweets, fav_food, irritability, color):
        self.name = name
        self.fit = fit
        self.sweets = sweets
        self.fav_food = fav_food
        self.irritability = irritability
        self.color = color
        self.money = 0
        
    def char_creation(self):
        stats = Table.grid(padding=1)
        stats.add_column(style=f'{self.color}', justify='left')
        stats.add_row(f"Fitness: {self.fit}")
        stats.add_row(f"Sweets: {self.sweets}")
        stats.add_row(f"Favorite food: {self.fav_food}")
        stats.add_row(f"Irritability: {self.irritability}")

        stats_panel = Panel(
                        Align.left(
                            Group(Align.left(stats)),
                                ), box=box.ROUNDED, title=f"{self.name}", border_style=f"{self.color}"
                            )
        return stats_panel

    def moneys(self):
        print(dif)
        if dif == 'Normal':
            self.money += difficulty['Normal']
        elif dif == 'Hard':
            self.money += difficulty['Hard']
        elif dif == 'Easy':
            self.money += difficulty['Easy']
        return self.money

    def status_layout(self):
        stats = Table.grid(padding=1)
        stats.add_column(style=f'{self.color}', justify='left')
        stats.add_row(f"Fitness: {self.fit}")
        stats.add_row(f"Sweets: {self.sweets}")
        stats.add_row(f"Favorite food: {self.fav_food}")
        stats.add_row(f"Irritability: {self.irritability}")
        stats.add_row(f'Money: [dark_red]{self.money}[/dark_red]')
        stats_panel = Panel(
                        Align.left(
                            Group(Align.left(stats)),
                                ), box=box.ROUNDED, title=f"{self.name}", border_style=f"{self.color}"
                            )
        return stats_panel
##############################################################################33
################################################################################

#Intro screen, first thing you see when you start the game
def intro():
    loading_screen_before_intro()
    string = """
Welcome to the game of Hunger & Satisfaction
            """
    intro = Align.center(Panel.fit(f"[bold yellow]{string}",
                                    title=" Hunger & Satisfaction ",
                                    subtitle="Created by MujoHarac"),
                                     vertical="middle")
    space_creation()
    print(intro)
    time.sleep(1) #should be 3
    string = """
Your job is to satisfy needs of different people. Choose and play accordingly
                          Press Enter to continue
    """
    intro = Align.center(Panel.fit(f"[bold yellow]{string}",
                                    title="Description"),
                                     vertical="middle")
    print(intro)
    input()
    main_menu()
# goal_progress = Progress(
#                     "{task.description}",
#                     TextColumn("{task.percentage:>3.0f}%"),
#                     BarColumn(),
#                             )

#     sat_task = goal_progress.add_task('Satisfaction',total=100)
#     hung_task = goal_progress.add_task('Hungriness',total=100)

#     goal_table = Table.grid(expand = True)
#     goal_table.add_row(Panel.fit(
#                             goal_progress,
#                             title = "Goal Progress",
#                             border_style = 'medium_purple4',
#                             padding = (2,2)
#                             #highlight = "Progress",
#                                 ),
#                         )
def loading_screen_before_intro():
    layout.split(
            Layout(name='middle'))
    space_creation()
    loading_progress = Progress(
                    "{task.description}",
                    TextColumn("{task.percentage:>3.0f}%"),
                    BarColumn(),
                    SpinnerColumn(spinner_name='dots', style='progress.spinner'),
                            )
    
    loading_actions = ['Loading Character...', 'Assets...', 'Weather...', 'Maps and Layouts...']
    loading_size = [100,100,100,100]
    loading_time = [0.001, 0.03, 0.002, 0.01]
    #char_loading = loading_progress.add_task("[red]Loading Characters...", total=50, visible=vis1)
    #assets_loading = loading_progress.add_task("[red]Assets...", total=50,visible=vis2)
    #weather_loading = loading_progress.add_task("[red]Weather...", total=50,visible=vis3)
    #maps_loading = loading_progress.add_task("[red]Maps and layouts...", total=50,visible=vis4)

    loading_table = Table(expand=True, box= None )
    loading_table.add_row(Panel(
                                    loading_progress,
                                    style= 'black',
                                    
                                    padding = (15,10),
                                    expand= True,
                                    
                                    )
                        )
    pointer = 1
    with Live(loading_table, refresh_per_second=4,transient=True): 
            for i,j in enumerate(loading_actions):
                current_task = loading_progress.add_task(f"{loading_actions[i]}")
            
                for _ in range(loading_size[i]):
                    time.sleep(loading_time[i])
                    loading_progress.update(current_task, advance=1)

                loading_progress.stop_task(current_task)

def main_menu():
    global dif
    space_creation()
    start = console.rule("""[bold gray]... 1.START ...""")
    dif_setting = console.rule("[bold gray]... 2.DIfficulty Settings ...")
    q_uit = console.rule("[bold gray]... 3.Quit ...")
    print("\n"*5)
    while True:
        state = input("Choose by typing the number:  ")
        if state == "1":
            choosing_char(dif)
        elif state == "2":
            dif = choosing_difficulty(dif)
        elif state == "3":
            sys.exit("Thank you for playing the game")
        main_menu()



#Screen wherer you choose your character, shows stats of everyone it does it based on a class
############################  CHOOSING CHARACTER LAYOUT   #####################3333333
def choosing_char(dif):
    Bogdan = Character("Bogdan",BOGDAN['fitness'], BOGDAN['sweets'],BOGDAN['favorite_food'], BOGDAN['irritability'],BOGDAN['color'])
    Marko = Character("Marko",MARKO['fitness'], MARKO['sweets'],MARKO['favorite_food'], MARKO['irritability'], MARKO['color'])
    Teodora = Character("Teodora",TEODORA['fitness'], TEODORA['sweets'],TEODORA['favorite_food'], TEODORA['irritability'], TEODORA['color'])
    Veljko = Character("Veljko",VELJKO['fitness'], VELJKO['sweets'],VELJKO['favorite_food'], VELJKO['irritability'], VELJKO['color'])
    Ana = Character("Ana",ANA['fitness'], ANA['sweets'],ANA['favorite_food'], ANA['irritability'], ANA['color'])
    _names = [Bogdan, Marko, Teodora, Veljko, Ana]

    space_creation()
    layout.split(
            Layout(name='upper', size=10),
            Layout(name='middle', ratio=2),
            Layout(name="down"),
            )
    layout["middle"].split_row(
        Layout(name="Bogdan"),
        Layout(name="Marko"),
        Layout(name="Teodora"),
        Layout(name="Veljko"),
        Layout(name="Ana")
    )
    #Layout being updated from the Panel that are created in the class
    layout['Bogdan'].update(Bogdan.char_creation())
    layout['Marko'].update(Marko.char_creation())
    layout['Teodora'].update(Teodora.char_creation())
    layout['Veljko'].update(Veljko.char_creation())
    layout['Ana'].update(Ana.char_creation())
    #time.sleep(4)
    description_char_layout()
    upper_char_layout()
    print(layout)
    name = Prompt.ask("[grey37]Type the name of the character you want:",
                        choices=['Bogdan', 'Marko', 'Teodora', 'Veljko', 'Ana'], show_choices=False)
    if name:
        for i in _names:
            if name == i.name:
                break

        main_game_screen(i,dif)    #sending the right object to the main game loop

#######
######
#####
#i should create many tips and then based on random chance
#you get random tips and tricks

def description_char_layout():
    description = """
There is couple of things you should think about when choosing a character. Their prefrences are very important in
regards of food you'll be buying and how far are you willing to travel for them, because more distance you
travers more iritated person becomes.
When you start a yellow '*' will indicate where are you on the map

            """

    table = Table.grid(expand= True)
    table.add_column(style='cyan2', justify='left')
    a = Panel(f"[cyan2]{description}",
                        title="Description",
                        subtitle="Created by MujoHarac",
                        box = box.ROUNDED)
    layout['down'].update(a)

def upper_char_layout():
    table = Table.grid(expand = True)
    table.add_column(justify="left", ratio=5)
    #fonts =  Bloody
    #it can fit 14 characters
    string = """

    █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████      ▄████  ▄▄▄       ███▄ ▄███▓▓█████  ██▀███
   ▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
   ▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███      ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   ▓██ ░▄█ ▒
   ░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄
   ░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
   ░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
     ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░     ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
     ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░      ░ ░   ░   ░   ▒   ░      ░      ░     ░░   ░
       ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░         ░       ░  ░       ░      ░  ░   ░
                        ░

            """
    table.add_row(string)

    a = Panel(table, style="yellow")
    layout['upper'].update(a)


 ####   ###################################################################33
 ####   ##############################################################################3


def choosing_difficulty(dif,*diffculty):
    space_creation()
    hard = difficulty['Hard']
    normal = difficulty['Normal']
    easy = difficulty['Easy']
    def selecting_dif(dif):
        diff_h = ''
        style_h = ''
        diff_n = ''
        style_n = ''
        diff_e = ''
        style_e = ''
        if dif == 'Hard':
            diff_h = '[bold yellow]'
            style_h = '[/bold yellow]'
            diff_n = ''
        elif dif== 'Normal':
            diff_n = '[bold yellow]'
            style_n = '[/bold yellow]'
        elif dif == 'Easy':
            diff_e = '[bold yellow]'
            style_e = '[/bold yellow]'
        return diff_h,style_h, diff_n,style_n, diff_e, style_e

    dif_h,styl_h, dif_n,styl_n, dif_e, styl_e = selecting_dif(dif)
    string = f"""
    Default difficulty is normal
    Choose wisely, higher the difficulty harder to get a high score and less money at the start
                1. {dif_h}Hard:    -{hard} starting gold
                                    -
                                    - {styl_h}
                2. {dif_n}Normal:  -{normal} starting gold
                                    -
                                    - {styl_n}
                3. {dif_e}Easy:    -{easy} starting gold
                                    -
                                    -{styl_e}
            """
    panel = Align.center(Panel.fit(f"[dark_green]{string}",
                                    title="Difficulty Settings"),
                                     vertical="middle",
                                     style='spring_green2',
                                      #border_style='light_sea_green',
                                      )
    print(panel)

    dif = Prompt.ask("[dark_cyan]Type the name of the difficulty you choose to play: ",choices=["Hard", "Normal", "Easy", 'back'], show_choices=False)
    space_creation()
    dif_h,styl_h, dif_n,styl_n, dif_e, styl_e = selecting_dif(dif)
    string2 = f"""
    Default difficulty is normal
    Choose wisely, higher the difficulty harder to get a high score and less money at the start
                1. {dif_h}Hard:    -{hard} starting gold
                                    -
                                    - {styl_h}
                2. {dif_n}Normal:  -{normal} starting gold
                                    -
                                    - {styl_n}
                3. {dif_e}Easy:    -{easy} starting gold
                                    -
                                    -{styl_e}
                                    """
    panel2 = Align.center(Panel.fit(f"[dark_green]{string2}",
                                    title="Difficulty Settings"),
                                     vertical="middle",
                                     style='spring_green2',
                                      #border_style='light_sea_green',
                                      )
    print(panel2)

    input('Press Enter to continue: ')
    return dif


def space_creation():
    print("\n"*30)



#################################################################################3#########333
##########3   Main Screens Layouts   #####################################################333

def layout_main_game_screen(name):
    layout_screen = Layout()
    layout_screen.split(
            Layout(name='upper', size=4),
            Layout(name='middle', ratio=3),
            Layout(name="down", size = 5, visible=True),
            )

    layout_screen['middle'].split_row(
                Layout(name='left'),
                Layout(name='right', ratio=3)
                                )

    layout_screen['left'].split(
                Layout(name="stats_box",minimum_size=13),
                Layout(name='goal_box', minimum_size=6)
                        )

    return layout_screen
#############################################################################################
#################  sub Main layout   ######
################   Town layouts ###########
def town_layout(layout_map,place):
    town_names = {'town': 'City map'}
    #main_city_layout imported from a file
    map = main_city_layout(place)
    main_panel = Panel.fit(map, title = f"{town_names['town']}",box = box.ROUNDED)
    layout_map['right'].update(main_panel)
    print(layout_map)

def zemun(layout_map,place):
    #zemun_layout imported from a file
    map = zemun_layout()
    zemun_panel = Panel(map, title = f"[yellow]{place}",box = box.ROUNDED,expand=True, style='bright_black')
    layout_map['right'].update(zemun_panel)
    print(layout_map)
    #name.money()
    shop = Prompt.ask('[cyan]You can type only the name[/cyan]')
    # while True:
    #     shop = Prompt.ask('[cyan]You can type only the name[/cyan]')
    #     if shop.lower() == 'kiklop':
    #         return
    #     elif shop.lower() == 'back':
    #          main(layout_map)


def novi_beograd(layout_map, place):
    map = novi_beograd_layout()
    novi_panel = Panel(map, title = f"[yellow]{place}", box=box.ROUNDED, expand=True, style='bright_black')
    layout_map['right'].update(novi_panel)
    print(layout_map)
    shop = Prompt.ask('[cyan]You should type only the name[/cyan]')

def vracar(layout_map, place):
    map = vracar_layout()
    vracar_panel = Panel(map, title = f"[yellow]{place}", box=box.ROUNDED, expand=True, style='bright_black')
    layout_map['right'].update(vracar_panel)
    print(layout_map)
    shop = Prompt.ask('[cyan]You should type only the name[/cyan]')

def zvezdara(layout_map, place):
    map = zvezdara_layout()
    zvezdara_panel = Panel(map, title = f"[yellow]{place}", box=box.ROUNDED, expand=True, style='bright_black')
    layout_map['right'].update(zvezdara_panel)
    print(layout_map)
    shop = Prompt.ask('[cyan]You should type only the name[/cyan]')

def vozdovac(layout_map, place):
    map = vozdovac_layout()
    vozdovac_panel = Panel(map, title = f"[yellow]{place}", box=box.ROUNDED, expand=True, style='bright_black')
    layout_map['right'].update(vozdovac_panel)
    print(layout_map)
    shop = Prompt.ask('[cyan]You should type only the name[/cyan]')

def grocka(layout_map, place):
    map = grocka_layout()
    grocka_panel = Panel(map, title = f"[yellow]{place}", box=box.ROUNDED, expand=True, style='bright_black')
    layout_map['right'].update(grocka_panel)
    print(layout_map)
    shop = Prompt.ask('[cyan]You should type only the name[/cyan]')
############################################
############################################################################################3

#Needed for shop printing layout
dict_places_in_town_layout = {'Zemun': zemun,
                              'Novi Beograd': novi_beograd,
                              'Vracar': vracar,
                              'Zvezdara': zvezdara,
                              'Vozdovac': vozdovac,
                              'Grocka': grocka}
###################   SHOPS   ###########################################################

#Shops in ZEMUN

#Shops in NOVI BEOGRAD

#Shops in VRACAR

#Shops in ZVEZDARA

#Shops in VOZDOVAC

#Shops in GROCKA

###########################################################################################
def goal_update(hung_points,hung_task,sat_task,goal_table,goal_progress):
    hung_points = sum(hung_points)
    goal_progress.update(hung_task, advance=hung_points)
    hung_points = 0

def goal_layout(layout_map):

    goal_progress = Progress(
                    "{task.description}",
                    TextColumn("{task.percentage:>3.0f}%"),
                    BarColumn(),
                            )

    sat_task = goal_progress.add_task('Satisfaction',total=100)
    hung_task = goal_progress.add_task('Hungriness',total=100)

    goal_table = Table.grid(expand = True)
    goal_table.add_row(Panel.fit(
                            goal_progress,
                            title = "Goal Progress",
                            border_style = 'medium_purple4',
                            padding = (2,2)
                            #highlight = "Progress",
                                ),
                        )
    layout_map['left']['goal_box'].update(goal_table) #OVo treba da bude drugacije od goal_box funkcije
    #print(layout_map)
    return goal_progress,sat_task, hung_task, goal_table

def stats_layout(name, layout_map):
    """ Character stats """
    layout_map['stats_box'].update(name.status_layout())

#Treba da napravim classu ili funkciju gde nasumicno odredjuje prvi dan
def upper_main_layout(layout_map):
    table = Table.grid(expand= True)
    table.add_column(justify="left", ratio=5)
    table.add_column(justify="center", ratio=5)
    table.add_column(justify="right", ratio=5)

    day, temp = weather_setter()
    table.add_row(f'Today is {day}', '[bold red]Hunger & Satisfaction[/bold red]', f"{temp}")
    table_panel = Panel(table, style="dark_olive_green3")
    layout_map['upper'].update(table_panel)

def tip_trick_main_layout(layout_map):
    tip_1 = """
You should watch out for rainy days, it can make your character agitated if you travel too much
            """

    table = Table.grid(expand= True)
    table.add_column(style='green', justify='left')
    a = Panel(f"[deep_pink4]{tip_1}",
                        title="Tips & Tricks",
                        subtitle="Created by MujoHarac",
                        box = box.ROUNDED,
                        style = "medium_orchid3")
    layout_map['down'].update(a)

def weather_setter():
    #upper_main_layout returns to this func
    #PAZI NA KOEFICIJENTE MNOZENJA, treba i to da napisem
    day=['sunny', 'cloudy', 'rainy', 'snowie ']
    sunny = {'sunny' :'15°C Precipitation-50% Humidity-63% Wind-<12 km/h',
            'sunny1' :'20°C Precipitation-30% Humidity-37% Wind-15 km/h',
            'sunny2' :'25°C Precipitation-45% Humidity-57% Wind-8 km/h'}

    cloudy = {'cloudy': '16°C Precipitation: 55% Humidity-70% Wind-30 km/h',
            'cloudy1' :'12°C Precipitation-49% Humidity-90% Wind-<12 km/h',
            'cloudy2' :'8°C Precipitation-44% Humidity-89% Wind-26 km/h'}

    rainy = {'rainy' :'15°C Precipitation-60% Humidity-63% Wind-13 km/h',
            'rainy1' :'10°C Precipitation-73% Humidity-88% Wind-17 km/h',
            'rainy2' :'7°C Precipitation-55% Humidity-96% Wind-29 km/h'}

    snowie = {'snowie': '3°C Precipitation-40% Humidity-63% Wind-15 km/h',
            'snowie1' :'-5°C Precipitation-68% Humidity-50% Wind-24 km/h',
            'snowie2' :'0°C Precipitation-50% Humidity-75% Wind-40 km/h'}
    lista = [sunny, cloudy, rainy, snowie]
    sunny_mod = 1
    cloudy_mod = 0.9
    rainy_mod = 0.6
    snowie_mod = 0.3
    set_wether = random.randint(0, len(day)-1)
    l = list(lista[set_wether].keys())
    k = random.choice(l)
    type_day = lista[set_wether]
    return (day[set_wether], type_day[k])
#################################################################################3###########3
##########################################################################3#######################
def end_game_screen(name,dif):
    space_creation()
    space_creation()
    end_screen_layout = Layout()
    end_screen_layout.split(
                            Layout(name='upper'),
                            Layout(name='down'),)
    string = """
        Thanks for playing this game, i hope your character is not hungry and satasfied.
                        If you have any feed back please let me know.
                                Press Enter to continue     
            """
    end_screen_upper = Align.center(Panel.fit(f"[bold yellow]{string}",
                                    title=" Hunger & Satisfaction ",
                                    subtitle="Created by MujoHarac"),
                                     vertical="middle")
    end_screen_layout['upper'].update(end_screen_upper)
    
    string = f"""
This are the end result with the [bold red]{name.name}[/bold red]
    -Hungriness: {hungriness_points}%
    -Satisfaction: {satisfaction_points}%
            """ 
    end_screen_down = Align.center(Panel.fit(f"[green1]{string}",
                                    title=" Hunger & Satisfaction ",
                                    subtitle="Created by MujoHarac"),
                                    vertical="middle")
    end_screen_layout['down'].update(end_screen_down)
    print(end_screen_layout)
    input()
    p = Prompt.ask("[bold red]Do you want to save this the end result[/bold red]?[cyan]y/n[/cyan]")
    if p == 'y':
        player = Prompt.ask("[bold red]What is your name ?[/bold red]?")
        dic = {'person played': player,
            'name': name.name,
           'difficulty': dif,
           'hungfriness': hungriness_points,
           'satisfaction': satisfaction_points}
        game_saving(dic)
        sys.exit()
    elif p == 'n':
        sys.exit()

def game_saving(dic, filename ='score_board.json'):
    with open(filename, 'r+') as scoreBoard:
        char_json = json.loads(scoreBoard.read())
        char_json.append(dic)
        scoreBoard.seek(0)
        json.dump(char_json, scoreBoard, indent=4)


#called in main_game_screen on 590line
def adding_goal_progress(goal_progress, sat_task, hung_task, layout_map,goal_table):
    #sat_task,hung_task, goal_progress,layout_map
    #Here im updating Panel for the goals of the game
    lista = [sat_task, hung_task]
    goal_list = [satisfaction_points, hungriness_points]
    if hungriness_points > 0 or satisfaction_points > 0:
        for i,j in enumerate(lista):
            goal_progress.update(i, advance=goal_list[i])
            goal=0
        layout_map["goal_box"].update(goal_table)
    ##print(layout_map)



###################   MAIN GAME PRINTING SCREEN   #################

def main_game_screen(name,dif):
    name.moneys()
    layout_map = layout_main_game_screen(name)
    goal_progress, sat_task, hung_task, goal_table = goal_layout(layout_map)
    stats_layout(name, layout_map)
    upper_main_layout(layout_map)
    #adding_goal_progress(goal_progress, sat_task, hung_task, layout_map,goal_table)
    tip_trick_main_layout(layout_map)
    main(layout_map,goal_progress, sat_task, hung_task,goal_table, name,dif)

##########################################################

#######################   MAIN   ###############################################
def main(layout_map, goal_progress, sat_task, hung_task, goal_table, name,dif):
#place starts with place='' because in function town_layout(code line 413), we have a function that calls
#from a file maps_layout and depending on the place you visit the yellow * acts as a pointer
#where you are currently
    global place
    global hungriness_points
    town_layout(layout_map, place)
    choices=['Zemun', 'Vracar', 'Novi Beograd', 'Zvezdara', 'Grocka', 'Vozdovac']
    money = name.money
    while True:
        place = Prompt.ask("[bright_yellow]Choose the place you want to visit?")
        if place == 'back':
            p = Prompt.ask("Are you sure you want to go back to Character screen?[cyan]y/n[/cyan]")
            if p == 'y':
                choosing_char(dif)
            else:
                continue
        elif place == 'end':
            p = Prompt.ask("Are you sure you want to end the session?[cyan]y/n[/cyan]")
            if p == 'y':
                end_game_screen(name,dif)
                break
            else:
                continue
        elif place not in choices:
            continue
        elif place in choices:
            shop = dict_of_shops[f'{place}']
            dict_places_in_town_layout[f'{place}'](layout_map, place)
            hungriness_points, spent = shop_menu(layout_map, shop, name,money,place)
            print(hungriness_points)
            name.money -= spent
            layout_map['stats_box'].update(name.status_layout())
            print(layout_map)
            adding_goal_progress(goal_progress, sat_task, hung_task, layout_map,goal_table)
            main(layout_map,goal_progress, sat_task, hung_task, goal_table,name,dif)

        








intro()
