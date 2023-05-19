import random


def main_city_layout(place=""):

    def starting_location(place):
        if place == '':
            start_location = random.randint(1,2)
            if  start_location == 1:
                start_1,start_2 = '[yellow1]*[/yellow1]', ''
            elif start_location == 2:
                start_2,start_1 = '[yellow1]*[/yellow1]', ''
        else:
            start_2,start_1 = '',''

        return start_1, start_2

    def indication(place):
        zemun_pointer = ''
        vracar_pointer = ''
        novi_pointer = ''
        zvezdara_pointer = ''
        grocka_pointer = ''
        vozdovac_pointer = ''
        #pointer that points where you are on the map
        if place == 'Zemun':
            zemun_pointer = '[yellow1]*[/yellow1]'
        elif place == 'Vracar':
            vracar_pointer = '[yellow1]*[/yellow1]'
        elif place == 'Novi Beograd':
            novi_pointer = '[yellow1]*[/yellow1]'
        elif place == 'Zvezdara':
            zvezdara_pointer = '[yellow1]*[/yellow1]'
        elif place == 'Grocka':
            grocka_pointer = '[yellow1]*[/yellow1]'
        elif place == 'Vozdovac':
            vozdovac_pointer = '[yellow1]*[/yellow1]'
        return zemun_pointer, vracar_pointer,novi_pointer,zvezdara_pointer,grocka_pointer,vozdovac_pointer
    start_1, start_2 = starting_location(place)
    #style = grey37, s is short for it
    zem, vra, novi, zvez, grock, vozd = indication(place)
    s = 'grey37'
    """        Look of the map without styling, map looks the same with styling
                just with the syntax it looks disorted
                               {start_1}
                                   |
                                   |
                ---------          |          ----------            ------------
                | Zemun |----------|----------| Vracar |------------| Zvezdara |
                ---------         /|          ----------            ------------
                    |            / |
          ----------------      /  |
          | Novi Beograd |-----/   | ------|
          ----------------         |       |                    ------------
                                   |       |--------------------| Vozdovac |
                                   |                            ------------
                                   |           ----------
                                   |-----------| Grocka |
                                   |           ----------
                               {start_2}
        """


    string = f"""                                       {start_1}
                                       |
                                       |
                    ---------          |           ----------           ------------
                    | [{s}]Zemun[/{s}]{zem} |----------|-----------| [{s}]Vracar[/{s}]{vra} |-----------| [{s}]Zvezdara[/{s}]{zvez} |
                    ---------         /|           ----------           ------------
                        |            / |
              ----------------      /  |
              | [{s}]Novi Beograd[/{s}]{novi} |-----/   |-------|
              ----------------         |       |                    ------------
                                       |       |--------------------| [{s}]Vozdovac[/{s}]{vozd} |
                                       |                            ------------
                                       |           ----------
                                       |-----------| [{s}]Grocka[/{s}]{grock} |
                                       |           ----------
                                       {start_2}
            """
    return string

def zemun_layout():
    #color of the layout
    string = f"""
        [yellow]
                            --------------------
                            | Fast Food Kiklop |
                            --------------------

            """
    return string
def novi_beograd_layout():
    string = f"""
    [yellow]
                            --------------------------
                            | Fast Food Food Factory |
                            --------------------------

            """
    return string
def vracar_layout():
    string = f"""
    [yellow]
                            ------------------
                            | Fast Food Mara |
                            ------------------
            """
    return string
def zvezdara_layout():
    string = f"""
    [yellow]
                            -------------------
                            | Fast Food Gusar |
                            -------------------
            """
    return string
def vozdovac_layout():
    string = f"""
    [yellow]
                            --------------------------
                            | Fast Food Stepin Vajat |
                            --------------------------
            """
    return string
def grocka_layout():
    string = f"""
    [yellow]
                            ---------------------------
                            | Fast Food Panter Grocka |
                            ---------------------------
            """
    return string
