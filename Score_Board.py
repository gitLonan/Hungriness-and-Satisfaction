from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.panel import Panel
from rich import print
from rich import box
import json

def score_board():
    #summary: create Layout, than create Tables, to be able to have more controle of the said Tables, we put them in to Panels
    #which we will than update the said Layout with thoes Panels and than we just print the layout.
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
    score_easy_table = Table(title= 'Score for Easy',    title_justify='center',box = box.SIMPLE, title_style='chartreuse3', border_style='sea_green2',header_style='grey23')
    score_normal_table = Table(title='Score for Normal', title_justify='center',box = box.SIMPLE, title_style='yellow3', border_style='khaki3',header_style='grey23')
    score_hard_table = Table(title='Score for Hard',     title_justify='center',box = box.SIMPLE, title_style='deep_pink2', border_style='magenta2',header_style='grey23')

    #table_panel = Align.center(Panel.fit(table, style="dark_olive_green3"))


    score_normal_table.add_column(header='Player', style='khaki3')
    score_normal_table.add_column(header='Character name',style='khaki3')
    score_normal_table.add_column(header='difficulty', style='khaki3')
    score_normal_table.add_column(header='hungriness', style='khaki3')
    score_normal_table.add_column(header='satisfaction', style='khaki3')
    

    for num,row in enumerate(score_normal):
        for j,k in enumerate(row):
            values = list(row.values())
            score_normal_table.add_row(f'{values[0]}',f'{values[1]}',f'{values[2]}',f'{values[3]}',f'{values[4]}')
            break
           
    normal_table_Panel = Align.center(Panel(score_normal_table))


    score_easy_table.add_column(header='Player', style='sea_green2')
    score_easy_table.add_column(header='Character name', style='sea_green2')
    score_easy_table.add_column(header='difficulty', style='sea_green2')
    score_easy_table.add_column(header='hungriness', style='sea_green2')
    score_easy_table.add_column(header='satisfaction', style='sea_green2')

    for num,row in enumerate(score_easy):
        for j,k in enumerate(row):
            values = list(row.values())
            score_easy_table.add_row(f'{values[0]}',f'{values[1]}',f'{values[2]}',f'{values[3]}',f'{values[4]}')
            break

    easy_table_Panel = Align.center(Panel(score_easy_table))


    score_hard_table.add_column(header='Player',style='magenta2')
    score_hard_table.add_column(header='Character name',style='magenta2')
    score_hard_table.add_column(header='difficulty',style='magenta2')
    score_hard_table.add_column(header='hungriness',style='magenta2')
    score_hard_table.add_column(header='satisfaction', style='magenta2')

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