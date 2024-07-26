from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd
from romantic import rom_program
from adventure import adv_program
from fantasy import fant_program
from horror import hor_program
from comedy import com_program
from drama import drm_program
from detective import det_program
from action import act_program

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')
xl_anime = 'anime.xlsx'
# list_search = 'search.xlsx'

anime = pd.read_excel(
    xl_anime,
    sheet_name='Лучшее',
    na_values=['N/A', 'NA'],
    keep_default_na=False).to_dict(orient='records')
rendered_card = template.render(anime=anime)


# search = pd.read_excel(
#     list_search,
#     sheet_name='Поиск',
#     na_values=['N/A', 'NA'],
#     keep_default_na=False).to_dict(orient='records')
# rendered_search = template.render(search=search)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_card)
    # file.write(rendered_search)

if __name__=='__main__':
    rom_program()
    adv_program()
    fant_program()
    hor_program()
    com_program()
    drm_program()
    det_program()
    act_program()

