from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from rich import print
from rich import box
import json

def score_board():
    score_layout = Layout()
    score_layout.split_row( Layout(name='Easy'),
                 Layout(name='Normal'),
                 Layout(name='Hard'))
    score_normal = []
    score_easy = []
    score_hard = []
    with open('score_board.json', 'r') as file:
        score_sheet = json.load(file)
        for entry in score_sheet:
            if entry['difficulty'] == 'Normal':
                score_normal.append(entry)
            elif entry['difficulty'] == 'Easy':
                score_easy.append(entry)
            elif entry['difficulty'] == 'Hard':
                score_hard.append(entry)
    score_normal_table = Table(title='Score for Normal', title_justify='center', box = box.SIMPLE,)
    score_easy_table = Table(title= 'Score for Easy',expand= True,title_justify='center',box = box.SIMPLE)
    score_hard_table = Table(title='Score for Hard', expand= True,title_justify='center',box = box.SIMPLE)

    #table_panel = Align.center(Panel.fit(table, style="dark_olive_green3"))


    score_normal_table.add_column(header='Player')
    score_normal_table.add_column(header='Character name', justify='left')
    score_normal_table.add_column(header='difficulty', justify='center')
    score_normal_table.add_column(header='hungriness', justify='right')
    score_normal_table.add_column(header='satisfaction', justify='right')
    

    for num,row in enumerate(score_normal):
        for j,k in enumerate(row):
            values = list(row.values())
            score_normal_table.add_row(f'{values[0]}',f'{values[1]}',f'{values[2]}',f'{values[3]}',f'{values[4]}')
            break
           
    normal_table_Panel = Align.center(Panel(score_normal_table))


    score_easy_table.add_column(header='Player')
    score_easy_table.add_column(header='Character name', justify='left')
    score_easy_table.add_column(header='difficulty', justify='center')
    score_easy_table.add_column(header='hungriness', justify='right')
    score_easy_table.add_column(header='satisfaction', justify='right')

    for num,row in enumerate(score_easy):
        for j,k in enumerate(row):
            values = list(row.values())
            score_easy_table.add_row(f'{values[0]}',f'{values[1]}',f'{values[2]}',f'{values[3]}',f'{values[4]}')
            break

    easy_table_Panel = Align.center(Panel(score_easy_table))


    score_hard_table.add_column(header='Player')
    score_hard_table.add_column(header='Character name', justify='left')
    score_hard_table.add_column(header='difficulty', justify='center')
    score_hard_table.add_column(header='hungriness', justify='right')
    score_hard_table.add_column(header='satisfaction', justify='right')

    for num,row in enumerate(score_hard):
        for j,k in enumerate(row):
            values = list(row.values())
            score_hard_table.add_row(f'{values[0]}',f'{values[1]}',f'{values[2]}',f'{values[3]}',f'{values[4]}')
            break

    hard_table_Panel = Align.center(Panel(score_hard_table))

    score_layout['Normal'].update(normal_table_Panel)
    score_layout['Easy'].update(easy_table_Panel)
    score_layout['Hard'].update(hard_table_Panel)
    print(score_layout)
    input()