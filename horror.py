from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd

def hor_program():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('tp_hor.html')
    file_xl = 'anime.xlsx'
    anime = pd.read_excel(
        file_xl,
        sheet_name='Ужасы',
        na_values=['N/A', 'NA'],
        keep_default_na=False).to_dict(orient='records')
    rendered_page = template.render(anime=anime)

    with open('horror.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)