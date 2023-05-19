from rich.prompt import Prompt
from rich.table import Table
from rich import print


############  CHARACTER TAGS  #####################################################3

"""
        {'broad': {'meat': , 'vegetable': , 'sweet':},
        'specific': {'sesam':,'eggs':,'french fries':,'kajmak':,'sandwich':,
                    'tortilla':,'bun':,'flatbread':,
                    'chicken':,'schnitzel':,'sausage':,'kebab':,'bacon':,
                    'kinder':,'nutella':, 'eurocrem':, 'vanilla':, 'pies':,
                    'bananas':,},
        'way_of_making':{'roasted':, 'grilled':, 'smoked':,'toasted':,},
        'volume_of_eating': {'big':, 'medium':, 'low':}}
"""

#tags Bogdan
BOGDAN = {'broad': {'meat': 0.1, 'vegetable':0.1, 'sweet':0.3},
        'specific': {'sesam':0,'eggs':-0.1,'french fries':0.2,'kajmak':0,'sandwich':0,
                    'tortilla':0.3,'bun':0.3,'flatbread':-0.1,
                    'chicken':0,'schnitzel':-0.2,'sausage':0,'kebab':0.1,'bacon':0,
                    'kinder':0.4,'nutella':0.4, 'eurocrem':0.2, 'vanilla':0.3, 'pies':0.4,
                    'bananas':0.4,},
        'way_of_making':{'roasted':0.1, 'grilled':0, 'smoked':0.2,'toasted':0,},
        'volume_of_eating': {'big':0.3, 'medium':0.25, 'low':0.1}}
#tags Marko
MARKO = {'broad': {'meat': 0.3, 'vegetable': 0.2, 'sweet':0.1},
        'specific': {'sesam':0.1,'eggs':0.2,'french fries':0.2,'kajmak':-0.2,'sandwich':0.2,
                    'tortilla':-0.2,'bun':0.2,'flatbread':0.1,
                    'chicken':0.2,'schnitzel':0.3,'sausage':0.2,'kebab':0.4,'bacon':0.5,
                    'kinder':0.1,'nutella':0.1, 'eurocrem':0.1, 'vanilla':0.1, 'pies':0.1,
                    'bananas':0,},
        'way_of_making':{'roasted':0.2, 'grilled':0.1, 'smoked':0,'toasted':0.1,},
        'volume_of_eating': {'big':0.5, 'medium':0.3, 'low':0.1}}
#tags Teodora
TEODORA = {'broad': {'meat':0.1 , 'vegetable':0.3, 'sweet':0},
        'specific': {'sesam':0.2,'eggs':0.4,'french fries':0.3,'kajmak':0,'sandwich':0.2,
                    'tortilla':0.1,'bun':0.1,'flatbread':0.3,
                    'chicken':0,'schnitzel':0,'sausage':0.3,'kebab':0.2,'bacon':0.2,
                    'kinder':0.2,'nutella':0, 'eurocrem':-0.2, 'vanilla':-0.1, 'pies':0,
                    'bananas':0,},
        'way_of_making':{'roasted':-0.1, 'grilled':0, 'smoked':0.2,'toasted':0.1,},
        'volume_of_eating': {'big':0.1, 'medium':0.3, 'low':0.3}}
#tags Veljko
VELJKO = {'broad': {'meat': 0.35, 'vegetable': 0.25, 'sweet':0.2},
        'specific': {'sesam':0.1,'eggs':-0.1,'french fries':0.2,'kajmak':0.1,'sandwich':0.2,
                    'tortilla':0.3,'bun':0.1,'flatbread':0.2,
                    'chicken':0.3,'schnitzel':0.2,'sausage':-0.1,'kebab':-0.1,'bacon':0.2,
                    'kinder':0.3,'nutella':0.1, 'eurocrem':0.1, 'vanilla':0.4, 'pies':-0.1,
                    'bananas':0.1,},
        'way_of_making':{'roasted':0, 'grilled':0.2, 'smoked':0.2,'toasted':0.1,},
        'volume_of_eating': {'big':0, 'medium':0.2, 'low':0.3}}
#tags Ana
ANA = {'broad': {'meat': 0.2, 'vegetable': 0.3, 'sweet': -0.2},
        'specific': {'sesam':0.4,'eggs':0.1,'french fries':0.1,'kajmak':0.1,'sandwich':0.2,
                    'tortilla':0.3,'bun':0.2,'flatbread':0.2,
                    'chicken':0.4,'schnitzel':0.2,'sausage':0,'kebab':-0.2,'bacon':0,
                    'kinder':0,'nutella':0.2, 'eurocrem':0, 'vanilla':-0.2, 'pies':0,
                    'bananas':0.1,},
        'way_of_making':{'roasted':0.2, 'grilled':0, 'smoked':0,'toasted':-0.2,},
        'volume_of_eating': {'big':0.1, 'medium':0.3, 'low':0.2}}



###################   SHOPS   ###########################################################
#Shops in ZEMUN
#For functionality of the algoritam for this func is: we have nested dic soo we need 2 for loops
#every menu and every food has tags in their dictionery(you can find it in the main file of the game)
#this func checks if prefrences of a character overlaps with the tags for that food, if it does
#then it just adds thoes values and thats it
def shop_menu(layout_map ,shop, name, money, place):
    hung = []
    hung_tag = []
    
    currently_spent = 0
    char_tags_strings = ['BOGDAN', 'MARKO', 'TEODORA', 'VELJKO', 'ANA']
    char_tags_value = [BOGDAN, MARKO, TEODORA, VELJKO, ANA]
    #Ako ikad budem hteo da ubacim vise prodavnica, onda mogu ime prodavnice da vratim iz func iz dela koda u glavnom fajlu i njega prosledim ovde, onda imam 
    #i tu povezanost, a ne samo place
    dict_title_of_shops = {'Zemun': 'Kiklop menu',
                              'Novi Beograd': 'Food Factory menu',
                              'Vracar': 'Mara menu',
                              'Zvezdara': 'Gusar menu',
                              'Vozdovac': 'Stepin Vajat menu',
                              'Grocka': 'Panter Grocka'}
    char_name = name.name.upper()
    grid = Table(expand=True, title=f'[grey69]{dict_title_of_shops[place]} menu')

    grid.add_column('Food',header_style='blue', style="magenta")
    grid.add_column('Price', header_style='red3',style="green")

    grid.add_row(f"1.{shop[0]['hrana']}", f"{shop[0]['cena']}")
    grid.add_row(f"2.{shop[1]['hrana']}", f"{shop[1]['cena']}")
    grid.add_row(f"3.{shop[2]['hrana']}", f"{shop[2]['cena']}")
    grid.add_row(f"4.{shop[3]['hrana']}", f"{shop[3]['cena']}")

    layout_map['right'].update(grid)
    print(layout_map)
    #print(money)
    while True:
        choices = ['1','2','3','4']
        buy = Prompt.ask('[dark_orange3]What do you want to buy(just type the number)?').lower()
                    
        if buy == 'back':
            ##print(hung) 
            hung = (sum(hung) + sum(hung_tag))*10
            #print(hung,sum(hung_tag))
            return hung, currently_spent
        if buy not in choices:
            continue
        elif buy in choices:
           
            #gets the name of the char and their tags
            if currently_spent + shop[int(buy)-1]['cena'] <= money:
                hung.append(shop[int(buy)-1]['koeficijent'])
                currently_spent  += shop[int(buy)-1]['cena']
            index = int(char_tags_strings.index(char_name))
            for i in char_tags_value[index]:
                    #print('tagovi',i)
                    for j in char_tags_value[index][i]:
                        #print('tagovi',j)
                        #print('1',shop[int(buy)-1]['cena'],j)
                        if currently_spent + shop[int(buy)-1]['cena'] <= money:
                                if j in shop[int(buy)-1]['tags']:
                                #print('2',shop[int(buy)-1]['cena'],char_tags_value[index][i][j])
                                        #print('3',shop[int(buy)-1]['cena'],j,shop[int(buy)-1]['tags'],shop[int(buy)-1]['koeficijent'])
                                        
                                        hung_tag.append(char_tags_value[index][i][j])
                                        #print('asdasd',hung, hung_tag,currently_spent)
                                        
                                        continue
            print(layout_map)
            if currently_spent + shop[int(buy)-1]['cena'] > money:
                print('[bold yellow]You dont have enough money for that')
            print('[bold red]You currently spent:[/bold red] ',currently_spent)
    
    
    return 